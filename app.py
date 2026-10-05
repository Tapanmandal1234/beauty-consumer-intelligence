import os
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

st.set_page_config(
    page_title="Beauty Consumer Intelligence | Tapan Mandal",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="expanded",
)

BG="#171513"; PANEL="#211E1B"; CREAM="#F3EEE6"; MUTED="#A79F96"
ROSE="#C98F87"; SAGE="#92A48D"; GOLD="#C6A46B"; BLUE="#8E9FA8"
GRID="rgba(243,238,230,0.12)"
HERO="#8FA58A"; HIDDEN="#C6A46B"; HYPE="#C47E72"; LOW="#7D8588"

st.markdown(f"""
<style>
.stApp {{background-color:{BG};color:{CREAM};}}
.block-container {{max-width:1220px;padding-top:3.2rem;padding-bottom:5rem;}}
[data-testid="stSidebar"] {{background-color:#1D1A18;border-right:1px solid rgba(255,255,255,.08);}}
h1,h2,h3 {{font-family:Georgia,serif!important;color:{CREAM}!important;letter-spacing:-.025em;}}
h1 {{font-size:3.25rem!important;line-height:1.02!important;}}
.eyebrow {{color:{ROSE};font-size:10px;letter-spacing:.20em;text-transform:uppercase;margin-bottom:14px;font-weight:600;}}
.intro {{color:#D0C9C1;font-size:18px;line-height:1.65;max-width:950px;margin-bottom:42px;}}
.section-number {{color:{MUTED};font-size:10px;letter-spacing:.20em;text-transform:uppercase;margin-top:48px;margin-bottom:7px;}}
.insight-box {{border-left:2px solid {ROSE};background:rgba(255,255,255,.035);padding:18px 22px;margin:14px 0 28px;line-height:1.65;}}
.action-box {{border:1px solid rgba(255,255,255,.11);background:rgba(255,255,255,.025);padding:22px 24px;margin-top:15px;line-height:1.65;}}
.small-note {{color:{MUTED};font-size:12px;line-height:1.55;}}
[data-testid="stMetric"] {{background:rgba(255,255,255,.035);border:1px solid rgba(255,255,255,.10);padding:17px;min-height:116px;}}
[data-testid="stMetricLabel"] {{text-transform:uppercase;letter-spacing:.07em;font-size:10px;}}
hr {{border-color:rgba(255,255,255,.10);}}
</style>
""", unsafe_allow_html=True)

PLOT_CONFIG={"displayModeBar":False,"responsive":True}
def style_fig(fig,height=430,legend=True):
    fig.update_layout(template="plotly_dark",paper_bgcolor=BG,plot_bgcolor=BG,
        font=dict(color=MUTED),height=height,margin=dict(l=15,r=15,t=35,b=20),
        showlegend=legend,hoverlabel=dict(bgcolor=PANEL,font_color=CREAM),
        legend=dict(orientation="h",yanchor="bottom",y=1.02,xanchor="right",x=1))
    fig.update_xaxes(showgrid=False,zeroline=False)
    fig.update_yaxes(gridcolor=GRID,zeroline=False)
    return fig

@st.cache_data(show_spinner=False)
def load_data():
    p=pd.read_csv("products_processed.csv",low_memory=False)
    t=pd.read_csv("themes_processed.csv",low_memory=False)
    s=pd.read_csv("segments_processed.csv",low_memory=False)
    for d in (p,t,s):
        d["product_id"]=d["product_id"].astype(str)
    return p,t,s

required=["products_processed.csv","themes_processed.csv","segments_processed.csv"]
missing=[x for x in required if not os.path.exists(x)]
if missing:
    st.error("Missing deployment file(s): "+", ".join(missing))
    st.stop()

products,themes,segments=load_data()

# Sidebar
st.sidebar.markdown("## Consumer Lens")
brands=["All Brands"]+sorted(products["brand_name"].dropna().unique().tolist())
brand=st.sidebar.selectbox("Brand",brands)
cats=["All Categories"]+sorted(products["primary_category"].dropna().unique().tolist())
category=st.sidebar.selectbox("Category",cats)
signals=["All Signals","HERO PRODUCT","HIDDEN GEM","HYPE GAP","LOW TRACTION"]
signal_filter=st.sidebar.selectbox("Consumer Signal",signals)

filtered=products.copy()
if brand!="All Brands": filtered=filtered[filtered["brand_name"]==brand]
if category!="All Categories": filtered=filtered[filtered["primary_category"]==category]
if signal_filter!="All Signals": filtered=filtered[filtered["Consumer_Signal"]==signal_filter]
if filtered.empty:
    st.warning("No products match these filters."); st.stop()

filtered=filtered.sort_values("Review_Count",ascending=False)
labels=(filtered["product_name"].fillna("Unknown")+" — "+filtered["brand_name"].fillna("Unknown")).tolist()
lookup=dict(zip(labels,filtered["product_id"].tolist()))
selected_label=st.sidebar.selectbox("Product Deep Dive",labels)
pid=lookup[selected_label]
st.sidebar.markdown("---")
st.sidebar.caption(f"{len(products):,} products analyzed")
st.sidebar.caption(f"{int(products['Review_Count'].sum()):,} reviews represented")
st.sidebar.caption("Full raw review data was pre-aggregated for fast deployment.")

# Header
st.markdown('<div class="eyebrow">02 / Consumer & Brand Strategy</div>',unsafe_allow_html=True)
st.title("Beauty Consumer Intelligence")
st.markdown("""<div class="intro"><b>When does product hype translate into consumer love — and when does it create an expectation gap?</b><br>
Combining product attention, consumer experience, review language and audience characteristics to identify hero products, hidden gems, hype gaps and the consumer friction behind them.</div>""",unsafe_allow_html=True)

# Market pulse
st.markdown('<div class="section-number">01 / Market Pulse</div>',unsafe_allow_html=True)
st.header("Where is consumer attention going?")
a,b,c,d=st.columns(4)
a.metric("Products Analyzed",f"{len(filtered):,}")
b.metric("Consumer Reviews",f"{int(filtered['Review_Count'].sum()):,}")
c.metric("Average Rating",f"{filtered['Consumer_Rating'].mean():.2f} / 5")
d.metric("Recommendation Rate",f"{filtered['Recommendation_Rate'].mean():.1%}")

top=filtered.nlargest(12,"Attention_Index").sort_values("Attention_Index")
fig=go.Figure(go.Bar(x=top["Attention_Index"],y=top["product_name"],orientation="h",
    marker_color=ROSE,customdata=np.stack((top["brand_name"],top["loves_count"],top["Review_Count"]),axis=-1),
    hovertemplate="<b>%{y}</b><br>%{customdata[0]}<br>Attention: %{x:.2f}<br>Loves: %{customdata[1]:,.0f}<br>Reviews: %{customdata[2]:,.0f}<extra></extra>"))
style_fig(fig,520,False); fig.update_xaxes(title="Relative consumer attention",range=[0,1.03])
st.plotly_chart(fig,use_container_width=True,config=PLOT_CONFIG)
leader=filtered.loc[filtered["Attention_Index"].idxmax()]
st.markdown(f"""<div class="insight-box"><b>Attention leader:</b> {leader['product_name']} by {leader['brand_name']} has the strongest relative attention signal in this view, combining Sephora loves and review volume. Attention alone does not tell us whether experience lives up to it.</div>""",unsafe_allow_html=True)

# Hype vs experience
st.markdown('<div class="section-number">02 / Hype vs Experience</div>',unsafe_allow_html=True)
st.header("Does attention translate into love?")
colors={"HERO PRODUCT":HERO,"HIDDEN GEM":HIDDEN,"HYPE GAP":HYPE,"LOW TRACTION":LOW}
# Global medians used in preprocessing; reconstruct from classifications/indices as portfolio median.
att_cut=products["Attention_Index"].median(); exp_cut=products["Experience_Index"].median()
fig=px.scatter(filtered,x="Attention_Index",y="Experience_Index",size="Review_Count",color="Consumer_Signal",
    color_discrete_map=colors,hover_name="product_name",
    hover_data={"brand_name":True,"Consumer_Rating":":.2f","Recommendation_Rate":":.1%","Review_Count":":,.0f",
                "Attention_Index":":.2f","Experience_Index":":.2f"},
    labels={"Attention_Index":"Consumer attention","Experience_Index":"Consumer experience"},size_max=30)
fig.add_vline(x=att_cut,line_dash="dash",line_color=MUTED,opacity=.7)
fig.add_hline(y=exp_cut,line_dash="dash",line_color=MUTED,opacity=.7)
for x,y,txt,col,anchor in [(0.98,.98,"HERO PRODUCTS",HERO,"right"),(.02,.98,"HIDDEN GEMS",HIDDEN,"left"),
                            (.98,.04,"HYPE GAP",HYPE,"right"),(.02,.04,"LOW TRACTION",LOW,"left")]:
    fig.add_annotation(x=x,y=y,xref="paper",yref="paper",text=txt,showarrow=False,xanchor=anchor,font=dict(size=10,color=col))
style_fig(fig,620,True)
st.plotly_chart(fig,use_container_width=True,config=PLOT_CONFIG)
counts=filtered["Consumer_Signal"].value_counts()
st.markdown(f"""<div class="insight-box"><b>Portfolio read:</b> this view identifies <b>{counts.get('HERO PRODUCT',0)} hero products</b>, <b>{counts.get('HIDDEN GEM',0)} hidden gems</b>, and <b>{counts.get('HYPE GAP',0)} hype-gap products</b> within the selected view.</div>""",unsafe_allow_html=True)

# Brand intelligence
st.markdown('<div class="section-number">03 / Brand Intelligence</div>',unsafe_allow_html=True)
st.header("Which brands convert attention into experience?")
bs=filtered.groupby("brand_name").agg(Products=("product_id","nunique"),Reviews=("Review_Count","sum"),
    Attention=("Attention_Index","mean"),Experience=("Experience_Index","mean"),
    Rating=("Consumer_Rating","mean"),Recommendation=("Recommendation_Rate","mean")).reset_index()
bs=bs[bs["Products"]>=2]
if not bs.empty:
    fig=px.scatter(bs,x="Attention",y="Experience",size="Reviews",hover_name="brand_name",
        hover_data={"Products":True,"Reviews":":,.0f","Rating":":.2f","Recommendation":":.1%"})
    fig.update_traces(marker=dict(color="#B8AEA3",opacity=.75,line=dict(width=1,color=CREAM)))
    style_fig(fig,520,False); fig.update_xaxes(title="Average product attention"); fig.update_yaxes(title="Average consumer experience")
    st.plotly_chart(fig,use_container_width=True,config=PLOT_CONFIG)

# Deep dive
sel=products[products["product_id"]==pid].iloc[0]
st.markdown('<div class="section-number">04 / Product Deep Dive</div>',unsafe_allow_html=True)
st.header(sel["product_name"])
st.markdown(f'<div class="small-note">{sel["brand_name"]} · {sel.get("primary_category","")} · ${sel["price_usd"]:.2f}</div>',unsafe_allow_html=True)
a,b,c,d=st.columns(4)
a.metric("Consumer Signal",sel["Consumer_Signal"])
b.metric("Consumer Rating",f'{sel["Consumer_Rating"]:.2f} / 5')
c.metric("Recommendation",f'{sel["Recommendation_Rate"]:.1%}')
d.metric("Reviews",f'{sel["Review_Count"]:,.0f}')

# Consumer language
st.markdown('<div class="section-number">05 / Consumer Language</div>',unsafe_allow_html=True)
st.header("What do consumers love — and where does experience break?")
pt=themes[themes["product_id"]==pid].copy()
min_mentions=max(3,int(sel["Review_Count"]*.01))
pt=pt[pt["Mentions"]>=min_mentions]
if pt.empty:
    st.info("No recurring themes pass the minimum mention threshold for this product.")
else:
    love=pt.sort_values(["Positive_Share","Mentions"],ascending=[False,False]).head(5)
    friction=pt.sort_values(["Negative_Share","Mentions"],ascending=[False,False]).head(5)
    left,right=st.columns(2)
    with left:
        st.subheader("Love Drivers")
        fig=go.Figure(go.Bar(x=love["Positive_Share"],y=love["Theme"],orientation="h",marker_color=SAGE,
            customdata=love["Mentions"],hovertemplate="%{y}<br>Positive share: %{x:.1%}<br>Mentions: %{customdata:,}<extra></extra>"))
        style_fig(fig,330,False); fig.update_xaxes(tickformat=".0%",title="Positive review share")
        st.plotly_chart(fig,use_container_width=True,config=PLOT_CONFIG)
    with right:
        st.subheader("Friction Drivers")
        fig=go.Figure(go.Bar(x=friction["Negative_Share"],y=friction["Theme"],orientation="h",marker_color=HYPE,
            customdata=friction["Mentions"],hovertemplate="%{y}<br>Negative share: %{x:.1%}<br>Mentions: %{customdata:,}<extra></extra>"))
        style_fig(fig,330,False); fig.update_xaxes(tickformat=".0%",title="Negative review share")
        st.plotly_chart(fig,use_container_width=True,config=PLOT_CONFIG)

# Consumer differences
st.markdown('<div class="section-number">06 / Consumer Differences</div>',unsafe_allow_html=True)
st.header("Who experiences the product differently?")
ss=segments[(segments["product_id"]==pid)&(segments["Reviews"]>=10)].copy().sort_values("Rating")
if len(ss)>=2:
    fig=go.Figure(go.Bar(x=ss["Rating"],y=ss["skin_type"],orientation="h",marker_color=BLUE,
        customdata=np.stack((ss["Reviews"],ss["Recommendation"]),axis=-1),
        hovertemplate="%{y}<br>Rating: %{x:.2f}<br>Reviews: %{customdata[0]:,.0f}<br>Recommendation: %{customdata[1]:.1%}<extra></extra>"))
    style_fig(fig,360,False); fig.update_xaxes(title="Average rating",range=[max(1,ss["Rating"].min()-.25),5])
    st.plotly_chart(fig,use_container_width=True,config=PLOT_CONFIG)
    hi=ss.loc[ss["Rating"].idxmax()]; lo=ss.loc[ss["Rating"].idxmin()]
    st.markdown(f"""<div class="insight-box"><b>Audience signal:</b> among skin types with at least 10 reviews, <b>{hi['skin_type']}</b> reviewers report the strongest experience ({hi['Rating']:.2f}/5), compared with {lo['skin_type']} reviewers at {lo['Rating']:.2f}/5. The observed gap is <b>{hi['Rating']-lo['Rating']:.2f} points</b>. This is descriptive evidence, not proof of causation.</div>""",unsafe_allow_html=True)
else:
    st.info("This product does not have enough skin-type observations for a reliable segment comparison.")

# Brand action
st.markdown('<div class="section-number">07 / Brand Action</div>',unsafe_allow_html=True)
st.header("What should the brand do?")
sig=sel["Consumer_Signal"]
actions={
"HERO PRODUCT":("Protect the experience. Scale the proof.","Strong relative attention is matched by strong consumer experience. Protect the attributes consumers already value and use review evidence as proof in positioning and acquisition."),
"HIDDEN GEM":("The experience is stronger than the attention.","Consumers who reach this product respond relatively well, but attention is below the portfolio benchmark. Test stronger discovery, merchandising, creator support or sampling before changing the product itself."),
"HYPE GAP":("Diagnose the expectation gap before adding more hype.","Attention is strong but experience sits below the portfolio benchmark. Investigate recurring friction, audience differences and positioning before simply increasing awareness."),
"LOW TRACTION":("Clarify the role of the product.","Both relative attention and experience sit below the portfolio benchmark. Determine whether the opportunity is repositioning, product improvement, tighter targeting or lower strategic priority.")
}
title,body=actions[sig]
st.markdown(f'<div class="action-box"><h3>{title}</h3>{body}</div>',unsafe_allow_html=True)

# Priorities
st.markdown('<div class="section-number">08 / Portfolio Priorities</div>',unsafe_allow_html=True)
st.header("Where should we look first?")
order={"HYPE GAP":1,"HIDDEN GEM":2,"HERO PRODUCT":3,"LOW TRACTION":4}
tab=filtered[["product_name","brand_name","Consumer_Signal","Consumer_Rating","Recommendation_Rate","Review_Count","loves_count","price_usd"]].copy()
tab["_order"]=tab["Consumer_Signal"].map(order)
tab=tab.sort_values(["_order","Review_Count"],ascending=[True,False]).drop(columns="_order")
tab.columns=["Product","Brand","Signal","Rating","Recommendation","Reviews","Loves","Price"]
st.dataframe(tab.style.format({"Rating":"{:.2f}","Recommendation":"{:.1%}","Reviews":"{:,.0f}","Loves":"{:,.0f}","Price":"${:,.2f}"}),
    use_container_width=True,height=500,hide_index=True)

st.markdown("---")
with st.expander("How this analysis works"):
    st.markdown("""
### Attention
The **Attention Index** combines percentile-ranked Sephora loves (60%) and review volume (40%). It represents relative observed attention in this dataset—not sales, awareness, ad spend or market share.

### Consumer Experience
The **Experience Index** combines normalized average rating (55%), recommendation rate (30%), and 4–5-star review share (15%).

### Hype vs Experience
Products with at least 25 reviews are compared with portfolio medians:
- **Hero Product:** higher attention + higher experience
- **Hidden Gem:** lower attention + higher experience
- **Hype Gap:** higher attention + lower experience
- **Low Traction:** lower attention + lower experience

### Consumer language
Review themes use transparent keyword dictionaries across the full review text. They surface recurring topics such as hydration, texture, irritation, breakouts, scent, packaging, value and application.

### Consumer differences
Skin-type comparisons use reviewer-reported skin type and require at least 10 reviews in a displayed segment. These are descriptive associations, not causal claims.

### Limitation
The source data contains product information and consumer reviews, not verified unit sales, market share, advertising spend, profitability or customer acquisition cost. This is therefore a **consumer-intelligence and brand-strategy exercise**, not a sales-performance model.
""")
st.caption("Portfolio project · Beauty Consumer Intelligence · Python / Pandas / Plotly / Streamlit")

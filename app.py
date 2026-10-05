import os
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st


# ============================================================
# PAGE SETUP
# ============================================================

st.set_page_config(
    page_title="Beauty Consumer Intelligence ",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ============================================================
# DESIGN SYSTEM
# ============================================================

BG = "#171513"
SIDEBAR = "#1D1A18"
PANEL = "#211E1B"

CREAM = "#F3EEE6"
TEXT = "#DED7CF"
MUTED = "#A79F96"

ROSE = "#C98F87"
SAGE = "#92A48D"
GOLD = "#C6A46B"
BLUE = "#8E9FA8"

GRID = "rgba(243,238,230,0.12)"

PROVEN = "#92A48D"
HIDDEN = "#C6A46B"
GAP = "#C47E72"
LOW = "#7D8588"

PLOT_CONFIG = {
    "displayModeBar": False,
    "responsive": True,
}


# ============================================================
# GLOBAL CSS
# ============================================================

st.markdown(
    f"""
<style>

/* APP */

html, body, [class*="css"] {{
    color: {TEXT};
}}

.stApp {{
    background-color: {BG};
    color: {TEXT};
}}

.block-container {{
    max-width: 1220px;
    padding-top: 3rem;
    padding-bottom: 5rem;
}}


/* SIDEBAR */

[data-testid="stSidebar"] {{
    background-color: {SIDEBAR};
    border-right: 1px solid rgba(255,255,255,0.08);
}}

[data-testid="stSidebar"] * {{
    color: {TEXT};
}}

[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3 {{
    color: {CREAM} !important;
}}

[data-testid="stSidebar"] label {{
    color: {TEXT} !important;
    font-weight: 500 !important;
}}

[data-testid="stSidebar"] .stCaptionContainer p {{
    color: {MUTED} !important;
}}


/* SELECT BOXES */

div[data-baseweb="select"] > div {{
    background-color: #F4F2EF !important;
    color: #25211F !important;
    border: 1px solid rgba(0,0,0,0.12) !important;
}}

div[data-baseweb="select"] span {{
    color: #25211F !important;
}}

div[data-baseweb="select"] svg {{
    fill: #25211F !important;
}}


/* TYPOGRAPHY SYSTEM */

h1, h2, h3 {{
    color: {CREAM} !important;
    margin-bottom: 0.55rem !important;
}}

h1 {{
    font-family: Georgia, "Times New Roman", serif !important;
    font-size: 3.25rem !important;
    line-height: 1.08 !important;
    font-weight: 700 !important;
    letter-spacing: -0.035em !important;
}}

h2 {{
    font-family: Georgia, "Times New Roman", serif !important;
    font-size: 2.35rem !important;
    line-height: 1.15 !important;
    font-weight: 700 !important;
    letter-spacing: -0.025em !important;
}}

h3 {{
    font-family: Georgia, "Times New Roman", serif !important;
    font-size: 1.55rem !important;
    line-height: 1.2 !important;
    font-weight: 700 !important;
    letter-spacing: -0.015em !important;
}}

p,
li,
label,
div {{
    font-family: Arial, Helvetica, sans-serif;
}}

p {{
    color: {TEXT};
    font-size: 15px;
    line-height: 1.65;
}}

.eyebrow {{
    font-family: Arial, Helvetica, sans-serif !important;
    color: {ROSE};
    font-size: 10px;
    line-height: 1;
    letter-spacing: 0.20em;
    text-transform: uppercase;
    margin-bottom: 16px;
    font-weight: 700;
}}

.intro {{
    font-family: Arial, Helvetica, sans-serif !important;
    color: {TEXT};
    font-size: 18px;
    line-height: 1.65;
    max-width: 970px;
    margin-top: 8px;
    margin-bottom: 48px;
}}

.section-number {{
    font-family: Arial, Helvetica, sans-serif !important;
    color: {MUTED};
    font-size: 10px;
    line-height: 1;
    letter-spacing: 0.20em;
    text-transform: uppercase;
    margin-top: 54px;
    margin-bottom: 14px;
    font-weight: 600;
}}

.small-note {{
    font-family: Arial, Helvetica, sans-serif !important;
    color: {MUTED};
    font-size: 13px;
    line-height: 1.6;
}}

.method-note,
.metric-definition {{
    font-family: Arial, Helvetica, sans-serif !important;
    color: {MUTED};
    font-size: 13px;
    line-height: 1.7;
}}

.insight-box,
.action-box,
.framework-box {{
    font-family: Arial, Helvetica, sans-serif !important;
}}


/* FRAMEWORK */

.framework-box {{
    border: 1px solid rgba(255,255,255,0.10);
    background: rgba(255,255,255,0.025);
    padding: 24px 26px;
    margin: 18px 0 28px;
}}

.framework-title {{
    font-family: Arial, Helvetica, sans-serif !important;
    color: {CREAM};
    font-size: 16px;
    font-weight: 700;
    margin-bottom: 18px;
}}

.framework-row {{
    display: grid;
    grid-template-columns: 210px 1fr;
    column-gap: 26px;
    align-items: start;
    padding: 15px 0;
    border-top: 1px solid rgba(255,255,255,0.07);
}}

.framework-row:first-of-type {{
    border-top: none;
    padding-top: 0;
}}

.framework-label {{
    font-family: Arial, Helvetica, sans-serif !important;
    color: {CREAM};
    font-size: 13px;
    font-weight: 700;
    line-height: 1.5;
}}

.framework-copy {{
    font-family: Arial, Helvetica, sans-serif !important;
    color: {TEXT};
    font-size: 13px;
    line-height: 1.65;
}}


/* CARDS */

.insight-box {{
    border-left: 2px solid {ROSE};
    background: rgba(255,255,255,0.035);
    padding: 18px 22px;
    margin: 14px 0 28px;
    line-height: 1.65;
    color: {TEXT};
}}

.action-box {{
    border: 1px solid rgba(255,255,255,0.11);
    background: rgba(255,255,255,0.03);
    padding: 24px 26px;
    margin-top: 15px;
    line-height: 1.7;
    color: {TEXT};
}}


/* METRICS */

[data-testid="stMetric"] {{
    background: rgba(255,255,255,0.035);
    border: 1px solid rgba(255,255,255,0.10);
    padding: 18px;
    min-height: 116px;
    overflow: visible !important;
}}

[data-testid="stMetricLabel"] p {{
    font-family: Arial, Helvetica, sans-serif !important;
    color: {MUTED} !important;
    font-size: 10px !important;
    line-height: 1.2 !important;
    font-weight: 700 !important;
    text-transform: uppercase;
    letter-spacing: 0.08em;
}}

[data-testid="stMetricValue"] {{
    color: {CREAM} !important;
    overflow: visible !important;
}}

[data-testid="stMetricValue"] > div {{
    font-family: Arial, Helvetica, sans-serif !important;
    color: {CREAM} !important;
    font-size: 2rem !important;
    line-height: 1.1 !important;
    white-space: normal !important;
    overflow: visible !important;
    text-overflow: clip !important;
}}


/* STRATEGIC SIGNAL CARD */

.signal-card {{
    background: rgba(255,255,255,0.035);
    border: 1px solid rgba(255,255,255,0.10);
    padding: 18px;
    min-height: 116px;
    box-sizing: border-box;
}}

.signal-label {{
    font-family: Arial, Helvetica, sans-serif !important;
    color: {MUTED};
    font-size: 10px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    margin-bottom: 15px;
}}

.signal-value {{
    font-family: Arial, Helvetica, sans-serif !important;
    color: {CREAM};
    font-size: 1.35rem;
    font-weight: 500;
    line-height: 1.15;
    white-space: normal;
}}


/* TABLE / EXPANDER */

[data-testid="stDataFrame"] {{
    border: 1px solid rgba(255,255,255,0.08);
}}

[data-testid="stExpander"] {{
    border-color: rgba(255,255,255,0.10) !important;
}}


hr {{
    border-color: rgba(255,255,255,0.10);
}}

</style>
""",
    unsafe_allow_html=True,
)


# ============================================================
# HELPERS
# ============================================================

def style_fig(fig, height=430, legend=True):

    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor=BG,
        plot_bgcolor=BG,
        font=dict(
            color=MUTED,
            family="Arial",
            size=12,
        ),
        height=height,
        margin=dict(
            l=20,
            r=20,
            t=40,
            b=30,
        ),
        showlegend=legend,
        hoverlabel=dict(
            bgcolor=PANEL,
            bordercolor="rgba(255,255,255,0.15)",
            font_color=CREAM,
        ),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1,
            font=dict(
                color=TEXT,
            ),
        ),
    )

    fig.update_xaxes(
        showgrid=False,
        zeroline=False,
        tickfont=dict(
            color=MUTED,
        ),
        title_font=dict(
            color=MUTED,
        ),
    )

    fig.update_yaxes(
        gridcolor=GRID,
        zeroline=False,
        tickfont=dict(
            color=MUTED,
        ),
        title_font=dict(
            color=MUTED,
        ),
    )

    return fig


def section(number, label):

    st.markdown(
        f"""
        <div class="section-number">
        {number} / {label}
        </div>
        """,
        unsafe_allow_html=True,
    )


def safe_money(value):

    try:
        if pd.isna(value):
            return "Price unavailable"

        return f"${float(value):,.2f}"

    except Exception:
        return "Price unavailable"


# ============================================================
# LOAD DATA
# ============================================================

@st.cache_data(show_spinner=False)
def load_data():

    products = pd.read_csv(
        "products_processed.csv",
        low_memory=False,
    )

    themes = pd.read_csv(
        "themes_processed.csv",
        low_memory=False,
    )

    segments = pd.read_csv(
        "segments_processed.csv",
        low_memory=False,
    )

    for frame in (
        products,
        themes,
        segments,
    ):

        frame["product_id"] = (
            frame["product_id"]
            .astype(str)
        )

    return products, themes, segments


required_files = [
    "products_processed.csv",
    "themes_processed.csv",
    "segments_processed.csv",
]


missing = [
    filename
    for filename in required_files
    if not os.path.exists(filename)
]


if missing:

    st.error(
        "Missing deployment file(s): "
        + ", ".join(missing)
    )

    st.stop()


products, themes, segments = load_data()


# ============================================================
# DISPLAY LABELS
# ============================================================

SIGNAL_DISPLAY = {
    "HERO PRODUCT": "PROVEN FAVORITE",
    "HIDDEN GEM": "HIDDEN GEM",
    "HYPE GAP": "EXPECTATION GAP",
    "LOW TRACTION": "LOWER TRACTION",
}


SIGNAL_COLORS = {
    "PROVEN FAVORITE": PROVEN,
    "HIDDEN GEM": HIDDEN,
    "EXPECTATION GAP": GAP,
    "LOWER TRACTION": LOW,
}


products["Signal_Display"] = (
    products["Consumer_Signal"]
    .map(SIGNAL_DISPLAY)
    .fillna(
        products["Consumer_Signal"]
    )
)


# ============================================================
# SIDEBAR FILTERS
# ============================================================

st.sidebar.markdown(
    "## Consumer Lens"
)


brands = (
    ["All Brands"]
    + sorted(
        products[
            "brand_name"
        ]
        .dropna()
        .astype(str)
        .unique()
        .tolist()
    )
)


brand = st.sidebar.selectbox(
    "Brand",
    brands,
)


brand_filtered = products.copy()


if brand != "All Brands":

    brand_filtered = brand_filtered[
        brand_filtered["brand_name"]
        == brand
    ]


categories = (
    ["All Categories"]
    + sorted(
        brand_filtered[
            "primary_category"
        ]
        .dropna()
        .astype(str)
        .unique()
        .tolist()
    )
)


category = st.sidebar.selectbox(
    "Category",
    categories,
)


category_filtered = (
    brand_filtered.copy()
)


if category != "All Categories":

    category_filtered = (
        category_filtered[
            category_filtered[
                "primary_category"
            ]
            == category
        ]
    )


signal_options = [
    "All Signals",
    "Proven Favorites",
    "Hidden Gems",
    "Expectation Gaps",
    "Lower Traction",
]


signal_reverse = {
    "Proven Favorites":
        "HERO PRODUCT",
    "Hidden Gems":
        "HIDDEN GEM",
    "Expectation Gaps":
        "HYPE GAP",
    "Lower Traction":
        "LOW TRACTION",
}


signal_filter = (
    st.sidebar.selectbox(
        "Strategic Signal",
        signal_options,
    )
)


filtered = (
    category_filtered.copy()
)


if signal_filter != "All Signals":

    filtered = filtered[
        filtered["Consumer_Signal"]
        == signal_reverse[
            signal_filter
        ]
    ]


if filtered.empty:

    st.warning(
        "No products match the selected filters."
    )

    st.stop()


# ============================================================
# PRODUCT EXPLORER
# ============================================================

st.sidebar.markdown("---")

st.sidebar.markdown(
    "### Explore a Product"
)


focus_options = [
    "Most Reviewed",
    "Highest Attention",
    "Proven Favorites",
    "Hidden Gems",
    "Expectation Gaps",
]


product_focus = (
    st.sidebar.selectbox(
        "Product shortlist",
        focus_options,
    )
)


shortlist = filtered.copy()


if product_focus == "Most Reviewed":

    shortlist = shortlist.sort_values(
        "Review_Count",
        ascending=False,
    )

elif product_focus == "Highest Attention":

    shortlist = shortlist.sort_values(
        "Attention_Index",
        ascending=False,
    )

elif product_focus == "Proven Favorites":

    shortlist = shortlist[
        shortlist["Consumer_Signal"]
        == "HERO PRODUCT"
    ].sort_values(
        "Review_Count",
        ascending=False,
    )

elif product_focus == "Hidden Gems":

    shortlist = shortlist[
        shortlist["Consumer_Signal"]
        == "HIDDEN GEM"
    ].sort_values(
        "Experience_Index",
        ascending=False,
    )

elif product_focus == "Expectation Gaps":

    shortlist = shortlist[
        shortlist["Consumer_Signal"]
        == "HYPE GAP"
    ].sort_values(
        "Attention_Index",
        ascending=False,
    )


if shortlist.empty:

    shortlist = filtered.sort_values(
        "Review_Count",
        ascending=False,
    )


shortlist = (
    shortlist
    .head(100)
    .copy()
)


shortlist["Selector_Label"] = (
    shortlist[
        "product_name"
    ]
    .fillna("Unknown Product")
    .astype(str)
    + " — "
    + shortlist[
        "brand_name"
    ]
    .fillna("Unknown Brand")
    .astype(str)
)


labels = (
    shortlist[
        "Selector_Label"
    ].tolist()
)


product_lookup = dict(
    zip(
        shortlist[
            "Selector_Label"
        ],
        shortlist[
            "product_id"
        ],
    )
)


selected_label = (
    st.sidebar.selectbox(
        "Product",
        labels,
    )
)


pid = (
    product_lookup[
        selected_label
    ]
)


st.sidebar.caption(
    f"Showing up to 100 products "
    f"from {len(filtered):,} matching products."
)


st.sidebar.markdown("---")


st.sidebar.caption(
    f"{len(products):,} products analyzed"
)


st.sidebar.caption(
    f"{int(products['Review_Count'].sum()):,} reviews represented"
)


st.sidebar.caption(
    "Full raw review data was pre-aggregated "
    "for fast portfolio deployment."
)


# ============================================================
# HEADER
# ============================================================

st.markdown(
    """
    <div class="eyebrow">
    02 / Consumer & Brand Strategy
    </div>
    """,
    unsafe_allow_html=True,
)


st.title(
    "Beauty Consumer Intelligence"
)


st.markdown(
    """
    <div class="intro">

    <b>
    When does product attention translate into consumer love —
    and when does it create an expectation gap?
    </b>

    <br><br>

    Combining product attention, consumer experience,
    review language and audience characteristics to identify
    proven favorites, hidden gems, expectation gaps,
    and the consumer friction behind them.

    </div>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# 01 — MARKET PULSE
# ============================================================

section(
    "01",
    "Market Pulse",
)


st.header(
    "Where is consumer attention going?"
)


c1, c2, c3, c4 = st.columns(4)


c1.metric(
    "Products in View",
    f"{len(filtered):,}",
)


c2.metric(
    "Consumer Reviews",
    f"{int(filtered['Review_Count'].sum()):,}",
)


c3.metric(
    "Average Rating",
    f"{filtered['Consumer_Rating'].mean():.2f} / 5",
)


c4.metric(
    "Recommendation Rate",
    f"{filtered['Recommendation_Rate'].mean():.1%}",
)


st.markdown(
    """
    <div class="metric-definition">

    <b>Relative Attention Index</b>
    combines two observable Sephora-platform signals:
    <b>Sephora loves (60%)</b>
    and
    <b>review volume (40%)</b>.

    Both are percentile-ranked across the analyzed portfolio.

    It represents relative observed product attention —
    not sales, market share, advertising spend,
    or brand awareness.

    </div>
    """,
    unsafe_allow_html=True,
)


top_attention = (
    filtered
    .nlargest(
        12,
        "Attention_Index",
    )
    .sort_values(
        "Attention_Index"
    )
)


fig = go.Figure()


fig.add_trace(
    go.Bar(
        x=top_attention[
            "Attention_Index"
        ],
        y=top_attention[
            "product_name"
        ],
        orientation="h",
        marker_color=ROSE,
        customdata=np.stack(
            (
                top_attention[
                    "brand_name"
                ],
                top_attention[
                    "loves_count"
                ],
                top_attention[
                    "Review_Count"
                ],
            ),
            axis=-1,
        ),
        hovertemplate=(
            "<b>%{y}</b>"
            "<br>%{customdata[0]}"
            "<br>Relative Attention Index: %{x:.2f}"
            "<br>Sephora Loves: %{customdata[1]:,.0f}"
            "<br>Reviews: %{customdata[2]:,.0f}"
            "<extra></extra>"
        ),
    )
)


style_fig(
    fig,
    height=520,
    legend=False,
)


fig.update_xaxes(
    title="Relative Attention Index",
    range=[0, 1.03],
)


fig.update_yaxes(
    title=None,
)


st.plotly_chart(
    fig,
    use_container_width=True,
    config=PLOT_CONFIG,
)


leader = filtered.loc[
    filtered[
        "Attention_Index"
    ].idxmax()
]


st.markdown(
    f"""
    <div class="insight-box">

    <b>Attention leader:</b>
    {leader['product_name']}
    by
    {leader['brand_name']}
    has the strongest relative attention signal
    in the selected view.

    The next question is whether that attention
    is matched by a similarly strong consumer experience.

    </div>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# 02 — ATTENTION VS EXPERIENCE
# ============================================================

section(
    "02",
    "Attention vs Experience",
)


st.header(
    "Does attention translate into consumer love?"
)


st.markdown(
    """
    <div class="framework-box">

        <div class="framework-title">
        How to read this framework
        </div>

        <div class="framework-row">

            <div class="framework-label">
            Relative Attention Index
            </div>

            <div class="framework-copy">
            60% Sephora-loves percentile +
            40% review-volume percentile.
            Measures relative observed product attention
            within the analyzed portfolio.
            </div>

        </div>


        <div class="framework-row">

            <div class="framework-label">
            Consumer Experience Index
            </div>

            <div class="framework-copy">
            55% normalized average rating +
            30% recommendation rate +
            15% share of reviews rated 4–5 stars.
            </div>

        </div>


        <div class="framework-row">

            <div class="framework-label">
            Strategic classification
            </div>

            <div class="framework-copy">
            Products are classified relative to the
            portfolio median on both dimensions.
            Bubble size represents review volume.
            </div>

        </div>

    </div>
    """,
    unsafe_allow_html=True,
)


att_cut = (
    products[
        "Attention_Index"
    ].median()
)


exp_cut = (
    products[
        "Experience_Index"
    ].median()
)


plot_df = filtered.copy()


fig = px.scatter(
    plot_df,
    x="Attention_Index",
    y="Experience_Index",
    size="Review_Count",
    color="Signal_Display",
    color_discrete_map=SIGNAL_COLORS,
    hover_name="product_name",
    hover_data={
        "brand_name": True,
        "Consumer_Rating": ":.2f",
        "Recommendation_Rate": ":.1%",
        "Review_Count": ":,.0f",
        "Attention_Index": ":.2f",
        "Experience_Index": ":.2f",
        "Signal_Display": False,
    },
    labels={
        "Attention_Index":
            "Relative Attention Index",
        "Experience_Index":
            "Consumer Experience Index",
        "Signal_Display":
            "Strategic Signal",
    },
    size_max=30,
)


fig.add_vline(
    x=att_cut,
    line_dash="dash",
    line_color=MUTED,
    opacity=0.8,
)


fig.add_hline(
    y=exp_cut,
    line_dash="dash",
    line_color=MUTED,
    opacity=0.8,
)


annotations = [
    (
        0.98,
        0.97,
        "PROVEN FAVORITES",
        PROVEN,
        "right",
    ),
    (
        0.02,
        0.97,
        "HIDDEN GEMS",
        HIDDEN,
        "left",
    ),
    (
        0.98,
        0.05,
        "EXPECTATION GAP",
        GAP,
        "right",
    ),
    (
        0.02,
        0.05,
        "LOWER TRACTION",
        LOW,
        "left",
    ),
]


for (
    x,
    y,
    text,
    color,
    anchor,
) in annotations:

    fig.add_annotation(
        x=x,
        y=y,
        xref="paper",
        yref="paper",
        text=text,
        showarrow=False,
        xanchor=anchor,
        font=dict(
            size=10,
            color=color,
        ),
    )


style_fig(
    fig,
    height=620,
    legend=True,
)


fig.update_layout(
    legend_title_text="Strategic Signal",
)


st.plotly_chart(
    fig,
    use_container_width=True,
    config=PLOT_CONFIG,
)


counts = (
    filtered[
        "Consumer_Signal"
    ]
    .value_counts()
)


st.markdown(
    f"""
    <div class="insight-box">

    <b>Portfolio read:</b>
    the selected view contains

    <b>{counts.get('HERO PRODUCT', 0)}
    proven favorites</b>,

    <b>{counts.get('HIDDEN GEM', 0)}
    hidden gems</b>,

    <b>{counts.get('HYPE GAP', 0)}
    expectation-gap products</b>,

    and

    <b>{counts.get('LOW TRACTION', 0)}
    lower-traction products</b>.

    These are relative portfolio classifications,
    not claims about absolute commercial performance.

    </div>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# 03 — BRAND INTELLIGENCE
# ============================================================

section(
    "03",
    "Brand Intelligence",
)


st.header(
    "Which brands convert product attention into consumer experience?"
)


brand_summary = (
    filtered
    .groupby(
        "brand_name"
    )
    .agg(
        Products=(
            "product_id",
            "nunique",
        ),
        Reviews=(
            "Review_Count",
            "sum",
        ),
        Attention=(
            "Attention_Index",
            "mean",
        ),
        Experience=(
            "Experience_Index",
            "mean",
        ),
        Rating=(
            "Consumer_Rating",
            "mean",
        ),
        Recommendation=(
            "Recommendation_Rate",
            "mean",
        ),
    )
    .reset_index()
)


brand_summary = (
    brand_summary[
        brand_summary[
            "Products"
        ]
        >= 2
    ]
)


if brand_summary.empty:

    st.info(
        "The selected filters do not contain "
        "enough multi-product brands for comparison."
    )

else:

    fig = px.scatter(
        brand_summary,
        x="Attention",
        y="Experience",
        size="Reviews",
        hover_name="brand_name",
        hover_data={
            "Products": True,
            "Reviews": ":,.0f",
            "Rating": ":.2f",
            "Recommendation": ":.1%",
            "Attention": ":.2f",
            "Experience": ":.2f",
        },
        labels={
            "Attention":
                "Average Relative Attention Index",
            "Experience":
                "Average Consumer Experience Index",
        },
        size_max=30,
    )


    fig.update_traces(
        marker=dict(
            color="#B8AEA3",
            opacity=0.78,
            line=dict(
                width=1,
                color=CREAM,
            ),
        )
    )


    style_fig(
        fig,
        height=520,
        legend=False,
    )


    st.plotly_chart(
        fig,
        use_container_width=True,
        config=PLOT_CONFIG,
    )


    strongest_experience = (
        brand_summary.loc[
            brand_summary[
                "Experience"
            ].idxmax()
        ]
    )


    strongest_attention = (
        brand_summary.loc[
            brand_summary[
                "Attention"
            ].idxmax()
        ]
    )


    st.markdown(
        f"""
        <div class="insight-box">

        <b>Brand signal:</b>
        among brands with at least two products
        in the selected view,

        <b>{strongest_experience['brand_name']}</b>
        has the strongest average
        consumer-experience index,

        while

        <b>{strongest_attention['brand_name']}</b>
        has the strongest average
        relative-attention index.

        This distinction helps separate
        <b>being noticed</b>
        from
        <b>delivering a strong consumer experience</b>.

        </div>
        """,
        unsafe_allow_html=True,
    )


# ============================================================
# SELECTED PRODUCT
# ============================================================

selected_rows = (
    products[
        products[
            "product_id"
        ]
        == pid
    ]
)


if selected_rows.empty:
    st.stop()


sel = selected_rows.iloc[0]


# ============================================================
# 04 — PRODUCT DEEP DIVE
# ============================================================

section(
    "04",
    "Product Deep Dive",
)


st.header(
    sel["product_name"]
)


st.markdown(
    f"""
    <div class="small-note">

    {sel['brand_name']}
    &nbsp;&nbsp;·&nbsp;&nbsp;
    {sel.get('primary_category', 'Category unavailable')}
    &nbsp;&nbsp;·&nbsp;&nbsp;
    {safe_money(sel.get('price_usd', np.nan))}

    </div>
    """,
    unsafe_allow_html=True,
)


d1, d2, d3, d4 = st.columns(4)


signal_name = (
    SIGNAL_DISPLAY.get(
        sel["Consumer_Signal"],
        sel["Consumer_Signal"],
    )
)


with d1:

    st.markdown(
        f"""
        <div class="signal-card">

            <div class="signal-label">
            Strategic Signal
            </div>

            <div class="signal-value">
            {signal_name}
            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )


d2.metric(
    "Consumer Rating",
    f"{sel['Consumer_Rating']:.2f} / 5",
)


d3.metric(
    "Recommendation",
    f"{sel['Recommendation_Rate']:.1%}",
)


d4.metric(
    "Reviews",
    f"{sel['Review_Count']:,.0f}",
)


st.markdown(
    f"""
    <div class="insight-box">

    <b>Product position:</b>
    this product has a
    <b>{sel['Attention_Index']:.2f}</b>
    Relative Attention Index

    and a

    <b>{sel['Experience_Index']:.2f}</b>
    Consumer Experience Index.

    It is therefore classified as

    <b>{signal_name}</b>

    relative to the analyzed portfolio.

    </div>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# 05 — CONSUMER LANGUAGE
# ============================================================

section(
    "05",
    "Consumer Language",
)


st.header(
    "What do consumers love — and where does experience break?"
)


st.markdown(
    """
    <div class="method-note">

    Themes are identified through transparent
    keyword dictionaries applied to review text.

    <b>Positive-rated share</b>
    means the percentage of reviews mentioning a theme
    that received a 4–5 star rating.

    <b>Negative-rated share</b>
    means the percentage of reviews mentioning a theme
    that received a 1–2 star rating.

    These measures identify themes associated with
    stronger or weaker review experiences;
    they do not prove that every mention itself
    was positive or negative.

    </div>
    """,
    unsafe_allow_html=True,
)


product_themes = (
    themes[
        themes[
            "product_id"
        ]
        == pid
    ]
    .copy()
)


minimum_mentions = max(
    3,
    int(
        sel["Review_Count"]
        * 0.01
    ),
)


product_themes = (
    product_themes[
        product_themes[
            "Mentions"
        ]
        >= minimum_mentions
    ]
)


if product_themes.empty:

    st.info(
        "No recurring review themes pass "
        "the minimum mention threshold."
    )

else:

    love = (
        product_themes
        .sort_values(
            [
                "Positive_Share",
                "Mentions",
            ],
            ascending=[
                False,
                False,
            ],
        )
        .head(5)
        .sort_values(
            "Positive_Share"
        )
    )


    friction = (
        product_themes
        .sort_values(
            [
                "Negative_Share",
                "Mentions",
            ],
            ascending=[
                False,
                False,
            ],
        )
        .head(5)
        .sort_values(
            "Negative_Share"
        )
    )


    left, right = st.columns(2)


    with left:

        st.subheader(
            "Love Drivers"
        )

        fig = go.Figure()

        fig.add_trace(
            go.Bar(
                x=love[
                    "Positive_Share"
                ],
                y=love[
                    "Theme"
                ],
                orientation="h",
                marker_color=SAGE,
                customdata=love[
                    "Mentions"
                ],
                hovertemplate=(
                    "<b>%{y}</b>"
                    "<br>Positive-rated share: %{x:.1%}"
                    "<br>Theme mentions: %{customdata:,}"
                    "<extra></extra>"
                ),
            )
        )


        style_fig(
            fig,
            height=340,
            legend=False,
        )


        fig.update_xaxes(
            tickformat=".0%",
            title=(
                "% of theme mentions "
                "in 4–5 star reviews"
            ),
            range=[
                0,
                1,
            ],
        )


        fig.update_yaxes(
            title=None,
        )


        st.plotly_chart(
            fig,
            use_container_width=True,
            config=PLOT_CONFIG,
        )


    with right:

        st.subheader(
            "Friction Drivers"
        )

        fig = go.Figure()


        fig.add_trace(
            go.Bar(
                x=friction[
                    "Negative_Share"
                ],
                y=friction[
                    "Theme"
                ],
                orientation="h",
                marker_color=GAP,
                customdata=friction[
                    "Mentions"
                ],
                hovertemplate=(
                    "<b>%{y}</b>"
                    "<br>Negative-rated share: %{x:.1%}"
                    "<br>Theme mentions: %{customdata:,}"
                    "<extra></extra>"
                ),
            )
        )


        style_fig(
            fig,
            height=340,
            legend=False,
        )


        fig.update_xaxes(
            tickformat=".0%",
            title=(
                "% of theme mentions "
                "in 1–2 star reviews"
            ),
        )


        fig.update_yaxes(
            title=None,
        )


        st.plotly_chart(
            fig,
            use_container_width=True,
            config=PLOT_CONFIG,
        )


    love_leader = (
        love.loc[
            love[
                "Positive_Share"
            ].idxmax()
        ]
    )


    friction_leader = (
        friction.loc[
            friction[
                "Negative_Share"
            ].idxmax()
        ]
    )


    st.markdown(
        f"""
        <div class="insight-box">

        <b>Review-language signal:</b>
        <b>{love_leader['Theme']}</b>
        has the strongest association
        with positive-rated reviews
        among the recurring themes shown.

        The strongest friction signal is

        <b>{friction_leader['Theme']}</b>.

        </div>
        """,
        unsafe_allow_html=True,
    )


# ============================================================
# 06 — CONSUMER DIFFERENCES
# ============================================================

section(
    "06",
    "Consumer Differences",
)


st.header(
    "Does product experience differ by reviewer skin type?"
)


skin = (
    segments[
        (
            segments[
                "product_id"
            ]
            == pid
        )
        &
        (
            segments[
                "Reviews"
            ]
            >= 10
        )
    ]
    .copy()
)


skin = skin.sort_values(
    "Rating",
    ascending=True,
)


if len(skin) >= 2:

    fig = go.Figure()


    fig.add_shape(
        type="line",
        x0=sel[
            "Consumer_Rating"
        ],
        x1=sel[
            "Consumer_Rating"
        ],
        y0=-0.5,
        y1=len(skin) - 0.5,
        line=dict(
            color=MUTED,
            width=1,
            dash="dash",
        ),
    )


    fig.add_trace(
        go.Scatter(
            x=skin[
                "Rating"
            ],
            y=skin[
                "skin_type"
            ],
            mode="markers+text",
            marker=dict(
                size=15,
                color=BLUE,
                line=dict(
                    color=CREAM,
                    width=1,
                ),
            ),
            text=[
                f"{rating:.2f} · n={int(n):,}"
                for rating, n
                in zip(
                    skin[
                        "Rating"
                    ],
                    skin[
                        "Reviews"
                    ],
                )
            ],
            textposition="middle right",
            textfont=dict(
                color=TEXT,
                size=11,
            ),
            customdata=np.stack(
                (
                    skin[
                        "Reviews"
                    ],
                    skin[
                        "Recommendation"
                    ],
                ),
                axis=-1,
            ),
            hovertemplate=(
                "<b>%{y}</b>"
                "<br>Average rating: %{x:.2f} / 5"
                "<br>Reviews: %{customdata[0]:,.0f}"
                "<br>Recommendation: %{customdata[1]:.1%}"
                "<extra></extra>"
            ),
        )
    )


    style_fig(
        fig,
        height=380,
        legend=False,
    )


    fig.update_xaxes(
        title="Average rating (fixed 1–5 scale)",
        range=[
            1,
            5.15,
        ],
        tickvals=[
            1,
            2,
            3,
            4,
            5,
        ],
    )


    fig.update_yaxes(
        title=None,
    )


    st.plotly_chart(
        fig,
        use_container_width=True,
        config=PLOT_CONFIG,
    )


    strongest_skin = (
        skin.loc[
            skin[
                "Rating"
            ].idxmax()
        ]
    )


    weakest_skin = (
        skin.loc[
            skin[
                "Rating"
            ].idxmin()
        ]
    )


    gap = (
        strongest_skin[
            "Rating"
        ]
        -
        weakest_skin[
            "Rating"
        ]
    )


    st.markdown(
        f"""
        <div class="insight-box">

        <b>Audience signal:</b>
        among reviewer skin types with at least 10 reviews,

        <b>{strongest_skin['skin_type']}</b>
        reviewers report the highest average rating
        ({strongest_skin['Rating']:.2f}/5),

        compared with

        <b>{weakest_skin['skin_type']}</b>
        reviewers at
        {weakest_skin['Rating']:.2f}/5.

        The observed difference is
        <b>{gap:.2f} rating points</b>.

        This is descriptive evidence
        and should not be interpreted as causal.

        </div>
        """,
        unsafe_allow_html=True,
    )


else:

    st.info(
        "This product does not have enough "
        "skin-type observations for comparison."
    )


# ============================================================
# 07 — STRATEGIC IMPLICATION
# ============================================================

section(
    "07",
    "Strategic Implication",
)


st.header(
    "What should the brand investigate next?"
)


signal = (
    sel[
        "Consumer_Signal"
    ]
)


actions = {

    "HERO PRODUCT": (
        "Protect the experience. Scale the proof.",
        """
        Relative attention is matched by a strong consumer experience.

        The strategic opportunity is to protect the attributes
        consumers already value, amplify credible consumer proof,
        and understand which experience drivers contribute most
        strongly to that performance.
        """,
    ),

    "HIDDEN GEM": (
        "The experience may be stronger than the attention.",
        """
        Consumers who reach this product report a relatively strong
        experience, while observed attention remains below the
        portfolio benchmark.

        That creates a case for testing stronger discovery,
        merchandising, sampling, creator support or positioning
        before assuming the product itself needs to change.
        """,
    ),

    "HYPE GAP": (
        "Diagnose the expectation gap before adding more attention.",
        """
        Observed attention is strong, but consumer experience sits
        below the portfolio benchmark.

        The priority should be to understand recurring friction,
        audience differences and expectation-setting issues
        before simply increasing awareness.
        """,
    ),

    "LOW TRACTION": (
        "Clarify the product's role.",
        """
        Both observed attention and consumer experience sit below
        the portfolio benchmark.

        The strategic question is whether the opportunity lies
        in repositioning, tighter audience targeting,
        product improvement or lower portfolio priority.
        """,
    ),
}


action_title, action_body = (
    actions[
        signal
    ]
)


st.markdown(
    f"""
    <div class="action-box">

    <h3>{action_title}</h3>

    {action_body}

    </div>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# 08 — PORTFOLIO PRIORITIES
# ============================================================

section(
    "08",
    "Portfolio Priorities",
)


st.header(
    "Which products deserve a closer look?"
)


st.markdown(
    """
    <div class="method-note">

    This is a prioritization view,
    not a sales ranking.

    Expectation-gap products appear first because
    they combine strong observed attention
    with weaker relative experience.

    Hidden gems appear next because they combine
    stronger relative experience with lower observed attention.

    </div>
    """,
    unsafe_allow_html=True,
)


priority_order = {
    "HYPE GAP": 1,
    "HIDDEN GEM": 2,
    "HERO PRODUCT": 3,
    "LOW TRACTION": 4,
}


table = filtered[
    [
        "product_name",
        "brand_name",
        "Consumer_Signal",
        "Consumer_Rating",
        "Recommendation_Rate",
        "Review_Count",
        "loves_count",
        "price_usd",
    ]
].copy()


table["Priority"] = (
    table[
        "Consumer_Signal"
    ]
    .map(
        priority_order
    )
)


table["Signal"] = (
    table[
        "Consumer_Signal"
    ]
    .map(
        SIGNAL_DISPLAY
    )
)


table = (
    table
    .sort_values(
        [
            "Priority",
            "Review_Count",
        ],
        ascending=[
            True,
            False,
        ],
    )
    .drop(
        columns=[
            "Priority",
            "Consumer_Signal",
        ]
    )
)


table = table[
    [
        "product_name",
        "brand_name",
        "Signal",
        "Consumer_Rating",
        "Recommendation_Rate",
        "Review_Count",
        "loves_count",
        "price_usd",
    ]
]


table.columns = [
    "Product",
    "Brand",
    "Strategic Signal",
    "Rating",
    "Recommendation",
    "Reviews",
    "Sephora Loves",
    "Price",
]


styled_table = (
    table.style.format(
        {
            "Rating":
                "{:.2f}",
            "Recommendation":
                "{:.1%}",
            "Reviews":
                "{:,.0f}",
            "Sephora Loves":
                "{:,.0f}",
            "Price":
                "${:,.2f}",
        }
    )
)


st.dataframe(
    styled_table,
    use_container_width=True,
    height=500,
    hide_index=True,
)


# ============================================================
# METHODOLOGY
# ============================================================

st.markdown("---")


with st.expander(
    "Methodology, definitions & limitations"
):

    st.markdown(
        """
### Relative Attention Index

The dataset does not contain verified sales,
advertising spend, market share or awareness data.

The **Relative Attention Index** combines:

- **60%:** percentile-ranked Sephora loves
- **40%:** percentile-ranked review volume


### Consumer Experience Index

The **Consumer Experience Index** combines:

- **55%:** normalized average consumer rating
- **30%:** recommendation rate
- **15%:** share of reviews receiving 4–5 stars


### Strategic classification

Products with at least 25 reviews are compared against
portfolio medians.

**Proven Favorite**  
Higher attention + higher experience

**Hidden Gem**  
Lower attention + higher experience

**Expectation Gap**  
Higher attention + lower experience

**Lower Traction**  
Lower attention + lower experience


### Consumer-language analysis

Review themes are identified using transparent
keyword dictionaries.

A theme's positive-rated share is the percentage
of reviews mentioning the theme that received 4–5 stars.

A theme's negative-rated share is the percentage
of reviews mentioning the theme that received 1–2 stars.


### Consumer differences

Skin-type comparisons use reviewer-reported skin type.

Displayed segments require at least 10 reviews.

These are descriptive associations,
not causal evidence.


### Commercial limitation

The source data does not provide verified:

- unit sales
- revenue
- market share
- advertising spend
- acquisition cost
- gross margin
- profitability

This project is therefore a
**consumer-intelligence and brand-strategy exercise**,
not a sales-performance model.
"""
    )


st.caption(
    "Portfolio project · Beauty Consumer Intelligence · "
    "Python / Pandas / Plotly / Streamlit"
)

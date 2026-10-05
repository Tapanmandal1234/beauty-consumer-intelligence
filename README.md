# Beauty Consumer Intelligence

An interactive consumer and brand intelligence application exploring when product attention translates into consumer love — and when it creates an expectation gap.

**Live Application:**  
https://beauty-consumer-intelligence.streamlit.app/

---

## Overview

Popular products are not necessarily the products delivering the strongest consumer experience.

This project analyzes Sephora product and review data to explore the relationship between:

- product attention
- consumer experience
- review language
- audience characteristics

The goal is to move beyond simple ratings and identify strategically different types of products:

- **Proven Favorites**
- **Hidden Gems**
- **Expectation Gaps**
- **Lower-Traction Products**

The application then helps diagnose *why* a product may occupy one of those positions by examining review themes and consumer differences.

---

## Business Question

**When does product attention translate into consumer love — and when does it create an expectation gap?**

The analysis is designed around a brand-strategy problem.

A highly visible product with a strong consumer experience represents a very different strategic situation from a highly visible product receiving weaker consumer feedback.

Likewise, a product with relatively limited attention but strong consumer experience may represent an under-recognized opportunity.

---

## Dataset

The analysis uses Sephora product and consumer review data containing:

- **1,873 products**
- **1,089,331 consumer reviews**

The raw review data was processed and aggregated into deployment-ready analytical datasets for the interactive application.

The source data includes information such as:

- product
- brand
- category
- price
- Sephora loves
- review volume
- consumer rating
- recommendation behavior
- review text
- reviewer-reported skin type

---

## Analytical Framework

The core framework evaluates products across two dimensions:

### Relative Attention Index

A relative measure of observed product attention within the analyzed Sephora portfolio.

The index combines:

- **60% — percentile-ranked Sephora loves**
- **40% — percentile-ranked review volume**

This is intentionally described as **relative attention**, not awareness or sales.

The dataset does not contain verified advertising spend, brand awareness, market share, or unit sales.

### Consumer Experience Index

A composite measure designed to capture the strength of the consumer experience.

The index combines:

- **55% — normalized average consumer rating**
- **30% — recommendation rate**
- **15% — share of reviews receiving 4–5 stars**

Together, these measures provide a broader view of consumer experience than average star rating alone.

---

## Strategic Product Classification

Products are compared with portfolio medians on both dimensions.

### Proven Favorite

**Higher Attention + Higher Consumer Experience**

The product is receiving substantial attention while also delivering a relatively strong consumer experience.

**Strategic question:**  
How can the brand protect what consumers value and scale credible consumer proof?

### Hidden Gem

**Lower Attention + Higher Consumer Experience**

Consumers who reach the product report a relatively strong experience, but observed attention remains below the portfolio benchmark.

**Strategic question:**  
Could stronger discovery, merchandising, sampling, creator support, or positioning unlock additional attention?

### Expectation Gap

**Higher Attention + Lower Consumer Experience**

The product receives substantial attention, but the consumer experience falls below the portfolio benchmark.

**Strategic question:**  
What friction or expectation-setting problem should be addressed before increasing attention further?

### Lower Traction

**Lower Attention + Lower Consumer Experience**

Both dimensions sit below the portfolio benchmark.

**Strategic question:**  
Does the product require repositioning, tighter targeting, product improvement, or lower portfolio priority?

---

## Consumer Language Analysis

The application goes beyond product-level scores by analyzing recurring themes within consumer reviews.

Review themes are identified using transparent keyword dictionaries.

Examples of themes can include aspects of the consumer experience such as:

- hydration
- texture
- scent
- packaging
- irritation
- value
- application

For each recurring theme, the application examines its association with stronger and weaker review outcomes.

### Positive-Rated Share

The percentage of reviews mentioning a theme that received a **4–5 star rating**.

### Negative-Rated Share

The percentage of reviews mentioning a theme that received a **1–2 star rating**.

These measures identify themes associated with stronger or weaker review experiences.

They are not sentence-level sentiment classification and do not imply that every individual mention of a theme was positive or negative.

---

## Consumer Differences

The application also examines whether product experience differs across reviewer-reported skin types.

Only segments with sufficient review observations are displayed.

This can reveal situations where the same product receives somewhat different experiences across consumer groups.

These comparisons are descriptive and should not be interpreted as causal relationships.

---

## Application Structure

The dashboard moves from portfolio-level intelligence to individual product diagnosis:

**01 — Market Pulse**  
Where is consumer attention going?

**02 — Attention vs Experience**  
Does attention translate into consumer love?

**03 — Brand Intelligence**  
Which brands convert attention into stronger consumer experience?

**04 — Product Deep Dive**  
How is an individual product positioned?

**05 — Consumer Language**  
What do consumers love — and where does experience break?

**06 — Consumer Differences**  
Does experience differ across consumer groups?

**07 — Strategic Implication**  
What should the brand investigate next?

**08 — Portfolio Priorities**  
Which products deserve closer attention?

---

## Tools & Technologies

- **Python**
- **Pandas**
- **NumPy**
- **Plotly**
- **Streamlit**
- Review-text analysis
- Consumer segmentation
- Composite index development
- Interactive data visualization

---

## Why I Built This

Many consumer analytics projects stop at identifying highly rated products or frequently mentioned review terms.

I wanted to approach the dataset from a more strategic perspective:

**Attention alone does not tell us whether consumers are satisfied, and satisfaction alone does not tell us whether a product is being discovered.**

Combining those dimensions creates a more useful framework for identifying different product opportunities and risks.

The review-language and consumer-segment analyses then provide additional context for understanding what may be driving those signals.

---

## Important Limitations

The source data does **not** provide verified:

- unit sales
- revenue
- market share
- advertising spend
- customer acquisition cost
- gross margin
- profitability

For that reason, the project does not claim to measure commercial performance.

It should be interpreted as a **consumer-intelligence and brand-strategy analysis**, not a sales or profitability model.

The strategic classifications are also relative to the analyzed portfolio rather than absolute measures of product success.

---

## Live Demo

Explore the interactive application here:

https://beauty-consumer-intelligence.streamlit.app/

---

## Author

**Tapan Mandal**
Built as a portfolio project demonstrating consumer analytics, brand strategy, review-text analysis, and decision-oriented data visualization.

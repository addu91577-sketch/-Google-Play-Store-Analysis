# Google Play Store Ecosystem Analysis & NLP Autocomplete/Autocorrect Analytics

[![GitHub Repository](https://img.shields.io/badge/GitHub-Repository-blue?logo=github)](https://github.com/addu91577-sketch/-Google-Play-Store-Analysis)

Comprehensive data analytics project covering real-world Android app market intelligence (Task 4) and natural language processing autocomplete & autocorrect algorithms (Task 5).

---

## 🗓️ 5-Day Project Roadmap & Execution Status

| Day | Date | Core Milestone | Focus & Deliverables | Git Commit Status |
| :--- | :--- | :--- | :--- | :--- |
| **Day 1** | **Mon, Oct 5** | **Task 4: Data Ingestion & Robust Cleaning Pipeline** | • Separate dataset ingestion (apps & reviews)<br>• Corrupted row shift resolution (row 10472)<br>• Type conversions (`Reviews`, `Installs`, `Price`, `Size_MB`)<br>• Deduplication prioritizing highest review count<br>• Cleaned datasets generation & pytest test suite | ✅ **Completed & Committed** (`7c6326b`) |
| **Day 2** | **Tue, Oct 6** | **Task 4: Category, Ratings & Size Market Analysis** | • App distribution bar chart (saturated vs niche sectors)<br>• Rating distribution analysis (KDE, box plots, category mean/median)<br>• Scatter plot of app size vs. installs with logarithmic scaling<br>• Pearson ($r$) and Spearman ($\rho$) correlation analysis<br>• Stratified correlation across 33 categories<br>• Modular script, pytest suite, and executed Jupyter notebook | ✅ **Completed & Committed** |
| **Day 3** | **Wed, Oct 7** | **Task 4: Pricing, Sentiment & Interactive Plotly Dashboard** | • Paid vs free app distribution & price curves<br>• Category revenue estimation (`Price * Installs`)<br>• Sentiment analysis using VADER & TextBlob<br>• Sentiment distribution by category<br>• Interactive Plotly bubble chart dashboard<br>• 3 strategic developer launch recommendations | ✅ **Completed & Verified** |
| **Day 4** | **Thu, Oct 8** | **Task 5: NLP Corpus Ingestion & Autocomplete Engine** | • Text corpus acquisition & preprocessing pipeline<br>• N-gram frequency language models (bigrams/trigrams)<br>• Top-3 word predictions across $\ge 10$ prompt prefixes<br>• Precision and recall metrics calculation<br>• Top 20 vocabulary frequency visualization | ⏳ Pending Day 4 Execution |
| **Day 5** | **Fri, Oct 9** | **Task 5: Autocorrect Implementation, Comparison & Metrics** | • Edit-distance autocorrect (Levenshtein + pyspellchecker)<br>• Deliberately misspelled test suite ($\ge 20$ words)<br>• Precision, recall, and accuracy evaluation<br>• Confusion matrix visualization<br>• Comparative evaluation vs production systems (Gboard) | ⏳ Pending Day 5 Execution |

---

## 🚀 Day 2 Milestones & Deliverables (Category, Ratings & Size Analysis)

### 1. Category Distribution & Market Saturation Analysis
Across 33 app categories in the 9,659 unique apps dataset:
- **Hyper-Saturated Sectors**:
  - `FAMILY`: **1,874 apps** (19.40% market share)
  - `GAME`: **946 apps** (9.79% market share)
  - `TOOLS`: **829 apps** (8.58% market share)
  - *Key Finding*: The top 3 categories account for **37.78%** of the entire catalog, while the top 5 represent nearly half (**46.22%**). New entrants face fierce organic keyword bidding and incumbent dominance.
- **Underserved Niche Opportunities**:
  - `BEAUTY` (53 apps, 0.55%), `COMICS` (56 apps, 0.58%), `PARENTING` (60 apps, 0.62%), `ART_AND_DESIGN` (61 apps, 0.63%), and `EVENTS` (64 apps, 0.66%).
  - *Strategic Advantage*: Lower App Store Optimization (ASO) barrier to entry with highly focused target audiences.

| Category Rank | Category Name | App Count | Market Share (%) | Cumulative Share (%) | Competitive Status |
| :---: | :--- | :---: | :---: | :---: | :--- |
| **1** | `FAMILY` | 1,874 | 19.40% | 19.40% | Hyper-Saturated |
| **2** | `GAME` | 946 | 9.79% | 29.20% | Hyper-Saturated |
| **3** | `TOOLS` | 829 | 8.58% | 37.78% | Hyper-Saturated |
| **4** | `BUSINESS` | 420 | 4.35% | 42.13% | Moderate Saturation |
| **5** | `MEDICAL` | 395 | 4.09% | 46.22% | Moderate Saturation |
| ... | ... | ... | ... | ... | ... |
| **29** | `EVENTS` | 64 | 0.66% | 97.62% | Niche Opportunity |
| **30** | `ART_AND_DESIGN` | 61 | 0.63% | 98.25% | Niche Opportunity |
| **31** | `PARENTING` | 60 | 0.62% | 98.87% | Niche Opportunity |
| **32** | `COMICS` | 56 | 0.58% | 99.45% | Niche Opportunity |
| **33** | `BEAUTY` | 53 | 0.55% | 100.00% | Niche Opportunity |

---

### 2. Rating Distribution & Category Performance

- **Rating Distribution Characteristics**:
  - **Sample Size**: 8,196 rated apps (84.85% coverage; 1,463 unrated apps).
  - **Mean Rating**: **4.173** | **Median Rating**: **4.300** | **Std Dev**: **0.536**.
  - **Interquartile Range (IQR)**: $[4.00, 4.50]$ ($\Delta = 0.50$).
  - **Skewness**: **-1.745** (Strong left-skewed distribution).
  - *Market Implication*: User rating inflation is pervasive. An app with a rating under **4.0** sits in the bottom quartile of the marketplace and suffers significant organic conversion and ranking penalties.
- **Top 5 Highest Rated Categories**:
  1. `EVENTS`: Mean **4.436** (Median: 4.5, Coverage: 70.3%)
  2. `ART_AND_DESIGN`: Mean **4.359** (Median: 4.4, Coverage: 96.7%)
  3. `EDUCATION`: Mean **4.355** (Median: 4.4, Std: **0.268** — most consistent quality in the store)
  4. `BOOKS_AND_REFERENCE`: Mean **4.345** (Median: 4.5, Coverage: 79.7%)
  5. `PERSONALIZATION`: Mean **4.332** (Median: 4.4, Coverage: 76.8%)
- **Bottom 5 Lowest Rated Categories**:
  1. `DATING`: Mean **3.980** (Median: 4.1, Std: 0.629 — *only category in the store with mean < 4.0*)
  2. `MAPS_AND_NAVIGATION`: Mean **4.036** (Median: 4.2, Std: 0.527)
  3. `TOOLS`: Mean **4.040** (Median: 4.2, Std: 0.619 — extreme polarity between reliable utilities and ad-heavy malware)
  4. `VIDEO_PLAYERS`: Mean **4.045** (Median: 4.2, Std: 0.562)
  5. `TRAVEL_AND_LOCAL`: Mean **4.070** (Median: 4.2, Std: 0.532)

---

### 3. App Size vs. Number of Installs Correlation Analysis

- **Hypothesis Evaluation**:
  - *Naive Assumption*: Users prefer smaller downloads due to storage/data constraints, resulting in a negative correlation.
  - *Empirical Finding*: **Statistically significant positive correlation** between binary size and installs!
- **Correlation Metrics ($n = 8,431$ apps with explicit sizes)**:
  - **Pearson Linear Correlation ($r$)**: $+0.1342$ ($p = 3.46 \times 10^{-35}$)
  - **Spearman Rank Correlation ($\rho$)**: **$+0.3101$** ($p = 2.13 \times 10^{-187}$)
  - **Pearson with $\log_{10}(\text{Installs})$**: $+0.2998$ ($p = 1.26 \times 10^{-174}$)
- **The "Feature Richness" Paradox**:
  - Top-tier apps that achieve 10M+, 100M+, and 1B+ installs invest heavily in multi-architecture native binaries, asset bundles, localization files, and extensive functionality.
  - With widespread high-speed broadband and 4G/5G, consumers tolerate larger APK sizes when apps provide rich, stable experiences.

#### Stratified Category-Level Correlations:
Correlation varies substantially by domain:
- **Strongest Positive Dependency**: `SHOPPING` ($\rho = +0.578$), `ART_AND_DESIGN` ($\rho = +0.552$), `PHOTOGRAPHY` ($\rho = +0.459$), `FAMILY` ($\rho = +0.450$), `GAME` ($\rho = +0.349$).
- **Zero / Neutral Dependency**: `PRODUCTIVITY` ($\rho = +0.001$), `MEDICAL` ($\rho = -0.004$), `PERSONALIZATION` ($\rho = -0.016$), `TOOLS` ($\rho = +0.085$). In utility sectors, users prioritize speed and simplicity over bundled bloatware.


---

## 🚀 Day 3 Milestones & Deliverables (Pricing, Revenue & Sentiment Analysis)

### 1. Pricing Structure & Paid vs. Free Market Dynamics
Across the 9,659 unique apps catalog:
- **Free vs. Paid App Split**:
  - **Free Apps**: **8,905 apps** (**92.19%** of the entire catalog)
  - **Paid Apps**: **754 apps** (**7.81%** of the catalog)
- **Paid App Price Distribution**:
  - **Mean Price**: **$14.06** | **Median Price**: **$2.99** | **Std Dev**: **$58.82**
  - **Interquartile Range (IQR)**: $[$1.49, $4.99$] ($\Delta = \$3.50$)
  - **Price Range**: Min **$0.99** to Max **$400.00**
  - *Key Structural Finding*: **79.0%** of all paid software in the marketplace clusters strictly below **$5.00**. Upfront software pricing experiences severe customer resistance beyond the $4.99 psychological threshold.
- **Price Elasticity Tiers**:
  - **Tier 1 ($0.99 – $1.99)**: 280 apps (37.1% of paid) — impulse buy micro-pricing.
  - **Tier 2 ($2.00 – $4.99)**: 316 apps (41.9% of paid) — standard utility & premium indie game pricing.
  - **Tier 3 ($5.00 – $9.99)**: 83 apps (11.0% of paid) — prosumer utilities and major studio ports.
  - **Tier 4 ($10.00 – $29.99)**: 46 apps (6.1% of paid) — specialized medical/enterprise software.
  - **Tier 5 ($30.00+)**: 29 apps (3.8% of paid) — luxury status apps (e.g., "I Am Rich" $399.99 novelty apps).

---

### 2. Category Gross Revenue Modeling & Top Earners
Using the standard market intelligence proxy:
$$\text{Estimated Gross Revenue} = \text{Price} \times \text{Installs}$$
- **Total Store Estimated Paid Gross Revenue**: **$291.18 Million USD**.
- **Top 5 Revenue-Generating Categories**:
  1. `FAMILY`: **$115.67M** (39.73% revenue share; 184 paid apps) — driven by dominant educational/family software.
  2. `LIFESTYLE`: **$57.58M** (19.78% share; 19 paid apps) — inflated by high-ticket status apps alongside legitimate lifestyle trackers.
  3. `GAME`: **$40.69M** (13.98% share; 82 paid apps) — high install velocity multipliers.
  4. `FINANCE`: **$25.73M** (8.84% share; 17 paid apps) — investment calculators and portfolio trackers.
  5. `PHOTOGRAPHY`: **$8.55M** (2.94% share; 19 paid apps) — professional editing tool suites.
- **Top 5 Highest Grossing Paid Titles**:
  1. `Minecraft` (`FAMILY`): **$69.90M** ($6.99 price × 10M+ installs)
  2. `I am rich` (`LIFESTYLE`): **$40.00M** ($399.99 price × 100k+ installs)
  3. `I Am Rich Premium` (`FINANCE`): **$20.00M** ($399.99 price × 50k+ installs)
  4. `Hitman Sniper` (`GAME`): **$9.90M** ($0.99 price × 10M+ installs)
  5. `Grand Theft Auto: San Andreas` (`GAME`): **$6.99M** ($6.99 price × 1M+ installs)

---

### 3. Multi-Engine Sentiment Analysis (VADER & TextBlob)
Benchmarking 29,692 cleaned user reviews across 816 apps and all 33 categories using **TextBlob** (lexicon-based polarity $[-1, +1]$ and subjectivity $[0, 1]$) and **NLTK VADER** (Valence Aware Dictionary and sEntiment Reasoner):
- **Sentiment Classification Distribution**:
  - **VADER Engine**: **63.7% Positive** (18,913), **14.4% Neutral** (4,281), **21.9% Negative** (6,498).
  - **TextBlob Engine**: **64.0% Positive** (19,015), **14.7% Neutral** (4,356), **21.3% Negative** (6,321).
  - **Multi-Engine Agreement Rate**: **65.5%** direct label match. VADER exhibits higher sensitivity to conversational idioms, sarcasm, and mobile slang.
- **Top 5 Highest Delight Categories (Highest Mean VADER Compound)**:
  1. `AUTO_AND_VEHICLES`: **+0.510** (VADER Pos: 67.8%, Neg: 10.9%)
  2. `PARENTING`: **+0.453** (VADER Pos: 65.6%, Neg: 9.0%)
  3. `EDUCATION`: **+0.449** (VADER Pos: 66.8%, Neg: 12.1%)
  4. `EVENTS`: **+0.443** (VADER Pos: 67.5%, Neg: 10.8%)
  5. `ART_AND_DESIGN`: **+0.437** (VADER Pos: 65.5%, Neg: 10.5%)
- **Top 4 Structural Friction Categories (Lowest Mean VADER Compound)**:
  1. `DATING`: **+0.144** (VADER Neg: **28.4%** — highest negative review share in the store; mean rating 3.98).
  2. `MAPS_AND_NAVIGATION`: **+0.231** (VADER Neg: **23.1%** — battery drain, routing errors).
  3. `GAME`: **+0.245** (VADER Neg: **24.5%** — aggressive monetization, pay-to-win backlash).
  4. `TOOLS`: **+0.252** (VADER Neg: **24.3%** — invasive full-screen advertising and permissions).

---

### 4. Strategic Market Opportunity Matrix & Interactive Dashboard
Combining Category Volume, User Ratings, Install Scale, Gross Revenue, and Review Sentiment into a **33-category Opportunity Matrix**:
- **Opportunity Score Ranking (0–100 Scale)**:
  - **#1** `EDUCATION` (**76.9** / 100) — High rating (4.35), high sentiment (+0.449), low volatility ($\sigma=0.268$).
  - **#2** `PARENTING` (**76.8** / 100) — Low market saturation (60 apps), high user loyalty (+0.453 sentiment).
  - **#3** `ART_AND_DESIGN` (**75.9** / 100) — High delight (+0.437), low competition (61 apps), strong size correlation ($\rho=+0.552$).
  - **#4** `EVENTS` (**72.7** / 100) — Store's highest average rating (4.44), pristine sentiment (+0.443).
  - **#5** `AUTO_AND_VEHICLES` (**72.3** / 100) — Store's highest mean sentiment (+0.510).
- **Quadrant Mapping**:
  - **Quadrant I (Delight Sweet Spot)**: High rating & high sentiment (`EDUCATION`, `ART_AND_DESIGN`, `EVENTS`, `HEALTH_AND_FITNESS`).
  - **Quadrant II (Latent Review Friction)**: High rating but declining review sentiment (`PERSONALIZATION`, `LIFESTYLE`).
  - **Quadrant III (Niche Execution Gaps)**: Moderate rating with passionate sentiment pockets (`AUTO_AND_VEHICLES`, `COMICS`).
  - **Quadrant IV (Red Ocean / Churn Risk)**: Low rating & low sentiment (`DATING`, `TOOLS`, `MAPS_AND_NAVIGATION`).

---

### 5. 💡 Three Strategic Developer Launch Recommendations

1. **REC-01: Target High-Delight Niche Sectors with Upfront Paid Pricing ($1.99 – $3.99)**
   - *Targets*: `EVENTS`, `ART_AND_DESIGN`, `PARENTING`, `AUTO_AND_VEHICLES`.
   - *Rationale*: Low competition (<65 apps each) combined with top-decile sentiment (+0.43 to +0.51) drastically lowers organic acquisition costs (CAC). Users in these utility niches demonstrate willingness to pay upfront for clean, ad-free workflows.
2. **REC-02: Adopt Freemium-First Monetization in Massive Scale Categories**
   - *Targets*: `GAME`, `FAMILY`, `PHOTOGRAPHY`, `TOOLS`.
   - *Rationale*: Free apps account for 92.2% of the catalog and >98% of downloads. Upfront paid pricing faces extreme friction without established intellectual property. Monetize through hybrid free downloads with rewarded opt-in ads and tiered in-app purchases ($0.99, $2.99, $4.99).
3. **REC-03: Disrupt Structural Friction Sectors by Eliminating Incumbent Pain Points**
   - *Targets*: `DATING`, `TOOLS`, `MAPS_AND_NAVIGATION`.
   - *Rationale*: Incumbents suffer from poor ratings (<4.05) and heavy negative review volume (up to 28.4% negative) due to invasive monetization and privacy intrusion. A transparent, privacy-first alternative entering with a 4.5+ rating can achieve rapid organic ranking advantages.

---

## 📁 Repository Structure

```
Google Playstore Analysis/
├── .gitignore                          # Ignored caches, environments, checkpoints
├── README.md                           # Project documentation & 5-day roadmap
├── requirements.txt                    # Project dependencies
├── Data/
│   ├── googleplaystore.csv             # Raw Play Store apps dataset
│   ├── googleplaystore_user_reviews.csv# Raw user reviews dataset
│   ├── license.txt                     # Dataset licensing
│   ├── cleaned_googleplaystore.csv     # Cleaned, deduplicated apps dataset (Day 1)
│   └── cleaned_user_reviews.csv        # Cleaned, deduplicated user reviews (Day 1)
├── notebooks/
│   ├── 01_playstore_data_cleaning.ipynb# Day 1: Interactive data cleaning notebook & audit
│   ├── 02_playstore_category_ratings_size_analysis.ipynb # Day 2: Category, Ratings & Size EDA
│   └── 03_playstore_pricing_sentiment_dashboard.ipynb   # Day 3: Pricing, Sentiment & Plotly Dashboard
├── reports/
│   ├── category_distribution_summary.csv   # Category market share data table (Day 2)
│   ├── category_ratings_summary.csv        # Category ratings benchmarks table (Day 2)
│   ├── stratified_correlations_summary.csv # Category-level size vs installs correlations (Day 2)
│   ├── category_revenue_summary.csv        # Category revenue estimation & monetization table (Day 3)
│   ├── top_revenue_apps_summary.csv        # Top grossing paid apps ranking (Day 3)
│   ├── category_sentiment_summary.csv      # Category sentiment polarity benchmarks table (Day 3)
│   ├── market_opportunity_matrix.csv       # Unified 33-category opportunity matrix & quadrants (Day 3)
│   └── figures/
│       ├── 01_category_distribution.png    # Saturated vs niche categories bar chart (Day 2)
│       ├── 02_rating_distributions.png     # Rating KDE & top 20 category box plots (Day 2)
│       ├── 03_size_vs_installs_scatter.png # Size vs installs log-scale scatter & trend (Day 2)
│       ├── 04_category_size_installs_correlations.png # Stratified Spearman correlation ranking (Day 2)
│       ├── 05_paid_vs_free_pricing.png     # Paid vs free distribution & price curve (Day 3)
│       ├── 06_category_revenue_estimation.png # Category revenue & paid catalog share (Day 3)
│       ├── 07_sentiment_distribution.png   # VADER vs TextBlob engine & polarity extremes (Day 3)
│       ├── 08_market_bubble_dashboard.png  # Publication 2D strategic opportunity bubble chart (Day 3)
│       └── 08_market_opportunity_dashboard.html # Interactive Plotly bubble chart dashboard (Day 3)
├── src/
│   ├── __init__.py                     # Package definition
│   ├── data_cleaning.py                # Day 1: Reusable data cleaning pipeline
│   ├── category_ratings_analysis.py    # Day 2: Category, ratings & correlation engine
│   └── pricing_sentiment_analysis.py   # Day 3: Pricing, sentiment & dashboard engine
└── tests/
    ├── test_cleaning.py                # Day 1: Data cleaning pytest suite (4 passed)
    ├── test_category_ratings.py        # Day 2: Category & ratings pytest suite (6 passed)
    └── test_pricing_sentiment.py       # Day 3: Pricing & sentiment pytest suite (8 passed)
```

---

## 🛠️ Installation & Verification

### 1. Set Up Environment
```bash
pip install -r requirements.txt
```

### 2. Run Data Cleaning & Analysis Pipelines
```bash
# Day 1 Cleaning Pipeline
python src/data_cleaning.py

# Day 2 Category, Ratings & Size Analysis Pipeline
python src/category_ratings_analysis.py

# Day 3 Pricing, Sentiment & Dashboard Pipeline
python src/pricing_sentiment_analysis.py
```

### 3. Run Automated Pytest Test Suite
```bash
# Execute entire test suite (18 passed across Day 1, Day 2, and Day 3)
pytest tests/ -v
```

### 4. Launch Jupyter Notebooks
```bash
jupyter notebook notebooks/01_playstore_data_cleaning.ipynb
jupyter notebook notebooks/02_playstore_category_ratings_size_analysis.ipynb
jupyter notebook notebooks/03_playstore_pricing_sentiment_dashboard.ipynb
```


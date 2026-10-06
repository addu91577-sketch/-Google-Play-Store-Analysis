# Google Play Store Ecosystem Analysis & NLP Autocomplete/Autocorrect Analytics

[![GitHub Repository](https://img.shields.io/badge/GitHub-Repository-blue?logo=github)](https://github.com/addu91577-sketch/-Google-Play-Store-Analysis)

Comprehensive data analytics project covering real-world Android app market intelligence (Task 4) and natural language processing autocomplete & autocorrect algorithms (Task 5).

---

## 🗓️ 5-Day Project Roadmap & Execution Status

| Day | Date | Core Milestone | Focus & Deliverables | Git Commit Status |
| :--- | :--- | :--- | :--- | :--- |
| **Day 1** | **Mon, Oct 5** | **Task 4: Data Ingestion & Robust Cleaning Pipeline** | • Separate dataset ingestion (apps & reviews)<br>• Corrupted row shift resolution (row 10472)<br>• Type conversions (`Reviews`, `Installs`, `Price`, `Size_MB`)<br>• Deduplication prioritizing highest review count<br>• Cleaned datasets generation & pytest test suite | ✅ **Completed & Committed** (`7c6326b`) |
| **Day 2** | **Tue, Oct 6** | **Task 4: Category, Ratings & Size Market Analysis** | • App distribution bar chart (saturated vs niche sectors)<br>• Rating distribution analysis (KDE, box plots, category mean/median)<br>• Scatter plot of app size vs. installs with logarithmic scaling<br>• Pearson ($r$) and Spearman ($\rho$) correlation analysis<br>• Stratified correlation across 33 categories<br>• Modular script, pytest suite, and executed Jupyter notebook | ✅ **Completed & Committed** |
| **Day 3** | **Wed, Oct 7** | **Task 4: Pricing, Sentiment & Interactive Plotly Dashboard** | • Paid vs free app distribution & price curves<br>• Category revenue estimation (`Price * Installs`)<br>• Sentiment analysis using VADER & TextBlob<br>• Sentiment distribution by category<br>• Interactive Plotly bubble chart dashboard<br>• 3 strategic developer launch recommendations | ⏳ Pending Day 3 Execution |
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
│   └── 02_playstore_category_ratings_size_analysis.ipynb # Day 2: Category, Ratings & Size EDA
├── reports/
│   ├── category_distribution_summary.csv # Category market share data table
│   ├── category_ratings_summary.csv      # Category ratings benchmarks table
│   ├── stratified_correlations_summary.csv # Category-level size vs installs correlations
│   └── figures/
│       ├── 01_category_distribution.png  # Saturated vs niche categories bar chart
│       ├── 02_rating_distributions.png   # Rating KDE & top 20 category box plots
│       ├── 03_size_vs_installs_scatter.png # Size vs installs log-scale scatter & trend
│       └── 04_category_size_installs_correlations.png # Stratified Spearman correlation ranking
├── src/
│   ├── __init__.py                     # Package definition
│   ├── data_cleaning.py                # Day 1: Reusable data cleaning pipeline
│   └── category_ratings_analysis.py    # Day 2: Category, ratings & correlation engine
└── tests/
    ├── test_cleaning.py                # Day 1: Data cleaning pytest suite (4 passed)
    └── test_category_ratings.py        # Day 2: Category & ratings pytest suite (6 passed)
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
```

### 3. Run Automated Pytest Test Suite
```bash
pytest tests/ -v
```

### 4. Launch Jupyter Notebooks
```bash
jupyter notebook notebooks/01_playstore_data_cleaning.ipynb
jupyter notebook notebooks/02_playstore_category_ratings_size_analysis.ipynb
```

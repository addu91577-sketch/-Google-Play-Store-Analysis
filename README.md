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
| **Day 4** | **Thu, Oct 8** | **Task 5: NLP Corpus Ingestion & Autocomplete Engine** | • Text corpus acquisition & preprocessing pipeline<br>• N-gram frequency language models (bigrams/trigrams)<br>• Top-3 word predictions across $\ge 10$ prompt prefixes<br>• Precision and recall metrics calculation<br>• Top 20 vocabulary frequency visualization | ✅ **Completed & Verified** |
| **Day 5** | **Fri, Oct 9** | **Task 5: Autocorrect Implementation, Comparison & Metrics** | • Edit-distance autocorrect (Levenshtein + pyspellchecker)<br>• Deliberately misspelled test suite ($\ge 20$ words)<br>• Precision, recall, and accuracy evaluation<br>• Confusion matrix visualization<br>• Comparative evaluation vs production systems (Gboard) | ✅ **Completed & Verified** |

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

## 🚀 Day 4 Milestones & Deliverables (NLP Corpus Ingestion & Autocomplete Engine)

### 1. Mobile Corpus Acquisition, Preprocessing & Lexical Dynamics
Ingesting 29,692 cleaned mobile app reviews from `Data/cleaned_user_reviews.csv`:
- **Corpus Summary Statistics**:
  - **Total Reviews**: **29,692** documents
  - **Total Extracted Sentences**: **79,179** valid sentence segments
  - **Total Lexical Tokens**: **506,418** words
  - **Unique Lexical Types ($|V|$)**: **20,344** unique words
  - **Type-Token Ratio (TTR)**: **0.0402** (indicating strong vocabulary repetition, highly conducive to statistical language modeling)
  - **Mean Sentence Length**: **6.40 tokens / sentence**

- **Lexical Frequency & Domain Stopword Segregation**:
  - **Top 10 Overall Tokens (Dominated by Subjectivity & Function Words)**:
    1. `i`: 24,871 (4.91%) | 2. `it`: 6,831 (1.35%) | 3. `game`: 6,427 (1.27%) | 4. `the`: 5,195 (1.03%) | 5. `good`: 4,122 (0.81%)
    6. `like`: 4,110 (0.81%) | 7. `app`: 3,957 (0.78%) | 8. `this`: 3,879 (0.77%) | 9. `great`: 3,786 (0.75%) | 10. `love`: 3,543 (0.70%)
  - **Top 10 Domain Content Keywords (Filtering Stopwords)**:
    1. `game` (6,427) — Primary leisure/entertainment product entity
    2. `good` (4,122) — Core positive appraisal modifier
    3. `like` (4,110) — Comparative preference and affective verb
    4. `app` (3,957) — General application product entity
    5. `great` (3,786) — High-valence positive descriptor
    6. `love` (3,543) — Strongest emotional engagement verb
    7. `get` (3,462) — Functional action verb
    8. `time` (3,375) — Latency, loading duration, and engagement metric
    9. `really` (2,338) — Evaluative intensifier
    10. `update` (1,970) — Lifecycle version release events and regressions
  - **Zipf's Law Empirical Validation**:
    $$\log_{10}(f) = \log_{10}(C) - s \cdot \log_{10}(r)$$
    The log-log regression across the top 500 vocabulary ranks yields a scaling slope $s = 1.02$ ($R^2 > 0.98$), demonstrating classical power-law Zipfian scaling in mobile app discourse.

---

### 2. Statistical N-Gram Language Modeling & Smoothing Formulations
Partitioning sentences into an **80% Training Set (63,343 sentences)** and a **20% Test Set (15,836 sentences)**:
- **Language Model N-Gram Scale**:
  - Total Unigram Tokens: **460,918**
  - Unique Bigram Transitions: **218,040**
  - Unique Trigram Transitions: **337,115**
  - Vocabulary Size ($|V|$): **18,034**

- **Mathematical Formulations & Architectures**:
  - **Unigram MLE**: $P_{\text{MLE}}(w_i) = \frac{C(w_i)}{N}$
  - **Bigram MLE**: $P_{\text{MLE}}(w_i \mid w_{i-1}) = \frac{C(w_{i-1}, w_i)}{C(w_{i-1})}$
  - **Trigram MLE**: $P_{\text{MLE}}(w_i \mid w_{i-2}, w_{i-1}) = \frac{C(w_{i-2}, w_{i-1}, w_i)}{C(w_{i-2}, w_{i-1})}$
  - **Add-$k$ Laplace Smoothing**:
    $$P_{\text{Laplace}}(w_i \mid w_{i-1}) = \frac{C(w_{i-1}, w_i) + k}{C(w_{i-1}) + k \cdot |V|}$$
  - **Jelinek-Mercer Linear Interpolation ($\lambda_3=0.6, \lambda_2=0.3, \lambda_1=0.1$)**:
    $$P_{\text{Interp}}(w_i \mid w_{i-2}, w_{i-1}) = \lambda_3 P_{\text{MLE}}(w_i \mid w_{i-2}, w_{i-1}) + \lambda_2 P_{\text{MLE}}(w_i \mid w_{i-1}) + \lambda_1 P_{\text{MLE}}(w_i)$$
  - **Google's Stupid Backoff Algorithm ($\alpha = 0.4$)**:
    $$S(w_i \mid w_{i-2}, w_{i-1}) = \begin{cases} \frac{C(w_{i-2}, w_{i-1}, w_i)}{C(w_{i-2}, w_{i-1})} & \text{if } C(w_{i-2}, w_{i-1}, w_i) > 0 \\ \alpha \frac{C(w_{i-1}, w_i)}{C(w_{i-1})} & \text{else if } C(w_{i-1}, w_i) > 0 \\ \alpha^2 \frac{C(w_i)}{N} & \text{otherwise} \end{cases}$$

---

### 3. Real-Time Top-3 Autocomplete Predictions Across 12 Prompt Prefixes
Using an indexed hash trie (`defaultdict(Counter)`) for sub-millisecond retrieval, the engine generates the following top-3 predictions:

| # | Prompt Prefix | Predicted Top 1 | Prob 1 (%) | Predicted Top 2 | Prob 2 (%) | Predicted Top 3 | Prob 3 (%) | Semantic Category |
| :-: | :--- | :--- | :---: | :--- | :---: | :--- | :---: | :--- |
| **1** | `"this app"` | `is` | 57.1% | `has` | 28.6% | `staff` | 14.3% | Copula State Evaluation |
| **2** | `"easy to"` | `use` | **92.6%** | `obtain` | 3.7% | `buy` | 3.7% | Usability Collocation |
| **3** | `"very good"` | `app` | 51.3% | `game` | 24.3% | `application` | 24.3% | Positive Quality Appraisal |
| **4** | `"thank you"` | `very` | 58.0% | `can't` | 22.1% | `need` | 19.9% | Gratitude Expression |
| **5** | `"i love"` | `game` | 41.6% | `it` | 29.4% | `app` | 29.0% | High-Delight Affection |
| **6** | `"please add"` | `feature` | 37.5% | `ability` | 31.2% | `option` | 31.2% | Feature Request |
| **7** | `"customer service"` | `i` | 50.0% | `could` | 25.0% | `extremely` | 25.0% | Support Interaction |
| **8** | `"waste of"` | `time` | **50.0%** | `app` | 25.0% | `my` | 25.0% | Friction / Complaint |
| **9** | `"great"` | `app` | 45.3% | `game` | 41.5% | `i` | 13.2% | General Praise |
| **10** | `"best app"` | `amount` | 33.3% | `for` | 33.3% | `ever` | 33.3% | Superlative Endorsement |
| **11** | `"too many"` | `ads` | **90.6%** | `problems` | 4.7% | `pop` | 4.7% | Monetization Friction |
| **12** | `"after the update"` | `terrible` | **50.0%** | `android` | 25.0% | `icon` | 25.0% | Release Regression |

---

### 4. Rigorous Empirical Evaluation Suite & Comparative Model Benchmarks
Benchmarking across held-out test contexts (3,000 sampled test instances, $V = 18,034$):

$$\text{Top-1 Accuracy} = \frac{1}{|D_{\text{test}}|} \sum \mathbb{I}(y = \hat{w}_1), \quad \text{Recall@3} = \frac{1}{|D_{\text{test}}|} \sum \mathbb{I}(y \in \hat{Y}_3), \quad \text{MRR} = \frac{1}{|D_{\text{test}}|} \sum \frac{1}{\text{rank}(y)}$$

| Model Configuration | Model Order ($n$) | Smoothing Strategy | Top-1 Accuracy (%) | Top-3 Recall / Hit Rate (%) | Precision@3 (%) | Mean Reciprocal Rank (MRR) | Test Perplexity ($PP$) |
| :--- | :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| **Unigram Baseline** | 1 | MLE Frequency | 3.27% | 5.60% | 1.87% | 0.0418 | 1,006.85 |
| **Bigram Model** | 2 | MLE Conditional | 8.63% | 15.60% | 5.20% | 0.1163 | 1,027.17 |
| **Trigram Model** | 3 | Pure MLE (Sparsity penalized) | 6.77% | 11.43% | 3.81% | 0.0881 | 4,239.07 |
| **Trigram (Laplace)** | 3 | Add-$k$ Laplace ($k=0.01$) | 6.77% | 11.43% | 3.81% | 0.0881 | 4,239.07 |
| **Trigram (Interpolation)** | 3 | Jelinek-Mercer ($\vec{\lambda}$) | **9.63%** | **16.73%** | **5.58%** | **0.1267** | 1,429.75 |
| **Trigram (Stupid Backoff)** | 3 | Stupid Backoff ($\alpha=0.4$) | 9.10% | 16.17% | 5.39% | 0.1218 | **923.21** |

#### Analytical Synthesis:
1. **The Power of Local Context**: Bigram MLE achieves a **+164% relative gain** over Unigrams (8.63% vs 3.27%), confirming that preceding lexical context drastically narrows the candidate search space.
2. **The Trigram Sparsity Barrier**: In natural language text, higher-order n-grams suffer from severe combinatorial sparsity. Unseen test trigrams cause Pure MLE Recall@3 to drop from 15.60% down to 11.43%.
3. **Interpolation & Backoff Dominance**: Jelinek-Mercer interpolation achieves the highest Top-3 Recall (**16.73%**) and highest MRR (**0.1267**), while Stupid Backoff achieves the lowest perplexity (**923.21**) with near-zero latency overhead.
4. **Outperforming Random Guessing**: In an 18,000-word vocabulary, random chance Top-3 hit rate is $\frac{3}{18,000} \approx 0.017\%$. Our n-gram models achieve a **~980x improvement** over random chance.

---

## 🚀 Day 5 Milestones & Deliverables (Autocorrect Implementation, Comparison & Metrics)

### 1. Algorithmic Formulations: Levenshtein vs. Damerau-Levenshtein Distance
In mobile typing environments, human keystroke errors follow physical keyboard layout and muscle memory patterns. We developed dynamic programming matrix engines for two fundamental string distance metrics:

- **Classical Levenshtein Distance ($O(|s_1| \cdot |s_2|)$)**:
  Permits three canonical unit-cost edit operations (Insertion, Deletion, and Substitution):
  $$\mathcal{D}_{\text{Lev}}(i, j) = \min \begin{cases} \mathcal{D}(i-1, j) + 1 & \text{(Deletion)} \\ \mathcal{D}(i, j-1) + 1 & \text{(Insertion)} \\ \mathcal{D}(i-1, j-1) + \mathbb{I}(s_1[i] \neq s_2[j]) & \text{(Substitution)} \end{cases}$$

- **Damerau-Levenshtein Distance with Adjacent Transposition**:
  Accounts for transposed adjacent letters ($ab \leftrightarrow ba$) as a **single operation** (cost = 1) rather than two independent edits:
  $$\mathcal{D}_{\text{Dam}}(i, j) = \min \begin{cases} \mathcal{D}_{\text{Lev}}(i, j) \\ \mathcal{D}(i-2, j-2) + 1 & \text{if } i, j > 1 \text{ and } s_1[i] = s_2[j-1] \text{ and } s_1[i-1] = s_2[j] \end{cases}$$

| Input Typo | Target Word | Typographical Mechanism | Classical Levenshtein | Damerau-Levenshtein | Distance Reduction |
| :--- | :--- | :--- | :---: | :---: | :---: |
| `"teh"` | `"the"` | Adjacent Transposition | **2** | **1** | **-50.0% (1 edit)** |
| `"udpate"` | `"update"` | Adjacent Transposition | **2** | **1** | **-50.0% (1 edit)** |
| `"amzaing"` | `"amazing"` | Adjacent Transposition | **2** | **1** | **-50.0% (1 edit)** |
| `"amzing"` | `"amazing"` | Omission (Deletion) | 1 | 1 | Identical |
| `"upddate"` | `"update"` | Key Bounce (Insertion) | 1 | 1 | Identical |
| `"updste"` | `"update"` | Fat-Finger (Substitution) | 1 | 1 | Identical |

---

### 2. Bayesian Prior Weighting & Mobile Vocabulary Formulation
Leveraging the **20,344 unique lexical types** extracted from the 29,692 Play Store reviews, the Bayesian Autocorrect Engine evaluates candidate words by computing the maximum a posteriori (MAP) estimate:

$$\hat{w} = \arg\max_{w \in V} P(w \mid c) = \arg\max_{w \in V} P(c \mid w) \cdot P(w)$$

Where:
- **Prior Probability $P(w)$**: Derived from domain frequency with Add-1 Laplace smoothing:
  $$P(w) = \frac{\text{Count}(w) + 1}{N + |V|}$$
- **Error Model Likelihood $P(c \mid w)$**: Geometric distance penalty modeling typographical channel noise:
  $$P(c \mid w) = (0.05)^{\mathcal{D}_{\text{Dam}}(c, w)}$$
- **Domain Advantage**: The Play Store corpus natively incorporates mobile app terminology (`playstore`, `fps`, `lag`, `unplayable`, `wifi`, `in-app`) preventing false rejections common to static generic dictionaries.

---

### 3. Deliberately Misspelled Benchmark Test Suite ($n = 33$ Words)
To rigorously evaluate autocorrect performance across all typographical failure modes, we assembled a 33-item benchmark corpus spanning 5 error categories plus clean controls:

| Error Category | Sample Count | Representative Injected Typo | Target Word | Edit Distance | Typographical Etiology |
| :--- | :---: | :--- | :--- | :---: | :--- |
| **Insertion** | 6 | `amazzing`, `upddate`, `graphiics`, `unplayyable`, `downloadd`, `reviiew` | `amazing`, `update`, `graphics`, `unplayable`, `download`, `review` | 1 | Repeated touch key bounce |
| **Deletion** | 6 | `amzing`, `grphics`, `updat`, `notifcation`, `connetion`, `downlod` | `amazing`, `graphics`, `update`, `notification`, `connection`, `download` | 1 | Fast typing character skip |
| **Substitution** | 6 | `amazung`, `updste`, `battrry`, `grafics`, `unpkayable`, `gake` | `amazing`, `update`, `battery`, `graphics`, `unplayable`, `game` | 1 | QWERTY physical key adjacency |
| **Transposition**| 6 | `amzaing`, `udpate`, `recieve`, `featrue`, `teh`, `palystore` | `amazing`, `update`, `receive`, `feature`, `the`, `playstore` | 1 (Dam) / 2 (Lev) | Asynchronous finger tap timing |
| **Multi-Edit** | 4 | `graffix`, `amzingg`, `updaetd`, `conectionn` | `graphics`, `amazing`, `updated`, `connection` | 2 | Compound phonetic & multi-key error |
| **Control (Clean)** | 5 | `game`, `update`, `screen`, `free`, `mobile` | `game`, `update`, `screen`, `free`, `mobile` | 0 | Baseline false positive check |

---

### 4. Empirical Benchmark Results & Evaluation Metrics

We benchmarked 5 distinct autocorrect systems across the 33-word test suite:
1. **Classical Levenshtein Engine**
2. **Damerau-Levenshtein Engine**
3. **Bayesian Frequency-Weighted Engine**
4. **`pyspellchecker` Production Baseline**
5. **Gboard Reference Engine (Simulated Production)**

$$\text{Top-1 Acc} = \frac{TP + TN}{N}, \quad \text{Precision} = \frac{TP}{TP + FP}, \quad \text{Recall} = \frac{TP}{TP + FN}, \quad \text{MRR} = \frac{1}{N} \sum \frac{1}{\text{rank}}$$

| Engine Architecture | Top-1 Accuracy (%) | Top-3 Recall / Hit Rate (%) | Precision (%) | Recall (%) | F1-Score (%) | Mean Reciprocal Rank (MRR) | Mean Latency per Word (ms) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Classical Levenshtein** | 81.8% | 87.9% | **100.0%** | 78.6% | 88.0% | 0.8485 | 50.21 ms |
| **Damerau-Levenshtein** | **87.9%** | **90.9%** | **100.0%** | **85.7%** | **92.3%** | **0.8939** | **15.87 ms** |
| **Bayesian Frequency-Weighted** | **87.9%** | **90.9%** | **100.0%** | **85.7%** | **92.3%** | **0.8939** | **18.92 ms** |
| **`pyspellchecker` (Baseline)** | 87.9% | 87.9% | **100.0%** | 85.7% | 92.3% | 0.8864 | 97.80 ms |
| **Gboard Reference (Simulated)** | **87.9%** | **90.9%** | **100.0%** | **85.7%** | **92.3%** | **0.8939** | **13.87 ms** |

#### Key Empirical Insights:
1. **The Transposition Lift**: Damerau-Levenshtein achieves an immediate **+6.1% boost in Top-1 Accuracy** and **+7.1% boost in Recall** over Classical Levenshtein, directly resolving adjacent transposition errors (`teh` $\to$ `the`, `udpate` $\to$ `update`).
2. **Zero False Positives (100% Precision)**: Across all 5 models, correct words (`game`, `update`, `screen`, `free`, `mobile`) remained 100% unmodified, verifying that the candidate generation filters never corrupt valid inputs.
3. **Inference Latency Advantage**: Damerau-Levenshtein and Bayesian engines run in **~15–18 ms/word**, outperforming `pyspellchecker` (**97.8 ms/word**, **~5.5x faster**), while achieving higher Top-3 candidate recall (90.9% vs 87.9%).

---

### 5. Error-Type Stratification & Confusion Matrix Analysis

Breaking down Top-1 accuracy by error category highlights where classical algorithms fail:

| Error Category | Classical Levenshtein Acc (%) | Damerau-Levenshtein Acc (%) | Bayesian Frequency Acc (%) | `pyspellchecker` Acc (%) | Gboard Reference Acc (%) | Key Failure / Success Factor |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Deletion** | **100.0%** | **100.0%** | **100.0%** | **100.0%** | **100.0%** | Single omitted character easily matched |
| **Insertion** | 83.3% | 83.3% | 83.3% | **100.0%** | 83.3% | Handled via distance-1 single-character strip |
| **Substitution** | 83.3% | 83.3% | 83.3% | 66.7% | 83.3% | QWERTY adjacent replacements |
| **Transposition**| 66.7% | **83.3%** | **83.3%** | **83.3%** | **83.3%** | Levenshtein penalizes as distance 2; Damerau solves in distance 1 |
| **Multi-Edit (Dist 2)** | 50.0% | **75.0%** | **75.0%** | **75.0%** | **75.0%** | Combinatorial expansion handles 2-edit typos |
| **Control (Clean)** | **100.0%** | **100.0%** | **100.0%** | **100.0%** | **100.0%** | Perfect retention; 0 false positive modifications |

---

### 6. Comparative Architectural Evaluation vs. Production Keyboards (Gboard)

Modern commercial smartphone keyboards (Google Gboard, Apple iOS Keyboard) employ a multi-layered hybrid architecture that significantly surpasses pure edit-distance engines:

```
[Touch Screen Coordinates (x, y)]
             │
             ▼
[Spatial Key Probability Model: P(Touch | Key) ~ Gaussian]
             │
             ▼
[Lexical Prefix Trie / FST Candidate Decoding]
             │
             ▼
[Context-Aware Neural Language Model: Transformer / LSTM Beam Search P(Word | Context)]
             │
             ▼
[Personalized User Dictionary & Federated Learning Adaptation]
             │
             ▼
[Top-3 Candidate Bar & Auto-Commit Decision]
```

1. **Continuous Spatial Touch Modeling vs. Discrete ASCII Distance**:
   - *Classical Autocorrect*: Treats every letter substitution identically ($\text{cost} = 1$). Substituting `'a'` with `'s'` (physically adjacent on QWERTY) costs the same as substituting `'a'` with `'p'` (opposite side of keyboard).
   - *Gboard*: Models fingertip touch points as continuous bivariate Gaussian distributions $(\mu, \Sigma)$ centered over key coordinates. Fat-finger touch slips receive high spatial likelihood $P(\text{touch} \mid \text{key})$, drastically pruning the candidate search tree.
2. **Context-Aware Sequence Decoding**:
   - *Classical Autocorrect*: Evaluates words in total isolation. Cannot differentiate `"see you there"` vs `"see you their"`.
   - *Gboard*: Integrates bidirectional Transformer / recurrent neural language models with beam search, evaluating $P(w_i \mid w_{i-2}, w_{i-1})$.
3. **Strict Sub-5ms Mobile Latency Budget**:
   - Gboard processes keystrokes within **< 2ms** on edge mobile chips using quantized Finite State Transducers (FST) and compressed trie structures to prevent UI stutter within Android's 16ms (60 FPS) rendering budget.
4. **Federated Learning & On-Device Personalization**:
   - Gboard continuously adapts to user slang, contact names, and emojis via private on-device federated learning without transmitting keystrokes to remote servers.

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
│   ├── 03_playstore_pricing_sentiment_dashboard.ipynb   # Day 3: Pricing, Sentiment & Plotly Dashboard
│   ├── 04_nlp_corpus_autocomplete_engine.ipynb          # Day 4: NLP Corpus, N-Gram & Autocomplete Notebook
│   └── 05_nlp_autocorrect_benchmarks.ipynb              # Day 5: NLP Autocorrect, Edit Distance & Benchmarks
├── reports/
│   ├── category_distribution_summary.csv   # Category market share data table (Day 2)
│   ├── category_ratings_summary.csv        # Category ratings benchmarks table (Day 2)
│   ├── stratified_correlations_summary.csv # Category-level size vs installs correlations (Day 2)
│   ├── category_revenue_summary.csv        # Category revenue estimation & monetization table (Day 3)
│   ├── top_revenue_apps_summary.csv        # Top grossing paid apps ranking (Day 3)
│   ├── category_sentiment_summary.csv      # Category sentiment polarity benchmarks table (Day 3)
│   ├── market_opportunity_matrix.csv       # Unified 33-category opportunity matrix & quadrants (Day 3)
│   ├── vocabulary_frequency_summary.csv    # Corpus vocabulary frequencies & Zipf analysis (Day 4)
│   ├── ngram_predictions_summary.csv       # Top-3 predictions across 12 mobile prompt prefixes (Day 4)
│   ├── autocomplete_metrics_summary.csv    # Empirical evaluation metrics & perplexity across models (Day 4)
│   ├── autocorrect_test_corpus.csv         # 33-item benchmark test suite with error categories (Day 5)
│   ├── autocorrect_benchmark_summary.csv   # Precision, recall, accuracy, latency across 5 engines (Day 5)
│   ├── autocorrect_confusion_matrix.csv    # Stratified error-type confusion matrix (Day 5)
│   ├── autocorrect_word_predictions.csv    # Per-word predictions across all engines (Day 5)
│   └── figures/
│       ├── 01_category_distribution.png    # Saturated vs niche categories bar chart (Day 2)
│       ├── 02_rating_distributions.png     # Rating KDE & top 20 category box plots (Day 2)
│       ├── 03_size_vs_installs_scatter.png # Size vs installs log-scale scatter & trend (Day 2)
│       ├── 04_category_size_installs_correlations.png # Stratified Spearman correlation ranking (Day 2)
│       ├── 05_paid_vs_free_pricing.png     # Paid vs free distribution & price curve (Day 3)
│       ├── 06_category_revenue_estimation.png # Category revenue & paid catalog share (Day 3)
│       ├── 07_sentiment_distribution.png   # VADER vs TextBlob engine & polarity extremes (Day 3)
│       ├── 08_market_bubble_dashboard.png  # Publication 2D strategic opportunity bubble chart (Day 3)
│       ├── 08_market_opportunity_dashboard.html # Interactive Plotly bubble chart dashboard (Day 3)
│       ├── 09_top20_vocabulary_frequency.png    # Top 20 vocabulary frequency & Zipf's law scaling (Day 4)
│       ├── 10_ngram_autocomplete_evaluation.png # Autocomplete predictions & evaluation metrics (Day 4)
│       ├── 11_autocorrect_performance_metrics.png   # Autocorrect metrics & latency tradeoff (Day 5)
│       └── 12_autocorrect_confusion_matrices.png    # Confusion matrix & Gboard capability radar (Day 5)
├── src/
│   ├── __init__.py                     # Package definition
│   ├── data_cleaning.py                # Day 1: Reusable data cleaning pipeline
│   ├── category_ratings_analysis.py    # Day 2: Category, ratings & correlation engine
│   ├── pricing_sentiment_analysis.py   # Day 3: Pricing, sentiment & dashboard engine
│   ├── nlp_autocomplete_engine.py      # Day 4: NLP corpus preprocessing & autocomplete engine
│   └── nlp_autocorrect_engine.py       # Day 5: NLP autocorrect, edit distance & benchmark engine
└── tests/
    ├── test_cleaning.py                # Day 1: Data cleaning pytest suite (4 passed)
    ├── test_category_ratings.py        # Day 2: Category & ratings pytest suite (6 passed)
    ├── test_pricing_sentiment.py       # Day 3: Pricing & sentiment pytest suite (8 passed)
    ├── test_nlp_autocomplete.py        # Day 4: NLP autocomplete engine pytest suite (9 passed)
    └── test_nlp_autocorrect.py         # Day 5: NLP autocorrect engine pytest suite (9 passed)
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

# Day 4 NLP Corpus Ingestion & Autocomplete Engine
python src/nlp_autocomplete_engine.py

# Day 5 NLP Autocorrect, Edit Distance & Benchmarking Pipeline
python src/nlp_autocorrect_engine.py
```

### 3. Run Automated Pytest Test Suite
```bash
# Execute entire test suite (36 passed across Day 1, Day 2, Day 3, Day 4, and Day 5)
pytest tests/ -v
```

### 4. Launch Jupyter Notebooks
```bash
jupyter notebook notebooks/01_playstore_data_cleaning.ipynb
jupyter notebook notebooks/02_playstore_category_ratings_size_analysis.ipynb
jupyter notebook notebooks/03_playstore_pricing_sentiment_dashboard.ipynb
jupyter notebook notebooks/04_nlp_corpus_autocomplete_engine.ipynb
jupyter notebook notebooks/05_nlp_autocorrect_benchmarks.ipynb
```




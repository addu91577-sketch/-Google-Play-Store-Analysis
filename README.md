# Google Play Store Ecosystem Analysis & NLP Autocomplete/Autocorrect Analytics

[![GitHub Repository](https://img.shields.io/badge/GitHub-Repository-blue?logo=github)](https://github.com/addu91577-sketch/-Google-Play-Store-Analysis)

Comprehensive data analytics project covering real-world Android app market intelligence (Task 4) and natural language processing autocomplete & autocorrect algorithms (Task 5).

---

## 🚀 Day 1 Milestones & Deliverables (Task 4 Data Cleaning)

### 1. Data Quality Issues Identified & Resolved
1. **Corrupted Record Removal**:
   - **Diagnosis**: Row 10472 (`Life Made WI-Fi Touchscreen Photo Frame`) was missing a `Category` entry, causing all subsequent columns to shift left (`Rating` became `1.9`, `Reviews` became `3.0M`, `Size` became `1,000+`, `Installs` became `Free`).
   - **Resolution**: Filtered out invalid shifted records using strict schema validation.
2. **Numeric Type Transformations**:
   - `Reviews`: Sanitized formatting (stripped commas) and converted from string object to `int64`.
   - `Installs`: Removed `+` and `,` formatting symbols, coerced non-numeric tokens, and converted to `int64`.
   - `Price`: Stripped currency symbol (`$`) and cast to `float64` (with `Free` apps set to `0.0`).
3. **App Size Standardization (`Size_MB`)**:
   - Parsed mixed unit representations: Megabytes (`M` -> float), Kilobytes (`k` -> float / 1024.0).
   - Handled `"Varies with device"` records as `NaN`, followed by category-median imputation (`Size_MB_Imputed`).
4. **Intelligent Deduplication**:
   - Out of 10,840 valid records, 1,181 duplicate app names were detected across scraped batches.
   - Preserved the record with the **highest review count** (representing the latest update) to avoid data skew.
   - Resulted in **9,659 unique apps**.
5. **User Reviews Sanitization**:
   - Dropped 26,868 rows missing translated text.
   - Removed 7,735 duplicate reviews.
   - Validated polarity ranges `[-1.0, 1.0]` and subjectivity ranges `[0.0, 1.0]`.
   - Resulted in **29,692 cleaned reviews** (19,015 Positive, 6,321 Negative, 4,356 Neutral).

### 2. Dataset Metrics (Before vs. After Cleaning)

| Feature / Metric | Raw Data | Cleaned Data (Day 1) | Data Type | Notes |
| :--- | :--- | :--- | :--- | :--- |
| **Play Store Apps Count** | 10,841 | 9,659 | - | Corrupted row removed, deduplicated |
| **Unique App Names** | 9,660 | 9,659 | string | 1:1 unique app mapping |
| **Installs** | String (`10,000+`) | Integer (`10000`) | `int64` | Range: `0` to `1,000,000,000` |
| **Reviews** | String (`'2490'`) | Integer (`2490`) | `int64` | Range: `0` to `78,158,306` |
| **Price** | String (`'$4.99'`) | Float (`4.99`) | `float64` | Range: `$0.00` to `$400.00` |
| **App Size** | String (`'19M'`) | Float (`19.0`) | `float64` | Normalized in Megabytes (MB) |
| **User Reviews Count** | 64,295 | 29,692 | - | Null & duplicated reviews purged |
| **Review Sentiment Classes** | Contains NaNs | 100% complete | Categorical | Positive: 64.0%, Negative: 21.3%, Neutral: 14.7% |

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
│   ├── cleaned_googleplaystore.csv     # Cleaned, deduplicated apps dataset
│   └── cleaned_user_reviews.csv        # Cleaned, deduplicated user reviews
├── notebooks/
│   └── 01_playstore_data_cleaning.ipynb# Interactive data cleaning notebook & audit
├── src/
│   ├── __init__.py                     # Package definition
│   └── data_cleaning.py                # Reusable, production cleaning pipeline
└── tests/
    └── test_cleaning.py                # Pytest validation test suite
```

---

## 🛠️ Installation & Verification

### 1. Set Up Environment
```bash
pip install -r requirements.txt
```

### 2. Run Data Cleaning Pipeline
```bash
python src/data_cleaning.py
```

### 3. Run Automated Tests
```bash
pytest tests/test_cleaning.py -v
```

### 4. Launch Jupyter Notebook
```bash
jupyter notebook notebooks/01_playstore_data_cleaning.ipynb
```

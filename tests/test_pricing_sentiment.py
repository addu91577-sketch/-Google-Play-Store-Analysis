"""Unit and regression tests for Day 3 Pricing, Sentiment & Interactive Dashboard Module.
"""

import sys
from pathlib import Path
import pytest
import pandas as pd
import numpy as np

# Ensure project root is in sys.path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.pricing_sentiment_analysis import (
    compute_pricing_distribution,
    compute_category_monetization,
    get_top_revenue_apps,
    compute_sentiment_scores,
    compute_sentiment_metrics,
    compute_category_sentiment_summary,
    compute_market_opportunity_matrix,
    generate_developer_recommendations,
    generate_all_day3_reports
)


@pytest.fixture(scope="module")
def playstore_df():
    """Load cleaned Play Store apps dataset."""
    data_path = Path(__file__).parent.parent / "Data" / "cleaned_googleplaystore.csv"
    assert data_path.exists(), f"Cleaned apps dataset missing at {data_path}"
    return pd.read_csv(data_path)


@pytest.fixture(scope="module")
def reviews_df():
    """Load cleaned user reviews dataset."""
    data_path = Path(__file__).parent.parent / "Data" / "cleaned_user_reviews.csv"
    assert data_path.exists(), f"Cleaned reviews dataset missing at {data_path}"
    return pd.read_csv(data_path)


def test_compute_pricing_distribution(playstore_df):
    """Test pricing descriptive statistics and tier distribution."""
    stats = compute_pricing_distribution(playstore_df)

    assert stats["total_apps"] == 9659
    assert stats["free_apps"] == 8905
    assert stats["paid_apps"] == 754
    assert np.isclose(stats["free_percentage"] + stats["paid_percentage"], 100.0, atol=1e-2)

    # Paid statistics
    assert np.isclose(stats["paid_median"], 2.99, atol=0.01)
    assert stats["paid_min"] == 0.99
    assert stats["paid_max"] == 400.00
    assert stats["paid_mean"] > stats["paid_median"]  # Right-skewed due to luxury outliers

    # Tiers
    tiers = stats["tier_breakdown"]
    total_tier_count = sum(t["count"] for t in tiers.values())
    assert total_tier_count == 754
    assert tiers["Tier 1: $0.99 - $1.99"]["count"] == 280
    assert tiers["Tier 2: $2.00 - $4.99"]["count"] == 316
    assert stats["outlier_count_gte_30"] == 29


def test_compute_category_monetization(playstore_df):
    """Test category revenue estimation and monetization metrics."""
    monetization_df = compute_category_monetization(playstore_df)

    assert isinstance(monetization_df, pd.DataFrame)
    assert len(monetization_df) == 33

    required_cols = [
        "Category", "Total_Apps", "Free_Apps", "Paid_Apps", "Paid_Share_Pct",
        "Mean_Paid_Price", "Median_Paid_Price", "Total_Installs", "Paid_Installs",
        "Estimated_Revenue", "Revenue_Per_Paid_App", "Revenue_Share_Pct"
    ]
    for col in required_cols:
        assert col in monetization_df.columns

    # Integrity checks
    assert (monetization_df["Free_Apps"] + monetization_df["Paid_Apps"] == monetization_df["Total_Apps"]).all()
    assert (monetization_df["Estimated_Revenue"] >= 0.0).all()
    assert np.isclose(monetization_df["Revenue_Share_Pct"].sum(), 100.0, atol=0.5)

    # Top grossing category is FAMILY
    assert monetization_df.iloc[0]["Category"] == "FAMILY"
    assert monetization_df.iloc[0]["Estimated_Revenue"] > 100_000_000.0


def test_get_top_revenue_apps(playstore_df):
    """Test top revenue paid apps retrieval."""
    top_apps = get_top_revenue_apps(playstore_df, n=10)

    assert len(top_apps) == 10
    assert "Estimated_Revenue" in top_apps.columns

    # Verify descending sort order
    revenues = top_apps["Estimated_Revenue"].tolist()
    assert revenues == sorted(revenues, reverse=True)

    # Minecraft is the #1 grossing paid app
    assert top_apps.iloc[0]["App"] == "Minecraft"
    assert top_apps.iloc[0]["Price"] == 6.99
    assert top_apps.iloc[0]["Installs"] == 10_000_000


def test_sentiment_scoring_sample(reviews_df):
    """Test VADER sentiment scoring and engine comparison on a representative sample."""
    sample_reviews = reviews_df.head(200).copy()
    scored = compute_sentiment_scores(sample_reviews)

    assert "VADER_Compound" in scored.columns
    assert "VADER_Sentiment" in scored.columns
    assert "TextBlob_Sentiment" in scored.columns

    # Bounds check
    assert (scored["VADER_Compound"] >= -1.0).all()
    assert (scored["VADER_Compound"] <= 1.0).all()
    assert scored["VADER_Sentiment"].isin(["Positive", "Negative", "Neutral"]).all()

    metrics = compute_sentiment_metrics(scored)
    assert metrics["total_reviews"] == 200
    assert 50.0 <= metrics["agreement_percentage"] <= 95.0


def test_compute_category_sentiment_summary(reviews_df, playstore_df):
    """Test aggregation of sentiment by category."""
    sample_scored = compute_sentiment_scores(reviews_df.head(1000))
    cat_sent = compute_category_sentiment_summary(sample_scored, playstore_df)

    assert isinstance(cat_sent, pd.DataFrame)
    assert "Category" in cat_sent.columns
    assert "Mean_VADER_Compound" in cat_sent.columns
    assert "Mean_TextBlob_Polarity" in cat_sent.columns
    assert (cat_sent["Mean_VADER_Compound"] >= -1.0).all()
    assert (cat_sent["Mean_VADER_Compound"] <= 1.0).all()


def test_market_opportunity_matrix(playstore_df, reviews_df):
    """Test creation and quadrant assignment of the Market Opportunity Matrix."""
    monetization_df = compute_category_monetization(playstore_df)
    sample_scored = compute_sentiment_scores(reviews_df.head(500))
    cat_sent = compute_category_sentiment_summary(sample_scored, playstore_df)

    matrix = compute_market_opportunity_matrix(playstore_df, monetization_df, cat_sent)

    assert len(matrix) == 33
    assert "Strategic_Quadrant" in matrix.columns
    assert "Opportunity_Score" in matrix.columns

    # Verify score ranges
    assert (matrix["Opportunity_Score"] >= 0.0).all()
    assert (matrix["Opportunity_Score"] <= 100.0).all()

    # Verify quadrants
    valid_quadrants = {
        "Quadrant I: High Satisfaction / High Delight",
        "Quadrant II: High Rating / Latent Review Friction",
        "Quadrant III: High Review Sentiment / Structural Gaps",
        "Quadrant IV: Red Ocean / High User Friction"
    }
    assert set(matrix["Strategic_Quadrant"]).issubset(valid_quadrants)


def test_generate_developer_recommendations(playstore_df, reviews_df):
    """Test synthesis of 3 developer launch recommendations."""
    monetization_df = compute_category_monetization(playstore_df)
    sample_scored = compute_sentiment_scores(reviews_df.head(500))
    cat_sent = compute_category_sentiment_summary(sample_scored, playstore_df)
    matrix = compute_market_opportunity_matrix(playstore_df, monetization_df, cat_sent)

    recs = generate_developer_recommendations(matrix)

    assert len(recs) == 3
    for rec in recs:
        assert "recommendation_id" in rec
        assert "title" in rec
        assert "category_targets" in rec
        assert "empirical_rationale" in rec
        assert "actionable_playbook" in rec


def test_all_day3_artifacts_exist():
    """Verify that all 9 Day 3 reports and figures exist on disk."""
    expected_files = [
        Path("reports") / "category_revenue_summary.csv",
        Path("reports") / "top_revenue_apps_summary.csv",
        Path("reports") / "category_sentiment_summary.csv",
        Path("reports") / "market_opportunity_matrix.csv",
        Path("reports") / "figures" / "05_paid_vs_free_pricing.png",
        Path("reports") / "figures" / "06_category_revenue_estimation.png",
        Path("reports") / "figures" / "07_sentiment_distribution.png",
        Path("reports") / "figures" / "08_market_bubble_dashboard.png",
        Path("reports") / "figures" / "08_market_opportunity_dashboard.html"
    ]
    for f in expected_files:
        assert f.exists(), f"Day 3 artifact missing: {f}"
        assert f.stat().st_size > 0, f"Day 3 artifact empty: {f}"

"""
Statistical Analysis - Language Match Impact on Customer Satisfaction
"""

import pandas as pd
from scipy.stats import ttest_ind

def analyze_language_impact(csv_path='../data/raw/multilingual_support_tickets.csv'):
    """
    Perform statistical analysis on language matching impact
    """
    # Load data
    df = pd.read_csv(csv_path)
    
    # Separate matched vs unmatched
    matched = df[df['Language_Match'] == True]
    unmatched = df[df['Language_Match'] == False]
    
    # T-test for satisfaction
    t_stat_satisfaction, p_value_satisfaction = ttest_ind(
        matched['Satisfaction'], 
        unmatched['Satisfaction']
    )
    
    # T-test for resolution time
    t_stat_resolution, p_value_resolution = ttest_ind(
        matched['Resolution_Time'], 
        unmatched['Resolution_Time']
    )
    
    print("🔬 STATISTICAL ANALYSIS RESULTS")
    print("=" * 50)
    print(f"\nSatisfaction Score:")
    print(f"  Matched: {matched['Satisfaction'].mean():.2f} ± {matched['Satisfaction'].std():.2f}")
    print(f"  Unmatched: {unmatched['Satisfaction'].mean():.2f} ± {unmatched['Satisfaction'].std():.2f}")
    print(f"  t-statistic: {t_stat_satisfaction:.3f}")
    print(f"  p-value: {p_value_satisfaction:.6f}")
    print(f"  {'✅ Statistically significant (p < 0.01)' if p_value_satisfaction < 0.01 else '❌ Not significant'}")
    
    print(f"\nResolution Time:")
    print(f"  Matched: {matched['Resolution_Time'].mean():.2f}h ± {matched['Resolution_Time'].std():.2f}h")
    print(f"  Unmatched: {unmatched['Resolution_Time'].mean():.2f}h ± {unmatched['Resolution_Time'].std():.2f}h")
    print(f"  t-statistic: {t_stat_resolution:.3f}")
    print(f"  p-value: {p_value_resolution:.6f}")
    print(f"  {'✅ Statistically significant (p < 0.01)' if p_value_resolution < 0.01 else '❌ Not significant'}")

if __name__ == "__main__":
    analyze_language_impact()

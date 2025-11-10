"""
Unit tests for data processing functions
"""

import unittest
import pandas as pd
import numpy as np
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from scripts.data_processing import (
    detect_outliers_zscore,
    clean_solar_data,
    calculate_summary_stats
)


class TestDataProcessing(unittest.TestCase):
    
    def setUp(self):
        """Set up test data"""
        self.test_data = pd.DataFrame({
            'GHI': [100, 200, 300, 400, 5000],  # Last value is outlier
            'DNI': [150, 250, 350, 450, 550],
            'DHI': [50, 100, 150, 200, 250],
            'Tamb': [25, 26, 27, 28, 29]
        })
    
    def test_detect_outliers(self):
        """Test outlier detection"""
        outliers = detect_outliers_zscore(self.test_data, ['GHI'])
        self.assertTrue(outliers['GHI'].iloc[-1])  # Last value should be outlier
    
    def test_clean_solar_data(self):
        """Test data cleaning"""
        df_with_na = self.test_data.copy()
        df_with_na.loc[0, 'GHI'] = np.nan
        
        cleaned = clean_solar_data(df_with_na)
        self.assertEqual(len(cleaned), len(df_with_na) - 1)
    
    def test_summary_stats(self):
        """Test summary statistics calculation"""
        stats = calculate_summary_stats(self.test_data, ['GHI', 'DNI'])
        self.assertIn('mean', stats.index)
        self.assertIn('std', stats.index)


if __name__ == '__main__':
    unittest.main()

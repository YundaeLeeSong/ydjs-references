#!/usr/bin/env python3
"""
Test script to verify the cumulative file functionality of load_trades_activity
"""

import sys
import os
from pathlib import Path

# Add the src directory to the Python path
sys.path.insert(0, str(Path(__file__).parent / "src" / "main" / "python"))

from alpaca_tradebot.core import load_trades_activity

def test_cumulative_functionality():
    """Test the cumulative file functionality"""
    
    # Test parameters
    today = "20250101"  # Use a fixed date for testing
    daily_file = Path(f"test_report/{today}-trades.xlsx")
    cumulative_file = Path("test_report/transaction_summary.xlsx")
    
    print("Testing cumulative file functionality...")
    print(f"Daily file: {daily_file}")
    print(f"Cumulative file: {cumulative_file}")
    
    # Clean up any existing test files
    if daily_file.exists():
        daily_file.unlink()
    if cumulative_file.exists():
        cumulative_file.unlink()
    
    # Ensure test directory exists
    daily_file.parent.mkdir(parents=True, exist_ok=True)
    
    try:
        # Test 1: First call - should create both daily and cumulative files
        print("\n=== Test 1: First call ===")
        load_trades_activity(
            file_path=daily_file,
            date_string="2025-01-01",
            cumulative_file_path=cumulative_file
        )
        
        # Test 2: Second call - should append to cumulative file
        print("\n=== Test 2: Second call (same date) ===")
        load_trades_activity(
            file_path=daily_file,
            date_string="2025-01-01",
            cumulative_file_path=cumulative_file
        )
        
        # Test 3: Third call with different date - should append to cumulative file
        print("\n=== Test 3: Third call (different date) ===")
        load_trades_activity(
            file_path=daily_file,
            date_string="2025-01-02",
            cumulative_file_path=cumulative_file
        )
        
        print("\n=== Test Results ===")
        print(f"Daily file exists: {daily_file.exists()}")
        print(f"Cumulative file exists: {cumulative_file.exists()}")
        
        if cumulative_file.exists():
            import pandas as pd
            df = pd.read_excel(cumulative_file)
            print(f"Cumulative file has {len(df)} records")
            print("Sample records:")
            print(df.head())
        
        print("\n✅ Test completed successfully!")
        
    except Exception as e:
        print(f"\n❌ Test failed with error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_cumulative_functionality() 
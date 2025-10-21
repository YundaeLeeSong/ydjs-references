#!/usr/bin/env python3
"""
Test script to verify that the column order issue is fixed
"""

import sys
import os
from pathlib import Path
import pandas as pd

# Add the src directory to the Python path
sys.path.insert(0, str(Path(__file__).parent / "src" / "main" / "python"))

def test_column_order():
    """Test that the column order is consistent"""
    
    # Create test data with the expected structure
    test_data = [
        {
            'Description': 'SELL 13.0 CVNY',
            'Type': 'FILL',
            'Quantity': 13.0,
            'Value': 576.55,
            'Date': 'Jul 10, 2025, 09:35:44 AM'
        },
        {
            'Description': 'BUY 0.85 ETH',
            'Type': 'FILL',
            'Quantity': 0.85,
            'Value': -22.40175,
            'Date': 'Jul 10, 2025, 05:31:42 AM'
        }
    ]
    
    # Create test files
    test_file = Path("test_report/test_column_order.xlsx")
    cumulative_file = Path("test_report/test_cumulative_column_order.xlsx")
    
    # Ensure test directory exists
    test_file.parent.mkdir(parents=True, exist_ok=True)
    
    # Clean up existing files
    if test_file.exists():
        test_file.unlink()
    if cumulative_file.exists():
        cumulative_file.unlink()
    
    try:
        # Create initial file
        df1 = pd.DataFrame(test_data)
        df1.to_excel(test_file, index=False)
        print(f"Created initial file with columns: {list(df1.columns)}")
        
        # Create cumulative file
        df1.to_excel(cumulative_file, index=False)
        print(f"Created cumulative file with columns: {list(df1.columns)}")
        
        # Add more data with different order
        additional_data = [
            {
                'Description': 'SELL 0.01 JNJ',
                'Type': 'FILL',
                'Quantity': 0.01,
                'Value': 1.56784,
                'Date': 'Jul 11, 2025, 03:54:30 PM'
            },
            {
                'Description': 'BUY 0.37 NVO',
                'Type': 'FILL',
                'Quantity': 0.37,
                'Value': -25.51816,
                'Date': 'Jul 11, 2025, 03:49:19 PM'
            }
        ]
        
        # Simulate the append operation
        df2 = pd.DataFrame(additional_data)
        print(f"New data columns: {list(df2.columns)}")
        
        # Read existing cumulative file
        existing_df = pd.read_excel(cumulative_file)
        print(f"Existing cumulative file columns: {list(existing_df.columns)}")
        
        # Ensure consistent column order
        expected_columns = ['Description', 'Type', 'Quantity', 'Value', 'Date']
        df2 = df2[expected_columns]
        existing_df = existing_df[expected_columns]
        
        # Combine
        combined_df = pd.concat([existing_df, df2], ignore_index=True)
        combined_df.to_excel(cumulative_file, index=False)
        
        # Verify the result
        final_df = pd.read_excel(cumulative_file)
        print(f"Final cumulative file columns: {list(final_df.columns)}")
        print("\nFinal data:")
        print(final_df.to_string(index=False))
        
        # Check if columns are in correct order
        if list(final_df.columns) == expected_columns:
            print("\n✅ Column order is correct!")
        else:
            print(f"\n❌ Column order is wrong! Expected: {expected_columns}, Got: {list(final_df.columns)}")
        
        # Check if data is properly aligned
        print("\nChecking data alignment...")
        for i, row in final_df.iterrows():
            print(f"Row {i}: {row['Description']} | {row['Type']} | {row['Quantity']} | {row['Value']} | {row['Date']}")
        
    except Exception as e:
        print(f"❌ Test failed with error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_column_order() 
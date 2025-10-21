# Cumulative File Functionality for load_trades_activity

## Overview
Modified the `load_trades_activity` function in `src/main/python/alpaca_tradebot/core.py` to support an optional cumulative file parameter. This allows the function to append trade data to a cumulative file while still maintaining the original daily file functionality.

## Changes Made

### 1. Function Signature Update
- **File**: `src/main/python/alpaca_tradebot/core.py`
- **Function**: `load_trades_activity`
- **New Parameter**: `cumulative_file_path: Path = None`

```python
def load_trades_activity(file_path: Path = None, date_string: str = None, append: bool = False, cumulative_file_path: Path = None):
```

### 2. Documentation Update
Added comprehensive documentation for the new parameter:

```python
"""
Args:
    file_path (Path, optional): Custom file path to save the Excel file. If None, uses default path.
    date_string (str, optional): Date in YYYY-MM-DD format. If None, uses today's date.
    append (bool): If True, append to existing file. If False, overwrite existing file.
    cumulative_file_path (Path, optional): Path to cumulative file. If provided, data will be appended to this file.

Usage:
    ### [LOAD] With cumulative file
    load_trades_activity(
        file_path=Path(f"report/{today}-trades.xlsx"),
        cumulative_file_path=Path("report/transaction_summary.xlsx")
    )
"""
```

### 3. Cumulative File Logic
Added new logic to handle cumulative file operations with consistent column ordering:

```python
# Handle cumulative file if provided
if cumulative_file_path is not None:
    # Ensure cumulative file directory exists
    cumulative_file_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Create DataFrame for new data with consistent column order
    new_df = pd.DataFrame(processed_records)
    
    # Define the expected column order
    expected_columns = ['Description', 'Type', 'Quantity', 'Value', 'Date']
    
    # Ensure new_df has the correct column order
    new_df = new_df[expected_columns]
    
    # Append to cumulative file
    if cumulative_file_path.exists():
        # Read existing cumulative data and append new data
        existing_cumulative_df = pd.read_excel(cumulative_file_path)
        
        # Ensure existing data has the correct column order
        if set(existing_cumulative_df.columns) == set(expected_columns):
            existing_cumulative_df = existing_cumulative_df[expected_columns]
        else:
            # If column structure is different, reorder to match expected columns
            print(f"\t⚠️ Warning: Existing cumulative file has different column structure. Reordering columns.")
            # Try to map existing columns to expected columns
            column_mapping = {}
            for col in expected_columns:
                if col in existing_cumulative_df.columns:
                    column_mapping[col] = col
                else:
                    # Try to find similar columns
                    for existing_col in existing_cumulative_df.columns:
                        if col.lower() in existing_col.lower() or existing_col.lower() in col.lower():
                            column_mapping[col] = existing_col
                            break
            
            # Reorder existing data
            reordered_columns = [column_mapping.get(col, col) for col in expected_columns]
            existing_cumulative_df = existing_cumulative_df[reordered_columns]
            existing_cumulative_df.columns = expected_columns
        
        # Combine data with consistent column order
        combined_cumulative_df = pd.concat([existing_cumulative_df, new_df], ignore_index=True)
        combined_cumulative_df.to_excel(cumulative_file_path, index=False)
        print(f"\t✔ Appended {len(processed_records)} FILL activities for {target_date} to cumulative file {cumulative_file_path}")
    else:
        # Create new cumulative file with correct column order
        new_df.to_excel(cumulative_file_path, index=False)
        print(f"\t✔ Created cumulative file with {len(processed_records)} FILL activities for {target_date} at {cumulative_file_path}")
```

### 4. Report Function Update
Updated the `report()` function to use the new cumulative file functionality:

```python
def report():
    ### [LOAD] Process activities
    today = datetime.now().strftime('%Y%m%d')
    load_trades_activity(
        file_path=Path(f"report/{today}-trades.xlsx"),
        cumulative_file_path=Path("report/transaction_summary.xlsx")
    )
    # ... rest of the function
```

## How It Works

1. **Daily File**: The function continues to save daily trade data to the specified daily file (e.g., `report/20250101-trades.xlsx`)

2. **Cumulative File**: If `cumulative_file_path` is provided:
   - If the cumulative file exists, new data is appended to the end
   - If the cumulative file doesn't exist, it's created with the new data
   - The cumulative file maintains all historical trade data

3. **Backward Compatibility**: The function remains fully backward compatible:
   - Existing calls without the `cumulative_file_path` parameter work exactly as before
   - The `append` parameter still works for the daily file
   - All existing functionality is preserved

## Usage Examples

### Basic Usage (No Cumulative File)
```python
# Original functionality - unchanged
load_trades_activity(Path(f"report/{today}-trades.xlsx"))
```

### With Cumulative File
```python
# New functionality - saves to both daily and cumulative files
load_trades_activity(
    file_path=Path(f"report/{today}-trades.xlsx"),
    cumulative_file_path=Path("report/transaction_summary.xlsx")
)
```

### Multiple Days Processing
```python
# Process multiple days and append to cumulative file
dates_to_process = ["2025-06-17", "2025-06-18", "2025-06-19", "2025-06-20"]
for i, date_str in enumerate(dates_to_process):
    if i == 0:
        load_trades_activity(
            file_path=Path("report/multi-day-trades.xlsx"),
            date_string=date_str,
            append=False,
            cumulative_file_path=Path("report/transaction_summary.xlsx")
        )
    else:
        load_trades_activity(
            file_path=Path("report/multi-day-trades.xlsx"),
            date_string=date_str,
            append=True,
            cumulative_file_path=Path("report/transaction_summary.xlsx")
        )
```

## File Structure
After running the function, you'll have:
```
report/
├── 20250101-trades.xlsx          # Daily trade data
├── 20250102-trades.xlsx          # Daily trade data
├── 20250103-trades.xlsx          # Daily trade data
└── transaction_summary.xlsx      # Cumulative trade data (all days combined)
```

## Testing
A test script `test_cumulative_functionality.py` has been created to verify the functionality works correctly.

## Column Order Fix

### Issue
The original implementation had a column order issue when appending data to existing cumulative files. This caused data misalignment where new records would have their values in the wrong columns.

### Solution
Added explicit column ordering to ensure consistent data structure:

1. **Expected Column Order**: `['Description', 'Type', 'Quantity', 'Value', 'Date']`
2. **Column Validation**: Checks existing files for correct column structure
3. **Automatic Reordering**: Reorders columns if they don't match the expected structure
4. **Warning System**: Alerts when column structure differences are detected

### Example Fix
**Before (Incorrect)**:
```
SELL 13.0 CVNY	FILL	13	576.55	Jul 10, 2025, 09:35:44 AM
SELL 0.01 JNJ	FILL			Jul 11, 2025, 03:54:30 PM	0.01	1.56784
```

**After (Correct)**:
```
SELL 13.0 CVNY	FILL	13	576.55	Jul 10, 2025, 09:35:44 AM
SELL 0.01 JNJ	FILL	0.01	1.56784	Jul 11, 2025, 03:54:30 PM
```

## Benefits
1. **Historical Data**: Maintains a complete history of all trades in one file
2. **Analysis**: Enables easy analysis of trading patterns over time
3. **Backup**: Provides a backup of all trade data in a single location
4. **Flexibility**: Optional parameter doesn't affect existing functionality
5. **Performance**: Efficient pandas operations for data concatenation
6. **Data Integrity**: Ensures consistent column structure and data alignment 
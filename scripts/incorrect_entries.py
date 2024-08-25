import pandas as pd

def check_incorrect_entries(df):
    incorrect_entries_count = {}

    # Check for incorrect entries in numeric columns (e.g., negative values)
    for col in df.select_dtypes(include=[float, int]).columns:
        incorrect_count = df[df[col] < 0].shape[0]
        if incorrect_count > 0:
            incorrect_entries_count[col] = incorrect_count

    # Add other checks if needed (e.g., for non-numeric columns)
    # Example: Check for unexpected values in categorical columns
    # for col in df.select_dtypes(include=[object]).columns:
    #     unexpected_values = df[~df[col].isin(expected_categories)]
    #     incorrect_count = unexpected_values.shape[0]
    #     if incorrect_count > 0:
    #         incorrect_entries_count[col] = incorrect_count

    return incorrect_entries_count


def replace_negative_with_zero(df):
    df[df < 0] = 0
    return df
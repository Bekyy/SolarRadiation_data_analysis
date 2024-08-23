import pandas as pd

def check_incorrect_entries(df):
    """
    This function checks for incorrect entries in a DataFrame.
    It considers negative values in numeric columns as incorrect entries.
    Returns a dictionary with column names as keys and the count of incorrect entries as values.
    """
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
    """
    Replaces all negative values in the DataFrame with zero.

    Parameters:
    df (pd.DataFrame): The DataFrame to process.

    Returns:
    pd.DataFrame: The DataFrame with negative values replaced by zero.
    """
    df[df < 0] = 0
    return df
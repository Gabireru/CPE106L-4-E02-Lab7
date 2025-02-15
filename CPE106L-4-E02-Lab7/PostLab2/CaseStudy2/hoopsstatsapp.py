"""
File: hoopstatsapp.py

The application for analyzing basketball stats.
"""

from hoopstatsview import HoopStatsView
import pandas as pd

def main():
    """Creates the data frame and view and starts the app."""
    frame = pd.read_csv("cleanbrogdonstats.csv")
    HoopStatsView(frame)

if __name__ == "__main__":
    main()
    import pandas as pd

def cleanStats(df):
    """
    Cleans a basketball statistics DataFrame by splitting columns (FG, 3PT, FT)
    from "<makes>-<attempts>" format into separate columns.

    Parameters:
    df (pd.DataFrame): The original DataFrame containing basketball statistics.

    Returns:
    pd.DataFrame: The cleaned DataFrame with separate "makes" and "attempts" columns.
    """
    # Define columns to process
    stat_columns = ['FG', '3PT', 'FT']

    for col in stat_columns:
        if col in df.columns:
            # Split only non-null values and handle potential errors
            new_cols = df[col].str.split('-', expand=True)
            
            if new_cols.shape[1] == 2:  # Ensure splitting was successful
                df[f"{col}M"] = pd.to_numeric(new_cols[0], errors='coerce')  # Makes
                df[f"{col}A"] = pd.to_numeric(new_cols[1], errors='coerce')  # Attempts
            
            # Drop the original column
            df.drop(columns=[col], inplace=True)

    return df


class HoopStatsView:
    """
    Class to represent the basketball statistics view.
    """

    def __init__(self, csv_file):
        """
        Initializes the class by loading and cleaning data from a CSV file.

        Parameters:
        csv_file (str): Path to the CSV file containing basketball statistics.
        """
        # Load the dataset
        self.df = pd.read_csv(csv_file)

        # Clean the dataset using cleanStats
        self.df = cleanStats(self.df)

    def display(self):
        """Displays the first few rows of the cleaned dataset."""
        print(self.df.head())


# Example usage
if __name__ == "__main__":
    # Replace 'basketball_data.csv' with the actual file path
    stats_view = HoopStatsView("basketball_data.csv")
    stats_view.display()

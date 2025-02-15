import pandas as pd
from hoopstatsview import HoopStatsView

def cleanStats(df):
    """Cleans the basketball statistics DataFrame by splitting 'makes-attempts' format into separate columns."""

    # Check if the FG, 3PT, and FT columns exist before processing
    if 'FG' in df.columns:
        df[['FGM', 'FGA']] = df['FG'].str.split('-', expand=True).astype(int)
        df.drop(columns=['FG'], inplace=True)

    if '3PT' in df.columns:
        df[['3PM', '3PA']] = df['3PT'].str.split('-', expand=True).astype(int)
        df.drop(columns=['3PT'], inplace=True)

    if 'FT' in df.columns:
        df[['FTM', 'FTA']] = df['FT'].str.split('-', expand=True).astype(int)
        df.drop(columns=['FT'], inplace=True)

    return df

def main():
    """Loads, cleans, and passes data to the HoopStatsView."""
    frame = pd.read_csv("rawbrogdonstats.csv")  # Load raw data
    frame = cleanStats(frame)  # Clean the data
    frame.to_csv("cleanbrogdonstats.csv", index=False)  # Save cleaned data
    print("Data cleaning completed. Check 'cleanbrogdonstats.csv'.")
    HoopStatsView(frame)  # Pass cleaned data to the UI

if __name__ == "__main__":
    main()

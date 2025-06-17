# Module for reading data from AWS S3 bucket

import pandas as pd
import boto3 as bt
import os

# Data stored in AWS S3 bucket and local copy
Bucket_Name = 'cqalvesp-data-ingestion'
S3_KEY = 'fraud_data/raw/creditcard.csv'
LOCAL_FILE = '../data/raw/creditcard.csv'

s3 = bt.client('s3')

# Function to download data file from S3
def download_from_s3():
    if not os.path.exists('../data/raw'):
        os.makedirs('../data/raw')

    print(f"Downloading {S3_KEY} from S3 bucket {Bucket_Name}...")
    s3.download_file(Bucket_Name, S3_KEY, LOCAL_FILE)
    print(f"Download complete.")
    return

# Load fraud data with pandas framework
def load_csv():
    df = pd.read_csv(LOCAL_FILE)
    print(f"Loaded {len(df)} rows and {len(df.columns)} columns.")
    return df



if __name__ == "__main__":
    download_from_s3()
    df = load_csv()

    # View the dataframe before cleaning
    print(df.info())
    print(df.head())

    # Clean the dataframe by dropping null values and duplicates
    cleaned_df = df.dropna()
    cleaned_df = cleaned_df.drop_duplicates()

    # Save the cleaned dataframe to a new csv file
    cleaned_df.to_csv("../data/clean/creditcard_clean.csv", index=False)



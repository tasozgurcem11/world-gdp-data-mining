import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import argparse



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process, analyze and plot GDP data.')
    # parser.add_argument('', '--analyze', action='store_true', help='Analyze data')
    parser.add_argument('--export', action='store_true', help='Export analyzed data')
    parser.add_argument('--input_dir', type=str, default='./data', help='Input directory')
    parser.add_argument('--output_dir', type=str, default='./output', help='Output directory')
    args = parser.parse_args(['--export'])

    # Read data
    gdp = pd.read_csv(os.path.join(args.input_dir, 'gdp.csv'))
    gdp_growth = pd.read_csv(os.path.join(args.input_dir, 'gdp_growth.csv'), index_col=0)
    gdp_per_capita = pd.read_csv(os.path.join(args.input_dir, 'gdp_per_capita.csv'), index_col=0)
    gdp_per_capita_growth = pd.read_csv(os.path.join(args.input_dir, 'gdp_per_capita_growth.csv'), index_col=0)
    gdp_ppp = pd.read_csv(os.path.join(args.input_dir, 'gdp_ppp.csv'), index_col=0)
    gdp_ppp_per_capita = pd.read_csv(os.path.join(args.input_dir, 'gdp_ppp_per_capita.csv'), index_col=0)

    # Process data
    unwanted_cols = ['Indicator Name', 'Indicator Code']
    gdp = gdp.drop(unwanted_cols, axis=1)
    gdp_growth = gdp_growth.drop(unwanted_cols, axis=1)
    gdp_per_capita = gdp_per_capita.drop(unwanted_cols, axis=1)
    gdp_per_capita_growth = gdp_per_capita_growth.drop(unwanted_cols, axis=1)
    gdp_ppp = gdp_ppp.drop(unwanted_cols, axis=1)
    gdp_ppp_per_capita = gdp_ppp_per_capita.drop(unwanted_cols, axis=1)


    gdp.fillna('', inplace=True)
    gdp_growth.fillna('', inplace=True)
    gdp_per_capita.fillna('', inplace=True)
    gdp_per_capita_growth.fillna('', inplace=True)
    gdp_ppp.fillna('', inplace=True)
    gdp_ppp_per_capita.fillna('', inplace=True)

    gdp.rename(columns={'Country Name': 'Country', 'Country Code': 'Code'}, inplace=True)
    gdp_growth.rename(columns={'Country Name': 'Country', 'Country Code': 'Code'}, inplace=True)
    gdp_per_capita.rename(columns={'Country Name': 'Country', 'Country Code': 'Code'}, inplace=True)
    gdp_per_capita_growth.rename(columns={'Country Name': 'Country', 'Country Code': 'Code'}, inplace=True)
    gdp_ppp.rename(columns={'Country Name': 'Country', 'Country Code': 'Code'}, inplace=True)
    gdp_ppp_per_capita.rename(columns={'Country Name': 'Country', 'Country Code': 'Code'}, inplace=True)

    print(gdp.head())
    print(gdp_growth.head())
    print(gdp_per_capita.head())
    print(gdp_per_capita_growth.head())
    print(gdp_ppp.head())
    print(gdp_ppp_per_capita.head())

    # Export data
    if args.export:
        # if output directory does not exist, create it
        if not os.path.exists(args.output_dir):

            os.makedirs(args.output_dir, exist_ok=True)

        gdp.to_csv(os.path.join(args.output_dir, 'gdp.csv'))
        gdp_growth.to_csv(os.path.join(args.output_dir, 'gdp_growth.csv'))
        gdp_per_capita.to_csv(os.path.join(args.output_dir, 'gdp_per_capita.csv'))
        gdp_per_capita_growth.to_csv(os.path.join(args.output_dir, 'gdp_per_capita_growth.csv'))
        gdp_ppp.to_csv(os.path.join(args.output_dir, 'gdp_ppp.csv'))
        gdp_ppp_per_capita.to_csv(os.path.join(args.output_dir, 'gdp_ppp_per_capita.csv'))

    # Load data
    df = pd.read_csv('data/gdp_per_capita.csv', on_bad_lines='skip')

    # Clean data
    temp_df = df[['Country Code', 'Country Name', 'Indicator Name', 'Indicator Code']]
    df.drop(columns=['Country Code', 'Country Name', 'Indicator Name', 'Indicator Code'], inplace=True)
    df = df.pct_change(axis='columns', periods=-1)

    df = pd.concat([df, temp_df], axis=1)

    print(df.loc[df['Country Name'] == 'France']['2018'])

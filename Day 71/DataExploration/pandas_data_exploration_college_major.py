# -*- coding: utf-8 -*-
"""Pandas Data Exploration - College Major.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14DSvDMKqlWVGvtcuqAF8RAD0ZtzeDgsG
"""

import pandas as pd
df = pd.read_csv('salaries_by_college_major.csv')

df.head()

df.shape

df.columns

df.isna()

df.tail()

clean_df = df.dropna()
clean_df.tail()

clean_df['Starting Median Salary'].max()

clean_df['Starting Median Salary'].idxmax()

clean_df['Undergraduate Major'][43]

clean_df.loc[43]

(clean_df['Undergraduate Major'][clean_df['Mid-Career Median Salary'].idxmax()], clean_df['Mid-Career Median Salary'].max())

(clean_df['Undergraduate Major'][clean_df['Starting Median Salary'].idxmin()], clean_df['Starting Median Salary'].min())

(clean_df['Undergraduate Major'][clean_df['Mid-Career Median Salary'].idxmin()], clean_df['Mid-Career Median Salary'].min())

"""Calculate the difference between the earnings of the 10th and 90th percentile:"""

spread_col = clean_df['Mid-Career 90th Percentile Salary'] - clean_df['Mid-Career 10th Percentile Salary']
clean_df.insert(1, 'Spread', spread_col)
clean_df.head()

"""See which degrees have the smallest spread"""

low_risk = clean_df.sort_values('Spread')
low_risk[['Undergraduate Major', 'Spread']].head()

"""Find the top 5 degrees with the highest values in the 90th percentile:"""

clean_df.sort_values('Mid-Career 90th Percentile Salary', ascending=False)[['Undergraduate Major', 'Mid-Career 90th Percentile Salary']].head()

"""Find the degrees with the greatest spread in salaries (which majors have the largest difference between high and low earners after graduation)."""

clean_df.sort_values('Spread', ascending=False)[['Undergraduate Major', 'Spread']].head()

"""Sum rows that belong to a particular category:"""

clean_df.groupby('Group').count()

"""And get the mean for each group:"""

pd.options.display.float_format = '{:,.2f}'.format 
clean_df.groupby('Group').mean()
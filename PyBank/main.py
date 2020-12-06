#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[4]:


#import budget file into dataframe
csv_path = "Resources/budget_data.csv"

budget_df = pd.read_csv(csv_path, low_memory=False)
budget_df


# In[5]:


#define required variables, ie. counts, sum, mean
total_months = budget_df["Date"].count()
sum_pnl = budget_df['Profit/Losses'].sum()
mean_pnl = (budget_df['Profit/Losses'].loc[(total_months-1)] - budget_df['Profit/Losses'].loc[0]) / (total_months-1)
mean_pnl = mean_pnl.round(2)

#find MOM PnL Change
budget_diff_df = budget_df['Profit/Losses'].diff()
#find max/min MOM PnL change
max_index = budget_diff_df.idxmax()
min_index = budget_diff_df.idxmin()
#find row data relative to max/min MOM PnL change, setting up to build summary
max_date = budget_df.iloc[max_index,0]
max_diff = budget_diff_df.iloc[max_index].round(decimals=0)
min_date = budget_df.iloc[min_index,0]
min_diff = budget_diff_df.iloc[min_index].round(decimals=0)


# In[14]:


#setting summary items to variable for cleaner look
header_1 = "Financial Analysis"
header_2 = "______________________________________________________"
header_3 = ""
total_months_summary = f'Total Months: {total_months}'
sum_pnl_summary = f'Total: ${sum_pnl}'
mean_pnl_summary = f'Average Change: ${mean_pnl}'
greatest_inc_summary = f'Greatest Increase in Profits: {max_date} (${max_diff:.0f})'
greatest_dec_summary = f'Greatest Decrease in Profits: {min_date} (${min_diff:.0f})'


# In[15]:


#set up print in Terminal
print(header_1)
print(header_2)
print(header_3)
print(total_months_summary)
print(sum_pnl_summary)
print(mean_pnl_summary)
print(greatest_inc_summary)
print(greatest_dec_summary)


# In[17]:


#export summary to .txt file
with open("Analysis/analysis.txt","w") as text_file:
        print(header_1,file=text_file)
        print(header_2,file=text_file)
        print(header_3,file=text_file)
        print(total_months_summary,file=text_file)
        print(sum_pnl_summary,file=text_file)
        print(mean_pnl_summary,file=text_file)
        print(greatest_inc_summary,file=text_file)
        print(greatest_dec_summary,file=text_file)


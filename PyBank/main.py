{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "from pandas import DataFrame\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Date</th>\n",
       "      <th>Profit/Losses</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Jan-2010</td>\n",
       "      <td>867884</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Feb-2010</td>\n",
       "      <td>984655</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Mar-2010</td>\n",
       "      <td>322013</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Apr-2010</td>\n",
       "      <td>-69417</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>May-2010</td>\n",
       "      <td>310503</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>81</th>\n",
       "      <td>Oct-2016</td>\n",
       "      <td>102685</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>82</th>\n",
       "      <td>Nov-2016</td>\n",
       "      <td>795914</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>83</th>\n",
       "      <td>Dec-2016</td>\n",
       "      <td>60988</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>84</th>\n",
       "      <td>Jan-2017</td>\n",
       "      <td>138230</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>85</th>\n",
       "      <td>Feb-2017</td>\n",
       "      <td>671099</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>86 rows × 2 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "        Date  Profit/Losses\n",
       "0   Jan-2010         867884\n",
       "1   Feb-2010         984655\n",
       "2   Mar-2010         322013\n",
       "3   Apr-2010         -69417\n",
       "4   May-2010         310503\n",
       "..       ...            ...\n",
       "81  Oct-2016         102685\n",
       "82  Nov-2016         795914\n",
       "83  Dec-2016          60988\n",
       "84  Jan-2017         138230\n",
       "85  Feb-2017         671099\n",
       "\n",
       "[86 rows x 2 columns]"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "csv_path = \"Resources/budget_data.csv\"\n",
    "\n",
    "budget_df = pd.read_csv(csv_path, low_memory=False)\n",
    "budget_df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "total_months = budget_df[\"Date\"].count()\n",
    "sum_pnl = budget_df['Profit/Losses'].sum()\n",
    "mean_pnl = (budget_df['Profit/Losses'].loc[(total_months-1)] - budget_df['Profit/Losses'].loc[0]) / (total_months-1)\n",
    "mean_pnl = mean_pnl.round(2)\n",
    "budget_diff_df = budget_df['Profit/Losses'].diff()\n",
    "max_index = budget_diff_df.idxmax()\n",
    "min_index = budget_diff_df.idxmin()\n",
    "\n",
    "max_date = budget_df.iloc[max_index,0]\n",
    "max_diff = budget_diff_df.iloc[max_index].round(decimals=0)\n",
    "min_date = budget_df.iloc[min_index,0]\n",
    "min_diff = budget_diff_df.iloc[min_index].round(decimals=0)\n"
   ]
  },
  {
   "cell_type": "code",
<<<<<<< Updated upstream
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'Financial Analysis': ['______________________________________________________',\n",
       "  ' ',\n",
       "  'Total Months: 86',\n",
       "  'Total: $38382578',\n",
       "  'Average Change: $-2315.12',\n",
       "  'Greatest Increase in Profits: Feb-2012 ($1926159.0)',\n",
       "  'Greatest Decrease in Profits: Sep-2013 ($-2196167.0)']}"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
=======
   "execution_count": 25,
   "metadata": {},
   "outputs": [],
>>>>>>> Stashed changes
   "source": [
    "header_1 = \"Financial Analysis\"\n",
    "header_2 = \"______________________________________________________\"\n",
    "header_3 = \" \"\n",
    "total_months_summary = f'Total Months: {total_months}'\n",
    "sum_pnl_summary = f'Total: ${sum_pnl}'\n",
    "mean_pnl_summary = f'Average Change: ${mean_pnl}'\n",
    "greatest_inc_summary = f'Greatest Increase in Profits: {max_date} (${max_diff})'\n",
<<<<<<< Updated upstream
    "greatest_dec_summary = f'Greatest Decrease in Profits: {min_date} (${min_diff})'\n",
    "\n",
    "summary_list = {header_1:[\n",
    "    header_2,\n",
    "    header_3,\n",
    "    total_months_summary,\n",
    "    sum_pnl_summary,\n",
    "    mean_pnl_summary,\n",
    "    greatest_inc_summary,\n",
    "    greatest_dec_summary\n",
    "    ]}\n",
    "summary_list\n"
=======
    "greatest_dec_summary = f'Greatest Decrease in Profits: {min_date} (${min_diff})'\n"
>>>>>>> Stashed changes
   ]
  },
  {
   "cell_type": "code",
<<<<<<< Updated upstream
   "execution_count": 21,
=======
   "execution_count": 26,
>>>>>>> Stashed changes
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Financial Analysis\n",
      "______________________________________________________\n",
      " \n",
      "Total Months: 86\n",
      "Total: $38382578\n",
      "Average Change: $-2315.12\n",
      "Greatest Increase in Profits: Feb-2012 ($1926159.0)\n",
      "Greatest Decrease in Profits: Sep-2013 ($-2196167.0)\n"
     ]
    }
   ],
   "source": [
    "print(header_1)\n",
    "print(header_2)\n",
    "print(header_3)\n",
    "print(total_months_summary)\n",
    "print(sum_pnl_summary)\n",
    "print(mean_pnl_summary)\n",
    "print(greatest_inc_summary)\n",
    "print(greatest_dec_summary)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "write() argument must be str, not dict",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-23-61dd0897831d>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[0;32mwith\u001b[0m \u001b[0mopen\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"Analysis/analysis.txt\"\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m\"w\"\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0moutput\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 2\u001b[0;31m     \u001b[0moutput\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mwrite\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0msummary_list\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;31mTypeError\u001b[0m: write() argument must be str, not dict"
     ]
    }
   ],
   "source": [
<<<<<<< Updated upstream
    "with open(\"Analysis/analysis.txt\", \"w\") as output:\n",
    "    output.write(summary_list)"
=======
    "with open(\"Analysis/analysis.txt\",\"w\") as text_file:\n",
    "        print(header_1)\n",
    "        print(header_2)\n",
    "        print(header_3)\n",
    "        print(total_months_summary)\n",
    "        print(sum_pnl_summary)\n",
    "        print(mean_pnl_summary)\n",
    "print(greatest_inc_summary)\n",
    "print(greatest_dec_summary)"
>>>>>>> Stashed changes
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}

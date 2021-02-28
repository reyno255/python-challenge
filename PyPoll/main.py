#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


#import file into df
csv_path = "Resources/election_data.csv"

election_df = pd.read_csv(csv_path, low_memory=False)
election_df


# In[3]:


#calc total votes
total_votes = election_df.Candidate.count()
#groupby candidate to get total votes by candidate, then sort descending
votes_byCandidate = election_df.groupby(['Candidate']).count()[['Voter ID']].sort_values(by="Voter ID",ascending=False)
#calc % votes by candidate name
perc_votes = (votes_byCandidate / total_votes * 100).round(decimals=3)


# In[4]:


#set up print statement
print("Election Results")
print("_____________________________________")
print(f'Total Votes: {total_votes}')
print("_____________________________________")
print(f'{votes_byCandidate.tail().index.values[0]}: {perc_votes.iloc[0,0]:.3f}% ({votes_byCandidate.iloc[0,0]})')
print(f'{votes_byCandidate.tail().index.values[1]}: {perc_votes.iloc[1,0]:.3f}% ({votes_byCandidate.iloc[1,0]})')
print(f'{votes_byCandidate.tail().index.values[2]}: {perc_votes.iloc[2,0]:.3f}% ({votes_byCandidate.iloc[2,0]})')
print(f'{votes_byCandidate.tail().index.values[3]}: {perc_votes.iloc[3,0]:.3f}% ({votes_byCandidate.iloc[3,0]})')
print("_____________________________________")
print(f'Winner: {votes_byCandidate.tail().index.values[0]}')
print("_____________________________________")


# In[5]:


#package and send print items to .txt file
with open("Analysis/analysis.txt","w") as text_file:
        print("Election Results", file=text_file)
        print("_____________________________________", file=text_file)
        print(f'Total Votes: {total_votes}', file=text_file)
        print("_____________________________________", file=text_file)
        print(f'{votes_byCandidate.tail().index.values[0]}: {perc_votes.iloc[0,0]:.3f}% ({votes_byCandidate.iloc[0,0]})', file=text_file)
        print(f'{votes_byCandidate.tail().index.values[1]}: {perc_votes.iloc[1,0]:.3f}% ({votes_byCandidate.iloc[1,0]})', file=text_file)
        print(f'{votes_byCandidate.tail().index.values[2]}: {perc_votes.iloc[2,0]:.3f}% ({votes_byCandidate.iloc[2,0]})', file=text_file)
        print(f'{votes_byCandidate.tail().index.values[3]}: {perc_votes.iloc[3,0]:.3f}% ({votes_byCandidate.iloc[3,0]})', file=text_file)
        print("_____________________________________", file=text_file)
        print(f'Winner: {votes_byCandidate.tail().index.values[0]}', file=text_file)
        print("_____________________________________", file=text_file)


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# read roster as data frame
roster = pd.read_csv('C:/Users/Annika - Accounting/roster-processing/roster.csv', encoding='latin-1')
print(len(roster.index))

# drop if organization contains the word leagues
noleaguesroster = roster[~roster.Organization.str.contains('League')]

# read goodtitles.csv
goodtitles = pd.read_csv('C:/Users/Annika - Accounting/roster-processing/goodtitles.csv', encoding='latin-1')
goodtitleslist = goodtitles['Title'].values.tolist()

# for title in goodtitles, add row to relevantroster
relevantroster = noleaguesroster[noleaguesroster['Title'].isin(goodtitleslist)]
print(len(relevantroster))
print(len(relevantroster.index)/len(roster.index))

relevantroster.to_excel("relevantattendees.xlsx")
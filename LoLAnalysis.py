#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 19:04:25 2017

@author: wellingtonjohnson
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df = pd.read_csv('../Desktop/leagueoflegends/_LeagueofLegends.csv')

LoL_teams = df[['Year','blueTeamTag','bResult','rResult']]
      
# C9 Analysis
Team = 'C9'
Blue_Side = df.loc[df['blueTeamTag'] == Team]
Red_Side = df.loc[df['redTeamTag'] == Team]
frames = [Blue_Side,Red_Side]
C9 = pd.concat(frames)

c9_red = C9['redTeamTag'].value_counts()[Team]
c9_red_win = C9.groupby('redTeamTag').rResult.sum()[Team]
c9_blue = C9['blueTeamTag'].value_counts()[Team]
c9_blue_win = C9.groupby('blueTeamTag').bResult.sum()[Team]

blue_win = C9.loc[df['bResult'] == True,['gamelength', 'blueTeamTag','Year']]
C9_blue_win = blue_win.loc[blue_win['blueTeamTag'] == 'C9',['blueTeamTag','gamelength','Year']]
C9_bluewin_avgtime = C9_blue_win.gamelength.mean() #C9 blue side avg win time 2015-2017

red_win = C9.loc[df['rResult'] == True,['gamelength', 'redTeamTag','Year']]
C9_red_win = red_win.loc[red_win['redTeamTag'] == 'C9',['redTeamTag','gamelength','Year']]
C9_red_win_avgtime = C9_red_win.gamelength.mean() #C9 red side avg win time 2015-2017

C9_avg_game_length = C9['gamelength'].mean() #C9 avg win time both sides combined 2015-2017

                       
                       
# North America Analysis for 2017
Region = 'North_America'
LoL_NA = df.loc[df['League'] == Region]


LoL_NA_17 = LoL_NA.loc[LoL_NA['Year'] == 2017]

Long_game_df17 = LoL_NA_17[LoL_NA_17['gamelength'] >= 40]

avg_game_time17 = LoL_NA_17['gamelength'].mean()
print(LoL_NA_17.describe()) # Avg gamelength is 37.72 minutes, longest is 67 minutes, shortest is 25 minutes

#Red Side NA 2017 Analysis

#Red Side Champ counts for each position
red_top_counts = LoL_NA_17['redTopChamp'].value_counts()
red_jungle_counts = LoL_NA_17['redJungleChamp'].value_counts()
red_mid_counts = LoL_NA_17['redMiddleChamp'].value_counts()
red_adc_counts = LoL_NA_17['redADCChamp'].value_counts()
red_support_counts = LoL_NA_17['redSupportChamp'].value_counts()

red_champs =[red_top_counts,red_jungle_counts,red_mid_counts,red_adc_counts,red_support_counts]
red_side_champs = pd.concat(red_champs)
red_side_champsDF = red_side_champs.to_frame(name=None)
red_side_champsDF['Index'] = red_side_champsDF.index
red_side_champsDF = red_side_champsDF.rename(columns={0:'Count','Index':'Champs'})
hi1 = red_side_champsDF.nlargest(30,'Count')
red_30 = hi1.drop_duplicates('Champs')


#Blue Side NA 2017 Analysis

#Blue side champ counts for each position
blue_top_counts = LoL_NA_17['blueTopChamp'].value_counts()
blue_jungle_counts = LoL_NA_17['blueJungleChamp'].value_counts()
blue_mid_counts = LoL_NA_17['blueMiddleChamp'].value_counts()
blue_adc_counts = LoL_NA_17['blueADCChamp'].value_counts()
blue_support_counts = LoL_NA_17['blueSupportChamp'].value_counts()

blue_champs =[blue_top_counts,blue_jungle_counts,blue_mid_counts,blue_adc_counts,blue_support_counts]
blue_side_champs = pd.concat(blue_champs)
blue_side_champsDF = blue_side_champs.to_frame(name=None)
blue_side_champsDF['Index'] = blue_side_champsDF.index
blue_side_champsDF = blue_side_champsDF.rename(columns={'Index':'Champs',0:'Count'})
hi2 = blue_side_champsDF.nlargest(30,'Count')
blue_30 = hi2.drop_duplicates('Champs')



# Plots for Top 30 Champs played Blue and Red Side in NA 2017
stripBlue = sns.stripplot(x='Count',y='Champs',data=blue_30,jitter=True)
plt.title("Top 30 Champs Played Blue Side in NA: 2017")
plt.show()

stripRed = sns.stripplot(x='Count',y='Champs',data=red_30,jitter=True)
plt.title("Top 30 Champs Played Red Side in NA: 2017")
plt.show()






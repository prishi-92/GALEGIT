import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image
import numpy as np # numerical computing 
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt #visualization
import seaborn as sns #modern visualization

st.set_page_config(page_title='Assignment')
st.header('IPL Stats')

###--------------LOAD DATAFRAME---------------------###
st.write("Matches Data")
excel_file = 'data_p.xlsx'
sheet_name = 'data'
sns.set_style("darkgrid")
plt.rcParams['figure.figsize'] = (14, 8)


@st.cache
def load_data(nrows):
    data = pd.read_csv(r'C:\Users\priya\Downloads\gale\matches.csv', encoding='unicode_escape')
    return data


@st.cache
def load_center_data(nrows):
    data = pd.read_csv(r'C:\Users\priya\Downloads\gale\deliveries.csv',encoding= 'unicode_escape')
    return data


data_load_state = st.text('Loading data...')
matches = load_data(1000)
deliveries = load_center_data(1000)
# matches = pd.read_csv(r'C:\Users\priya\Downloads\gale\matches.csv', encoding= 'unicode_escape')
st.dataframe(matches)
st.write("Deliveries Data")
# deliveries = pd.read_csv(r'C:\Users\priya\Downloads\gale\deliveries.csv', encoding= 'unicode_escape')
st.dataframe(deliveries)
#st.matches.info() 
st.write("How many rows & Columns are there.")
st.dataframe(matches.shape)
st.write("what stat says about matches data.")
st.dataframe(matches.describe())
st.write("Let's check the dataframe.")
st.dataframe(matches.head())


st.write("1.Top 4 teams in terms of wins by season?")
Match_winners = matches.groupby('season').winner.value_counts().nlargest(4).sort_index(ascending=True)
Match_winners.plot(x='season',kind='bar',stacked=False,title='Matches Won Each Season',color=['Orange', 'red', 'green', 'Violet'],rot=0, figsize=(10,7), fontsize=10)
st.set_option('deprecation.showPyplotGlobalUse', False)
st.pyplot()
st.write("2.Team winning the most number of tosses by season?")
st.write("Having solved those not-so-tough questions above, we are nowhere to extract a critical insight — which is — Has winning toss actually helped in winning the match?Using our same approach of dividing our problem into chunks — we can separate this question into two — match winner and toss winner if both of them are same — then it’s a success and if not it’s a failure. Before visualizing the outcome, let us first see how the numbers look.")
ss = matches['toss_winner'] == matches['winner']
ss.groupby(ss).size()
Team_winnng_most_tosses = pd.crosstab(ss, matches['season'])
plt.figure(figsize=(15, 9))
plt.xlabel('Seasons')
plt.ylabel('Teams')
plt.title('Team winning the most number of tosses by season')
sns.heatmap(Team_winnng_most_tosses, annot = True, cmap = 'flare', fmt = 'd', cbar_kws={"orientation": "horizontal"});
st.set_option('deprecation.showPyplotGlobalUse', False)
st.pyplot()
st.write("3.Player winning the highest number of “Player of the Match” by season?")
top_players = matches.groupby('season').player_of_match.value_counts().nlargest().sort_index(ascending=True)
top_players.plot(x='season',kind='bar',stacked=False,title='Player of the Match',color=['Orange', 'red', 'green', 'Violet','Blue','Grey'],rot=0, figsize=(10,7), fontsize=10)
st.pyplot()
st.write("4.Team winning the most matches by season?")
st.write("The most successful IPL team is the team that has won most number of times. Which also means, answer it to this is as same as the above exercise except counting the number of instances in each season, here we’ve to count the number of instances in each winning team.")
matches_won_each_season = pd.crosstab(matches['winner'], matches['season'])
plt.figure(figsize=(15, 9))
plt.xlabel('Seasons')
plt.ylabel('Teams')
plt.title('Matches Won By Each Season')
sns.heatmap(matches_won_each_season, annot = True, cmap = 'flare', fmt = 'd', cbar_kws={"orientation": "horizontal"});
st.write("The Chennai Super Kings have been the most consistent team, winning at least 8 matches in each of the seasons they have played. This is backed up by the fact that they are the only team to reach the playoffs stage every season.")
st.pyplot()
st.write("5.Location with the most number of wins for the top team by season?")
matches_won_location = matches.groupby(['season','city']).winner.value_counts().nlargest().sort_index(ascending=True)
matches_won_location.plot(x='season',kind='bar',stacked=False,title='Location with the most number of wins teams',color=['Orange', 'red', 'green', 'Violet','Blue','Grey'],rot=0, figsize=(15,9), fontsize=9)
st.pyplot()
st.write("6.Percentage of teams deciding to bat when they won the toss by season?")
toss_winner = matches.groupby('season').toss_winner.value_counts(normalize=True).nlargest().sort_index(ascending=True)*100
toss_winner.plot(x='season',kind='bar',stacked=False,title='Percentage of teams deciding to bat when they won the toss',color=['Orange', 'red', 'green', 'Violet','Blue','Grey'],rot=0, figsize=(15,9), fontsize=9)
st.pyplot()
st.write("7.Location hosting the most number of matches by Season?")
city = matches.groupby('season').city.value_counts().nlargest(10).sort_index(ascending=True)
city.plot(x='season',kind='bar',stacked=False,title='Player of the Match',color=['Orange', 'red', 'green', 'Violet','Blue','Grey'],rot=0, figsize=(15,9), fontsize=9)
st.pyplot()
st.write("8.Team winning by the highest margin of runs by season?")
matches_win_by_runs = matches[['season','winner','win_by_runs']].sort_values(['win_by_runs'],ascending=False).head(10)
st.dataframe(matches_win_by_runs)
st.write("9.Team winning by the highest number of wickets by season?")
matches_win_by_wickets = matches[['season','winner','win_by_wickets']].sort_values(['win_by_wickets'],ascending=False).head(10)
st.dataframe(matches_win_by_wickets)
st.write("10.Number of times a team won the toss and the match by season?")
toss_winner = matches.groupby('season').toss_winner.value_counts().nlargest().sort_index(ascending=True)
toss_winner.plot(x='season',kind='bar',stacked=False,title='Number of times a team won the toss and the match',color=['Orange', 'red', 'green', 'Violet','Blue','Grey'],rot=0, figsize=(15,9), fontsize=9)
st.pyplot()
st.write("11.Player scoring the most runs in a match")
deliveries_players = deliveries.groupby(['match_id','batsman'])['total_runs'].sum().sort_values(ascending=False).head()
deliveries_players.plot(x='season',kind='bar',stacked=False,title='Player scoring the most runs in a match',color=['Orange', 'red', 'green', 'Violet','Blue','Grey'],rot=0, figsize=(15,9), fontsize=9)
st.pyplot()
st.write("12.Highest number of catches by an individual player")
deliveries_individual_player = deliveries.groupby(['match_id','dismissal_kind']).fielder.value_counts().sort_values(ascending=False).head()
deliveries_individual_player.plot(x='season',kind='bar',stacked=False,title='Team winning by the highest margin of runs',color=['Orange', 'red', 'green', 'Violet','Blue','Grey'],rot=0, figsize=(15,9), fontsize=9)
st.pyplot()


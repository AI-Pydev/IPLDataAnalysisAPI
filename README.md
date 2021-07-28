# IPLDataAnalysisAPI

This repo contains both Django & jupyter notebook (IPL Data Analysis.ipynb)

Steps:
pip install -r requirements.txt

./manage.py runserver 

# API:

Below API URL Format which can be change dynamically based on the input.
Below are the list of the supported parameters.

## GET parameter
1. year (can be any one from the dataset season)
2. size (Input selection like top 1 team ex size=1)
3. location (it's boolean)
4. toss_decision (It's boolean)
5. win_by_runs (It's boolean)


http://127.0.0.1:8000/api/match/**<winner_type>** it can be changed based on the column name present in the dataset.

## Solution (Year & size params are dynamic)

### Choose season (years) and get these stats:
    • Top 4 teams in terms of wins
        Top 4 team in the selected Season: http://127.0.0.1:8000/api/match/winner?size=4&year=2012
        Top 4 team in All Season: http://127.0.0.1:8000/api/match/winner?size=4
        ### Other:
        In All Season: http://127.0.0.1:8000/api/match/winner
        In Selected or specific season: http://127.0.0.1:8000/api/match/winner?year=2008
    • Which team won the most number of tosses in the season
        In the selected Season: http://127.0.0.1:8000/api/match/toss_winner?size=1&year=2012
        All Season: http://127.0.0.1:8000/api/match/toss_winner?size=1
        Other:
        In All Season: http://127.0.0.1:8000/api/match/toss_winner
        In Selected or specific season: http://127.0.0.1:8000/api/match/toss_winner
    • Which player won the maximum number of Player of the Match awards in the whole season
        All Season: http://127.0.0.1:8000/api/match/player_of_match?size=1
        In the selected Season: http://127.0.0.1:8000/api/match/player_of_match?size=1&year=2012
        Other:
        In All Season: http://127.0.0.1:8000/api/match/player_of_match
        In Selected or specific season: http://127.0.0.1:8000/api/match/player_of_match
    • Which team won max matches in the whole season
        All Season: http://127.0.0.1:8000/api/match/winner?size=1
        Selected Season: http://127.0.0.1:8000/api/match/winner?size=1&year=2012
        Other:
        In All Season: http://127.0.0.1:8000/api/match/winner
        In Selected or specific season: http://127.0.0.1:8000/api/match/winner?year=2008
    • Which location has the most number of wins for the top team
        All Season: http://127.0.0.1:8000/api/match/winner?location=1&size=1
        Selected Season: http://127.0.0.1:8000/api/match/winner?location=1&size=1&year=2012
        Other:
        In All Season: http://127.0.0.1:8000/api/match/winner?location=1
        In Selected or specific season: http://127.0.0.1:8000/api/match/winner?location=1&year=2008
    • Which % of teams decided to bat when they won the toss
        All Season: http://127.0.0.1:8000/api/match/winner?toss_decision=1
        Selected Season: http://127.0.0.1:8000/api/match/winner?toss_decision=1&year=2012
        Other:
        In All Season: http://127.0.0.1:8000/api/match/winner?toss_decision=1
        In Selected or specific season: http://127.0.0.1:8000/api/match/winner?toss_decision=1&year=2008
    • Which location hosted most number of matches 
        All Season: http://127.0.0.1:8000/api/match/venue?size=1
        Selected Season: http://127.0.0.1:8000/api/match/venue?size=1&year=2012
        Other:
        In All Season: http://127.0.0.1:8000/api/match/venue
        In Selected or specific season: http://127.0.0.1:8000/api/match/venue?year=2008
    • Which team won by the highest margin of runs  for the season
        All Season: http://127.0.0.1:8000/api/match/winner?win_by_runs=1&size=1
        Selected Season: http://127.0.0.1:8000/api/match/winner?win_by_runs=1&year=2012
        Other:
        In All Season: http://127.0.0.1:8000/api/match/winner?win_by_runs=1
        In Selected or specific season: http://127.0.0.1:8000/api/match/winner?win_by_runs=1&year=2008

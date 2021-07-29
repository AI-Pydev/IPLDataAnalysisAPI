import json

import pandas as pd
from rest_framework.response import Response
from rest_framework.views import APIView


class ReadDataFile:
    """
    Read data file for matches & deliveries

    """

    def __init__(self):
        self.matches_file_path = 'api/ipl_data/matches.csv'
        self.deliveries_file_path = 'api/ipl_data/deliveries.csv'

    def read_matches(self):
        """
        Read matches csv file
        """
        try:
            matches = pd.read_csv(self.matches_file_path)
            return matches
        except FileNotFoundError:
            print("File Not Found")

    def read_deliveries(self):
        """
        Read deliveries csv file
        """
        try:
            deliveries = pd.read_csv(self.deliveries_file_path)
            return deliveries
        except FileNotFoundError:
            print('File Not Found')


class Match(APIView):
    """
    API View based class
    """

    def winner_team(self, winner_type):
        """
        Method to filter data based on the params
        """
        try:
            obj = ReadDataFile()
            matches = obj.read_matches()
            year = int(self.request.query_params.get('year', 0))
            size = int(self.request.query_params.get('size', 0))
            location = self.request.query_params.get('location', False)
            toss_decision = self.request.query_params.get('toss_decision', None)
            win_toss_and_match = self.request.query_params.get('win_toss_and_match', None)
            # Winning summary for all the season
            if year and year in matches.season.unique():
                data = matches.loc[matches['season'] == year]
            else:
                data = matches
            if location:
                data = data.groupby('venue')[winner_type].value_counts().sort_values(ascending=False)
            elif toss_decision:
                data = data.toss_decision.value_counts(normalize=True).mul(100).round(2).astype(str) + "%"
            elif winner_type in ['win_by_runs', 'win_by_wickets']:
                data = data[[winner_type, 'winner']].sort_values(by=winner_type, ascending=False)['winner']
            elif win_toss_and_match:
                data = matches.loc[matches['toss_winner'].str.lower() == matches['winner'].str.lower()]
            elif winner_type in ['batsman', 'fielder'] and year:
                deliveries = obj.read_deliveries()
                data = deliveries[deliveries['match_id'].isin(data.id)]
                if winner_type == 'batsman':
                    data = data.groupby('batsman')['batsman_runs'].count().sort_values(ascending=False)
                else:
                    data = data[data['dismissal_kind'] == 'caught'].groupby(['fielder'])[
                               'dismissal_kind'].count().sort_values(ascending=False)
            else:
                data = data.groupby(winner_type)[winner_type].count().sort_values(ascending=False)

            if size and size <= matches.shape[0]:
                data = data[:size]
            return data
        except Exception as ex:
            print(f'Error {ex}')

    def get(self, request, winner_type):
        """
        Get api to fetch data from the file
        """
        data = self.winner_team(winner_type)
        win_toss_and_match = self.request.query_params.get('win_toss_and_match', None)
        if win_toss_and_match:
            return Response({'winner_in_match': data.shape[0]})
        return Response(data=json.loads(data.to_json()))

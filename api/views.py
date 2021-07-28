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
        # try:
        matches = pd.read_csv(self.matches_file_path)
        return matches
        # except FileNotFoundError:
        #     pass

    def read_deliveries(self):
        # try:
        deliveries = pd.read_csv(self.deliveries_file_path)
        return deliveries
        # except FileNotFoundError:
        #     pass


class Match(APIView):

    def winner_team(self, winner_type, year, size, location=False, toss_decision=None, win_by_runs=None):
        obj = ReadDataFile()
        matches = obj.read_matches()
        if winner_type not in matches.columns:
            raise ValueError
        # Winning summary for all the season
        if year and year in matches.season.unique():
            data = matches.loc[matches['season'] == year]
        else:
            data = matches
        if location:
            data = data.groupby('venue')[winner_type].value_counts().sort_values(ascending=False)
        elif toss_decision:
            data = data.toss_decision.value_counts(normalize=True).mul(100).round(2).astype(str) + "%"
        elif win_by_runs:
            data = data[['win_by_runs', 'winner']].sort_values(by='win_by_runs', ascending=False)['winner']
            # data = data.iloc[data['win_by_runs'].idxmax()]
        else:
            data = data.groupby(winner_type)[winner_type].count().sort_values(ascending=False)

        if size and size <= matches.shape[0]:
            data = data[:size]
        return data

    def get(self, request, winner_type):
        year = int(self.request.query_params.get('year', 0))
        size = int(self.request.query_params.get('size', 0))
        location = self.request.query_params.get('location', False)
        toss_decision = self.request.query_params.get('toss_decision', None)
        win_by_runs = self.request.query_params.get('win_by_runs', None)
        data = self.winner_team(winner_type, year, size, location, toss_decision, win_by_runs)
        return Response(data=json.loads(data.to_json()))

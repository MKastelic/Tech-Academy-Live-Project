import urllib.request
import json
from django.db import models

from DataApp.models import HockeyTeam

url = 'https://www.thesportsdb.com/api/v1/json/1/search_all_teams.php?l=NHL'
json_data = json.loads(urllib.request.urlopen(url).read())

for index in range(0,31):
    team_data = json_data['teams'][index]
    HockeyTeam(team_id=team_data['idTeam'], team_name=team_data['strTeam']).save()
    

if __name__ == "__main__": main()

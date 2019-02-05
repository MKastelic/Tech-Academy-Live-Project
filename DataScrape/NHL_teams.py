#  This script will automatically populate the HockeyTeam model in the DataApp
#  with all of the current NHL team names using data from TheSportsDB.com api.
    
#  Run script in the Django Python shell (python manage.py shell)
#  at the shell prompt, >>> exec(open('NHL_teams.py').read())


import urllib.request
import json
from django.db import models

from DataApp.models import HockeyTeam
  
url = 'https://www.thesportsdb.com/api/v1/json/1/search_all_teams.php?l=NHL'
json_data = json.loads(urllib.request.urlopen(url).read())
 
for index in range(0, len(json_data['teams'])):
    team_data = json_data['teams'][index]
    HockeyTeam(team_id=team_data['idTeam'], team_name=team_data['strTeam']).save()

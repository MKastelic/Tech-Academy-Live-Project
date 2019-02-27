#  This script will automatically populate the BaseballTeam model in the DataApp
#  with all of the current MLB team names using data from TheSportsDB.com api.
    
#  Run script in the Django Python shell (python manage.py shell)
#  at the shell prompt, >>> exec(open('MLB_teams.py').read())

# Thank you to Mark -- this is basically a copy of his NHL_teams.py script

import urllib.request
import json
from django.db import models

from DataApp.models import BaseballTeam
  
url = 'https://www.thesportsdb.com/api/v1/json/1/search_all_teams.php?l=MLB'
json_data = json.loads(urllib.request.urlopen(url).read())
 
for index in range(0, len(json_data['teams'])):
    team_data = json_data['teams'][index]
    BaseballTeam(team_id=team_data['idTeam'], team_name=team_data['strTeam']).save()

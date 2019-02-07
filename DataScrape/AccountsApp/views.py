from django.shortcuts import render, redirect
import random
from .choices import state_choices # from our choices.py file, import our state_choices object.

# import our target model(s) below!
from django.contrib.auth.models import User
from DataApp.models import UserProfile, HockeyTeam

# Create your views here.
def register(request): # each view function takes an HttpRequest object as a parameter.

    nhl_team_list =  HockeyTeam.objects.all()
    nhl_team_names = list(nhl_team_list.values('team_name'))
    team_name_list = []
    for team in nhl_team_names:
        team_name_list.append(team['team_name'])

    context = { # basically saying 'this' object is equal to 'that' object; 'that' being the state_choices object we imported at the top of the page
        'state_choices': state_choices,
        'team_name_list': team_name_list
    }

    if request.method == 'POST':
        # create variables to pull the form input values; the request object for each variable will reference the name attribute defined in each input field in register.html
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        city = request.POST['city']
        state = request.POST['state']
        zipcode = request.POST['zipcode']
        favorite_nhl_team = request.POST['favorite_nhl_team']

        # use the User model's custom create_user helper method to insert values into the database under their correct fields; field = input name
        u1 = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password) # this also returns a user object which...
        u2 = UserProfile(user=u1, zip_code=zipcode, city=city, state=state, favorite_nhl_team=favorite_nhl_team) # we can pass into the UserProfile along with their zipcode.
        u1.save() # then we can save the changes to the database.
        u2.save()
        
        return redirect('login') # this currently redirects the user back to the homepage, potentially this can redirect a new user to a dashboard, etc.

    else:
        return render(request, 'accounts/register.html', context)

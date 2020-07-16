from django.contrib.auth import login
from django.shortcuts import redirect,render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
import sys
from django.contrib import messages
from django.conf import settings
from django.db.models import Sum
from datetime import date, timedelta
import base64

from appadmin.dashboard.forms import UserLoginForm
from appadmin.dashboard.models import *

def adminLogin(request):
    if request.method == "POST":
        username = "not logged in"
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            user = User.objects.filter(username=username).first()
            request.session['loggedin'] = 1
            request.session['usertype'] = 1
            request.session['username'] = user.username
            request.session['userid'] = user.id
            messages.add_message(request, messages.SUCCESS, "Welcome, Superadmin!")
            return HttpResponseRedirect(reverse('admindashboard'))
        context = {'form': form }
        messages.add_message(request, messages.ERROR, "Invalid login credentials!")
        return render(request, "login.html", context)
    else:
        return render(request, "login.html")
def adminDashboard(request):
    if request.method == "POST":
        goals = request.POST.getlist('goals', default=None)
        teamids = request.POST.getlist('teams', default=None)
        for idx, goal in enumerate(goals):
            goal = Goal(goal=goal, teamid=teamids[idx])
            goal.save()
    teams = Team.objects.all().values_list('id', flat=True)
    dateiter = date.today()
    dateiter = dateiter + timedelta(days=10)
    x = ','.join(str(i) for i in range(100) if i % 4 in (1, 2))
    xlist = x.split(',')
    count = 0
    goals = list(Goal.objects.all().values_list('goal','teamid'))
    goalidx = 0
    fixtures = []
    for pairings in schedule(list(teams)):
        if goals:
            goal1 = (int(goals[goalidx]), int(goals[goalidx+1]))
            goal2 = (int(goals[goalidx+2]), int(goals[goalidx+3]))
        else:
            goal1 = (0, 0)
            goal2 = (0, 0)
        index1 = int(xlist[count]) % 5 + 1
        index2 = int(xlist[count + 1]) % 5 + 1
        dateiter = dateiter + timedelta(days=1)
        datestr = dateiter.strftime("%B %d, %Y")
        fixtures.append({
            'goal1': goal1,
            'teamid1': (Team.objects.get(pk=pairings[1][0]).id, Team.objects.get(pk=pairings[1][1]).id),
            'match1': (Team.objects.get(pk=pairings[1][0]).name, Team.objects.get(pk=pairings[1][1]).name),
            'venue1': Venue.objects.get(id=index1).name,
            'goal2': goal2,
            'teamid2': (Team.objects.get(pk=pairings[3][0]).id, Team.objects.get(pk=pairings[3][1]).id),
            'match2': (Team.objects.get(pk=pairings[3][0]).name, Team.objects.get(pk=pairings[3][1]).name),
            'venue2': Venue.objects.get(id=index2).name,
            'date': datestr
        })
        count = count + 2
    teams = Team.objects.all()
    context = {
        'fixtures': fixtures,
        'teams': teams
    }
    return render(request, 'dashboard.html', context)
def showTeam(request, id):
    team = Team.objects.get(pk=id)
    members = Member.objects.filter(team=id).all()
    context = {
        'team':team,
        'members':members
    }
    return render(request, "team/showteam.html", context)

def adminLogout(request):
   try:
      del request.session['loggedin']
      del request.session['usertype']
      del request.session['username']
      del request.session['userid']
   except:
      pass
   messages.add_message(request, messages.SUCCESS, "See you, superadmin!")
   return render(request, "login.html")

def home(request):
    return redirect('/team/register')

def schedule(units, sets=None):
    if len(units) % 2:
        units.append(None)
    count = len(units)
    sets = sets or (count - 1)
    half = int(count / 2)
    schedule = []
    for turn in range(sets):
        pairings = []
        for i in range(half):
            pairings.append((units[i], units[count-i-1]))
        units.insert(1, units.pop())
        schedule.append(pairings)
    return schedule





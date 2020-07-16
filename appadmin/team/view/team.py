from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from datetime import date
from datetime import timedelta
import sys
from django.contrib import messages

from appadmin.team.forms import *
from appadmin.team.models import *
from appadmin.dashboard.forms import *
from appadmin.dashboard.models import *

# Create your views here.

def teamAdd(request):
    if Team.objects.all().count() >= 10:
        return HttpResponseRedirect(reverse('listfixture'))
    if request.method == "POST":
        team = Team(name=request.POST['name'],
                    coach=request.POST['coach'],
                    manager=request.POST['manager'])
        team.save()
        members = request.POST.getlist('members', default=None)
        for member in members:
            member = Member(name=member, team=team)
            member.save()
        context = {
            'team':team.name
        }
        return render(request,  "register-complete.html",context)
    context = {
        'user': 'user'
    }
    return render(request, 'team/add.html', context)

def listFixture(request):
    teams = Team.objects.all().values_list('id', flat=True)
    dateiter = date.today()
    dateiter = dateiter + timedelta(days=10)
    x =','.join(str(i) for i in range(100) if i % 4 in (1, 2))
    xlist = x.split(',')
    count = 0
    fixtures = []
    for pairings in schedule(list(teams)):
        index1 = int(xlist[count]) % 5 + 1
        index2 = int(xlist[count+1]) % 5 + 1
        dateiter = dateiter + timedelta(days=1)
        datestr = dateiter.strftime("%B %d, %Y")
        fixtures.append({
            'match1' : (Team.objects.get(pk = pairings[1][0]).name,Team.objects.get(pk = pairings[1][1]).name),
            'venue1': Venue.objects.get(id=index1).name,
            'match2' : (Team.objects.get(pk = pairings[3][0]).name,Team.objects.get(pk = pairings[3][1]).name),
            'venue2': Venue.objects.get(id=index2).name,
            'date' : datestr
        })
        count = count + 2
    context = {
        'fixtures': fixtures
    }
    return render(request, 'team/fixtures.html', context)

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
from django.views import View
from iplapp.models import *
from django.db.models import Q
from django.shortcuts import render,redirect

class Teamsview(View):
    def get(self,request,*args,**kwargs):
        teams=Matches.objects.all().values('team1').distinct()
        return render(
            request,
            template_name="teams.html",
            context={
                # 'year': kwargs['year'],

                'teams':teams,

                'request': request,
                'users': Userinfo.objects.filter(username=request.user.username),

                # 'pointstable': emptypointstable,
            }
        )

class Teamhomeview(View):
    def get(self,request,*args,**kwargs):
        teamseasons=Matches.objects.all().filter(Q(team1=kwargs['teamname'])|Q(team2=kwargs['teamname'])).values('season').distinct().order_by('-season')
        for teamseason in teamseasons:
            teamscount = Matches.objects.filter(season=teamseason['season']).values('team1').distinct().count()
            if teamseason['season'] == 2011:
                maxmatchid = Matches.objects.filter(season=teamseason['season'])[68].match_id
            else:
                maxmatchid = Matches.objects.filter(season=teamseason['season'])[teamscount * (teamscount - 1) - 1].match_id
            playoffs = Matches.objects.filter(match_id__gt=maxmatchid, season=teamseason['season'])
            playoffscount=playoffs.count()

            if playoffs[playoffscount-1].winner==kwargs['teamname']:
                teamseason['status']='Champion'
            elif playoffs[playoffscount-1].team1==kwargs['teamname'] or playoffs[playoffscount-1].team2==kwargs['teamname']:
                teamseason['status'] = 'Runner Up'
            else:
                for match in playoffs[:playoffscount-1]:
                    if match.team1==kwargs['teamname'] or match.team2==kwargs['teamname']:
                        teamseason['status'] = 'Reached The Playoffs'
                        break
                else:
                    teamseason['status'] = 'Lost in leagues'
        return render(
            request,
            template_name="teamhome.html",
            context={
                # 'year': kwargs['year'],

                'teamseasons':teamseasons,
                'teamname':kwargs['teamname'],

                'request': request,
                'users': Userinfo.objects.filter(username=request.user.username),

                # 'pointstable': emptypointstable,
            }
        )

class Teamseasonview(View):
    def get(self, request, *args, **kwargs):
        teamseasonmatches=Matches.objects.all().filter(Q(team1=kwargs['teamname'])|Q(team2=kwargs['teamname']),season=kwargs['year'])
        return render(
            request,
            template_name="teamseason.html",
            context={
                'year': kwargs['year'],
                'teamname': kwargs['teamname'],
                'teamseasonmatches':teamseasonmatches,

                'request': request,
                'users': Userinfo.objects.filter(username=request.user.username),

                # 'pointstable': emptypointstable,
            }
        )
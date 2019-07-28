from django.views import View
from django.urls import resolve
from iplapp.models import Matches,Deliveries,Userinfo
from django.shortcuts import render,redirect
from django.db.models import *
from django.contrib.auth.mixins import LoginRequiredMixin

class Matchview(LoginRequiredMixin,View):
    login_url = '/iplapp/login/'
    def get(self,request,*args,**kwargs):
        # if resolve(request.path_info).url_name == 'matchdetails':
        #     return redirect('matchinningdetails', year=kwargs['year'],matchid=kwargs['matchid'], inningno=1)
        # else:
            match = Matches.objects.get(match_id=kwargs['matchid'])
            delivrs=Deliveries.objects.filter(match_id=match)
            toprunscorers=delivrs.values('batting_team','batsman').annotate(runs=Sum('batsman_runs')).order_by('-runs')[:3]
            topwickettackers = delivrs.exclude(player_dismissed__isnull =True).exclude(player_dismissed__exact='').values('bowling_team', 'bowler').annotate(wickets=Count('player_dismissed')).order_by('-wickets')[:3]
            return render(
                request,
                template_name="match.html",
                context={
                    'match': match,
                    'firstinningdelivrs':delivrs.filter(inning=1),
                    'secondinningdelivrs': delivrs.filter(inning=2),
                    'team1totalruns':delivrs.filter(inning=1).values('batting_team').annotate(totalruns=Sum('total_runs'))[0],
                    'team1totalwickets':delivrs.filter(inning=1).exclude(player_dismissed__isnull =True).exclude(player_dismissed__exact='').values('batting_team').annotate(totalwickets=Count('player_dismissed'))[0],
                    'team1totalextras':delivrs.filter(inning=1).values('batting_team').annotate(totalextras=Sum('extra_runs'))[0],
                    'team2totalruns':delivrs.filter(inning=2).values('batting_team').annotate(totalruns=Sum('total_runs'))[0],
                    'team2totalwickets':delivrs.filter(inning=2).exclude(player_dismissed__isnull =True).exclude(player_dismissed__exact='').values('batting_team').annotate(totalwickets=Count('player_dismissed'))[0],
                    'team2totalextras': delivrs.filter(inning=2).values('batting_team').annotate(totalextras=Sum('extra_runs'))[0],

                    'toprunscorers':toprunscorers,
                    'topwickettackers':topwickettackers,

                    'request': request,
                    'users': Userinfo.objects.filter(username=request.user.username)
                }
            )
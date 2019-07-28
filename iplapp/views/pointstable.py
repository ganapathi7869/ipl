from django.views import View
from django.urls import resolve
from django.shortcuts import render,redirect
from django.db.models import Q
from django.db.models import *

from iplapp.models import *

class Pointstableview(View):
    def get(self,request,*args,**kwargs):
        emptypointstable=Matches.objects.filter(season=kwargs['year']).values('team1').distinct().annotate(plyd=Count('team1'),won=Count('team1'),lost=Count('team1'),noresult=Count('team1'),points=Count('team1'))
        teamscount=emptypointstable.count()

        # maxmatchid=Matches.objects.filter(season=kwargs['year']).all()[teamscount*(teamscount-1)].match_id + teamscount * (teamscount - 1) - 1
        if kwargs['year']==2011:
            maxmatchid = Matches.objects.filter(season=kwargs['year'])[68].match_id
            print(maxmatchid)
        else:
            maxmatchid=Matches.objects.filter(season=kwargs['year'])[teamscount*(teamscount-1)-1].match_id
        leaguematches = Matches.objects.filter(match_id__lte=maxmatchid,season=kwargs['year'])
        # print(leaguematches.count())
        actualpointstable=leaguematches.values('winner').annotate(won=Count('winner'))
        # print(actualpointstable)
        for row in emptypointstable:
            if kwargs['year'] == 2011:
                row['plyd'] = 14
            else:
                row['plyd']=(teamscount-1)*2
            row['noresult']=Matches.objects.filter(Q(team1=row['team1'])|Q(team2=row['team1']),season=kwargs['year'],result='no result').count()
            # row['noresult'] = Matches.objects.filter(team1=row['team1'],result='no result')
            # row['won']=actualpointstable.get(winner=row['team1'])['won']
            try:
                row['won']=list((inst['won'] for inst in actualpointstable if inst['winner']==row['team1']))[0]
            except IndexError:
                row['won']=0
            row['lost']=row['plyd']-row['noresult']-row['won']
            row['points']=row['won']*2+row['noresult']
        # print(actualpointstable)
        emptypointstable=list(emptypointstable)
        emptypointstable.sort(key=lambda dic:-dic['points'])
        # print(emptypointstable)
        return render(
            request,
            template_name="pointstable.html",
            context={
                'year': kwargs['year'],

                'request': request,
                'users': Userinfo.objects.filter(username=request.user.username),

                'pointstable':emptypointstable,
            }
        )
from django.views import View
from django.urls import resolve
from iplapp.models import Matches,Deliveries
from django.shortcuts import render

class Matchview(View):
    def get(self,request,*args,**kwargs):
        # if resolve(request.path_info).url_name == 'season2019':
        match = Matches.objects.get(match_id=kwargs['matchid'])
        delivrs=Deliveries.objects.filter(match_id=match)
        return render(
            request,
            template_name="match.html",
            context={
                'match': match,
                'delivrs':delivrs,
            }
        )
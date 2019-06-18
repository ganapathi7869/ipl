from django.views import View
from django.urls import resolve
from iplapp.models import Matches
from django.shortcuts import render,redirect
from django.core.paginator import Paginator

class Seasonsview(View):
    def get(self,request,*args,**kwargs):
        if resolve(request.path_info).url_name == 'season2019':
            return redirect('seasonyearpage',year=2019,pageno=1)
        elif resolve(request.path_info).url_name == 'seasonyear':
            return redirect('seasonyearpage', year=kwargs['year'], pageno=1)
        else:
            # matches=Matches.objects.filter(season=kwargs['year'])
            # return render(
            #     request,
            #     template_name="seasons.html",
            #     context={
            #         'matches': matches,
            #         'year':kwargs['year'],
            #     }
            # )
            matches = Matches.objects.filter(season=kwargs['year'])
            p = Paginator(matches, 8)
            page=p.page(kwargs['pageno'])
            prevpageno=kwargs['pageno']-1
            nextpageno=kwargs['pageno']+1
            if prevpageno < 1:
                prevpageno=1
            if nextpageno > p.num_pages:
                nextpageno=p.num_pages
            return render(
                request,
                template_name="seasons.html",
                context={
                    'page': page,
                    'curpageno':kwargs['pageno'],
                    'prevpageno':prevpageno,
                    'nextpageno':nextpageno,
                    'year':kwargs['year'],

                    'p':p,
                }
            )
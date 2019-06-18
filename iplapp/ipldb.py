# from openpyxl import load_workbook
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ipl.settings')

import django
django.setup()

from iplapp.models import *
import csv
# def dumpmatches():
#     with open('iplapp/matches.csv') as fptr:
#         fptr.readline()
#         for line in fptr:
#             list=line.split(',')
#             Matches()

def formatdate(d):
    if '-' in d:
        return d
    else:
        l=d.split('/')
        mon=l[1]
        day=l[0]
        year=l[2]
        if len(year)==4:
            return year + '-' + mon + '-' + day
        else:
            return '20' + year + '-' + mon + '-' + day


def dumpmatches():
    with open('./matches.csv') as fptr:
        sheet=csv.DictReader(fptr)
        for row in sheet:
            if row == []:
                continue
            inst=Matches(match_id=row['id'],season=row['season'],city=row['city'],date=formatdate(row['date']),team1=row['team1'],
                         team2=row['team2'],toss_winner=row['toss_winner'],toss_decision=row['toss_decision'],result=row['result'],
                         dl_applied=row['dl_applied'],winner=row['winner'],win_by_runs=row['win_by_runs'],win_by_wickets=row['win_by_wickets'],
                         player_of_match=row['player_of_match'],venue=row['venue'],umpire1=row['umpire1'],umpire2=row['umpire2'],
                         umpire3=row['umpire3'])
            inst.save()


def dumpdeliveries():
    with open('./deliveries.csv') as fptr:
        sheet=csv.DictReader(fptr)
        i=0
        for row in sheet:
            if row == []:
                continue
            inst=Deliveries(match_id=Matches.objects.get(match_id=row['match_id']),inning=row['inning'],batting_team=row['batting_team'],
                            bowling_team=row['bowling_team'],over=row['over'],ball=row['ball'],batsman=row['batsman'],
                            non_striker=row['non_striker'],bowler=row['bowler'],is_super_over=row['is_super_over'],
                            wide_runs=row['wide_runs'],bye_runs=row['bye_runs'],legbye_runs=row['legbye_runs'],
                            noball_runs=row['noball_runs'],penalty_runs=row['penalty_runs'],batsman_runs=row['batsman_runs'],
                            extra_runs=row['extra_runs'],total_runs=row['total_runs'],player_dismissed=row['player_dismissed'],
                            dismissal_kind=row['dismissal_kind'],fielder=row['fielder'])
            inst.save()
            i += 1
            if (i % 1000 == 0):
                print(i)

# dumpmatches()

# dumpdeliveries()
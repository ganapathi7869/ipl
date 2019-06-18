from django.db import models


# Create your models here.

class Matches(models.Model):
    match_id=models.IntegerField()
    season=models.IntegerField()
    city=models.CharField(max_length=20)
    date=models.DateField()
    team1=models.CharField(max_length=30)
    team2=models.CharField(max_length=30)
    toss_winner=models.CharField(max_length=30,null=True)
    toss_decision=models.CharField(max_length=10,null=True)
    result=models.CharField(max_length=10)
    dl_applied=models.IntegerField()
    winner=models.CharField(max_length=30,null=True)
    win_by_runs=models.IntegerField(null=True)
    win_by_wickets=models.IntegerField(null=True)
    player_of_match=models.CharField(max_length=30,null=True)
    venue=models.CharField(max_length=100)
    umpire1=models.CharField(max_length=30)
    umpire2=models.CharField(max_length=30)
    umpire3=models.CharField(max_length=30,null=True)

    def __str__(self):
        return 'season '+str(self.season)+' : '+str(self.team1)+' vs '+str(self.team2)

class Deliveries(models.Model):
    match_id = models.ForeignKey(Matches, on_delete=models.CASCADE)
    inning=models.IntegerField()
    batting_team=models.CharField(max_length=30)
    bowling_team=models.CharField(max_length=30)
    over=models.IntegerField()
    ball=models.IntegerField()
    batsman=models.CharField(max_length=30)
    non_striker=models.CharField(max_length=30)
    bowler=models.CharField(max_length=30)
    is_super_over=models.IntegerField()
    wide_runs=models.IntegerField()
    bye_runs=models.IntegerField()
    legbye_runs=models.IntegerField()
    noball_runs=models.IntegerField()
    penalty_runs=models.IntegerField()
    batsman_runs=models.IntegerField()
    extra_runs=models.IntegerField()
    total_runs=models.IntegerField()
    player_dismissed=models.CharField(max_length=30,null=True)
    dismissal_kind=models.CharField(max_length=30,null=True)
    fielder=models.CharField(max_length=30,null=True)


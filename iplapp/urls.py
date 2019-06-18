from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls import include, url  # For django versions before 2.0
from django.urls import include, path  # For django versions from 2.0 and up
from iplapp.views.seasons import *
from iplapp.views.match import *

urlpatterns = [

    path('seasons/',Seasonsview.as_view(),name='season2019'),
    path('seasons/<int:year>/',Seasonsview.as_view(),name='seasonyear'),
    path('seasons/<int:year>/page/<int:pageno>',Seasonsview.as_view(),name='seasonyearpage'),

    path('seasons/<int:year>/match/<int:matchid>',Matchview.as_view(),name='matchdetails'),

    # path('test_view/',myfirstview,name='myfirstview'),
    #
    # path('api/v1/token/',generateToken.as_view(),name='token_obtain_pair'),
    #
    # path('api/v1/colleges/',CollegeListView.as_view(),name="CollegeAPI"),
    # path('api/v1/colleges/<int:id>/',college_details_idView.as_view(),name="CollegeDetailsAPI"),
    # path('api/v1/colleges/<int:cpk>/students/',StudentAPIView.as_view(),name="ClgStudentsDetailsAPI"),
    # path('api/v1/colleges/<int:cpk>/students/<int:spk>/',StudentAPIView.as_view(),name="ClgStudentDetailsAPI"),
    # path('api/v1/students/<int:spk>/',StudentAPIView.as_view(),name="StuDetails"),
    # path('api/v1/students/',StudentAPIView.as_view(),name="AllStudentsDetailsAPI"),
    #
    # path('colleges/',CollegeView.as_view(),name="colleges.html"),
    # #path('students/<int:pk>/',StudentView.as_view(),name="students.html"),
    # path('colleges/<int:pk>/',CollegeView.as_view(),name="college_details"),
    # path('colleges/<str:acronym>/',CollegeView.as_view(),name="college_details"),
    # path('addcollege/',AddCollegeView.as_view(),name = "addCollege"),
    # path('colleges/<int:pk>/edit',AddCollegeView.as_view(),name = "editCollege"),
    # path('colleges/<int:pk>/delete',AddCollegeView.as_view(),name = "deleteCollege"),
    #
    # path('colleges/<int:college_id>/addstudent/',AddStudentView.as_view(),name='addstudent'),
    # path('colleges/<int:college_id>/edit/<int:student_id>/',AddStudentView.as_view(),name='editstudent'),
    # path('colleges/<int:college_id>/delete/<int:student_id>/',AddStudentView.as_view(),name='deletestudent'),
    #
    # path('login/', LoginView.as_view(), name='login'),
    # path('signup/', SignupView.as_view(), name='signup'),
    # path('logout/', logout_user, name='logout'),

]
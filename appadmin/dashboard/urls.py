from django.conf.urls import url
from .view import auth
from django.urls import path

urlpatterns = [
    url(r'^login/', auth.adminLogin, name="adminlogin"),
    url(r'^dashboard/', auth.adminDashboard, name="admindashboard"),
    path('admin/showteam/<int:id>', auth.showTeam, name="showteam"),
    url(r'^logout/', auth.adminLogout, name ="adminlogout")
]


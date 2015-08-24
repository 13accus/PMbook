from django.conf.urls import url
from . import views

urlpatterns = [
    
    #Access profile.html by project id (ex. localhost:8080/project/1000)
    url(r'^(?P<project>[0-9]{4})/$', views.projects, name='project'), 
    #Access index.html (ex. localhost:8080)
    url(r'^$', views.index, name= 'index'),
    #Access ritable.html by project id (ex. localhost:8080/project/1000/ri)
    url(r'^(?P<project>[0-9]{4})/ri', views.ri, name= 'ri'),
 	#Access miletable.html by project id (ex. localhost:8080/project/1000/milestone)
    url(r'^(?P<project>[0-9]{4})/milestone', views.milestone, name= 'milestone'),
    #Access notetable.html by project id (ex. localhost:8080/project/1000/note)
    url(r'^(?P<project>[0-9]{4})/note', views.note, name= 'note'),
    #THIS PAGE DOES NOT EXIST IN CURRENT VERSION
    url(r'^(?P<project>[0-9]{4})/gatedoc', views.gatedoc, name= 'gatedoc'),
    #Allows for search function
    url(r'^search/', views.search, name= 'search'),
  
]
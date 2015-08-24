from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'PMBook.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    #Access admin features
    url(r'^admin/', include(admin.site.urls)),
    #Access projects (project id follows)
    url(r'^project/', include('Models.urls')),
    #Access index/homepage
    url(r'^$', include('Models.urls')),
    #Access intake form
    url(r'^intake/', 'Models.views.intakeOne', name='intake'),
    #Access the pending project page
    url(r'^pending/', 'Models.views.pending', name= 'pending'),
    #Access the MPL
    url(r'^mpl/', 'Models.views.mpl', name= 'MPL'),
    #Acess Reporting
    url(r'^reports/', 'Models.views.report', name='reports'),
    #Access the Risk and Issues Deck
    url(r'^deck/', 'Models.views.deck', name='deck'),
]

from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.login, name='login'),
    url(r'^new/$',views.new,name='new'),
    url(r'^new/(?P<od>[0-9]+)/(?P<do>[0-9]+)$',views.rooms,name='rooms'),
    url(r'^see/$',views.see,name='see'),
    url(r'^logout/$',views.logoutview,name='logout'),
    url(r'^set/$',views.setings,name='set'),
    url(r'^menu/$',views.menu,name='menu'),
    url(r'^set/changepass/$',views.changepass,name='changepass'),
    url(r'^set/errors/$',views.adderror,name='error'),

    ]

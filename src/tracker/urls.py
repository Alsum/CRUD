from django.conf.urls import include, url
import views

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^(?P<profile_id>\d+)/edit/$', views.edit, name="edit_user"),
    url(r'^(?P<user_id>\d+)/edit/editcore/$', views.edit_core, name="edit_core"),
    url(r'^(?P<profile_id>\d+)/del/$', views.del_user, name="del_user"),
]

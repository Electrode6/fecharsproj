from django.conf.urls import url

from pyfeck.views import IndexView,CharacterView,ClassView,WeaponView

app_name = "pyfeck"

urlpatterns = [
    url(r'^$', IndexView.as_view(), name = "index"),
    url(r'^character/(?P<pk>[0-9]+)/$', CharacterView.as_view(), name='character'),
    url(r'^weapon/(?P<pk>[0-9]+)/$', WeaponView.as_view(), name='weapon'),
    url(r'^class/(?P<pk>[0-9]+)/$', ClassView, name='class'),

]
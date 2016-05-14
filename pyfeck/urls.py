from django.conf.urls import url

from pyfeck.views import IndexView, CharacterView

app_name = "pyfeck"

urlpatterns = [
    url(r'^$', IndexView.as_view(), name = "index"),
    url(r'^character/(?P<pk>[0-9]+)/$', CharacterView.as_view(), name = "character")
]
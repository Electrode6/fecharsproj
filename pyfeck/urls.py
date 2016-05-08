from django.conf.urls import url

from pyfeck.views import IndexView

app_name = "Pyfeck"

urlpatterns = [
    url(r'^$', IndexView, name = "index")
]
from django.urls import path

from webapp.views.records_view import records_view


urlpatterns = [
    path("", records_view, name='index'),
    path("guestbook/", records_view)

]
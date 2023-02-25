from django.urls import path

from webapp.views.records_view import records_view, record_add, record_edit


urlpatterns = [
    path("", records_view, name='index'),
    path("guestbook/", records_view),
    path('guestbook/add', record_add, name='record_add'),
    path('guestbook/<int:pk>/edit', record_edit, name='record_edit')
]


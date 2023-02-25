from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render
from webapp.models import Guestbook


def records_view(request: WSGIRequest):
    records = Guestbook.objects.filter(status='active').order_by('-created_at')
    context = {
        'records': records
    }
    return render(request, 'records.html', context=context)

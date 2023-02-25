from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect, get_object_or_404

from webapp.forms import GuestbookForm
from webapp.models import Guestbook


def records_view(request: WSGIRequest):
    records = Guestbook.objects.filter(status="active").order_by("-created_at")
    context = {"records": records}
    return render(request, "records.html", context=context)


def record_add(request: WSGIRequest):
    if request.method == "GET":
        form = GuestbookForm()
        return render(request, "record_add.html", context={"form": form})

    form = GuestbookForm(data=request.POST)
    if not form.is_valid():
        return render(request, "record_add.html", context={"form": form})
    else:
        Guestbook.objects.create(**form.cleaned_data)
        return redirect("index")


def record_edit(request, pk):
    record = get_object_or_404(Guestbook, pk=pk)

    if request.method == "POST":
        form = GuestbookForm(request.POST, instance=record)
        if form.is_valid():
            record.save()
            return redirect("index")

    form = GuestbookForm(instance=record)
    return render(
        request,
        "record_edit_view.html",
        context={"form": form, "record": record},
    )


def delete_record(request, pk):
    record = get_object_or_404(Guestbook, pk=pk)
    return render(
        request, "record_confirm_delete.html", context={"record": record}
    )


def confirm_delete(request, pk):
    record = get_object_or_404(Guestbook, pk=pk)
    record.delete()
    return redirect("index")

from django import forms
from django.core.exceptions import ValidationError

from webapp.models import Guestbook


class GuestbookForm(forms.ModelForm):
    class Meta:
        model = Guestbook
        fields = ("author_name", "mail", "text")

        labels = {
            "author_name": "Имя автора записи",
            "mail": "E-mail",
            "text": "Текст записи",
        }

    def clean_author_name(self):
        author_name = self.cleaned_data.get("author_name")
        if len(author_name) < 2:
            raise ValidationError(
                "Author name must be longer than 1 character"
            )
        return author_name

    def clean_mail(self):
        mail = self.cleaned_data.get("mail")
        if "@" not in mail:
            raise ValidationError(
                "Please enter your email address correctly (for example: johnsmith@ups.com.)"
            )
        return mail

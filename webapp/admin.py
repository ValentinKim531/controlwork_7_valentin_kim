from django.contrib import admin

from webapp.models import Guestbook


# Register your models here.
class GuestbookAdmin(admin.ModelAdmin):
    list_display = ('id', 'author_name', 'mail', 'text', 'created_at', 'status')
    list_filter = ('id', 'author_name', 'mail', 'created_at', 'status')
    search_fields = ('author_name', 'mail')
    fields = ('author_name', 'mail', 'text', 'created_at', 'status')
    readonly_fields = ('id', 'created_at', 'updated_at')


admin.site.register(Guestbook, GuestbookAdmin)
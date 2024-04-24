from django.contrib import admin

from .models import Header, Title, Stanza


class StanzaInLine(admin.TabularInline):
    model = Stanza
    extra = 0


class TitleInLine(admin.TabularInline):
    model = Title
    extra = 0


class TitleAdmin(admin.ModelAdmin):
    list_display = ('hymn_title', 'hymn_number')
    fieldsets = [('Hymn Header Text', {'fields': ['header_id']}), ('Hymn Title', {'fields': ['hymn_number', 'hymn_title', 'author']}), ]
    inlines = [StanzaInLine]


class HeaderAdmin(admin.ModelAdmin):
    fieldsets = [('Hymns Header', {'fields': ['header_text']}), ]
    # inlines = [TitleInLine, StanzaInLine]


admin.site.register(Header, HeaderAdmin)
admin.site.register(Title, TitleAdmin)

from django.contrib import admin

from .models import MutuSumu, Zina, Mizere


class MizereInLine(admin.TabularInline):
    model = Mizere
    extra = 0


class ZinaInLine(admin.StackedInline):
    model = Zina
    extra = 0


class ZinaAdmin(admin.ModelAdmin):
    list_display = ('zina_la_sumu', 'nambala_ya_sumu')
    fieldsets = [('Mutu Wa Sumu', {'fields': ['mutu_sumu_id']}), ('Zina Information', {'fields': ['nambala_ya_sumu', 'zina_la_sumu', 'mlembi']})]
    inlines = [MizereInLine]


class MutuSumuAdmin(admin.ModelAdmin):
    fieldsets = [('Mutu Wa Sumu', {'fields': ['mutu_wa_sumu']}), ]
    # inlines = [ZinaInLine, MizereInLine]


admin.site.register(MutuSumu, MutuSumuAdmin)
admin.site.register(Zina, ZinaAdmin)

from django.contrib import admin

from .models import MutuNyimbo, Dzina, Ndime


# This one did not correctly it has a few bottle necks
class NdimeAdmin(admin.ModelAdmin):
    fieldsets = [('Mutu', {'fields': ['mutu_nyimbo_id']}), ('Dzina La Nyimbo', {'fields': ['dzina_id']}), ('Ndime za Nyimbo', {'fields': ['nambara', 'ndime'], 'fields': ['nambara', 'ndime'], 'fields': ['nambara', 'ndime']}), ]


class NdimeInLine(admin.TabularInline):
    model = Ndime
    extra = 0


class DzinaInLine(admin.TabularInline):
    model = Dzina
    extra = 0


class DzinaAdmin(admin.ModelAdmin):
    list_display = ('dzina_la_nyimbo', 'nambara_ya_nyimbo')
    fieldsets = [('Mutu', {'fields': ['mutu_nyimbo_id']}), ('Dzina La Nyimbo', {'fields': ['nambara_ya_nyimbo', 'dzina_la_nyimbo', 'olemba']}), ]
    inlines = [NdimeInLine]


class MutuNyimboAdmin(admin.ModelAdmin):
    fieldsets = [('Mutu Wa Nyimbo', {'fields': ['mutu_wa_nyimbo']}), ]
    # inlines = [DzinaInLine, NdimeInLine]


admin.site.register(MutuNyimbo, MutuNyimboAdmin)
admin.site.register(Dzina, DzinaAdmin)
# admin.site.register(Ndime, NdimeAdmin)

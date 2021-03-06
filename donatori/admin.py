from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.html import format_html

from .models import (
    Donatore,
    Donazione,
    ProfiloUtente,
    Sesso,
    Sezione,
    StatoDonatore,
)


class ProfiloUtenteAdmin(admin.ModelAdmin):
    model = ProfiloUtente
    readonly_fields = ('utente',)
    list_display = ('utente', 'is_sezione', 'is_centro_di_raccolta',
                    'is_donatore', 'user_link')

    def user_link(self, obj):
        return format_html(
            '<a href="{}">{}</a>',
            reverse('admin:auth_user_change', args=(obj.utente.pk,)),
            'Modifica user',
        )
    user_link.short_description = 'Modifica Utente'


class ProfiloUtenteInline(admin.StackedInline):
    model = ProfiloUtente
    can_delete = False


class SezioneInline(admin.StackedInline):
    model = Sezione
    can_delete = False
    fields = ('descrizione',)
    show_change_link = True


class CustomUserAdmin(UserAdmin):
    inlines = (SezioneInline,)
    list_display = ('username', 'email', 'is_superuser', 'is_staff', 'is_active',
                    'sezione',)


class DonazioneInline(admin.TabularInline):
    model = Donazione
    extra = 0


class DonatoreAdmin(admin.ModelAdmin):
    model = Donatore
    inlines = (DonazioneInline,)
    list_select_related = ('sesso', 'stato_donatore')
    list_display = ('num_tessera', 'cognome', 'nome',
                    'citta', 'sesso', 'stato_donatore')
    ordering = ('cognome', 'nome', 'num_tessera')
    search_fields = ('cognome', 'nome', 'citta', 'num_tessera')


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Sezione)
admin.site.register(Sesso)
admin.site.register(StatoDonatore)
admin.site.register(Donatore, DonatoreAdmin)

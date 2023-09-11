from django.contrib import admin
from core.models import Animal, Cliente, Especie


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ativo',)


@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ('nome', 'idade', 'ativo', 'criado',)
    list_editable = ('ativo',)

@admin.register(Especie)
class EspecieAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'ativo', 'criado',)


from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Person, Documento, Venda, Produto

class PersonAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Dados Pessoais', {
        'classes': ('collapse',),
        'fields': ('first_name','last_name','doc')}),

        ('Dados complementares', {
        'classes': ('collapse',),
        'fields': ('age','salary','photo')}))

    #fields = (('first_name', 'last_name', 'age'), 'salary', ('photo', 'bio'))
    #exclude = ('bio',)
    list_display = ('first_name', 'doc', 'last_name', 'age', 'salary', 'bio', 'photo')


admin.site.register(Person, PersonAdmin)
admin.site.register(Documento)
admin.site.register(Venda)
admin.site.register(Produto)

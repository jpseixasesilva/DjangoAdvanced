from django.contrib import admin

from .models import Person, Documento


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
    list_filter = ('age', 'salary',)

    def tem_foto(self, obj):
        if obj.photo:
            return True
        else:
            return False
    tem_foto.short_description = 'Possui foto'




#class ProdutoAdmin(admin.ModelAdmin):
#    list_filter = ('id','descricao','preco')


admin.site.register(Person, PersonAdmin)
admin.site.register(Documento)
#admin.site.register(Produto, ProdutoAdmin)

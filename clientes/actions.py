def nfe_emitida(modeladmin, request, queryset):
    queryset.update(nfe_emitida=True)

nfe_emitida.short_description = 'NFE Emitida'


def nfe_nao_emitida(modeladmin, request, queryset):
    queryset.update(nfe_emitida=False)

nfe_nao_emitida.short_description = 'NFE Não Emitida'
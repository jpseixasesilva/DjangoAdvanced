from django.db import models
from django.db.models import F, Sum, FloatField, Max
from django.dispatch import receiver
from django.db.models.signals import m2m_changed, post_save
from clientes.models import Person
from produtos.models import Produto
from .managers import VendaManager


class Venda(models.Model):
    numero = models.CharField(max_length=7)
    valor = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    desconto = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    impostos = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    pessoa = models.ForeignKey(Person, null=True, blank=True, on_delete=models.PROTECT)
    # produtos = models.ManyToManyField(Produto, blank=True)
    nfe_emitida = models.BooleanField(default=False)

    objects = VendaManager()

    def calcular_total(self):
        tot = self.itemdopedido_set.all().aggregate(
            tot_ped=Sum((F('quantidade')*F('produto__preco')) - F('desconto'), output_field=FloatField())
        )['tot_ped'] or 0
        tot = tot - float(self.impostos) - float(self.desconto)
        self.valor = tot
        Venda.objects.filter(id=self.id).update(valor=tot)

    def __str__(self):
        return self.numero


#    def get_total(self):
#        tot = 0
#        for produto in self.produtos.all():
#            tot += produto.preco
#        return (tot - self.desconto) - self.desconto

class ItemDoPedido(models.Model):
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.FloatField()
    desconto = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.venda.numero + ' - ' + self.produto.descricao


@receiver(post_save, sender=ItemDoPedido)
def update_vendas_total(sender, instance, **kwargs):
    instance.venda.calcular_total()


@receiver(post_save, sender=Venda)
def update_vendas_total2(sender, instance, **kwargs):
    instance.calcular_total()


#@receiver(m2m_changed, sender=Venda.produtos.through)
#def update_vendas_total(sender, instance, **kwargs):
#    total = instance.get_total()
#    instance.save()
#    Venda.objects.filter(id=instance.id).update(total=total)


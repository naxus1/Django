from django.db import models

# Create your models here.
class InfoCompany(models.Model):
    creado = models.DateTimeField(auto_now_add=True)
    nombre = models.CharField(max_length=150, default = '')
    # Ingresos del negocio
    ingresos_totales = models.IntegerField()
    devoluciones = models.IntegerField()
    ingresos_netos = models.IntegerField()
    rete_fuente = models.IntegerField()
    # Costos del negocio
    valor_inven_311217 = models.IntegerField()
    valor_inven_311216 = models.IntegerField()
    valor_compras_inven_2017 = models.IntegerField()
    costo_mercancia_vendida = models.IntegerField() #
     # Gastos del negocio
    honorarios = models.IntegerField()
    impuestos = models.IntegerField()
    arrendamientos = models.IntegerField()
    seguros = models.IntegerField()
    servicios = models.IntegerField()
    gastos_legales = models.IntegerField()
    papeleria_copias = models.IntegerField()
    comisiones = models.IntegerField()
    publicidad = models.IntegerField()
    gastos_nomina = models.IntegerField()
    total_gastos = models.IntegerField() #
    realizo_aporte_SS = models.BooleanField(default = False)
    class Meta:
        ordering = ('creado',)
        verbose_name = ("Empresa")
        verbose_name_plural = ("Empresas")

    def __str__(self):
        return self.nombre


class SeguridadSocial(models.Model):
    id_company = models.ForeignKey("InfoCompany", related_name='seguridad_social',
                                    verbose_name=("id_company"), on_delete=models.CASCADE)
    salud = models.IntegerField()
    pension = models.IntegerField()
    fondo_solidaridad_pensional = models.IntegerField()
    cesantias = models.IntegerField()
    arl = models.IntegerField()
    pension_voluntaria = models.IntegerField()
    afc = models.IntegerField()
    total_aporte = models.IntegerField() #
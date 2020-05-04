from rest_framework import serializers
from Spec.models import InfoCompany, SeguridadSocial


class InfoCompanySerializer(serializers.ModelSerializer):
   class Meta:
        model = InfoCompany
        fields = ('id',
                'nombre',
                'ingresos_totales',
                'devoluciones',
                'ingresos_netos',
                'rete_fuente',
                'valor_inven_311217',
                'valor_inven_311216',
                'valor_compras_inven_2017',
                'costo_mercancia_vendida',
                'honorarios',
                'impuestos',
                'arrendamientos',
                'seguros',
                'servicios',
                'gastos_legales',
                'papeleria_copias',
                'comisiones',
                'publicidad',
                'gastos_nomina',
                'total_gastos',
                'realizo_aporte_SS')
    

class SeguridadSocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = SeguridadSocial
        fields = (
            'id_company',
            'salud',
            'pension', 
            'fondo_solidaridad_pensional',
            'cesantias',
            'arl',
            'pension_voluntaria',
            'afc',
            'total_aporte')
    



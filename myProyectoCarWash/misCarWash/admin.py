from django.contrib import admin
from .models import Slider,Galeria,Insumo,MisionyVision
# Register your models here.

class SliderAdmin(admin.ModelAdmin):
    list_display=['ident','imagen']
    search_fields=['ident','imagen']
    list_per_page=10 
    list_filter=['ident']


class GaleriaAdmin(admin.ModelAdmin):
    list_display=['ident','descripcion','imagen']
    search_fields=['ident','descripcion','imagen']
    list_per_page=10
    list_filter=['ident']

class InsumoAdmin(admin.ModelAdmin):
    list_display=['nombre','precio','descripcion','stock']
    search_fields=['nombre','precio','descripcion','stock']
    list_per_page=10
    list_filter=['nombre']

class MisionyVisionAdmin(admin.ModelAdmin):
    list_display=['ident','mision','vision']
    search_fields=['ident','mision','vision']
    list_per_page=10
    list_filter=['ident']



admin.site.register(Slider,SliderAdmin)
admin.site.register(Galeria,GaleriaAdmin)
admin.site.register(Insumo)
admin.site.register(MisionyVision)

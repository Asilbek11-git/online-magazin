from django.contrib import admin
from .models import Mahsulot

@admin.register(Mahsulot)
class MahsulotAdmin(admin.ModelAdmin):

    list_display = ('id', 'nom', 'narx', 'kategoriya')

    search_fields = ('nom', 'tavsif')
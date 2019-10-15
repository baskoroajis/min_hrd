from django.contrib import admin
from kehadiran.models import Kehadiran


class KehadiranAdmin(admin.ModelAdmin):
    list_display = ['karyawan', 'jenis_kehadiran', 'waktu']
    list_filter = ('jenis_kehadiran')
    list_per_page = 25
    search_fields = []

admin.site.register(Kehadiran,KehadiranAdmin)
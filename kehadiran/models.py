from django.db import models
from karyawan.models import Karyawan

class Kehadiran(models.Model):
    JENIS_KEHADIRAN_CHOICE = (
        ('izin', 'Izin'),
        ('cuti', 'Cuti'),
        ('alpa', 'Tanpa Alasan'),
        ('hadir', 'Hadir'),
    )

    karyawan = models.ForeignKey(Karyawan)
    jenis_kehadiran = models.CharField(max_length=20, choices=JENIS_KEHADIRAN_CHOICE)
    waktu = models.DateField()

    def __unicode__(self):
        return self.karyawan.nama


from django.contrib import admin
from.models import Mahasiswa
from.models import Mata_kuliah

class MahasiswaAdmin(admin.ModelAdmin):
    list_display = ("nama", "NPM", "Prodi",)

admin.site.register(Mahasiswa, MahasiswaAdmin)
admin.site.register(Mata_kuliah)

# Register your models here.

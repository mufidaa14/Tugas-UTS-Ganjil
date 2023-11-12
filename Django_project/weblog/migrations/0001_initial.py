# Generated by Django 4.2.6 on 2023-11-10 05:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mata_kuliah',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hari', models.CharField(max_length=255)),
                ('makul', models.CharField(max_length=255)),
                ('jumlah_sks', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Mahasiswa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=255)),
                ('NPM', models.CharField(max_length=255)),
                ('Prodi', models.CharField(max_length=255)),
                ('Mata_kuliah', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weblog.mata_kuliah')),
            ],
        ),
    ]
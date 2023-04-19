# Generated by Django 4.1.3 on 2023-04-13 17:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdultCamp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Įveskite vaikų stovyklos pavadinimą', max_length=200, verbose_name='Pavadinimas')),
                ('summary', models.TextField(help_text='Trumpas stovyklos aprašymas', max_length=1000, null=True, verbose_name='Aprašymas')),
                ('dateFrom', models.DateField(null=True, verbose_name='Nuo')),
                ('dateTo', models.DateField(null=True, verbose_name='Iki')),
                ('capacity', models.IntegerField(help_text='Pasirinkite grupės dydį', null=True, verbose_name='Grupės dydis')),
            ],
            options={
                'verbose_name': 'Suaugusiųjų stovykla',
                'verbose_name_plural': 'Suaugusiųjų stovyklos',
            },
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

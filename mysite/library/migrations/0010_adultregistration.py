# Generated by Django 4.1.3 on 2023-04-26 15:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0009_alter_childrenregistration_children_camp'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdultRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('info', models.TextField(max_length=300)),
                ('adult_camp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='registration1', to='library.adultcamp')),
            ],
            options={
                'verbose_name': 'Registracija',
                'verbose_name_plural': 'Registracijos',
            },
        ),
    ]

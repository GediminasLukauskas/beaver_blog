# Generated by Django 4.1.3 on 2023-04-25 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_contactus_delete_mymodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='camp',
            name='cover',
            field=models.ImageField(null=True, upload_to='covers', verbose_name='Viršelis'),
        ),
    ]
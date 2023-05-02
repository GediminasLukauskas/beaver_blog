# Generated by Django 4.1.3 on 2023-05-02 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0010_adultregistration'),
    ]

    operations = [
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField()),
            ],
        ),
    ]

# Generated by Django 4.1.3 on 2023-04-24 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_mymodel_reservation_camp_instance_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=100)),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='MyModel',
        ),
    ]
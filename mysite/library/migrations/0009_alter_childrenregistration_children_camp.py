# Generated by Django 4.1.3 on 2023-04-25 18:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0008_alter_childrenregistration_children_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='childrenregistration',
            name='children_camp',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='registration', to='library.childrencamp'),
        ),
    ]
# Generated by Django 4.1.4 on 2022-12-29 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crops_rate', '0003_alter_onionrate_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='onionrate',
            name='date',
            field=models.DateField(unique=True),
        ),
    ]
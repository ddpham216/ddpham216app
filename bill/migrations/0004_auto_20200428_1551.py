# Generated by Django 2.2.4 on 2020-04-28 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bill', '0003_auto_20200420_1019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='total',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=11, null=True),
        ),
    ]

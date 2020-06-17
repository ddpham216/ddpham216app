# Generated by Django 3.0.6 on 2020-05-20 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_orderproduct_total_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderproduct',
            name='status',
            field=models.CharField(choices=[('C', 'Complete'), ('W', 'Waiting'), ('R', 'Return')], default='W', max_length=1),
        ),
    ]

# Generated by Django 3.2.9 on 2021-11-21 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='dust_type',
            field=models.CharField(blank=True, choices=[('AD', '야망있는 먼지'), ('PD', '통통튀는 먼지'), ('TD', '조구만 먼지'), ('ED', '신나는 먼지')], max_length=10, null=True),
        ),
    ]

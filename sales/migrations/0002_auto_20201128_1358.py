# Generated by Django 3.1.3 on 2020-11-28 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salesdetails',
            name='sale_date',
            field=models.DateField(),
        ),
    ]

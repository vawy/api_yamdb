# Generated by Django 2.2.16 on 2022-07-30 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0005_auto_20220730_2322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='title',
            name='rating',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]

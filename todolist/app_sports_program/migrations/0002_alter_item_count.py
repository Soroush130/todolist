# Generated by Django 4.0.5 on 2022-07-12 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_sports_program', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='count',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
    ]

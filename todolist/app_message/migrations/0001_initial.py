# Generated by Django 4.0.5 on 2022-07-12 04:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('from_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages_from_user', to=settings.AUTH_USER_MODEL)),
                ('to_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages_to_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

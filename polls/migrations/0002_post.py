# Generated by Django 4.2.4 on 2024-06-06 17:02

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('text', models.TextField()),
                ('category', models.CharField(max_length=50)),
                ('released_date', models.DateField(default=datetime.datetime(2024, 6, 6, 17, 2, 51, 371394))),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.person')),
            ],
        ),
    ]

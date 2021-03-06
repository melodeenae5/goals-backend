# Generated by Django 3.1.4 on 2020-12-14 19:31

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
            name='BigGoal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('description', models.TextField()),
                ('timeframe', models.CharField(max_length=25)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='big_goals', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='days', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('big_goal_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notes', to='goals.biggoal')),
                ('day_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notes', to='goals.day')),
            ],
        ),
        migrations.CreateModel(
            name='ListItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.CharField(max_length=150)),
                ('category', models.CharField(max_length=50)),
                ('big_goal_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='list_items', to='goals.biggoal')),
                ('day_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='list_items', to='goals.day')),
            ],
        ),
    ]

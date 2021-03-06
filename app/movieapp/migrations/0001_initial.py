# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-03 10:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


def forwards_func(apps, schema_editor):
    # We get the model from the versioned app registry;
    # if we directly import it, it'll be the wrong version
    Movie = apps.get_model("movieapp", "Movie")
    Actor = apps.get_model("movieapp", "Actor")
    Cast = apps.get_model("movieapp", "Cast")
    db_alias = schema_editor.connection.alias

    movies = [
        Movie(id=1, title='The Terminator', year='1984'),
        Movie(id=2, title='The Expendables 2', year='2012'),
        Movie(id=3, title='The Expendables 3', year='2014'),
    ]
    Movie.objects.using(db_alias).bulk_create(movies)

    actors = [
        Actor(id=1, name='Arnold Schwarzenegger'),
        Actor(id=2, name='Sly Stalone'),
        Actor(id=3, name='Bruce Willis'),
    ]
    Actor.objects.using(db_alias).bulk_create(actors)

    Cast.objects.using(db_alias).bulk_create([
        Cast(actor=actors[0], movie=movies[0], salary=1000000),
        Cast(actor=actors[0], movie=movies[1], salary=1500000),
        Cast(actor=actors[0], movie=movies[2], salary=2000000),
        Cast(actor=actors[1], movie=movies[1], salary=1000000),
        Cast(actor=actors[1], movie=movies[2], salary=1500000),
        Cast(actor=actors[2], movie=movies[2], salary=500000),
    ])


def reverse_func(apps, schema_editor):
    # forwards_func() creates two Country instances,
    # so reverse_func() should delete them.
    Movie = apps.get_model("movieapp", "Movie")
    Actor = apps.get_model("movieapp", "Actor")
    db_alias = schema_editor.connection.alias
    Movie.objects.using(db_alias).filter(id=1).delete()
    Movie.objects.using(db_alias).filter(id=2).delete()
    Movie.objects.using(db_alias).filter(id=3).delete()
    Actor.objects.using(db_alias).filter(id=1).delete()
    Actor.objects.using(db_alias).filter(id=2).delete()
    Actor.objects.using(db_alias).filter(id=3).delete()


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Cast',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salary', models.IntegerField()),
                ('actor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movieapp.Actor')),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('year', models.IntegerField()),
                ('actors', models.ManyToManyField(through='movieapp.Cast', to='movieapp.Actor')),
            ],
        ),
        migrations.AddField(
            model_name='cast',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movieapp.Movie'),
        ),

        migrations.RunPython(forwards_func, reverse_func),
    ]

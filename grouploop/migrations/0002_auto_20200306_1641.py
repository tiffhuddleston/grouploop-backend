# Generated by Django 3.0.4 on 2020-03-06 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grouploop', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='circle',
            name='member',
        ),
        migrations.AddField(
            model_name='circle',
            name='member',
            field=models.ManyToManyField(to='grouploop.Member'),
        ),
    ]
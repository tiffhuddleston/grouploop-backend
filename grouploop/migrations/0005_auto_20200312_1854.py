# Generated by Django 3.0.4 on 2020-03-12 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grouploop', '0004_auto_20200310_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='circle',
            name='member',
            field=models.ManyToManyField(blank=True, to='grouploop.Member'),
        ),
        migrations.AlterField(
            model_name='member',
            name='facebook',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='github',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='instagram',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='linkedin',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='twitter',
            field=models.TextField(blank=True),
        ),
    ]

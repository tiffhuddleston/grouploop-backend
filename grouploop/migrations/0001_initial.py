# Generated by Django 3.0.4 on 2020-03-06 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Circle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('member', models.TextField()),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('github', models.TextField()),
                ('facebook', models.TextField()),
                ('instagram', models.TextField()),
                ('linkedin', models.TextField()),
                ('twitter', models.TextField()),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]

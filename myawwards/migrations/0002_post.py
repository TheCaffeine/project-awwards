# Generated by Django 2.2.6 on 2019-10-21 09:24

from django.db import migrations, models
import django.db.models.deletion
import pyuploadcare.dj.models


class Migration(migrations.Migration):

    dependencies = [
        ('myawwards', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=155)),
                ('url', models.URLField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('technologies', models.CharField(max_length=200)),
                ('photo', pyuploadcare.dj.models.ImageField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='myawwards.Profile')),
            ],
        ),
    ]

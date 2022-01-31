# Generated by Django 4.0.1 on 2022-01-31 13:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Client', '0010_remove_request_body_remove_request_handled_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='body',
            field=models.CharField(default='{}', max_length=10000),
        ),
        migrations.AddField(
            model_name='request',
            name='header',
            field=models.CharField(default='{}', max_length=10000),
        ),
        migrations.AddField(
            model_name='request',
            name='time',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='request',
            name='method',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='request',
            name='url',
            field=models.CharField(max_length=100),
        ),
    ]

# Generated by Django 4.0.6 on 2022-09-08 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0003_remove_artwork_isbn'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='first_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='artist',
            name='last_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='artwork',
            name='title',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='genre',
            name='name',
            field=models.CharField(help_text='Enter an arts genre (e.g. painting)', max_length=100),
        ),
    ]

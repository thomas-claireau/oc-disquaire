# Generated by Django 3.1.5 on 2021-01-23 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='artists',
            field=models.ManyToManyField(related_name='albums', to='store.Artist'),
        ),
    ]

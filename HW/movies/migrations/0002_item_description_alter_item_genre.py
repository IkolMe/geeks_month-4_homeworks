# Generated by Django 5.0 on 2023-12-24 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='genre',
            field=models.CharField(max_length=54),
        ),
    ]

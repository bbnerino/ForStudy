# Generated by Django 3.2.7 on 2021-09-09 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='content',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]

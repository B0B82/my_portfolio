# Generated by Django 3.1.6 on 2021-02-18 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_portfolio', '0003_auto_20210218_1859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(upload_to='my_portfolio/img'),
        ),
    ]

# Generated by Django 3.1.6 on 2021-03-05 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_portfolio', '0006_project_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='text',
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]

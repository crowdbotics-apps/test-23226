# Generated by Django 2.2.17 on 2020-12-07 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_load_initial_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='customtext',
            name='name',
            field=models.TextField(blank=True, null=True),
        ),
    ]

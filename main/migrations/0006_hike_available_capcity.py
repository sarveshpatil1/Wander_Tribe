# Generated by Django 4.1.7 on 2023-03-18 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_hike_level_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='hike',
            name='available_capcity',
            field=models.IntegerField(default=0),
        ),
    ]

# Generated by Django 4.1.7 on 2023-03-25 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='description',
            field=models.TextField(),
        ),
    ]

# Generated by Django 4.2.2 on 2023-07-08 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='email',
            field=models.EmailField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='mobile',
            field=models.IntegerField(),
        ),
    ]
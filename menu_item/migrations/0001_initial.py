# Generated by Django 4.2.3 on 2023-07-04 11:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('menu', '0001_initial'),
        ('item', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField()),
                ('itemId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='item.item')),
                ('menuId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.menu')),
            ],
        ),
    ]

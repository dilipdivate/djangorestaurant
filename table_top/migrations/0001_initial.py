# Generated by Django 4.2.3 on 2023-07-04 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TableTop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('NONE', 'None'), ('PENDING', 'Pending'), ('PROCESSING', 'Processing'), ('IN_PROCESS', 'In Process'), ('COMPLETE', 'Complete'), ('DELIVERED', 'Delivered')], default='NONE', max_length=10)),
                ('capacity', models.PositiveSmallIntegerField(default=0)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField(blank=True, null=True)),
            ],
        ),
    ]

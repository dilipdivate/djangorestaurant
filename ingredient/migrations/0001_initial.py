# Generated by Django 4.2.3 on 2023-07-04 11:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=75)),
                ('slug', models.CharField(max_length=100)),
                ('summary', models.TextField(blank=True, null=True)),
                ('type', models.PositiveSmallIntegerField(default=0)),
                ('sku', models.CharField(max_length=100)),
                ('quantity', models.FloatField(blank=True, default=0, null=True)),
                ('unit', models.PositiveSmallIntegerField(default=0)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_ingredients', to='user.user')),
                ('vendorId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vendor_ingredients', to='user.user')),
            ],
        ),
    ]

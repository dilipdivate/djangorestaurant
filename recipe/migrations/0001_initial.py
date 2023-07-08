# Generated by Django 4.2.3 on 2023-07-04 11:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ingredient', '__first__'),
        ('item', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.FloatField(blank=True, default=0, null=True)),
                ('unit', models.PositiveSmallIntegerField(default=0)),
                ('instructions', models.TextField(blank=True, null=True)),
                ('ingredientId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ingredient.ingredient')),
                ('itemId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_item_recipe', to='item.item')),
            ],
        ),
    ]
# Generated by Django 4.2.3 on 2023-07-04 15:57

from django.db import migrations, models
import user.models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_rename_admin_user_is_admin_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='middleName',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='mobile',
            field=models.CharField(default='1234567890', max_length=10, validators=[user.models.validate_digit_length]),
        ),
    ]

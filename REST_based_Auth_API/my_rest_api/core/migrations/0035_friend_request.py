# Generated by Django 3.2.5 on 2021-08-06 12:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0034_auto_20210806_1013'),
    ]

    operations = [
        migrations.AddField(
            model_name='friend',
            name='request',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='friend_request', to='core.request'),
        ),
    ]

# Generated by Django 5.1 on 2024-09-23 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Alev', '0016_alter_request_email_alter_request_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calculationrequest',
            name='phone',
            field=models.CharField(max_length=20),
        ),
    ]
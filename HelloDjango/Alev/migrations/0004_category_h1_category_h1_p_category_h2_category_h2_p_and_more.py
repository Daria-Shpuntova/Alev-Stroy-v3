# Generated by Django 5.1 on 2024-09-10 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Alev', '0003_kvartira_type_remont_service_remont'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='h1',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='h1_p',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='h2',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='h2_p',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='text_call',
            field=models.TextField(blank=True, null=True),
        ),
    ]
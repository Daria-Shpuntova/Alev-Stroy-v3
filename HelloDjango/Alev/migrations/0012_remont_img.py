# Generated by Django 5.1 on 2024-09-12 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Alev', '0011_kvartira_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='remont',
            name='img',
            field=models.TextField(null=True),
        ),
    ]

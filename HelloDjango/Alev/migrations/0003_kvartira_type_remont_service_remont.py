# Generated by Django 5.1 on 2024-09-10 20:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Alev', '0002_category_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kvartira',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
            ],
            options={
                'verbose_name': ('Вид квартиры',),
                'verbose_name_plural': 'Виды квартир',
            },
        ),
        migrations.CreateModel(
            name='Type_Remont',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('price', models.CharField(max_length=120)),
                ('text', models.TextField()),
                ('etapi', models.TextField()),
            ],
            options={
                'verbose_name': ('Вид ремонта квартиры',),
                'verbose_name_plural': 'Виды ремонта квартир',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('text', models.TextField()),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Alev.category')),
            ],
        ),
        migrations.CreateModel(
            name='Remont',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=120, verbose_name='Slug')),
                ('title', models.CharField(max_length=120)),
                ('text1', models.TextField()),
                ('text2', models.TextField()),
                ('text_call', models.TextField()),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Alev.category')),
                ('kvartira_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Alev.kvartira')),
                ('type_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Alev.type_remont')),
            ],
            options={
                'verbose_name': ('Вид ремонта',),
                'verbose_name_plural': 'Виды ремонтов',
            },
        ),
    ]

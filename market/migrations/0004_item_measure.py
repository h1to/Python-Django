# Generated by Django 3.2.10 on 2021-12-18 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0003_category_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='measure',
            field=models.CharField(blank=True, max_length=100, verbose_name='measure'),
        ),
    ]
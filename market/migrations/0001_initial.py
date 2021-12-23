# Generated by Django 3.0.7 on 2021-12-18 04:52

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='category_name')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='item_name')),
                ('description', models.CharField(max_length=500)),
                ('added_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='added_date')),
                ('image', models.ImageField(blank=True, upload_to='item_image')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market.Category')),
            ],
        ),
    ]

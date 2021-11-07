# Generated by Django 3.2.6 on 2021-09-28 14:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('img', models.ImageField(blank=True, upload_to='drugs/')),
            ],
        ),
        migrations.CreateModel(
            name='Drug',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('genericName', models.CharField(max_length=200)),
                ('brandName', models.CharField(max_length=200)),
                ('federalSchedule', models.CharField(max_length=200)),
                ('availability', models.CharField(max_length=200)),
                ('img', models.ImageField(blank=True, upload_to='drugs/')),
                ('description', models.TextField()),
                ('primaryIndications', models.CharField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='DrugClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('img', models.ImageField(blank=True, upload_to='drugs/')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('drugs', models.ManyToManyField(blank=True, related_name='Drugs', to='medcyclopedia.Drug')),
            ],
        ),
        migrations.AddField(
            model_name='drug',
            name='drugClass',
            field=models.ManyToManyField(blank=True, related_name='drugs', to='medcyclopedia.DrugClass'),
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('img', models.ImageField(blank=True, upload_to='drugs/')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('categories', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='articles', to='medcyclopedia.category')),
                ('tag', models.ManyToManyField(blank=True, related_name='articles', to='medcyclopedia.Tag')),
            ],
        ),
    ]
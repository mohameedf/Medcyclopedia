# Generated by Django 3.2.6 on 2021-10-30 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medcyclopedia', '0003_auto_20211030_2233'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='categories',
        ),
        migrations.AddField(
            model_name='article',
            name='categories',
            field=models.ManyToManyField(related_name='articles', to='medcyclopedia.Category'),
        ),
    ]

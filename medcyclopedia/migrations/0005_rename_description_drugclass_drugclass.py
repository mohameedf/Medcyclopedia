# Generated by Django 3.2.6 on 2021-11-07 13:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medcyclopedia', '0004_auto_20211030_2235'),
    ]

    operations = [
        migrations.RenameField(
            model_name='drugclass',
            old_name='description',
            new_name='drugClass',
        ),
    ]

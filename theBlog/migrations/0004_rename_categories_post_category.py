# Generated by Django 4.0.1 on 2022-01-23 10:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theBlog', '0003_categories_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='categories',
            new_name='category',
        ),
    ]

# Generated by Django 3.2.11 on 2022-01-26 11:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0009_remove_posts_author_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Users',
        ),
    ]
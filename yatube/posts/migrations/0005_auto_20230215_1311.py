# Generated by Django 2.2.19 on 2023-02-15 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_post_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='slug',
            field=models.SlugField(),
        ),
        migrations.AlterField(
            model_name='group',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]

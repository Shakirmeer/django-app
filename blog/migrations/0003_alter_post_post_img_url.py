# Generated by Django 4.2.13 on 2024-08-03 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_post_img_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_img_url',
            field=models.URLField(blank=True, max_length=300, null=True),
        ),
    ]

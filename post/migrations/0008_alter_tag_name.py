# Generated by Django 4.2.6 on 2023-12-27 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0007_rename_tag_post_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]

# Generated by Django 4.2.6 on 2024-01-05 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0010_tag_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, to='post.tag'),
        ),
    ]

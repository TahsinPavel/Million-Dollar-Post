# Generated by Django 3.2.8 on 2021-10-18 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0007_alter_post_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippet',
            field=models.CharField(default='Click Link Above to Read Blog Post', max_length=255),
        ),
    ]

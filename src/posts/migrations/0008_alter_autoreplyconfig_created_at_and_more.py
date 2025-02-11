# Generated by Django 5.0.7 on 2024-07-10 02:52

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0007_alter_reply_parent_reply"),
    ]

    operations = [
        migrations.AlterField(
            model_name="autoreplyconfig",
            name="created_at",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name="comment",
            name="created_at",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name="post",
            name="created_at",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name="reply",
            name="created_at",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]

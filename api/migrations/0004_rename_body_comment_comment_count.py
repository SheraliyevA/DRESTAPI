# Generated by Django 5.0.1 on 2024-01-27 13:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_comment_body'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='body',
            new_name='comment_count',
        ),
    ]

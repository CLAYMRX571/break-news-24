# Generated by Django 5.0 on 2024-09-08 21:49

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_contact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='views',
        ),
        migrations.AlterField(
            model_name='article',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]

# Generated by Django 2.2.5 on 2019-09-30 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0009_story_domain'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='domain',
            field=models.CharField(blank=True, db_index=True, max_length=255, null=True),
        ),
    ]

# Generated by Django 4.0.5 on 2022-06-08 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0013_alter_course_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='settings.ASSETS_ROOT'),
        ),
    ]

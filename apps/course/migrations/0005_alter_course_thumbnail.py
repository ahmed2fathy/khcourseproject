# Generated by Django 4.0.4 on 2022-06-08 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0004_alter_course_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='thumbnail',
            field=models.ImageField(upload_to='files/thumbnail'),
        ),
    ]

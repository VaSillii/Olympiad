# Generated by Django 3.0.7 on 2020-06-28 09:57

from django.db import migrations, models
import variant.models


class Migration(migrations.Migration):

    dependencies = [
        ('variant', '0002_questionanswerolympiad_file_answer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questionanswerolympiad',
            name='file_answer',
        ),
        migrations.AddField(
            model_name='userresultolympiad',
            name='file_answer',
            field=models.FileField(blank=True, null=True, upload_to=variant.models.content_file_name, validators=[variant.models.validate_file_extension], verbose_name='Файл с ответом на вопрос'),
        ),
    ]
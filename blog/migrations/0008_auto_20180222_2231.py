# Generated by Django 2.0.2 on 2018-02-22 20:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20180222_1446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagewithtests',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pageWithTests', to=settings.AUTH_USER_MODEL, verbose_name='author'),
        ),
        migrations.AlterField(
            model_name='pagewithtests',
            name='text_file',
            field=models.FileField(upload_to='pageWithTests'),
        ),
    ]

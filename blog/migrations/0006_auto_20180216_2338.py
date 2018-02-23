# Generated by Django 2.0.2 on 2018-02-16 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20180211_2015'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='hierarchy',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='text',
            field=models.TextField(blank=True, help_text='Any additional information'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='title',
            field=models.CharField(default='egor', max_length=200),
            preserve_default=False,
        ),
    ]

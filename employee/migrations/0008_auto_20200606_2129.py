# Generated by Django 3.0.6 on 2020-06-06 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0007_auto_20200606_2006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='postid',
            field=models.CharField(max_length=20),
        ),
    ]

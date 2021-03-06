# Generated by Django 3.0.6 on 2020-05-30 21:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False, unique=True, verbose_name='ID')),
                ('name', models.CharField(max_length=10, unique=True, verbose_name='Name')),
                ('civnum', models.CharField(default='civnum', max_length=15, unique=True, verbose_name='Civnum')),
                ('phnum', models.CharField(default='phnum', max_length=15, unique=True, verbose_name='Phnum')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date joined')),
                ('salt', models.CharField(blank=True, max_length=10, verbose_name='Salt')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'ordering': ('-date_joined',),
            },
        ),
    ]

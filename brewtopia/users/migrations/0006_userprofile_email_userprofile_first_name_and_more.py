# Generated by Django 4.1.7 on 2023-03-24 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_remove_userprofile_date_remove_userprofile_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='first_name',
            field=models.CharField(default='', max_length=30, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='last_name',
            field=models.CharField(default='', max_length=30, verbose_name='Last Name'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='password',
            field=models.CharField(default='', max_length=50, verbose_name='Password'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='password2',
            field=models.CharField(default='', max_length=50, verbose_name='rePassword'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='phone_number',
            field=models.CharField(default='', max_length=20, verbose_name='Number'),
        ),
    ]

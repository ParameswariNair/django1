# Generated by Django 2.1.3 on 2018-11-29 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='email',
            field=models.CharField(default='sinz@xyz', max_length=50),
        ),
        migrations.AddField(
            model_name='project',
            name='gender',
            field=models.CharField(default='male', max_length=50),
        ),
        migrations.AddField(
            model_name='project',
            name='username',
            field=models.CharField(default='sincy123', max_length=50),
        ),
    ]

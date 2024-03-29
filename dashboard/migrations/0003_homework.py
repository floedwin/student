# Generated by Django 2.2.1 on 2019-06-19 17:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_auto_20190619_1522'),
    ]

    operations = [
        migrations.CreateModel(
            name='Homework',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.IntegerField(db_index=True, unique=True, verbose_name='student_id')),
                ('name', models.CharField(default='', max_length=200, verbose_name='name')),
                ('year', models.CharField(default='', max_length=100, verbose_name='class')),
                ('subject', models.CharField(default='', max_length=100, verbose_name='subject')),
                ('homework_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='homework_date')),
                ('submission_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='submission_date')),
                ('status', models.CharField(default='', max_length=100, verbose_name='status')),
                ('action', models.CharField(default='', max_length=100, verbose_name='action')),
            ],
        ),
    ]

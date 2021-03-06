# Generated by Django 2.2.6 on 2020-06-20 18:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student_account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_roll', models.CharField(max_length=50)),
                ('s_pass', models.CharField(max_length=50)),
                ('s_class', models.CharField(max_length=10)),
                ('s_school', models.CharField(max_length=200)),
                ('SchoolEIIN', models.CharField(default=None, max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='student_feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback', models.TextField()),
                ('school', models.CharField(choices=[('Government Laboratory High School', 'Government Laboratory High School'), ('Viqarunnisa Noon School', 'Viqarunnisa Noon School'), ('Rifles Public School and College', 'Rifles Public School and College'), ('Dhaka Residential Model School and College', 'Dhaka Residential Model School and College'), ('Rajuk Uttara Model School & College', 'Rajuk Uttara Model School & College'), ('Dhanmondi Government Boys’ High School', 'Dhanmondi Government Boys’ High School'), ('Saint Joseph Higher Secondary School', 'Saint Joseph Higher Secondary School'), ('Sholla High School', 'Sholla High School'), ('St. Gregory’s High School', 'St. Gregory’s High School'), ('Motijheel Government Boys High school', 'Motijheel Government Boys High school'), ('Mirpur Govt. High School', 'Mirpur Govt. High School'), ('Django', 'Django')], max_length=300)),
                ('posted_time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]

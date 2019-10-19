# Generated by Django 2.2.2 on 2019-10-17 06:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_code', models.CharField(max_length=10)),
                ('course_name', models.CharField(max_length=25)),
                ('level', models.CharField(choices=[('ND-I', 'ND-I'), ('ND-II', 'ND-II'), ('HND-I', 'HND-I'), ('HND-II', 'HND-II')], max_length=8)),
                ('session', models.CharField(choices=[('1st-session', '1st-session'), ('2nd-session', '2nd-session')], max_length=15)),
                ('semester', models.CharField(choices=[('1st-semester', '1st-semester'), ('2nd-semester', '2nd-semester')], max_length=15)),
                ('levels', models.CharField(choices=[('difficult', 'Difficult'), ('easy', 'Easy')], max_length=10)),
                ('file', models.FileField(upload_to='')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25)),
                ('contents', models.TextField(max_length=1000)),
                ('file', models.FileField(upload_to='')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('levels', models.CharField(choices=[('difficult', 'Difficult'), ('easy', 'Easy')], max_length=10)),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='courses.Course')),
            ],
        ),
    ]

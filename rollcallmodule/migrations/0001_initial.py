# Generated by Django 3.0.7 on 2020-06-30 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('Attendance', models.CharField(max_length=45)),
                ('AttendanceID', models.AutoField(primary_key=True, serialize=False)),
                ('CourseName', models.CharField(max_length=45)),
                ('Date', models.DateField(max_length=45)),
                ('Password', models.CharField(max_length=45)),
                ('StudentName', models.CharField(max_length=45)),
                ('StudentNo', models.CharField(max_length=45)),
                ('TermName', models.CharField(max_length=45)),
                ('Username', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'History',
            },
        ),
    ]

# Generated by Django 3.0.7 on 2020-07-08 04:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('selectcourse', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tcourse',
            fields=[
                ('tcourseid', models.AutoField(primary_key=True, serialize=False)),
                ('tcoursename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'Tcourse',
            },
        ),
        migrations.CreateModel(
            name='TSelectCourse',
            fields=[
                ('tscid', models.AutoField(primary_key=True, serialize=False)),
                ('tcourse', models.ForeignKey(db_column='tcourseid', on_delete=django.db.models.deletion.CASCADE, to='selectcourse.Tcourse')),
            ],
            options={
                'db_table': 'TSelectCourse',
            },
        ),
        migrations.CreateModel(
            name='Tterm',
            fields=[
                ('ttermid', models.AutoField(primary_key=True, serialize=False)),
                ('ttermname', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'Tterm',
            },
        ),
        migrations.DeleteModel(
            name='Course',
        ),
        migrations.DeleteModel(
            name='Term',
        ),
        migrations.AddField(
            model_name='tselectcourse',
            name='tterm',
            field=models.ForeignKey(db_column='ttermid', on_delete=django.db.models.deletion.CASCADE, to='selectcourse.Tterm'),
        ),
    ]

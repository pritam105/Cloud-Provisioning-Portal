# Generated by Django 3.1.7 on 2021-12-29 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0010_server_instid'),
    ]

    operations = [
        migrations.CreateModel(
            name='test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Testname', models.CharField(max_length=200, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('start', models.TimeField(max_length=10, null=True)),
                ('stop', models.TimeField(max_length=10, null=True)),
                ('From', models.DateField(blank=True, null=True)),
                ('To', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'test',
            },
        ),
    ]

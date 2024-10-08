# Generated by Django 3.1.7 on 2021-09-22 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('schedule', '0007_scheduleserver_user_grp'),
    ]

    operations = [
        migrations.CreateModel(
            name='requestdetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sername', models.CharField(max_length=200, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('start', models.TimeField(max_length=10, null=True)),
                ('stop', models.TimeField(max_length=10, null=True)),
                ('From', models.DateField(blank=True, null=True)),
                ('To', models.DateField(blank=True, null=True)),
                ('didItStart', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default='N', max_length=1)),
                ('didItStop', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default='N', max_length=1)),
                ('scheduleFlag', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'requestdetail',
            },
        ),
        migrations.AddField(
            model_name='server',
            name='user_grp',
            field=models.ManyToManyField(to='auth.Group'),
        ),
        migrations.DeleteModel(
            name='scheduleserver',
        ),
    ]

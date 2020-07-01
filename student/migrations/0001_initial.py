# Generated by Django 2.2 on 2020-06-30 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll_no', models.IntegerField(default=1)),
                ('name', models.CharField(default='', max_length=70)),
                ('age', models.IntegerField(default=1)),
                ('marks', models.IntegerField(default=0)),
            ],
        ),
    ]
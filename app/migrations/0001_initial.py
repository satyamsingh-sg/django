# Generated by Django 3.0.7 on 2021-02-24 16:26

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
                ('name', models.CharField(max_length=50)),
                ('videofile', models.FileField(null=True, upload_to='', verbose_name='')),
            ],
        ),
    ]

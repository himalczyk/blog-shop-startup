# Generated by Django 4.0 on 2022-01-14 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('pub_date', models.DateTimeField()),
                ('link', models.URLField()),
                ('image', models.URLField()),
                ('post_name', models.CharField(max_length=100)),
                ('guid', models.CharField(max_length=50)),
            ],
        ),
    ]

# Generated by Django 4.1.7 on 2023-03-04 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ARService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_ar', models.CharField(max_length=200)),
                ('Short_description_ar', models.TextField(max_length=700)),
            ],
        ),
        migrations.CreateModel(
            name='AVVService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_avv', models.CharField(max_length=200)),
                ('Short_description_avv', models.TextField(max_length=700)),
            ],
        ),
        migrations.CreateModel(
            name='CASService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_cas', models.CharField(max_length=200)),
                ('Short_description_cas', models.TextField(max_length=700)),
            ],
        ),
        migrations.CreateModel(
            name='CCGCRService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_ccgcr', models.CharField(max_length=200)),
                ('Short_description_ccgcr', models.TextField(max_length=700)),
            ],
        ),
        migrations.CreateModel(
            name='CITCService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_citc', models.CharField(max_length=200)),
                ('Short_description_citc', models.TextField(max_length=700)),
            ],
        ),
        migrations.CreateModel(
            name='CMService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_cm', models.CharField(max_length=200)),
                ('Short_description_cm', models.TextField(max_length=700)),
            ],
        ),
        migrations.CreateModel(
            name='IMAService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_ima', models.CharField(max_length=200)),
                ('Short_description_ima', models.TextField(max_length=700)),
            ],
        ),
    ]

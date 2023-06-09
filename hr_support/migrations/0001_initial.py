# Generated by Django 4.1.7 on 2023-03-05 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CardHS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo_img_hs', models.ImageField(upload_to='hs_service/card/')),
                ('title_slogan_hs', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerBenefitHS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_benefit_img_hs', models.ImageField(upload_to='hs_service/customerBenefit/')),
                ('title_hs', models.CharField(max_length=200)),
                ('description_hs', models.TextField(max_length=1024)),
                ('customer_service_hs_1', models.CharField(max_length=200)),
                ('customer_service_hs_2', models.CharField(max_length=200)),
                ('customer_service_hs_3', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceHS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_img_hs', models.ImageField(upload_to='hs_service/service/')),
                ('title_hs', models.CharField(max_length=200)),
                ('description_first_para_hs', models.TextField(max_length=1024)),
                ('description_second_para_hs', models.TextField(max_length=1024)),
                ('service_details_card_title_hs_1', models.CharField(max_length=200)),
                ('service_details_card_details_hs_1', models.CharField(max_length=200)),
                ('service_details_card_title_hs_2', models.CharField(max_length=200)),
                ('service_details_card_details_hs_2', models.CharField(max_length=200)),
            ],
        ),
    ]

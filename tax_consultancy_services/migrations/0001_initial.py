# Generated by Django 4.1.7 on 2023-03-04 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CardTC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo_img_tc', models.ImageField(upload_to='tc_service/card/')),
                ('title_slogan_tc', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerBenefitTC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_benefit_img_tc', models.ImageField(upload_to='tc_service/customerBenefit/')),
                ('title_tc', models.CharField(max_length=200)),
                ('description_tc', models.TextField(max_length=700)),
                ('customer_service_tc_1', models.CharField(max_length=200)),
                ('customer_service_tc_2', models.CharField(max_length=200)),
                ('customer_service_tc_3', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceTC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_img_tc', models.ImageField(upload_to='tc_service/service/')),
                ('title_tc', models.CharField(max_length=200)),
                ('description_first_para_tc', models.TextField(max_length=700)),
                ('description_second_para_tc', models.TextField(max_length=700)),
                ('service_details_card_title_tc_1', models.CharField(max_length=200)),
                ('service_details_card_details_tc_1', models.CharField(max_length=200)),
                ('service_details_card_title_tc_2', models.CharField(max_length=200)),
                ('service_details_card_details_tc_2', models.CharField(max_length=200)),
            ],
        ),
    ]
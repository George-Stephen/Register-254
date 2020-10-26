# Generated by Django 3.1.2 on 2020-10-26 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_number', models.CharField(max_length=20)),
                ('full_name', models.CharField(max_length=255)),
                ('age', models.CharField(max_length=255)),
                ('email_address', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=10)),
                ('county', models.CharField(max_length=255)),
                ('sub_county', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_cards', models.CharField(max_length=255)),
                ('destination', models.CharField(max_length=255)),
                ('ordered_by', models.CharField(max_length=255)),
            ],
        ),
    ]

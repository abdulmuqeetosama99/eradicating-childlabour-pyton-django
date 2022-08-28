# Generated by Django 2.2.3 on 2019-11-13 08:48

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ngo',
            fields=[
                ('name', models.CharField(default='ngo', max_length=100, primary_key=True, serialize=False)),
                ('manager_name', models.CharField(max_length=100)),
                ('email', models.EmailField(default='example23@gmail.com', max_length=254)),
                ('contact_no', phonenumber_field.modelfields.PhoneNumberField(blank=True, help_text='Contact phone number', max_length=128, region=None)),
                ('address', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=30)),
                ('document', models.FileField(blank=True, upload_to='document/ngo')),
                ('verify', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='NgoMember',
            fields=[
                ('username', models.CharField(default='user', max_length=50, primary_key=True, serialize=False)),
                ('first_name', models.CharField(default=None, max_length=50)),
                ('last_name', models.CharField(default=None, max_length=50)),
                ('email', models.EmailField(default='example23@gmail.com', max_length=254)),
                ('contact_no', phonenumber_field.modelfields.PhoneNumberField(blank=True, help_text='Contact phone number', max_length=128, region=None)),
                ('ngo_name', models.CharField(max_length=100)),
                ('Adharno', models.BigIntegerField()),
                ('ngo_id', models.IntegerField()),
                ('designation', models.CharField(max_length=100)),
                ('is_manager', models.BooleanField(default=False)),
                ('ngo_verified', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('username', models.CharField(default='user', max_length=50, primary_key=True, serialize=False)),
                ('first_name', models.CharField(default=None, max_length=50)),
                ('last_name', models.CharField(default=None, max_length=50)),
                ('email', models.EmailField(default='example23@gmail.com', max_length=254)),
                ('contact_no', phonenumber_field.modelfields.PhoneNumberField(blank=True, help_text='Contact phone number', max_length=128, region=None)),
                ('volunteer_id', models.IntegerField()),
                ('Adharno', models.BigIntegerField()),
                ('verified', models.BooleanField(default=False)),
            ],
        ),
    ]
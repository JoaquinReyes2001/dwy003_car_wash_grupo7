# Generated by Django 2.2.16 on 2020-10-12 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('ident', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('imagen', models.ImageField(null=True, upload_to='car')),
            ],
        ),
    ]
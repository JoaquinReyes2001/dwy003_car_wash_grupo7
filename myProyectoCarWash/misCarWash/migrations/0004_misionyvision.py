# Generated by Django 2.2.16 on 2020-10-26 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('misCarWash', '0003_insumo'),
    ]

    operations = [
        migrations.CreateModel(
            name='MisionyVision',
            fields=[
                ('ident', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('mision', models.TextField()),
                ('vision', models.TextField()),
            ],
        ),
    ]
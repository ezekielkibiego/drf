# Generated by Django 4.2.13 on 2024-06-13 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='state',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state_name', models.CharField(max_length=50)),
                ('state_abbrev', models.CharField(max_length=2)),
                ('region', models.CharField(verbose_name=50)),
                ('division', models.CharField(max_length=50)),
            ],
        ),
    ]

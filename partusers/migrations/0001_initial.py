# Generated by Django 2.0.7 on 2019-11-14 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PartnerUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, null=True)),
                ('surname', models.TextField(blank=True, null=True)),
                ('email', models.TextField(blank=True, null=True)),
                ('password', models.TextField(blank=True, null=True)),
                ('ideas', models.TextField(blank=True, null=True)),
            ],
        ),
    ]

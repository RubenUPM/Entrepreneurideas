# Generated by Django 2.0.7 on 2019-11-14 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entrusers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entrepreneuruser',
            name='user_id',
        ),
        migrations.AddField(
            model_name='entrepreneuruser',
            name='email',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='entrepreneuruser',
            name='password',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='entrepreneuruser',
            name='ideas',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='entrepreneuruser',
            name='name',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='entrepreneuruser',
            name='surname',
            field=models.TextField(blank=True, null=True),
        ),
    ]

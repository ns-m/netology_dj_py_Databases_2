# Generated by Django 2.2.5 on 2019-12-30 19:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0011_auto_20191230_2346'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='membership',
            name='group',
        ),
        migrations.RemoveField(
            model_name='membership',
            name='user',
        ),
        migrations.DeleteModel(
            name='Group',
        ),
        migrations.DeleteModel(
            name='Membership',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]

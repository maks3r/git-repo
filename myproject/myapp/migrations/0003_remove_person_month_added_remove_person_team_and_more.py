# Generated by Django 4.2.16 on 2024-11-08 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_team_website'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='month_added',
        ),
        migrations.RemoveField(
            model_name='person',
            name='team',
        ),
        migrations.AlterField(
            model_name='person',
            name='shirt_size',
            field=models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large')], max_length=1),
        ),
    ]

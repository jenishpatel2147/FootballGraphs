# Generated by Django 3.2.8 on 2021-10-13 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FootAnalytics', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='footgraph',
            old_name='title',
            new_name='league',
        ),
        migrations.RemoveField(
            model_name='footgraph',
            name='completed',
        ),
        migrations.RemoveField(
            model_name='footgraph',
            name='description',
        ),
        migrations.AddField(
            model_name='footgraph',
            name='per',
            field=models.CharField(default=5, max_length=120),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='footgraph',
            name='position',
            field=models.CharField(default='att', max_length=120),
            preserve_default=False,
        ),
    ]
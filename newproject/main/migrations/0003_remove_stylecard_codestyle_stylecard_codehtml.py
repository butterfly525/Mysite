# Generated by Django 4.2.5 on 2023-10-30 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_stylecard_codecss_stylecard_codejs'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stylecard',
            name='codeStyle',
        ),
        migrations.AddField(
            model_name='stylecard',
            name='codeHTML',
            field=models.TextField(default='', verbose_name='HTML'),
            preserve_default=False,
        ),
    ]
# Generated by Django 5.0.2 on 2024-02-19 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_alter_buyer_uploadimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyer',
            name='uploadimage',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
    ]

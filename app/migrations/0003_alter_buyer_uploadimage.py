# Generated by Django 5.0.2 on 2024-02-16 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_buyer_uploadimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyer',
            name='uploadimage',
            field=models.ImageField(upload_to='media/media1'),
        ),
    ]
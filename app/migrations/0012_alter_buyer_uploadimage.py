# Generated by Django 5.0.2 on 2024-02-19 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_alter_buyer_bookname_alter_buyer_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyer',
            name='uploadimage',
            field=models.ImageField(blank=True, null=True, upload_to='mypicture'),
        ),
    ]

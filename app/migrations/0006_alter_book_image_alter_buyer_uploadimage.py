# Generated by Django 5.0.2 on 2024-02-16 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_book_image_alter_buyer_uploadimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(upload_to='Author/media/media'),
        ),
        migrations.AlterField(
            model_name='buyer',
            name='uploadimage',
            field=models.ImageField(upload_to='Author/media/media1'),
        ),
    ]

# Generated by Django 5.0.2 on 2024-02-18 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_book_image_alter_buyer_uploadimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(blank=True, max_length=254)),
                ('message', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='buyer',
            name='uploadimage',
            field=models.ImageField(upload_to='media'),
        ),
        migrations.DeleteModel(
            name='Book',
        ),
    ]

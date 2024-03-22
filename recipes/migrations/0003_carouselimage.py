# Generated by Django 4.1.6 on 2024-02-20 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_alter_category_options_alter_cuisine_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarouselImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_image', models.ImageField(upload_to='carousel/')),
                ('second_image', models.ImageField(upload_to='carousel/')),
                ('third_image', models.ImageField(upload_to='carousel/')),
            ],
            options={
                'verbose_name': 'Фото карусели',
                'verbose_name_plural': 'Фотографии карусели',
            },
        ),
    ]

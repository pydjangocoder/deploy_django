# Generated by Django 4.1.6 on 2024-02-20 10:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='cuisine',
            options={'verbose_name': 'Кухня', 'verbose_name_plural': 'Кухни'},
        ),
        migrations.AlterModelOptions(
            name='difficulty',
            options={'verbose_name': 'Уровень сложности', 'verbose_name_plural': 'Уровни сложностей'},
        ),
        migrations.AlterModelOptions(
            name='ingredient',
            options={'verbose_name': 'Ингредиент', 'verbose_name_plural': 'Ингредиенты'},
        ),
        migrations.AlterModelOptions(
            name='instruction',
            options={'verbose_name': 'Инструкция', 'verbose_name_plural': 'Инструкции'},
        ),
        migrations.AlterModelOptions(
            name='recipe',
            options={'verbose_name': 'Рецепт', 'verbose_name_plural': 'Рецепты'},
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=255, unique=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='cuisine',
            name='title',
            field=models.CharField(max_length=255, unique=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='difficulty',
            name='title',
            field=models.CharField(max_length=255, unique=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='quantity',
            field=models.IntegerField(verbose_name='Количество'),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipes.recipe', verbose_name='Рецепт'),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='unit',
            field=models.CharField(max_length=15, verbose_name='Единица измерения'),
        ),
        migrations.AlterField(
            model_name='instruction',
            name='image',
            field=models.ImageField(upload_to='instructions/', verbose_name='Фото инструкции'),
        ),
        migrations.AlterField(
            model_name='instruction',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipes.recipe', verbose_name='Рецепт'),
        ),
        migrations.AlterField(
            model_name='instruction',
            name='title',
            field=models.TextField(verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipes.category', verbose_name='Категория рецепта'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='cookTime',
            field=models.IntegerField(verbose_name='Время приготовления'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='cuisine',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipes.cuisine', verbose_name='Кухня рецепта'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='description',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='difficulty',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipes.difficulty', verbose_name='Уровень сложности'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=models.ImageField(upload_to='recipes/', verbose_name='Изображение рецепта'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='prepTime',
            field=models.IntegerField(verbose_name='Время подготовки'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='title',
            field=models.CharField(max_length=255, unique=True, verbose_name='Название'),
        ),
    ]

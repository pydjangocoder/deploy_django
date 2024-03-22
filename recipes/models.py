from django.db import models


# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=255, unique=True,
                             verbose_name="Название")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Cuisine(models.Model):
    title = models.CharField(max_length=255, unique=True,
                             verbose_name="Название")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Кухня"
        verbose_name_plural = "Кухни"


class Difficulty(models.Model):
    title = models.CharField(max_length=255, unique=True,
                             verbose_name="Название")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Уровень сложности"
        verbose_name_plural = "Уровни сложностей"


class Recipe(models.Model):
    title = models.CharField(max_length=255, unique=True,
                             verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    prepTime = models.IntegerField(verbose_name="Время подготовки")
    cookTime = models.IntegerField(verbose_name="Время приготовления")
    image = models.ImageField(upload_to='recipes/',
                              verbose_name="Изображение рецепта")
    cuisine = models.ForeignKey(Cuisine, on_delete=models.CASCADE,
                                verbose_name="Кухня рецепта")
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 verbose_name="Категория рецепта")
    difficulty = models.ForeignKey(Difficulty, on_delete=models.CASCADE,
                                   verbose_name="Уровень сложности")

    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Рецепт"
        verbose_name_plural = "Рецепты"


class Instruction(models.Model):
    title = models.TextField(verbose_name="Название")
    image = models.ImageField(upload_to='instructions/',
                              verbose_name="Фото инструкции")

    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE,
                               verbose_name="Рецепт")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Инструкция"
        verbose_name_plural = "Инструкции"


class Ingredient(models.Model):
    title = models.CharField(max_length=255,
                             verbose_name="Название")
    quantity = models.IntegerField(verbose_name="Количество")
    unit = models.CharField(max_length=15, verbose_name="Единица измерения")
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE,
                               verbose_name="Рецепт")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Ингредиент"
        verbose_name_plural = "Ингредиенты"


class CarouselImage(models.Model):
    first_image = models.ImageField(upload_to="carousel/")
    second_image = models.ImageField(upload_to="carousel/")
    third_image = models.ImageField(upload_to="carousel/")

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name = "Фото карусели"
        verbose_name_plural = "Фотографии карусели"
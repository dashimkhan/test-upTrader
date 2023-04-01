from django.db import models


class Menu(models.Model):
    title = models.CharField(max_length=255, unique=True, verbose_name='Название меню')
    slug = models.SlugField(max_length=255, verbose_name="Элемент slug")

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Менюшки'

    def __str__(self):
        return self.title


class Item(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название продукта')
    slug = models.SlugField(max_length=255, verbose_name="Название slug")
    menu = models.ForeignKey(Menu, blank=True, related_name='items', on_delete=models.CASCADE)
    parent = models.ForeignKey('self', blank=True, null=True, related_name='childrens', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Элемент Меню'
        verbose_name_plural = 'Элементы меню'

    def __str__(self):
        return self.title

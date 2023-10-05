from django.db import models


class Phone(models.Model) :
    name = models.CharField('Название' , max_length=50)

    price = models.DecimalField('Цена' , max_digits=16 , decimal_places=2)
    image = models.ImageField('URL изображения' , max_length=256)
    release_date = models.DateField('Дата релиза')
    lte_exists = models.BooleanField('Наличие LTE')
    slug = models.SlugField()

    class Meta :
        verbose_name = 'Телефон'
        verbose_name_plural = 'Телефоны'

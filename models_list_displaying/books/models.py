# coding=utf-8

from django.db import models


class Book(models.Model):
    name = models.CharField( max_length=50)
    author = models.CharField( max_length=50)
    pub_date = models.DateField('Дата публикации')


    def __str__(self):
        return self.name + " " + self.author
    def get_previous_book(self):
        """Получает предыдущую книгу по дате
        """
        return Book.objects.filter(pub_date_lt=self.pub_date).order_by('-pub_date').first()
    def get_next_book(self):
        """
        Получаю следующую книгу по дате
        """
        return Book.objects.filter(pub_date_lt=self.pub_date).order_by('-pub_date').first()
    def get_pub_date_path(self):
        """
        Преобразует дату книги в формат url запроса
        """
        old_date =self.pub_date

        return old_date.strftime('%Y-%m-%d')




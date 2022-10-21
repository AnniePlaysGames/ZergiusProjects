from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Course(models.Model):
    name = models.CharField(verbose_name='Название', max_length=50)
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(verbose_name='Стоимость', max_digits=7, decimal_places=2)
    image = models.ImageField(verbose_name='Обложка', upload_to='media/course_images/%Y/%m/%d')
    archive = models.FileField(verbose_name='Архив с курсом', upload_to='media/course_archives/%Y/%m/%d')
    creating_date = models.DateField(auto_now_add=True)
    slug = models.SlugField(max_length=50)
    users = models.ManyToManyField(User, related_name='purchesed_courses')

    class Meta:
        db_table = 'courses'
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('course_detail', kwargs={'slug': self.slug})

from django.db import models

class School(models.Model):
    logo = models.ImageField(upload_to='for_me/logos/',
    verbose_name='Логотип сайта')
    whatsapp = models.URLField(verbose_name='Вотсапп')
    twitter = models. URLField(verbose_name='Твиттер')
    facebook = models.URLField(verbose_name='Фейсбук')

    name = models.CharField(max_length=127, verbose_name='название')
    description = models.TextField(verbose_name='описание')
    admissiontouniversity = models.CharField(max_length=127,verbose_name='Поступление')
    staff = models.PositiveIntegerField(verbose_name='Персонал')
    students = models.PositiveIntegerField(verbose_name='Студенты')
    successworkyear = models.CharField(max_length=127, verbose_name='Рабочий год')
    mail = models.URLField(verbose_name='Почта')
    address = models.CharField(max_length=127, verbose_name='Адрес')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Школа'
        verbose_name_plural = 'Школы'


class Teacher(models.Model):
    School = models.ForeignKey(School, on_delete=models.CASCADE, related_name='teachers')
    position = models.CharField(max_length=127, verbose_name='Позиция')
    name = models.CharField(max_length=127, verbose_name=' Имя')
    photo = models.ImageField(upload_to='for_me/photo/',verbose_name='Фото')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Учитель'
        verbose_name_plural = 'Учителя'


class Gallery(models.Model):
    photos = models.ImageField(upload_to='for_me/photos/', verbose_name='Фотки')
    name = models.CharField(max_length=127, verbose_name='ФИО')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Галерея'
        verbose_name_plural = 'Галереи'


class Review(models.Model):
    photo = models.ImageField(upload_to='for_me/photo/', verbose_name='Фотка')
    name = models.CharField(max_length=127, verbose_name='ФИО')
    gender = models.CharField(max_length=127, verbose_name='Пол')
    description = models.TextField(verbose_name='описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


class New(models.Model):
    author = models.CharField(max_length=127, verbose_name = 'Автор')
    photo = models.ImageField(upload_to='for_me/photo/', verbose_name='Фотка')
    created_at = models.DateField(verbose_name='Дата создания')
    description = models.TextField(verbose_name='описание')


    def __str__(self):
        return self.author

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'






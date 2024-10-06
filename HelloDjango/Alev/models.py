from django.db import models
from django.urls import reverse


class Category(models.Model):
    slug = models.CharField(max_length=150, verbose_name='Слаг')
    title = models.CharField(max_length=120)
    img = models.TextField(verbose_name = 'Background', null = True)
    h1 = models.TextField(null=True, blank=True)
    h1_span = models.TextField(null=True, blank=True)
    h1_after_span = models.TextField(null=True, blank=True)
    h1_p = models.TextField(null=True, blank=True)
    h2 = models.TextField(null=True, blank=True)
    h2_p = models.TextField(null=True, blank=True)
    h2_p2 = models.TextField(null=True, blank=True)
    text_call =models.TextField(null=True, blank=True)


    class Meta:
        verbose_name = 'Вид услуг',
        verbose_name_plural = 'Виды услуг'

    def get_absolute_url(self):
        return reverse('serves', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

class Kvartira(models.Model):
    title = models.CharField(max_length=120)
    img = models.TextField(null = True)

    class Meta:
        verbose_name = 'Вид квартиры',
        verbose_name_plural = 'Виды квартир'

    def __str__(self):
        return self.title

class Type_Remont(models.Model):
    title = models.CharField(max_length=120)
    price = models.CharField(max_length=120)
    text = models.TextField()
    etapi = models.TextField()

    class Meta:
        verbose_name = 'Вид ремонта квартиры',
        verbose_name_plural = 'Виды ремонта квартир'

    def __str__(self):
        return self.title

class Remont(models.Model):
    slug = models.CharField(max_length=120, verbose_name='Slug')
    name = models.CharField(max_length=120, null=True, blank=True)
    h1 = models.TextField(null=True, blank=True)
    h1_span = models.TextField(null=True, blank=True)
    h1_after_span = models.TextField(null=True, blank=True)
    h1_p = models.TextField(null=True, blank=True)
    title_h2 = models.CharField(max_length=120)
    text1 = models.TextField()
    text2 = models.TextField()
    text_call = models.TextField()
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    kvartira_id = models.ForeignKey(Kvartira, on_delete=models.CASCADE, null=True, blank=True)
    type_id = models.ForeignKey(Type_Remont, on_delete=models.CASCADE, null=True, blank=True)
    img = models.TextField(null = True)

    class Meta:
        verbose_name = 'Вид ремонта',
        verbose_name_plural = 'Виды ремонтов'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('remont', kwargs={'slug': self.category_id.slug, 'remont_slug': self.slug})



class Service(models.Model):
    title = models.CharField(max_length=120)
    text = models.TextField()
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)


class Objects(models.Model):
    name_object = models.CharField(max_length=120)
    address = models.CharField(max_length=250, null=True)

    class Meta:
        verbose_name = 'Объект',
        verbose_name_plural = 'Объекты'

    def __str__(self):
        return self.name_object

class Image(models.Model):
    img = models.ImageField(upload_to='object')
    name = models.ForeignKey(Objects, null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Фото',
        verbose_name_plural = 'Фото'

class Type_work(models.Model):
    title = models.CharField(max_length=120)

    class Meta:
        verbose_name = 'Вид работ',
        verbose_name_plural = 'Виды работ'

    def __str__(self):
        return self.title

class Surface(models.Model):
    title = models.CharField(max_length=120)

    class Meta:
        verbose_name = 'Поверхность',
        verbose_name_plural = 'Поверхность'

    def __str__(self):
        return self.title

class Price(models.Model):
    title = models.CharField(max_length=300, verbose_name='Наименование работ')
    unit = models.CharField(max_length=50, verbose_name='Единица измерения')
    price = models.IntegerField(verbose_name='Цена')
    surface = models.ForeignKey(Surface, null=True, on_delete=models.CASCADE)
    type_work = models.ForeignKey(Type_work, null=True, on_delete=models.CASCADE)
    type_work = models.ForeignKey(Type_work, null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Прайс',
        verbose_name_plural = 'Прайс'

    def __str__(self):
        return self.title


class CalculationRequest(models.Model):
    room_type = models.CharField(max_length=50)
    repair_type = models.CharField(max_length=50)
    room_count = models.CharField(max_length=50)
    area = models.FloatField()
    design_project = models.BooleanField(default=False)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Калькулятор',
        verbose_name_plural = 'Калькулятор'

    def __str__(self):
        return self.room_type


class Request(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField(null=True, blank=True)
    message = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Обратная связь',
        verbose_name_plural = 'Обратная связь'

    def __str__(self):
        return self.name
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

class Catalog(models.Model):
    name = models.CharField(max_length=30, verbose_name='Имя Категории')
    images = models.ImageField(upload_to='catalogImg', verbose_name='Иконка')
    description = models.CharField(max_length=50, verbose_name='Доп. описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Payment(models.Model):
    method = models.CharField(max_length=30, verbose_name='Предпочитаемый способ оплаты')

    def __str__(self):
        return self.method

    class Meta:
        verbose_name = 'Способ оплаты'
        verbose_name_plural = 'Способ оплаты'


class Shipping(models.Model):
    method = models.CharField(max_length=30, verbose_name='Способ доставки')
    price = models.CharField(max_length=30, verbose_name='Cтоимость доставки', blank=True, null=True)

    def __str__(self):
        return self.method

    class Meta:
        verbose_name = 'Способ доставки'
        verbose_name_plural = 'Способ доставки'


class Tegs(models.Model):
    name = models.CharField(max_length=20, verbose_name='Тег')
    category = models.ForeignKey(Catalog, on_delete=models.CASCADE, verbose_name='Категория', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class Leaders(models.Model):
    name = models.CharField(max_length=1, verbose_name='Статус Y или N')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статус'



class ProductImagesDescr(models.Model):
    images = models.ImageField(upload_to='productImagesDescr/%Y/%m/%d/', verbose_name='Картинка Товара для описания')

    class Meta:
        verbose_name = 'Картинки для карточки'
        verbose_name_plural = 'Картинки для карточки'


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название товара')
    descriptions = models.TextField(verbose_name='Описание')
    price = models.IntegerField(verbose_name='Цена Товара')
    sale = models.IntegerField(verbose_name='Скидка в %')
    differencePrice = models.IntegerField(verbose_name='Скидка в $')
    newPrice = models.IntegerField(verbose_name='Конечная цена товара')
    rayting = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(0)], verbose_name='Рейтинг')
    tegs = models.ForeignKey(Tegs, on_delete=models.CASCADE, verbose_name='Тег')
    images = models.ImageField(upload_to='productIcon', verbose_name='Картинка Товара')
    states = models.ForeignKey(Leaders, on_delete=models.CASCADE, verbose_name='Лидер продаж?', null=True, blank=True)
    category = models.ForeignKey(Catalog, on_delete=models.CASCADE, verbose_name='Категория', blank=True, null=True)
    imagesDescr = models.ManyToManyField(ProductImagesDescr, verbose_name='Картинки для карточки товара')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class MainSlider(models.Model):
    text1 = models.CharField(max_length=255, verbose_name='Текст Слайда', null=True)
    text2 = models.CharField(max_length=255, verbose_name='Текст Слайда', null=True)
    text3 = models.CharField(max_length=255, verbose_name='Текст Слайда', null=True)
    image = models.ImageField(upload_to='mainSliderImages', verbose_name='Картанка слайда')

    def __str__(self):
        return self.text1

    class Meta:
        verbose_name = 'Главный Слайдер'
        verbose_name_plural = 'Главный Слайдер'


class News(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название новости')
    disc = models.TextField(max_length=755, verbose_name='Описание новости')
    image = models.ImageField(upload_to='newsImages', verbose_name='Картинка новости')
    published_date = models.DateTimeField(auto_created=True, verbose_name="Дата")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новости'
        verbose_name_plural = 'Новости'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatarsUser/', default="/avatarsUser/user-defalt.png")
    phone = models.IntegerField(verbose_name='Телефон')
    city = models.TextField(verbose_name='Город', max_length=20, blank=True, null=True)
    address = models.TextField(verbose_name='Адрес', max_length=155, blank=True, null=True)
    mail_index = models.CharField(verbose_name='Почтовый индекс', max_length=10, blank=True, null=True)
    preferredPaymentMethod = models.ForeignKey(Payment, verbose_name='Предпочитаемый способ оплаты',
                                               on_delete=models.CASCADE, blank=True, null=True)
    preferredShippingMethod = models.ForeignKey(Shipping, verbose_name='Предпочитаемый способ доставки',
                                                on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профиль'


# данная модель пока что в демо
# вероятнее всего будет удаленна
class BasketOfGoods(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Товар')
    users = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, null=True)
    delivery_Info = models.ForeignKey(Shipping, on_delete=models.CASCADE, verbose_name='Доставка', blank=True,
                                      null=True)
    payment_Info = models.ForeignKey(Payment, on_delete=models.CASCADE, verbose_name='Оплата', blank=True, null=True)
    totalPrice = models.IntegerField(blank=True, null=True, verbose_name='Общая стоимость товаров в корзине')

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзина'


# ==============================================================

class History(models.Model):
    basketInfo = models.ForeignKey(BasketOfGoods, on_delete=models.CASCADE, blank=True, null=True)
    userInfo = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, null=True)
    started_date = models.DateTimeField(auto_created=True, verbose_name="Дата добавления заказа")

    class Meta:
        verbose_name = 'История заказов'
        verbose_name_plural = 'История заказов'


class FeaturedProducts(models.Model):
    featuredProducts_User = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, null=True,
                                              verbose_name='Пользователь')
    featuredProducts_Product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True,
                                                 verbose_name='Товар')

    class Meta:
        verbose_name = 'Избран. тов.'
        verbose_name_plural = 'Избран. тов.'


class Comment(models.Model):
    user = models.ForeignKey(User, verbose_name="Никнейм", on_delete=models.CASCADE)
    commentText = models.TextField(verbose_name="Комментарий")
    published_date = models.DateTimeField(auto_created=True, verbose_name="Дата")
    product = models.ForeignKey(Product, verbose_name="Товар", on_delete=models.CASCADE)

    def __str__(self):
        return self.commentText

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

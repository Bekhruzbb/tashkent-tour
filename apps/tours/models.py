from django.db import models
from apps.common.models import BaseModel
from decimal import Decimal
# Create your models here.


class HouseType(BaseModel):

    class HouseChoices(models.TextChoices):
        Cabin = "cabin", "Cabin"
        Tiny_house = "tiny house", "Tiny House"
        A_frame = "a frame", "A Frame"
        Yurt = "yurt", "Yurt"
        Treehouse = "Treehouse", "treehouse"
        Boat = "Boat", "boat"

    name = models.CharField(choices=HouseChoices.choices, null=True, blank=True)
    slug = models.SlugField(unique=True, verbose_name="Ссылка для типа дома", null=True)

    def __str__(self):
        return self.name


class Tour(BaseModel):
    title = models.CharField(max_length=20, verbose_name="Заголовок тура")
    numb_people = models.TextField(verbose_name="Кол-во людей")
    slug = models.SlugField(unique=True)
    house_type = models.ForeignKey(HouseType, on_delete=models.CASCADE, verbose_name="Тип помещения")
    real_price = models.DecimalField(verbose_name="Реальная цена", decimal_places=2, max_digits=10)
    discount_percent = models.IntegerField(verbose_name="Скидочная процент", null=True)
    stars_number = models.IntegerField(verbose_name="Кол-во звезд")
    home_country = models.CharField(max_length=30, null=True, verbose_name="Страна вылета")
    away_country = models.CharField(max_length=30, verbose_name="Гостевая страна", null=True)

    def get_away_city_name(self):
        for i in [self.away_country]:
            return i[:3]

    def get_home_city_name(self):
        for i in [self.home_country]:
            return i[:3]

    def __str__(self):
        return f"{self.title} - {self.created_at}"

    @property
    def first_image(self):
        return self.images.first()

    def discount_calculate(self):
        return self.real_price - int(self.real_price * (Decimal(self.discount_percent/100)))

    class Meta:
        verbose_name = "Тур"
        verbose_name_plural = "Туры"


class ImagesTour(BaseModel):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, verbose_name="Тур", related_name="images", null=True)
    image = models.ImageField(upload_to="images/tours/", verbose_name="Фото туров",)

    class Meta:
        verbose_name = "Фото туров"


class Overview(BaseModel):
    tour = models.OneToOneField(Tour, related_name="overview", on_delete=models.CASCADE)
    text = models.TextField(verbose_name="Описание")
    duration = models.CharField(verbose_name="Продолжительность тура", max_length=30)
    tour_type = models.CharField(verbose_name="Тип тура", max_length=40)
    language = models.CharField(max_length=30, verbose_name="Язык тура")

    def __str__(self):
        return self.tour.title

    class Meta:
        verbose_name = "Оюзор тура"


class Highlights(BaseModel):
    tour = models.OneToOneField(Tour, on_delete=models.CASCADE, verbose_name="Преимущества", related_name="highlights")
    text = models.TextField()

    def __str__(self):
        return self.tour.title


class FAQ(BaseModel):
    question = models.CharField(max_length=50, verbose_name="Вопрос")
    answer = models.TextField(verbose_name="Ответ")

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = "Вопрос-ответ"
        verbose_name_plural = "Вопросы-ответы"


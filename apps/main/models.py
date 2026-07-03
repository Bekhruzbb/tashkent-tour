from django.db import models
from apps.common.models import BaseModel
from apps.users.models import CustomUser
# Create your models here.


class BookingBenefits(BaseModel):
    image = models.ImageField(upload_to="main/images/booking/", verbose_name="Фото пользы туров")
    title = models.CharField(verbose_name="Название пользы туров", max_length=20, null=True)
    text = models.TextField()

    class Meta:
        verbose_name = "Польза туров"
        verbose_name_plural = "Пользы туров"


class RecommendedPackages(BaseModel):
    title = models.CharField(max_length=30, verbose_name="Название рекомендуемого тура")
    photo = models.ImageField(upload_to="photos/recommended", null=True, blank=True)
    destination = models.CharField(max_length=20, verbose_name="Место отдыха")
    country = models.CharField(max_length=10, verbose_name="Страна")
    price = models.IntegerField(verbose_name="Рекомедуемая цена")

    class Meta:
        verbose_name = "Рекоммендуемый тур"
        verbose_name_plural = "Рекоммендуемые туры"


class ClientReviews(BaseModel):
    name = models.CharField(verbose_name="Имя пользователя", max_length=20, null=True)
    author_img = models.ImageField(upload_to="img/author/", verbose_name="Фото комментария", null=True, blank=True)
    work_type = models.CharField(max_length=20, verbose_name="Занятие автора")
    review_text = models.TextField()

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"


class NewsLetter(BaseModel):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="Пользователь отправляющий email")
    email_text = models.EmailField(max_length=20)

    def __str__(self):
        return f"{self.user} -> {self.email_text}"

    class Meta:
        verbose_name = "Отправка сообщений"
        verbose_name_plural="Отправка сообщений"

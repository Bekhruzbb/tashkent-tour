from django.urls import path, include
from .views import Booking_benefits_view, Recommended_packages_view, ArticleSerializer_view, \
    NewsLetterSerializer_view, ArticleSerializer_by_category_view, ArticleSerializer_by_detail_view,\
    Article_by_tag__view, Blog_comments_serializer_view, CommentCreateView, UpdateDeleteComments, show_tours_view, \
    ArticleCreateView

urlpatterns = [
    path("api/booking/v1/benefits/", Booking_benefits_view),
    path("api/booking/recommended/", Recommended_packages_view),
    path("api/articles/", ArticleSerializer_view.as_view()),
    path("api/article/<str:id>", ArticleSerializer_by_category_view),
    path("api/tag/<str:id>", Article_by_tag__view),
    path("api/newsletter/", NewsLetterSerializer_view),
    path("api/article-detail/<uuid:id>", ArticleSerializer_by_detail_view),
    path("api/comments/", Blog_comments_serializer_view),
    path("api/create/comments/", CommentCreateView.as_view()),
    path("api/create/articles/", ArticleCreateView.as_view()),
    path("api/action/comments/<uuid:id>", UpdateDeleteComments.as_view()),
    path("api/tours/page", show_tours_view),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt'))
]



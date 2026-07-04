from django.shortcuts import render
from django.http import HttpResponse
from apps.main.models import *
from apps.blog.models import Article, BlogComment
from apps.tours.models import Tour
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import \
    BookingBenefitsSerializer, CommentCreateSerializer, \
    RecommendedPackagesSerializer, ArticleSerializer, EmailNewsletterSerializer, BlogCommentSerializor, \
    TourSerializer, ArticleCreateSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView
# Create your views here.
from .services import IsAuthor


@api_view(["GET"])
def Booking_benefits_view(request):
    booking_benefits = BookingBenefits.objects.all()
    serializer = BookingBenefitsSerializer(booking_benefits, many=True)
    return Response(serializer.data)


@api_view()
def Recommended_packages_view(request):
    recommended_packages = RecommendedPackages.objects.all().order_by("-created_at")
    serializer = RecommendedPackagesSerializer(recommended_packages, many=True)
    return Response(serializer.data)


class ArticleSerializer_view(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


@api_view()
def ArticleSerializer_by_category_view(request, id):
    articles = Article.objects.filter(category=id)
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data)


@api_view()
def Article_by_tag__view(request, id):
    articles = Article.objects.filter(tag=id)
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def NewsLetterSerializer_view(request):
    newsletters = NewsLetter.objects.all()
    serializer = EmailNewsletterSerializer(newsletters, many=True)
    return Response(serializer.data)


@api_view()
def ArticleSerializer_by_detail_view(request, id):
    article = Article.objects.get(id=id)
    serializer = ArticleSerializer(article)
    return Response(serializer.data)


@api_view()
def Blog_comments_serializer_view(request):
    comments = BlogComment.objects.all()
    serializer = BlogCommentSerializor(comments, many=True)
    return Response(serializer.data)


class CommentCreateView(CreateAPIView):
    queryset = BlogComment.objects.all()
    serializer_class = CommentCreateSerializer
    permission_classes = [IsAuthenticated]


class ArticleCreateView(CreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleCreateSerializer


class UpdateDeleteComments(RetrieveUpdateDestroyAPIView):
    queryset = BlogComment.objects.all()
    serializer_class = CommentCreateSerializer
    permission_classes = [IsAuthenticated, IsAuthor]

    lookup_field = "id"
    lookup_url_kwarg = "id"


@api_view()
def show_tours_view(request):
    tours = Tour.objects.all()
    serializer = TourSerializer(tours, many=True)
    return Response(serializer.data)


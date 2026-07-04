import uuid
from rest_framework import serializers
from apps.main.models import BookingBenefits, RecommendedPackages
from apps.blog.models import BlogComment, Article
from apps.tours.models import Tour
# class BookingBenefitsSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = BookingBenefits
#         fields = ["id", "title"]


class BookingBenefitsSerializer(serializers.Serializer):
    id = serializers.UUIDField(default=uuid.uuid4)
    title = serializers.CharField(max_length=40)


class RecommendedPackagesSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=30)
    photo = serializers.ImageField()
    destination = serializers.CharField()
    country = serializers.CharField()
    price = serializers.IntegerField()


class Article_by_Category_Serializer(serializers.Serializer):
    name = serializers.CharField()
    slug = serializers.SlugField()


class Article_by_Tag_Serializer(serializers.Serializer):
    name = serializers.CharField()
    slug = serializers.SlugField()


class BlogCommentSerializor(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%d. %m. %Y")
    user = serializers.CharField(source="user.username", read_only=True)

    class Meta:
        model = BlogComment
        fields = ["id", "user", "text", "created_at", "article"]


class ArticleSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    title = serializers.CharField()
    photo = serializers.ImageField()
    slug = serializers.SlugField()
    date = serializers.CharField()
    text = serializers.CharField()
    views = serializers.IntegerField(source="views.count", read_only=True)
    category = Article_by_Category_Serializer()
    tag = Article_by_Tag_Serializer()
    comments = BlogCommentSerializor(many=True, read_only=True)


class EmailNewsletterSerializer(serializers.Serializer):
    user = serializers.CharField()
    email_text = serializers.EmailField()


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogComment
        fields = ["article", "user", "text", "parent"]


class TourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tour
        fields = "__all__"


class ArticleCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"

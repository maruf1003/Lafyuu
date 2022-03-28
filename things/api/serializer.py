from things.models import CustomUser, Category, Product, Color, Size, Image, Review_product, Rw_pr_img, UserCard, \
    Notification, NotificationType
from rest_framework import serializers
from django.db.models import Avg, Sum, Count
from django_filters import rest_framework as filters


# Serializers define the API representation.

# User serialazer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = "__all__"  # Bizga CustomUser'dagi hamma polyalar kerak bolgani uchun "__all__" yozilgan.
        # Agar bizga opredelyonniy polyasi kerak bolsa uni massiv korinishida korsatamiz ['full_name', ...]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    color = serializers.SerializerMethodField()
    review_avg = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = "__all__"

    def get_category(self, obj):
        return CategorySerializer(obj.size, many=False, context={"request": self.context["request"]}).data

    def get_image(self, obj):
        return ImageSerializer(obj.image, many=False, context={"request": self.context["request"]}).data

    def get_color(self, obj):
        return ColorSerializer(obj.color, many=True, context={"request": self.context["request"]}).data

    def get_size(self, obj):
        return SizeSerializer(obj.size, many=False, context={"request": self.context["request"]}).data

    def get_review_avg(self, obj):
        return Review_product.objects.filter(product=obj).aggregate(Avg('star'), Sum('star'), Count('star'))


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = "__all__"


class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = "__all__"


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = "__all__"


class Review_productSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review_product
        fields = "__all__"


class Rw_pr_imgSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rw_pr_img
        fields = "__all__"


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class ProductFilter(filters.FilterSet):  # Product'ларни category' бойича филтрлаб чикарябмиз
    category = filters.ModelChoiceFilter(queryset=Category.objects.all(), field_name='category')

    class Meta:
        model = Product
        fields = ['category']


class UserCardSerializer(serializers.ModelSerializer):
    product = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()

    class Meta:
        model = UserCard
        fields = "__all__"

    # User tanlagan productlarni sifatlari bilan chiqarish
    def get_product(self, obj):
        return ProductSerializer(obj.product, many=False, context={"request": self.context["request"]}).data

    # Userning ma'lumotlari
    def get_user(self, obj):
        return UserSerializer(obj.user, many=False, context={"request": self.context["request"]}).data


#######################################################################################################################

# Уведомления
class NotificationTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationType
        fields = "__all__"


# Уведомления типлари
class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = "__all__"


class NotificationFilter(filters.FilterSet):  # notification'ларни type' бойича филтрлаб чикарябмиз
    notificationType = filters.ModelChoiceFilter(queryset=NotificationType.objects.all(), field_name='notificationType')

    class Meta:
        model = Notification
        fields = ['notificationType']


#########################################################################################
# Pay Click
class ClickUzSerializer(serializers.Serializer):
    click_trans_id = serializers.CharField(allow_blank=True)
    service_id = serializers.CharField(allow_blank=True)
    merchant_trans_id = serializers.CharField(allow_blank=True)
    merchant_prepare_id = serializers.CharField(allow_blank=True, required=False, allow_null=True)
    amount = serializers.CharField(allow_blank=True)
    action = serializers.CharField(allow_blank=True)
    error = serializers.CharField(allow_blank=True)
    error_note = serializers.CharField(allow_blank=True)
    sign_time = serializers.CharField()
    sign_string = serializers.CharField(allow_blank=True)
    click_paydoc_id = serializers.CharField(allow_blank=True)

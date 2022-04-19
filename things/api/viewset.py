from rest_framework import viewsets, mixins, filters
from Store.pagination import LargeResultsSetPagination
from things.models import Product, Color, Size, Review_product, Category, Image, Rw_pr_img, UserCard, Notification, \
    NotificationType
from things.api.serializer import ProductSerializer, ColorSerializer, SizeSerializer, Review_productSerializer, \
    Rw_pr_imgSerializer, ImageSerializer, CategorySerializer, ProductFilter, UserCardSerializer, NotificationSerializer, \
    NotificationTypeSerializer
from django_filters.rest_framework import DjangoFilterBackend  # djangofilter(поиск)
from rest_framework.permissions import IsAuthenticated


class CategoryViewSet(mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      viewsets.GenericViewSet):  # магазин учун товарлар категорияси CRUD амаллари кошилмади чунки бу user учун керак эмас
    queryset = Category.objects.all().order_by("my_order")  # my_order'ni API qismiga uladig. admin sahifasidan Product Category'sini qay tartibda o'zgartirsak xuddi shu tartibda USER'ga ko'rinadi
    serializer_class = CategorySerializer
    filter_backends = (DjangoFilterBackend,)


class ProductViewSet(mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     viewsets.GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filterset_class = ProductFilter
    pagination_class = LargeResultsSetPagination # paginatsiya

    search_fields = ['name', 'style']  # поискда кайси ном бойича кидириши
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]  # поиск API кисмида


# продуктлар учун ранг
class ColorViewSet(mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   viewsets.GenericViewSet):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer


class SizeViewSet(mixins.ListModelMixin,  # продуктлар размерлари
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    queryset = Size.objects.all()
    serializer_class = SizeSerializer


class ImageViewSet(mixins.ListModelMixin,  # продуктлар расми
                   mixins.RetrieveModelMixin,
                   viewsets.GenericViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class Review_productViewSet(mixins.ListModelMixin,  # отзыв
                            mixins.CreateModelMixin,
                            mixins.UpdateModelMixin,
                            mixins.DestroyModelMixin,
                            viewsets.GenericViewSet):
    queryset = Review_product.objects.all()
    serializer_class = Review_productSerializer


class Rw_pr_imgViewSet(mixins.ListModelMixin,  # отзыв остидаги продуктлар сурати
                       mixins.RetrieveModelMixin,
                       viewsets.GenericViewSet):
    queryset = Rw_pr_img.objects.all()
    serializer_class = Rw_pr_imgSerializer


class UserCardViewSet(mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      mixins.RetrieveModelMixin,
                      viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    queryset = UserCard.objects.all()
    serializer_class = UserCardSerializer


####################################################################################################################33

class NotificationTypeViewSet(mixins.ListModelMixin,  # Уведомления
                              mixins.RetrieveModelMixin,
                              viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    queryset = NotificationType.objects.all()
    serializer_class = NotificationTypeSerializer


class NotificationViewSet(mixins.ListModelMixin,  # Уведомления типлари
                          mixins.RetrieveModelMixin,
                          viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

###########################################################################################33

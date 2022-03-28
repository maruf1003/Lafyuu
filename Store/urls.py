from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers

from things.api.payments import ClickUzMerchantAPIView
from things.api.views import UserViewSet, login_view, me, save_registr, set_card, update_password, update_user, order_creat
from things.api.viewset import *
from things.views import subscribe

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)  # User api
router.register(r'products', ProductViewSet)
router.register(r'images', ImageViewSet)
router.register(r'colors', ColorViewSet)
router.register(r'sizes', SizeViewSet)
router.register(r'review_products', Review_productViewSet)
router.register(r'rw_pr_imgs', Rw_pr_imgViewSet)
router.register(r'categorys', CategoryViewSet)
router.register(r'usercards', UserCardViewSet)
router.register(r'notifications', NotificationViewSet)
router.register(r'notificationTypes', NotificationTypeViewSet)

urlpatterns = [
                  path('api/v1/', include(router.urls)),
                  path('api/v1/login/', login_view),
                  path('api/v1/add/', set_card),
                  path('api/v1/register/', save_registr),
                  path('api/v1/me', me),
                  path('api/v1/update_password/', update_password),
                  path('api/v1/update_user/', update_user),
                  path('api/v1/order_creat/', order_creat),
                  path('', subscribe, name='subscribe'),
                  path('click/', ClickUzMerchantAPIView.as_view()),
                  path('admin/', admin.site.urls),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

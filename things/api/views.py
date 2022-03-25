from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from things.models import CustomUser, UserCard, Order
from rest_framework import viewsets
from things.api.serializer import UserSerializer
from rest_framework_jwt.settings import api_settings
from django.core.files.storage import FileSystemStorage


# ViewSets define the view behavior.

# User view
class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER  # token uchun
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


# User log in (avtorizatsiya 1-martta royxatdan otganda)
@api_view(["POST"])
@permission_classes([AllowAny])  # ([HammagaRuxsat])
def save_registr(request):
    try:
        email = request.POST["email"]
        password = request.POST["password"]
        full_name = request.POST["full_name"]
        user = CustomUser.objects.filter(email=email).first()  # bu yerda unikal ma'lumot tekshiriladi
        if user:  # agar user kiritgan email'ga o'xshagan email bolsa-
            res = {
                "status": 0,
                "error": "User alerdy exits"  # -unda bunday user bor degan yozuv qaytaramiz
            }  # bolmasam-
            return Response(res)
        user = CustomUser.objects.create(  # -yangi user yaratamiz
            email=email,
            # aslida username unikal bolishi kerak, bizda email unikal bolgani uchun uni username'ga tenglashtirib kettik
            username=email,
            full_name=full_name,
        )
        user.set_password(password)  # password tekshirish (password=password)
        user.save()

        # token yasash
        payload = jwt_payload_handler(user)  # token uchun
        token = jwt_encode_handler(payload)
        res = {
            "status": 1,
            "msg": "Login",
            "user": UserSerializer(user, many=False).data,  # user ma'lumotlari qaytarilayapti
            "token": token
        }
        return Response(res)

    except KeyError:
        res = {
            "status": 0,
            "error": "Key error"
        }

    return Response(res)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def me(request):
    user = request.user
    res = {
        "status": 1,
        "user": UserSerializer(user, many=False).data,

    }

    return Response(res)


# User oz saxifasiga kirishi uchun tekshiruvdan otishi
@api_view(["POST"])
@permission_classes([AllowAny])
def login_view(request):
    try:
        login = request.data['login']
        password = request.data['password']
        # user name va paroli biz kiritgan qiymatlarga teng bo'lsa login qilamiz (kirishga ruxsat berilsdi)
        user = CustomUser.objects.filter(username=login).first()
        if user and user.check_password(password):
            payload = jwt_payload_handler(user)
            token = jwt_encode_handler(payload)
            res = {
                "status": 1,
                "msg": "Login",
                "user": UserSerializer(user, many=False).data,
                "token": token
            }
        else:
            res = {
                "status": 1,
                "error": "login or password error"
            }
        return Response(res)

    except KeyError:
        res = {
            "status": 0,
            "error": "Key error"
        }
    return Response(res)


# Product'ni tanlanganda UserCard'ga qoshilishi
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def set_card(request):
    try:
        user = request.user
        product = request.data['product']
        if not UserCard.objects.filter(user=user, product_id=product).exists():
            UserCard.objects.create(
                user=user,
                product_id=product
            ).save()
        res = {
            "status": 1,
            "error": "Product append"
        }
    except KeyError:
        res = {
            "status": 1,
            "error": "key error"
        }
    return Response(res)


###############################################################################################33
# UP_DATE
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def update_user(request):
    first_name = request.POST.get("first_name")
    last_name = request.POST.get("last_name")
    user = request.user
    if user:
        if 'image' in request.FILES:
            upload = request.FILES['image']
            fss = FileSystemStorage()
            file = fss.save(upload.name, upload)
            user.image = file
        user.name = first_name
        user.last_name = last_name
        user.save()
        res = {
            "status": 1,
            "error": "changed successfully"
        }
    else:
        res = {
            "status": 0,
            "error": "wrong changed"
        }
    return Response(res)


# passwordni'ni yangilash
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def update_password(request):
    try:
        password = request.data['password']
        old_password = request.data['old_password']
        user = request.user
        if user and user.check_password(old_password):
            user.set_password(password)
            user.save()
            res = {
                "password changed successfully"
            }
        else:
            res = {
                "status": 0,
                "error": "wrong password"
            }
        return Response(res)
    except KeyError:
        res = {
            "status": 0,
            "error": "Key error"
        }

    return Response(res)


########################################################################################33333
from things.models import OrderItem, Product


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def order_creat(request):
    product_ids = request.data["product_ids"]
    order = Order.objects.create(
        title=request.data["title"],
        status=0,
        price=0,
        user=request.user
    )
    order.save()
    total_price = 0
    for i in product_ids:
        product = Product.objects.filter(id=i).first()
        if product:
            OrderItem.objects.create(
                order=order,
                product=product,
                price=product.price
            ).save()
            total_price = total_price + product.price
    order.price = total_price
    order.save()
    return Response({"status": 1})



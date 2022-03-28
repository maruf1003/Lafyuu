from django.contrib import admin
from things.models import *


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name', 'size']


admin.site.register(CustomUser)  # User
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Color)
admin.site.register(Size)
admin.site.register(Image)
admin.site.register(Review_product)
admin.site.register(Rw_pr_img)
admin.site.register(UserCard)
admin.site.register(NotificationType)
admin.site.register(Notification)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Address)
admin.site.register(Country_Region)
admin.site.register(City)
admin.site.register(Transaction)




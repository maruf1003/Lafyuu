from django.contrib import admin
from things.models import *
from adminsortable2.admin import SortableAdminMixin


class ProductStoreInline(admin.TabularInline):  # Inline faqatgina ForeignKey turdagi modellarga yaratiladi
    model = Product


class CategoryAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ['name']
    inlines = [ProductStoreInline]  # Bu yerda Product Inline'ni Adminni Category qismiga ulayapmiz


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'style']
    search_fields = ['name', 'style']
    list_filter = ['category']


admin.site.register(CustomUser)  # User
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
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

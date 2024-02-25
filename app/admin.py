from django.contrib import admin
from .models import CustomModel,  Buyer, Seller, Contact
# Register your models here.

@admin.register(CustomModel)
class CustomModelAdmin(admin.ModelAdmin):
    list_display = ['id','first_name','last_name','email','password','phonenumber']

@admin.register(Buyer)
class BuyerModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','bookname','price','image']

@admin.register(Seller)
class SellerModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','bookname','price','image']

@admin.register(Contact)
class SellerModelAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','address','message']
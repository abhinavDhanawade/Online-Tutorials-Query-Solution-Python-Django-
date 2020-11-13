from django.contrib import admin
from services.models import ContactUs, Category, Tutorial,Purchase,Userprofile

admin.site.register(ContactUs)
admin.site.register(Userprofile)
admin.site.register(Category)
admin.site.register(Tutorial)
admin.site.register(Purchase)
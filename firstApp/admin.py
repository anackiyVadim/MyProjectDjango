from django.contrib import admin
from .models import Catalog, Tegs, Product, MainSlider, Leaders, News, Payment, BasketOfGoods, Profile, Shipping, \
    History, FeaturedProducts, ProductImagesDescr, Comment

# Register your models here.
admin.site.register(Catalog)
admin.site.register(Tegs)
admin.site.register(Product)
admin.site.register(MainSlider)
# admin.site.register(Leaders)
admin.site.register(News)
# admin.site.register(Payment)
admin.site.register(BasketOfGoods)
admin.site.register(Profile)
# admin.site.register(Shipping)
admin.site.register(History)
admin.site.register(FeaturedProducts)
admin.site.register(ProductImagesDescr)
# admin.site.register(Comment)

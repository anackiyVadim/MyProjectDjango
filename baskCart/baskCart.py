from decimal import Decimal
from django.conf import settings
from firstApp.models import Product


class Cart(object):
    def __init__(self, request):
        self.session = request.session
        baskCart = self.session.get(settings.CART_SESSION_ID)
        if not baskCart:
            baskCart = self.session[settings.CART_SESSION_ID] = {}
        self.baskCart = baskCart

    def add(self, product, quantity=1, update_quantity=False):
        product_id = str(product.id)
        if product_id not in self.baskCart:
            self.baskCart[product_id] = {'quantity': 0, 'price': str(product.newPrice)}
        if update_quantity:
            self.baskCart[product_id]['quantity'] = quantity
        else:
            self.baskCart[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.baskCart
        # Это говорит о том, что сессия modified и должна быть сохранена.
        self.session.modified = True

    def remove(self, product):
        # Метод remove() удаляет заданный продукт из словаря корзины
        # и вызывает метод save() для обновления корзины в сессии.
        product_id = str(product.id)
        if product_id in self.baskCart:
            del self.baskCart[product_id]
            self.save()

    def __iter__(self):
        product_ids = self.baskCart.keys()
        products = Product.objects.filter(id__in=product_ids)
        for product in products:
            self.baskCart[str(product.id)]['product'] = product

        for item in self.baskCart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        # Подсчет всех товаров в корзине.
        return sum(item['quantity'] for item in self.baskCart.values())

    def get_total_price(self):
        # для расчета общей стоимости товаров в корзине
        return sum(Decimal(item['price']) * item['quantity'] for item in self.baskCart.values())

    def clear(self):
        # удаление корзины из сессии
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True

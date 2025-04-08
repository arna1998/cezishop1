from Clothing.models import Product, Profile


class Cart:
    def __init__(self, request):
        self.session = request.session
        self.request = request

        cart = self.session.get('session_key')
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        self.cart = cart

    def db_add(self, product, quantity):
        product_id = str(product)
        product_qty = int(quantity)

        # اگر محصول از قبل در سبد باشد، تعداد آن به‌روزرسانی شود
        if product_id in self.cart:
            pass
        else:
            self.cart[product_id] = int(product_qty)

        self.session.modified = True

        if self.request.user.is_authenticated:
            current_user = Profile.objects.filter(user__id = self.request.user.id)
            db_cart = str(self.cart).replace('\'','\"')

            current_user.update(old_cart=str(db_cart))

    def __len__(self):
        # تعداد کل آیتم‌های موجود در سبد
        return sum(self.cart.values())


    def add(self, product, quantity):
        product_id = str(product.id)
        product_qty = int(quantity)

        # اگر محصول از قبل در سبد باشد، تعداد آن به‌روزرسانی شود
        if product_id in self.cart:
            pass
        else:
            self.cart[product_id] = int(product_qty)

        self.session.modified = True

        if self.request.user.is_authenticated:
            current_user = Profile.objects.filter(user__id=self.request.user.id)
            db_cart = str(self.cart).replace('\'', '\"')

            current_user.update(old_cart=str(db_cart))

    def __len__(self):
        # تعداد کل آیتم‌های موجود در سبد
        return sum(self.cart.values())

    def get_prods(self):
        # دریافت محصولات از مدل بر اساس آیدی‌های موجود در سبد
        product_ids = self.cart.keys()
        return Product.objects.filter(id__in=product_ids)

    def get_quants(self):
        return self.cart

    def get_total(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        product_map = {product.id: product for product in products}

        total = 0
        for product_id, quantity in self.cart.items():
            product = product_map.get(int(product_id))
            if product:
                if product.is_sale:
                    total += product.sale_price * quantity
                else:
                    total += product.price * quantity

        return total

    def update(self, product, quantity):
        product_id = str(product)
        product_qty = int(quantity)

        if product_id in self.cart:
            self.cart[product_id] = product_qty
            self.session.modified = True

            if self.request.user.is_authenticated:
                current_user = Profile.objects.filter(user__id=self.request.user.id)
                db_cart = str(self.cart).replace('\'', '\"')

                current_user.update(old_cart=str(db_cart))

            jens = self.cart
            return jens

    def delete(self, product):
        product_id = str(product)

        if product_id in self.cart:
            del self.cart[product_id]
            self.session.modified = True

            if self.request.user.is_authenticated:
                current_user = Profile.objects.filter(user__id=self.request.user.id)
                db_cart = str(self.cart).replace('\'', '\"')

                current_user.update(old_cart=str(db_cart))


from django.db import models


# Create your models here.
class BotUser(models.Model):
    full_name = models.CharField(verbose_name="Ism", max_length=100)
    username = models.CharField(verbose_name="Telegram username", max_length=100, null=True)
    telegram_id = models.BigIntegerField(verbose_name='Telegram ID', unique=True, default=1)

    # email = models.CharField(verbose_name='Email', max_length=50, null=True)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'TelegramBot User'
        verbose_name_plural = 'TelegramBot Users'
        db_table = "bot_user"


class Product(models.Model):
    name = models.CharField(verbose_name="Mahsulot nomi", max_length=50)
    # photo = models.ImageField(upload_to="images/", verbose_name="Rasmi", max_length=200, null=True, blank=True)
    image = models.CharField(verbose_name="Rasmi", max_length=200, null=True, blank=True)
    price = models.DecimalField(verbose_name="Narxi", decimal_places=2, max_digits=10)
    description = models.TextField(verbose_name="Mahsulot haqida", max_length=3000, null=True)
    category = models.ForeignKey(
        'Category',
        verbose_name="Kategoriya",
        related_name="products",
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'
        db_table = "product"


class Category(models.Model):
    name = models.CharField(verbose_name="Kategoriya nomi", max_length=100)

    # description = models.TextField(verbose_name="Kategoriya haqida", max_length=3000, null=True, blank=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        db_table = "category"

    def __str__(self):
        return self.name


# class SubCategory(models.Model):
#     name = models.CharField(verbose_name="Kategoriya nomi", max_length=100)
#     # description = models.TextField(verbose_name="Kategoriya haqida", max_length=3000, null=True, blank=True)
#     category = models.ForeignKey(
#         'Category',
#         verbose_name="Ota Kategoriya",
#         related_name="sub_categories",
#         on_delete=models.CASCADE
#     )
#
#     class Meta:
#         verbose_name = 'sub_category'
#         verbose_name_plural = 'sub_categories'
#         db_table = "sub_category"
#
#     def __str__(self):
#         return self.name


# class Cart(models.Model):
#     user = models.ForeignKey(
#         'BotUser',
#         verbose_name="Foydalanuvchi",
#         related_name="cart",
#         on_delete=models.CASCADE
#     )
#     product = models.ForeignKey(
#         'Product',
#         verbose_name="Mahsulot",
#         related_name="carts",
#         on_delete=models.CASCADE
#     )
#     quantity = models.IntegerField(verbose_name="Soni", default=1)
#     total_price = models.DecimalField(verbose_name="Narxi", decimal_places=2, max_digits=10)
#
#     class Meta:
#         verbose_name = 'cart'
#         verbose_name_plural = 'carts'
#         db_table = "cart"

# class Cart(models.Model):
#     user = models.ForeignKey(BotUser, on_delete=models.CASCADE)
#
#     # created_at = models.DateTimeField(default=datetime.now)
#
#     class Meta:
#         verbose_name = 'cart'
#         verbose_name_plural = 'carts'
#         db_table = "cart"
#
#     def __str__(self):
#         return self.user.full_name
#
#
# class CartItem(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField(default=1)
#     price_ht = models.FloatField(blank=True)
#     cart = models.ForeignKey('Cart', on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.product.name + " " + str(self.quantity)

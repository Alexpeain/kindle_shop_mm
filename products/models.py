from django.db import models


class DeviceModel(models.Model):
    """Stores all supported e-reader models"""
    BRAND_CHOICES = [
        ('kindle', 'Amazon Kindle'),
        ('kobo', 'Kobo'),
        ('boox', 'Boox'),
        ('bigme', 'Bigme'),
    ]

    brand = models.CharField(max_length=20, choices=BRAND_CHOICES)
    name = models.CharField(max_length=100)  # e.g. "Kindle Paperwhite 7\" (2024)"
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['brand', 'name']

    def __str__(self):
        return f"{self.get_brand_display()} - {self.name}"


class Product(models.Model):
    BRAND_CHOICES = [
        ('kindle', 'Amazon Kindle'),
        ('kobo', 'Kobo'),
        ('boox', 'Boox'),
        ('bigme', 'Bigme'),
    ]

    name = models.CharField(max_length=200)
    full_title = models.CharField(max_length=500, blank=True, help_text="Longer title displayed below the main name")
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    brand = models.CharField(
        max_length=20,
        choices=BRAND_CHOICES,
        default='kindle'
    )
    # One product can be compatible with MULTIPLE models
    compatible_models = models.ManyToManyField(
        DeviceModel,
        blank=True,
        related_name='products'
    )
    price_ks = models.PositiveIntegerField(help_text="Price in MMK")
    original_price_ks = models.PositiveIntegerField(default=0)
    image_url = models.URLField(blank=True)
    delivery_days = models.PositiveIntegerField(default=14)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['brand', 'name']

    def __str__(self):
        return f"{self.get_brand_display()} | {self.name}"

    @property
    def discount_percent(self):
        if self.original_price_ks > self.price_ks:
            return int(((self.original_price_ks - self.price_ks) / self.original_price_ks) * 100)
        return 0

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='product_images/')
    order = models.PositiveIntegerField(default=0)

class PreOrder(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
        related_name="preorders"
    )
    # Customer selects which model they want
    device_model = models.ForeignKey(
        DeviceModel,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name="preorders"
    )
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=30)
    address = models.TextField()
    quantity = models.PositiveIntegerField(default=1)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.full_name} - {self.product.name} ({self.device_model}) x{self.quantity}"
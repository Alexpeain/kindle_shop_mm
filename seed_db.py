import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kindle_shop.settings')
django.setup()

from products.models import Product

def seed():
    products = [
        {
            "name": "Van Gogh Starry Night Kindle Case",
            "slug": "van-gogh-starry-night",
            "description": "A beautiful protective case featuring Van Gogh's Starry Night masterpiece.",
            "price_ks": 25000,
            "image_url": "https://images.unsplash.com/photo-1541185933-ef5d8ed016c2?w=500",
            "is_active": True,
        },
        {
            "name": "Cyberpunk Neon City Kindle Case",
            "slug": "cyberpunk-neon-city",
            "description": "Vibrant cyberpunk aesthetics for your Kindle Paperwhite.",
            "price_ks": 28000,
            "image_url": "https://images.unsplash.com/photo-1605810230434-7631ac76ec81?w=500",
            "is_active": True,
        },
        {
            "name": "Minimalist Marble Kindle Case",
            "slug": "minimalist-marble",
            "description": "Elegant and clean marble texture for a sophisticated look.",
            "price_ks": 22000,
            "image_url": "https://images.unsplash.com/photo-1563290231-36d758960682?w=500",
            "is_active": True,
        }
    ]

    for p_data in products:
        product, created = Product.objects.get_or_create(
            slug=p_data["slug"],
            defaults=p_data
        )
        if created:
            print(f"Created product: {product.name}")
        else:
            print(f"Product already exists: {product.name}")

if __name__ == "__main__":
    seed()

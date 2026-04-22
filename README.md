# Kindle Shop MM 🇲🇲

A modern, responsive e-commerce platform built with Django, specifically designed for selling Kindle cases and accessories in the Myanmar market.

## 🚀 Features

- **Dynamic Product Gallery**: High-quality product display using Swiper.js with sticky constraints to prevent layout breakage.
- **Smart Discounting**: Automated calculation and display of discount percentages based on original vs. current price.
- **Enhanced Mobile Experience**: Optimized for mobile shoppers with a sticky "Order Now" button and responsive grid layouts.
- **Comprehensive Pre-order Form**: Custom ordering system supporting specific device models (Kindle, Kobo, Boox, Bigme).
- **Clean Architecture**: Decoupled settings using environment variables and a clear app structure.

## 🛠️ Technology Stack

- **Backend**: Django 4.2
- **Database**: SQLite (Development)
- **Styling**: Vanilla CSS (Custom UI/UX)
- **Frontend Utilities**: Swiper.js (Gallery), Font Awesome / Custom Badges
- **Deployment Ready**: Configured with WhiteNoise for static file serving.

## ⚙️ Setup & Installation

### 1. Prerequisites
- Python 3.10+
- Git

### 2. Clone and Environment
```bash
# Clone the repository
git clone https://github.com/yourusername/kindle_shop_mm.git
cd kindle_shop_mm

# Create and activate virtual environment
python -m venv .venv
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configuration
Create a `.env` file in the root directory:
```env
SECRET_KEY=your-secure-secret-key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

### 5. Database Initialization
```bash
# Run migrations
python manage.py migrate

# Seed the database with sample products
python seed_db.py
```

### 6. Start the Server
```bash
python manage.py runserver
```
Visit `http://127.0.0.1:8000/` in your browser.

## 📂 Project Structure
- `kindle_shop/`: Project configuration and settings.
- `products/`: Core application handling products, images, and pre-orders.
- `product_images/`: (Ignored) Local media storage for product photos.
- `seed_db.py`: Utility script for quick environment setup.

---
*Created for portfolio demonstration purposes.*

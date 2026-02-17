# Jewelry Shop E-commerce

A fully functional e-commerce web application for a Jewelry Shop built with Django. This project allows users to browse jewelry collections, manage their cart, place orders, and manage their profile and shipping addresses.

## 🌟 Features

- **Product Management**: Browse products by category (Gifts, Rings, etc.), view detailed product information, stock status, and images.
- **Shopping Cart**: Add items to cart, adjust quantities, view total price, and remove items.
- **Order System**: streamlined checkout process with stock validation, multiple payment methods (Simulation), and order tracking.
- **User Accounts**: User registration, login, and profile management.
- **Address Management**: Users can save multiple shipping addresses.
- **Responsive Design**: Modern, responsive UI for seamless shopping on any device.

## 🛠 Tech Stack

- **Backend**: Python, Django 3.2.3
- **Database**: SQLite (Default)
- **Frontend**: HTML5, CSS3, JavaScript (Django Template Engine)
- **Image Handling**: Pillow
- **Development Tools**: VS Code

## ⚙️ Installation & Setup

1.  **Clone the repository** (if you have git set up):
    ```bash
    git clone <repository-url>
    cd django_project
    ```
    *Or simply navigate to the project directory if you have it downloaded.*

2.  **Create and Activate a Virtual Environment** (Recommended):
    ```bash
    # Windows
    python -m venv venv
    venv\Scripts\activate

    # macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run Database Migrations**:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5.  **Create a Superuser** (Access Admin Panel):
    ```bash
    python manage.py createsuperuser
    ```

6.  **Run the Development Server**:
    ```bash
    python manage.py runserver
    ```

7.  **Access the Application**:
    - **Storefront**: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
    - **Admin Panel**: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

## 📂 Project Structure

```
django_project/
├── jewelryshop/        # Project configuration (settings, urls, etc.)
├── store/              # Main application logic
│   ├── migrations/     # Database migrations
│   ├── models.py       # Data models (Product, Category, Order, Cart, etc.)
│   ├── views.py        # Application logic and views
│   ├── urls.py         # URL routing for the store
│   └── forms.py        # Django forms
├── templates/          # HTML Templates
│   ├── base.html       # Base template
│   ├── store/          # Store templates (index, product details, cart, etc.)
│   └── account/        # User account templates (login, register, profile)
├── media/              # User-uploaded content (Product images)
├── static/             # Static files (CSS, JS, Images)
├── db.sqlite3          # SQLite Database file
├── requirements.txt    # Project dependencies
└── manage.py           # Django command-line utility
```

## 📝 Usage

1.  **Register a new account** or login.
2.  **Browse Categories** like "Gifts" or "Rings" from the navigation menu.
3.  **Add Products** to your cart.
4.  **Proceed to Checkout**, select a shipping address, and choose a payment method.
5.  **View Orders** in the "Orders" section of your profile.

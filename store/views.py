import django
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Address, Cart, Order, Product
from django.views import View
from django.contrib.auth.models import User
from .forms import RegistrationForm, AddressForm

def home(request):
    # Display homepage with products
    products = Product.objects.all()
    return render(request, 'store/index.html', {'products': products})

def shop(request):
    products = Product.objects.all()
    return render(request, 'store/shop.html', {'products': products})

def detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'store/detail.html', {'product': product})

def all_categories(request):
    categories = Product.objects.values_list('category', flat=True).distinct()
    return render(request, 'store/categories.html', {'categories': categories})

def category_products(request, slug):
    products = Product.objects.filter(category__slug=slug)
    return render(request, 'store/category_products.html', {'products': products, 'category': slug})

@login_required
def add_to_cart(request):
    user = request.user
    product_id = request.GET.get('prod_id')
    product = get_object_or_404(Product, id=product_id)
    
    # Check if product already exists in cart
    item_already_in_cart = Cart.objects.filter(product=product, user=user)
    if item_already_in_cart:
        cart_item = item_already_in_cart[0]
        cart_item.quantity += 1
        cart_item.save()
    else:
        Cart(user=user, product=product).save()
    return redirect('store:cart')

@login_required
def remove_cart(request, cart_id):
    cart_item = get_object_or_404(Cart, id=cart_id)
    cart_item.delete()
    return redirect('store:cart')

@login_required
def plus_cart(request, cart_id):
    cart_item = get_object_or_404(Cart, id=cart_id)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('store:cart')

@login_required
def minus_cart(request, cart_id):
    cart_item = get_object_or_404(Cart, id=cart_id)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('store:cart')

@login_required
def cart(request):
    user = request.user
    cart_products = Cart.objects.filter(user=user)
    amount = 0
    for p in cart_products:
        value = p.quantity * p.product.price
        amount += value
    total_amount = amount
    return render(request, 'store/cart.html', {'cart_products': cart_products, 'amount': amount, 'total_amount': total_amount})

@login_required
def checkout(request):
    user = request.user
    address_id = request.GET.get('address')
    
    address = get_object_or_404(Address, id=address_id)
    # Get all the products of User in Cart
    cart = Cart.objects.filter(user=user)
    for c in cart:
        # Check if product has enough stock
        if c.quantity > c.product.stock_quantity:
            messages.error(request, f"Sorry, only {c.product.stock_quantity} units of {c.product.title} available.")
            return redirect('store:cart')
            
        # Saving all the products from Cart to Order
        Order(user=user, address=address, product=c.product, quantity=c.quantity).save()
        
        # Update product stock
        product = c.product
        product.stock_quantity -= c.quantity
        product.save()
        
        # And Deleting from Cart
        c.delete()
    return redirect('store:orders')

@login_required
def checkout_confirm(request):
    user = request.user
    addresses = Address.objects.filter(user=user)
    cart_items = Cart.objects.filter(user=user)
    amount = 0
    for item in cart_items:
        value = item.quantity * item.product.price
        amount += value
    total_amount = amount
    return render(request, 'store/checkout.html', {
        'addresses': addresses,
        'cart_items': cart_items,
        'total_amount': total_amount
    })

@login_required
def orders(request):
    user_orders = Order.objects.filter(user=request.user)
    return render(request, 'store/orders.html', {'orders': user_orders})

@login_required
def place_order(request):
    return redirect('store:orders')

class RegistrationView(View):
    def get(self, request):
        form = RegistrationForm()
        return render(request, 'account/register.html', {'form': form})
    
    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Congratulations! Registration Successful!")
            return redirect('store:login')
        return render(request, 'account/register.html', {'form': form})

@login_required
def profile(request):
    addresses = Address.objects.filter(user=request.user)
    return render(request, 'account/profile.html', {'addresses': addresses})

class AddressView(View):
    def get(self, request):
        form = AddressForm()
        return render(request, 'account/add_address.html', {'form': form})

    def post(self, request):
        form = AddressForm(request.POST)
        if form.is_valid():
            address = form.save(commit=False)
            address.user = request.user
            address.save()
            return redirect('store:profile')
        return render(request, 'account/add_address.html', {'form': form})

@login_required
def remove_address(request, id):
    address = get_object_or_404(Address, id=id)
    address.delete()
    return redirect('store:profile')

def test(request):
    return render(request, 'store/test.html')

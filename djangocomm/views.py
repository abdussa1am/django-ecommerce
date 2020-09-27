from django.shortcuts import render , redirect
from django.shortcuts import get_object_or_404
# Create your views here.
from django.views.generic import ListView
from .models import Product , Cart , Order
from django.contrib import messages

class Home(ListView):
    model = Product
    template_name = 'home.html'

def add_to_cart(request, slug):
    item = get_object_or_404(Product, slug=slug)
    order_item, created = Cart.objects.get_or_create(
        item=item,
        user=request.user
    )
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.orderitems.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, "This item quantity was updated.")
            return redirect("http://127.0.0.1:8000/")
        else:
            order.orderitems.add(order_item)
            messages.info(request, "This item was added to your cart.")
            return redirect("http://127.0.0.1:8000/")
    else:
        order = Order.objects.create(
            user=request.user)
        order.orderitems.add(order_item)
        messages.info(request, "This item was added to your cart.")
        return redirect("mainapp:home")

def remove_from_cart(request, slug):
    item = get_object_or_404(Product, slug=slug)
    cart_qs = Cart.objects.filter(user=request.user, item=item)
    if cart_qs.exists():
        cart = cart_qs[0]
        # Checking the cart quantity
        if cart.quantity > 1:
            cart.quantity -= 1
            cart.save()
        else:
            cart_qs.delete()
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.orderitems.filter(item__slug=item.slug).exists():
            order_item = Cart.objects.filter(
                item=item,
                user=request.user,
            )[0]
            order.orderitems.remove(order_item)
            messages.info(request, "This item was removed from your cart.")
            return redirect("mainapp:home")
        else:
            messages.info(request, "This item was not in your cart")
            return redirect("mainapp:home")
    else:
        messages.info(request, "You do not have an active order")
        return redirect("core:home")
from django.db.models import Q # new


class SearchResultsView(ListView):
    model = Product
    template_name = 'home.html'

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = Product.objects.filter(
            Q(name__icontains=query)
        )
        return object_list
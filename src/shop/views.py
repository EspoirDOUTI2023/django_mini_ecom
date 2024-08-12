from django.shortcuts import render, redirect
from .models import Product, Order
from django.core.paginator import Paginator


# Create your views here.
def index(request):
    products = Product.objects.all()
    item_name = request.GET.get('item-name')
    if item_name != '' and item_name is not None:
        products =  Product.objects.filter(title__icontains = item_name)
    
    paginator = Paginator(products, 4)
    page = request.GET.get('page')
    products = paginator.get_page(page)
    return render(request, 'shop/index.html', {'products' : products})


def product_detail(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'shop/product_detail.html', {'product' : product})


def checkout(request):
    if request.method == 'POST':
        items = request.POST.get('items')
        name = request.POST.get('name')
        email = request.POST.get('email')
        amount = request.POST.get('amount')
        country = request.POST.get('country')
        city = request.POST.get('city')
        address = request.POST.get('address')
        zipcode = request.POST.get('zipcode')

        order = Order(
            items = items,
            name = name,
            email = email,
            amount = amount,
            country = country,
            city = city,
            address = address,
            zipcode = zipcode,
        )
        order.save()
        return redirect('confirmation')

    return render(request, 'shop/checkout.html')


def confirmation(request):
    #get the latest order, select the 1st in db cause i change the order of savings(check in models)
    order = Order.objects.all()[:1]

    #get the object we need in the list
    for info in order:
        data = info

    return render(request, 'shop/confirmation.html', {'data' : data})
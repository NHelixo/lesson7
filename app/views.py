from django.shortcuts import render, get_object_or_404, redirect
from app.models import Product, Review
from django.http import HttpResponse


def product_list(request):
    product = Product.objects.all()
    context = {"product_list": product}
    return render(
        request,
        template_name = 'app/product.html',
        context = context,
    )

def product_info(request, product_name):
    product = Product.objects.get(name=product_name)
    response = Review.objects.filter(product=product)
    context = {"product": product, "responses": response}
    return render(
        request,
        template_name = 'app/product_info.html',
        context = context,
    )

def user_response(request, product_name):
    product = get_object_or_404(Product, name=product_name)
    if request.method == "POST":
        name = request.POST.get("name")
        text = request.POST.get("text")
        rating = request.POST.get("rating")
        Review(product=product,
               author=name,
               text=text,
               rating=rating).save()
        
        return redirect('product_info', product_name=product.name)

    else:
        context = {"product": product}
        return render(request, 'app/product_info.html', context)

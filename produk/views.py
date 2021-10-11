from django.shortcuts import render, redirect
from api.models import Product
from produk.forms import PostingForm
# Create your views here.
def produk_view(request):
    
    if request.method == 'GET':
        produk_data = Product.objects.all()
        context = {
            'title':'Data Produk',
            'dataproduk': produk_data,
        }
    return render(request, 'produk/indexposting.html', context)

def posting(request):
    form = PostingForm()
    if request.method == "POST":
        form = PostingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('produk:product')
        else:
            print(form.errors)
            return redirect('produk:product')
    context={
        'title':'Posting Produk | Test Coding',
        'header':'Posting Produk',
        'forms':form,
    }
    return render(request, 'produk/posting.html',context)

def edit(request, id):
    data = Product.objects.get(id=id)
    dataubah = {
            'product_title': data.product_title,
            'product_desc':data.product_desc,
            'product_image':data.product_image,
            'product_price':data.product_price,
            'product_stock':data.product_stock,
            'category_id':data.category_id,
        }
    form = PostingForm(request.POST or None, request.FILES or None, initial=dataubah, instance=data)
    if request.method == "POST":
            if form.is_valid():
                form.save()
                return redirect('produk:product')
            else:
                print('salah')
                return render(request, 'produk/editposting.html', {'data':form})
    elif request.method == "GET":
        form = PostingForm(request.POST or None, request.FILES or None, initial=dataubah, instance=data)
    context={
        'title':'Edit Posting | testcoding',
        'header':'Ubah Posting',
        'gambar': data,
        'forms':form,
    }
    return render(request, 'produk/editposting.html', context)

def delete(request, id):
    if request.method == 'GET':
        Product.objects.get(id=id).delete()
    
    return redirect('produk:product')
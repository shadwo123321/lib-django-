from django.shortcuts import redirect, render , get_object_or_404 
from django.http import  HttpResponse
from .models import *
from .forms import BookForm, CategoryForm
def index(request):
    status = Status.objects.all()
    book = Books.objects.all()
    statusbook = request.GET.get('status')
    category = Category.objects.all()
    categoryID = request.GET.get('category')
    if categoryID:
        book = Books.objects.filter(category = categoryID)
    elif statusbook :
        book = Books.objects.filter(status = statusbook)

    else:
        book = Books.objects.all()

    if request.method == 'POST':
        add_book = BookForm(request.POST, request.FILES)
        if add_book.is_valid():
            add_book.save()
    if request.method == 'POST':
        add_cat = CategoryForm(request.POST)
        if add_cat.is_valid():
            add_cat.save()
    context = {
        'status':status,
        'book' : book,
        'category' : category,
        'form' : BookForm(),
        'catform': CategoryForm(),
        'st' :Status.objects.filter(id=1),
        'allbook':Books.objects.filter(active=True).count,
        'avabook':Books.objects.filter(status=4).count,
        'renbook':Books.objects.filter(status=3).count,
        'solbook':Books.objects.filter(status=2).count
    }
    return render(request , 'pages/index.html', context )


def books(request):
    statusbook = request.GET.get('status')
    category = Category.objects.all()
    categoryID = request.GET.get('category')
    if categoryID:
        book = Books.objects.filter(category = categoryID)
    elif statusbook :
        book = Books.objects.filter(status = statusbook)

    else:
        book = Books.objects.all()
    
    title = None
    if 'search_name' in request.GET:
        title = request.GET['search_name']
        if title:
            book = book.filter(title__icontains=title)

    context = {
        'book' : book,
        'category' :category,
        'catform':CategoryForm(),
        'status':Status.objects.all(),
        }
        
    return render(request, 'pages/books.html', context )

def update(request , id):
    book_id = Books.objects.get(id=id)
    if request.method == 'POST':
        book_save = BookForm(request.POST, request.FILES , instance=book_id)
        if book_save.is_valid():
            book_save.save()
            return redirect('/')
    else:
        book_save = BookForm(instance=book_id)

    context = {
        'form':book_save,
    }
    return render(request, 'pages/update.html', context )

def delete(request, id):
    book_delete = get_object_or_404(Books, id=id)
    if request.method == 'POST':
        book_delete.delete()
        return redirect('/')   
    context = {
        'book' : Books.objects.all(),
        'category' :Category.objects.all(),
        'catform':CategoryForm(),
        'status':Status.objects.all(),
        } 
    
    return render(request , 'pages/delete.html',context)


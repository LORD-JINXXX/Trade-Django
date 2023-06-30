from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from .models import Item, Category

from .forms import NewItemForm, EditItemForm


def detail(request,pk):
    item = get_object_or_404(Item,pk=pk)
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[:3]
    
    return render(request,'detail.html', {
        'item' : item,
        'related_items' : related_items
    })

@login_required    
def new(request):  
    if request.method == 'POST':
        form = NewItemForm(request.POST,request.FILES)
        
        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()
            
            return redirect('item:detail',pk=item.id)
    
    else:    
        form = NewItemForm()  
        
    return render(request,'form.html',{
        'form' : form,
        'title' : 'New Item',
    }) 
    
@login_required
def delete(request,pk):
    item = get_object_or_404(Item,pk=pk,created_by=request.user)    
    item.delete()
    
    return redirect('dashboard:dash_index')


@login_required    
def edit(request,pk):  
    item = get_object_or_404(Item,pk=pk,created_by=request.user)  
    
    if request.method == 'POST':
        form = EditItemForm(request.POST,request.FILES, instance=item)
        
        if form.is_valid():
            form.save()
            
            return redirect('item:detail',pk=item.id)
    else:    
        form = EditItemForm(instance=item)  
        
    return render(request,'form.html',{
        'form' : form,
        'title' : 'New Item',
    }) 
    
    
def browse(request):
    query = request.GET.get('query','')
    items = Item.objects.filter(is_sold = False)
    categories = Category.objects.all()
    categoryID = request.GET.get('category')
    
    if query:
        items = items.filter(name__icontains=query)
    
    if categoryID:
        items = items.filter(is_sold=False,category=categoryID).all()
    else:
        items = items.filter(is_sold=False).all()
    
    return render(request,'browse.html',{
        'items' : items,
        'query' : query,
        'categories' : categories,
        'categoryID' : categoryID,
    })
    
    
        
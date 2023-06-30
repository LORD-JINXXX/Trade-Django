from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from item.models import Item

@login_required
def dash_index(request):
    items = Item.objects.filter(created_by = request.user)
    
    return render(request,'dash_index.html',{
        'items' : items
    })

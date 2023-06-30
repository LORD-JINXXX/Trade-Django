from .models import Item

from django import forms

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['category','name','description','price','image']
    widgets = {
        'category': forms.Select(attrs={
            'class' : 'input_class'
        }),
        'name': forms.TextInput(attrs={
            'class' : 'input_class'
        }),
        'description': forms.Textarea(attrs={
            'class' : 'input_class'
        }),
        'price': forms.TextInput(attrs={
            'class' : 'input_class'
        }),
        'image': forms.FileInput(attrs={
            'class' : 'input_class'
        })
    }
    
class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name','description','price','image','is_sold']
    widgets = {
        'name': forms.TextInput(attrs={
            'class' : 'input_class'
        }),
        'description': forms.Textarea(attrs={
            'class' : 'input_class'
        }),
        'price': forms.TextInput(attrs={
            'class' : 'input_class'
        }),
        'image': forms.FileInput(attrs={
            'class' : 'input_class'
        })
    }    
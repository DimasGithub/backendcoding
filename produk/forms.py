from django import forms
from django.forms import ModelForm
from api.models import Product
from crispy_forms.helper import FormHelper
class PostingForm(ModelForm):
    class Meta:
        model = Product
        fields = ('product_title', 'product_desc', 'product_image','product_price','product_stock','category_id',)
        widgets={  
        'product_title':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Judul produk', 'style':'border-radius:20px;'}),
        'product_desc':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Deskripsi', 'style':'border-radius:20px;'}),
        'product_price':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Harga', 'style':'border-radius:20px;'}),
        'product_stock':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Stok', 'style':'border-radius:20px;'}),
        'category_id':forms.Select(attrs={'class':'form-control', 'placeholder':'Kecamatan', 'style':'border-radius:20px;'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_show_labels = False

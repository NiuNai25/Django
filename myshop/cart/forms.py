from django import forms
from orders.models import OrderItem



class CartAddProductForm(forms.Form):
 
    quantity = forms.IntegerField(min_value=1,  initial= 1, max_value= 20, 
                                      label=(''))
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)

class CartAddProductFormList(forms.Form):
    
    quantity = forms.IntegerField(label=(''),min_value=1,  initial= 1)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput) 


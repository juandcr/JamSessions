from django import forms

class ContactForm(forms.Form):
    name= forms.CharField(label='Nombre', required=True,widget=forms.TextInput(
        attrs={'class':'form-control','placeholder':'Nombre'}
        ))
    phone= forms.CharField(label='Teléfono', required=True,widget=forms.NumberInput(
        attrs={'class':'form-control','placeholder':'Teléfono'}
        ))
    email= forms.EmailField(label='Correo', required=True,widget=forms.EmailInput(
        attrs={'class':'form-control','placeholder':'Correo electrónico'}
        ))
    content=forms.CharField(label='Mensaje',required=True,widget=forms.Textarea(
        attrs={'class':'form-control','rows':5,'placeholder':'Cuéntanos, ¿cómo podemos ayudarte?'}
    ))


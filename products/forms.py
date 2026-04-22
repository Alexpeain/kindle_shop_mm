from django import forms
from .models import PreOrder, DeviceModel


class PreOrderForm(forms.ModelForm):

    def __init__(self, *args, product=None, **kwargs):
        super().__init__(*args, **kwargs)
        # Only show models compatible with this product
        if product:
            self.fields['device_model'].queryset = product.compatible_models.filter(is_active=True)
        self.fields['device_model'].empty_label = "Select your model"

    class Meta:
        model = PreOrder
        fields = ['device_model', 'full_name', 'email', 'phone', 'address', 'quantity', 'notes']
        widgets = {
            'address': forms.Textarea(attrs={'rows': 3}),
            'notes': forms.Textarea(attrs={'rows': 2}),
        }
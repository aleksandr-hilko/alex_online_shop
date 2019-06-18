from django.forms import ModelForm
from .models import Product


# Create the form class.
class ProductForm(ModelForm):
    def __init__(self, user=None, *args, **kwargs):
        self._user = user
        super().__init__(*args, **kwargs)

    def save(self, **kwargs):
        self.cleaned_data["author"] = self._user
        return Product.objects.create(**self.cleaned_data)

    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'image', 'category']

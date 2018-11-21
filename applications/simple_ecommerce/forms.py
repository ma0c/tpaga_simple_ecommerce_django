from django import forms

from . import (
    models,
    conf,
)


class Item(forms.ModelForm):
    class Meta:
        model = models.Item
        fields = '__all__'


class Order(forms.ModelForm):
    class Meta:
        model = models.Order
        fields = '__all__'


class OrderItem(forms.ModelForm):
    class Meta:
        model = models.OrderItem
        fields = '__all__'


class SingleItemOrder(forms.Form):
    item = forms.ModelChoiceField(
        queryset=models.Item.objects.all(),
        label=conf.MAIN_INPUT_LABEL,
        widget=forms.HiddenInput(),
    )
    quantity = forms.IntegerField(
        initial=1,
        label=conf.MAIN_QUANTITY_LABEL,
        widget=forms.NumberInput(
            attrs={
                "min": 1,
                "max": 10,
                "step": 1
            }
        )
    )

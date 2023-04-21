from django import forms
from .models import Payment


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ["name", "amount"]  # FIXME: 유저에게 노출되도 되는 필드만

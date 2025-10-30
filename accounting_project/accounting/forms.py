from django import forms
from django.contrib.auth.models import User
from .models import Profile, Sale, Purchase, Expense

def get_dynamic_form(model_class):
    class DynamicForm(forms.ModelForm):
        class Meta:
            model = model_class
            exclude = ['employee']
    return DynamicForm

class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ['date', 'product', 'quantity', 'price', 'total']

class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ['date', 'product', 'quantity', 'price', 'total']

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['date', 'description', 'amount']

class UserCreationForm(forms.ModelForm):
    role = forms.ChoiceField(choices=Profile.ROLE_CHOICES)

    class Meta:
        model = User
        fields = ('username', 'password')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
            profile = Profile(user=user, role=self.cleaned_data['role'])
            profile.save()
        return user

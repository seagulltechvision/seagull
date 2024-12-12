# forms.py
from django import forms

class InquiryForm(forms.Form):
    email = forms.EmailField(label="Email Address", required=True)

class CallbackForm(forms.Form):
    full_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"placeholder": "Full Name"}))
    phone = forms.CharField(max_length=15, widget=forms.TextInput(attrs={"placeholder": "Phone Number"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder": "Email Address"}))
    message = forms.CharField(widget=forms.Textarea(attrs={"placeholder": "Your Message"}))
from django import forms
from .models import NewsLetter


class NewsLetterForm(forms.ModelForm):
    class Meta:
        model = NewsLetter
        fields = ["email_text"]
        widgets = {
            "email": forms.EmailInput(attrs={
                "class": "email-write",
                "placeholder": "example@gmail.com"
            })
        }

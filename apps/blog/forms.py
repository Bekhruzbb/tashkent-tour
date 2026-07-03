from django import forms
from .models import BlogComment


class BlogCommentForm(forms.ModelForm):
    class Meta:
        model = BlogComment
        fields = ["text"]
        widgets = {
            "text": forms.Textarea(attrs={
                "class": "email-text"
            })
        }


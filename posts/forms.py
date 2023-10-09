from django import forms
from .models import Post

class PostModelForm(forms.ModelForm):
    content = forms.CharField(
        widget = forms.Textarea(
            attrs = {
                'rows': 5,
                'cols': 50,
                'placeholder': 'What are you doing?',
            }
        )
    )
    class Meta:
        model = Post
        fields = '__all__'

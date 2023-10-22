from django import forms
from .models import Post, Comment


class PostModelForm(forms.ModelForm):
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'rows': 5,
                'cols': 50,
                'placeholder': 'What are you doing?',
            }
        )
    )

    class Meta:
        model = Post
        exclude = ('user',)

class CommentModelForm(forms.ModelForm):
    content = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Leave comment here!' 
            }
        )
    )
    class Meta:
        model = Comment
        fields = ('content',)
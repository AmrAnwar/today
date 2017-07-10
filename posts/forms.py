from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    # content = forms.CharField(widget=forms.TextInput(attrs={'size': '40'}))

    class Meta:
        model = Post
        fields = [
            'content'
        ]
        widgets = {
            'content': forms.Textarea(attrs={'rows': 5, 'cols': 40})
        }

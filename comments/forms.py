from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    # comment = forms.CharField(widget=forms.TextInput(attrs={'size': '40'}))
    class Meta:
        model = Comment
        fields = [
            'content'
        ]
        widgets = {
            'content': forms.Textarea(attrs={'rows': 4, 'cols': 30}),
        }

from django import forms

from .models import Comments


class CommentForm(forms.ModelForm):
    """Форма комментария"""

    class Meta:
        model = Comments
        fields = ("name", "text")

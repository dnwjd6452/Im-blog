from django import forms
from .models import Comment, Photo

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'content',) 

class UploadForm(forms.ModelForm):
    title = forms.CharField(max_length=255)
    class Meta:
        model = Photo                         
        fields = ('image', 'author') 

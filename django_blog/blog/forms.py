from django import forms
from django.contrib.auth.models import User
from taggit.forms import TagWidget
from .models import Post, Comment

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
        widgets = {
            'tags': TagWidget(),   # 👈 REQUIRED
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

    # Optional: Custom validation rule
    def clean_content(self):
        content = self.cleaned_data.get('content')

        if not content:
            raise forms.ValidationError("Comment cannot be empty.")

        if len(content) < 3:
            raise forms.ValidationError("Comment must be at least 3 characters long.")

        return content

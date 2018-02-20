from django import forms

from .models import Post, Publication, UserProfile


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('published_date', 'title', 'text')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('title', 'avatar', 'position', 'info')

class PublicationForm(forms.ModelForm):
    class Meta:
        model = Publication
        fields = ('title', 'text_file', 'publication_date')

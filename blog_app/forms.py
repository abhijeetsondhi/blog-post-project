from django import forms
from blog_app.models import Post,Comment,UserProfileInfo

class PostForm(forms.ModelForm):

    class Meta():
        model = Post
        fields = ('title','text')

        widgets = {
        'title' : forms.TextInput(attrs = {'class':'textinputclass'}),
        'text' : forms.Textarea(attrs = {'class':'editable medium-editor-textarea postcontent'})
        }

class CommentForm(forms.ModelForm):

    class Meta():
        model = Comment
        fields = ('author','text')

        widgets = {
        'author': forms.TextInput(attrs = {'class':'textinputclass'}),
        'text' : forms.Textarea(attrs = {'class':'editable medium-editor-textarea'})
        }


class ProfileForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('profile_pic',)

from django import forms

from post.models import Post


class PostCreateModelForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('slug', 'likes', )
        widgets = {
            'body': forms.Textarea()
        }


class PostUpdateModelForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('slug', 'likes', )
        widgets = {
            'body': forms.Textarea()
            }





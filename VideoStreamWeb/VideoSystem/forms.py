from VideoSystem.models import *
from django import forms
class VideoUpload (forms.ModelForm):
    class Meta:
        model = VideoUpload
        fields = ['Video_title','Upload_Thumbnail','Video_description','Upload_video']
class CommentForm (forms.ModelForm):
    class Meta:
        model = VideoComment
        fields = ['comment']

class SearchForm(forms.Form):
    query = forms.CharField(max_length=255, label='Search')
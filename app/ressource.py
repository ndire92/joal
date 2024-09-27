
from django import forms

from app.models import Ressource, Video


class Ressou(forms.ModelForm):
    title = forms.CharField(label='Title',widget=forms.TextInput(
        attrs={'placeholder': ' ', 'style': 'border: 4px solid #1da8dd;border-radius: 10px;', 'class': 'form-control'}))
    mot_cle = forms.CharField(label=' mot clé',widget=forms.Textarea(attrs={'placeholder': ' ', 'style': 'border: 4px solid #1da8dd;border-radius: 10px;', 'class': 'form-control'}))
    
    date_en=  forms.CharField(widget=forms.DateInput(attrs={'type': 'date','style': 'width: 300px;border: 4px solid #1da8dd;border-radius: 10px;', 'class': 'form-control'}))
   
    action =forms.FileField()
    
    
    class Meta:
        model = Ressource
        fields = ('title','mot_cle','date_en','action')




class Video_form(forms.ModelForm):
    title = forms.CharField(label='Title',widget=forms.TextInput(
        attrs={'placeholder': ' ', 'style': 'border: 4px solid #1da8dd;border-radius: 10px;', 'class': 'form-control'}))
    date_en=  forms.CharField(widget=forms.DateInput(attrs={'type': 'date','style': 'border: 4px solid #1da8dd;border-radius: 10px;', 'class': 'form-control'}))
    video =forms.FileField()
    
    class Meta:
        model=Video
        fields=("title","date_en","video")
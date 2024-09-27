
from django import forms
from .models import Post, UserProfile,Video
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


User = get_user_model()



class SignUpForm(UserCreationForm):
    username = forms.CharField(
        label='Utilisateur',
        widget=forms.TextInput(attrs={'placeholder': '', 'class': 'form-control'}),
        error_messages={
            'unique': "Ce nom d'utilisateur est déjà utilisé. Veuillez en choisir un autre.",
        }
    )
    password1 = forms.CharField(
        label='Mot de passe',
        widget=forms.PasswordInput(attrs={'placeholder': '', 'class': 'form-control'}),
        error_messages={
            'min_length': "Le mot de passe doit contenir au moins 8 caractères.",
            'password_entirely_numeric': "Le mot de passe ne peut pas être entièrement numérique.",
        }
    )
    password2 = forms.CharField(
        label='Confirmer le mot de passe',
        widget=forms.PasswordInput(attrs={'placeholder': '', 'class': 'form-control'}),
        error_messages={
            'password_mismatch': "Les mots de passe ne correspondent pas.",
        }
    )
    role = forms.ChoiceField(
        choices=(('decideur', 'Décideur'), ('gestionnaire', 'Gestionnaire')),
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Role'
    )

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({'style': 'color: black'})

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'role')

    def clean_username(self):
        username = self.cleaned_data.get('username')

        if User.objects.filter(username=username).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError(
                self.fields['username'].error_messages['unique']
            )

        return username

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')

        if len(password1) < 8:
            raise forms.ValidationError(
                self.fields['password1'].error_messages['min_length']
            )

        if password1.isdigit():
            raise forms.ValidationError(
                self.fields['password1'].error_messages['password_entirely_numeric']
            )

        return password1

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.fields['password2'].error_messages['password_mismatch']
            )

        return password2

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')

        if password1 and not any(char.isdigit() for char in password1):
            raise forms.ValidationError(
                self.fields['password1'].error_messages['password_entirely_numeric']
            )

        return cleaned_data


class PostForm(forms.ModelForm):

    title = forms.CharField(label='Titre',widget=forms.TextInput(
        attrs={'placeholder': ' ', 'style': 'width: 350px;border: 4px solid #1da8dd;border-radius: 10px;', 'class': 'form-control'}))

    content = forms.CharField(label='Contenu', widget=forms.Textarea(attrs={'style': 'border: 4px solid #1da8dd;border-radius: 10px;',
        'class': 'form-control'
    }))
    
    date_en=  forms.CharField(widget=forms.DateInput(attrs={'type': 'date','style': 'width: 300px;', 'class': 'form-control'}))
   
    class Meta:
        model = Post
        fields = ('title', 'content', 'image','date_en')
		
class VideoForm(forms.ModelForm):
    title = forms.CharField(label='Titre de la Vidéo', widget=forms.TextInput(
        attrs={'placeholder': 'Titre', 'style': 'border: 4px solid #1da8dd;', 'class': 'form-control'}))
    date_en = forms.DateField(label='Date de la Vidéo', widget=forms.DateInput(
        attrs={'type': 'date', 'style': 'border: 4px solid #1da8dd;', 'class': 'form-control'}))

    class Meta:
        model = Video
        fields = ['title', 'date_en', 'video']


class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(label='Prénom', widget=forms.TextInput(
        attrs={'placeholder': ' ', 'style': 'width: 800px;border: 1px solid #1da8dd; border-radius: 10px;', 'class': 'form-control'}))
    last_name = forms.CharField(label='Nom', widget=forms.TextInput(
        attrs={'placeholder': ' ', 'style': 'width: 800px;border: 1px solid #1da8dd; border-radius: 10px;', 'class': 'form-control'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(
        attrs={'placeholder': ' ', 'style': 'width: 800px;border: 1px solid #1da8dd; border-radius: 10px;', 'class': 'form-control'}))
    description = forms.CharField(label='description', widget=forms.TextInput(
        attrs={'placeholder': ' ', 'style': 'width: 800px;border: 1px solid #1da8dd; border-radius: 10px;', 'class': 'form-control'}))
    phone_number = forms.CharField(label='Tel', widget=forms.NumberInput(
        attrs={'placeholder': ' ', 'style': 'width: 800px;border: 1px solid #1da8dd; border-radius: 10px;', 'class': 'form-control'}))
    address = forms.CharField(label='address', widget=forms.TextInput(
        attrs={'placeholder': ' ', 'style': 'width: 800px;border: 1px solid #1da8dd; border-radius: 10px;', 'class': 'form-control'}))
    profile_picture =forms.FileField()

    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'email', 'description',
                  'phone_number', 'address', 'profile_picture']

    def save(self, commit=True, user=None):
        profile = super(ProfileForm, self).save(commit=False)
        if user:
            profile.user = user  # Assurez-vous d'ajouter l'utilisateur s'il est fourni
        if commit:
            profile.save()
        return profile
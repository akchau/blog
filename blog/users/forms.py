from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()


class CreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')

class Feedback(forms.Form):
    subject = forms.CharField(label='Тема', required=False, label_suffix=': ', help_text='Укажите тему сообщения', max_length=200 , error_messages={'max_length': 'Превышено допустимое кол-во симоволов!'})
    message = forms.CharField(label='Письмо', widget=forms.Textarea, label_suffix=': ', help_text='Ваше сообщение', max_length=2000, error_messages={'max_length': 'Превышено допустимое кол-во симоволов!', 'required': 'Это обязятельное поле'})
    email = forms.EmailField(label='Контактый email', label_suffix=': ', help_text='Куда ответить на ваше сообшение', error_messages={'invalid': 'Некорректный email', 'required': 'Это обязятельное поле'})

class EditName(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name',)


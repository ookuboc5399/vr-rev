from django import forms


class BlogForm(forms.Form):
    title = forms.CharField(max_length=30, label='タイトル')
    content = forms.CharField(label='内容', widget=forms.Textarea())

class ContactForm(forms.Form):
    name = forms.CharField(max_length=30, label='名前')
    email = forms.EmailField(max_length=30, label='メールアドレス')
    message = forms.CharField(label='メッセージ', widget=forms.Textarea())


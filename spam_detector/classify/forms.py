from django import forms

class EmailForm(forms.Form):
    email_text=forms.CharField(widget=forms.Textarea, label='Paste your email here', max_length=10000)
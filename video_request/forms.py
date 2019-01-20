from django import forms


class VideoForm(forms.Form):
    video_name = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Name',
            'id': 'inputName'
        }))

    video_desc = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': '5',
            'id': 'comment',
            'placeholder': 'Comment'
        }))

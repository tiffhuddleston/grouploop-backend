from django import forms
from .models import Circle, Member


class CircleForm(forms.ModelForm):
    class Meta:
        model = Circle
        fields = ('title', 'description', 'member')


class MemberForm(forms.ModelForm):

    github = models.TextField(required=False)
    facebook = models.TextField(required=False)
    instagram = models.TextField(required=False)
    linkedin = models.TextField(required=False)
    twitter = models.TextField(required=False)

    class Meta:
        model = Member
        fields = ('github', 'linkedin', 'twitter', 'instagram', 'facebook')

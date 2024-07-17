from django import forms

from myapp.models import movie


class MovieForm(forms.Form):

    title=forms.CharField( widget=forms.TextInput(attrs={"class":"form-control border border-info"}))

    year=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control border border-info"}))

    director=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control border border-info"}))

    run_time=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control border border-info"}))

    language=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control border border-info"}))

    genre=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control border border-info"}))

    producer=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control border border-info"}))



class MovieModelForm(forms.ModelForm):

    class Meta:

        model=movie

        fields="__all__"

        model:movie
        exclude=("id",)


from django import forms
from . models import Client, NewFaultReport

ch = [
    ('request','Request'),
    ('enquiry','Enquiry')
]


class PostForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.TextInput(attrs={'class': 'form-control'}),
            'title': forms.Select(choices=ch, attrs={'class': 'form-control'}),

        }


class DescripDetForm(forms.ModelForm):
    class Meta:
        model = NewFaultReport
        fields = '__all__'

        widgets = {
            'Subject_Title': forms.Textarea(attrs={  "rows":3, "cols":30, "placehoder":'Enter Title'}),
            'description': forms.Textarea(attrs={ "rows":3, "cols":30}),
            'date_created': forms.DateInput(attrs={"rows":1, "cols":30}),
            'time': forms.TimeInput(attrs={"rows":1, "cols":30}),
         }
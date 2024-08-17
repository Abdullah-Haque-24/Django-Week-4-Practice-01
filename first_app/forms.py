from django import forms
from .models import MyModel

class MyForm(forms.ModelForm):
    class Meta:
        model = MyModel
        fields = "__all__"
    name = forms.CharField()
    comment = forms.CharField(widget=forms.Textarea)
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
    email = forms.EmailField()
    agree = forms.BooleanField()
    date = forms.DateField()
    # birth_date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    value = forms.DecimalField()
    message = forms.CharField(max_length = 10,)
    email_address = forms.EmailField(label="Please enter your email address",)
    # day = forms.DateField(initial=datetime.date.today)

    FAVORITE_COLORS_CHOICES = [('blue', 'Blue'),('green', 'Green'),('black', 'Black'),]
    favorite_color = forms.ChoiceField(choices=FAVORITE_COLORS_CHOICES)

    FAVORITE_COLORS = [('blue', 'Blue'),('green', 'Green'),('black', 'Black'),]
    favorite_colors = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=FAVORITE_COLORS,)
    roll_number = forms.IntegerField( 
                    help_text = "Enter 6 digit roll number"
                    ) 
    password = forms.CharField(widget = forms.PasswordInput()) 
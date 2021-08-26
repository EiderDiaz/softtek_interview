from django import forms

#from just containing a boolean field to determine the dates in which the weather became bad 
# (i.e. when the weather changed from FALSE to TRUE)
# or became good 
# (i.e. when the weather changed from TRUE to FALSE)
class WeatherChangeForm(forms.Form):
    is_good_to_bad = forms.BooleanField(required=False, widget=forms.CheckboxInput)

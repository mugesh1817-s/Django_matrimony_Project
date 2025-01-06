from django import forms
from myapp.models import Image

class Imageform(forms.ModelForm):
	class Meta:
		model = Image
		fields = "__all__"
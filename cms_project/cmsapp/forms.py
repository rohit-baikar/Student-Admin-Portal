from .models import DeptModel, StudentModel
from django import forms


class DeptForm(forms.ModelForm):
    class Meta:
        model = DeptModel
        fields = "__all__"


class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentModel
        fields = "__all__"

class SpForm(forms.Form):
	ms1 = forms.FileField(label="Select Marksheet 1(pdf_file)")
	ms2 = forms.FileField(label="Select Marksheet 2(pdf_file)")


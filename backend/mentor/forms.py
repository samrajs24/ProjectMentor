from django import forms
from .models import LearningItem

class LearningItemForm(forms.ModelForm):
    class Meta:
        model = LearningItem
        fields = ['title', 'profile_picture', 'name', 'description', 'attachments', 'start_time', 'end_time', 'book_a_slot']

    def __init__(self, *args, **kwargs):
        super(LearningItemForm, self).__init__(*args, **kwargs)
        self.fields['attachments'].widget.attrs['multiple'] = True  # Allow multiple attachments
        self.fields['start_time'].widget.attrs['class'] = 'datepicker'  # Add class for datepicker
        self.fields['end_time'].widget.attrs['class'] = 'datepicker'    # Add class for datepicker

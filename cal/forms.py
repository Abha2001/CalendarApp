from django.forms import ModelForm,DateInput
from cal.models import Event
from django.contrib.auth.models import User

class EventForm(ModelForm):
	class Meta:
		model=Event
		widgets={
		'day':DateInput(attrs={'type':'datetime-local'},format='%Y-%m-%d'),
		'start_time':DateInput(attrs={'type':'datetime-local'},format='%H:%M:%S'),
		'end_time':DateInput(attrs={'type':'datetime-local'},format='%H:%M:%S')
		}

		fields=['day','start_time','end_time','notes']

	def save(self, user_id ,commit=True):
		form = super(EventForm, self).save(commit=False)
		form.name = User.objects.get(pk=user_id)
		if commit:
			form.save()
			return form

		self.fields['day'].input_formats=('%Y-%m-%d',)
		self.fields['start_time'].input_formats=('%H:%M:%S',)
		self.fields['end_time'].input_formats=('%H:%M:%S',)
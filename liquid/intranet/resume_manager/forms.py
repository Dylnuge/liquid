from django.forms import ModelForm, CharField
from intranet.models import Resume, Recruiter
from utils.widgets import BootstrapDateInput
from django.forms.models import modelformset_factory

ResumeFormSet = modelformset_factory(Resume,fields = ['approved'],can_delete=True,extra=0)

class RecruiterForm(ModelForm):
   first_name = CharField(label="Company Name")
   username = CharField(label="Username")
   class Meta:
      model = Recruiter
      widgets = {'expires': BootstrapDateInput}
      fields = ('first_name', 'username', 'email', 'expires')

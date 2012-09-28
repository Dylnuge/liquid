from django import template
from intranet.models import Job
register = template.Library()

@register.filter
def pk_to_company(id):
   j = Job.objects.get(pk=id)
   return j.company

@register.filter
def pk_to_types(id):
   j = Job.objects.get(pk=id)
   return j.types()

@register.filter
def pk_to_contact(id):
   j = Job.objects.get(pk=id)
   return j.contact_name + " <" + j.contact_email + ">"

@register.filter
def pk_to_phone(id):
   j = Job.objects.get(pk=id)
   return j.contact_phone
   
@register.filter
def pk_to_title(id):
   j = Job.objects.get(pk=id)
   return j.job_title

@register.filter
def pk_to_description(id):
   j = Job.objects.get(pk=id)
   description =  j.description
   return description

@register.filter
def pk_to_postdate(id):
   j = Job.objects.get(pk=id)
   timestamp =  j.timestamp
   return timestamp
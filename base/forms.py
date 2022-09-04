from dataclasses import field
from turtle import textinput
from xml.dom.minidom import Attr
from django import forms
from django.forms import ModelForm 
from .models import BookTable

class BookTableForm(forms.Form):
  Name = forms.CharField(
    max_length = 255,
    widget = forms.TextInput(
      attrs = {
        'class':'form-control',
        'placeholder':'Your Name',
        'name':'name',
        'id':'name'
      }
    )
  )
  Email = forms.EmailField(
    widget = forms.TextInput(
      attrs = {
        'class':'form-control',
        'placeholder':'Your Email',
        'name':'email',
        'id':'email'
      }
    )
  )
  Phone = forms.CharField(
    max_length = 13,
    widget = forms.TextInput(
      attrs = {
        'class':'form-control',
        'placeholder':'Your Phone Number',
        'name':'phone',
        'id':'phone'
      }
    )
  )
  Date = forms.CharField(
    max_length = 13,
    widget = forms.TextInput(
      attrs = {
        'class':'form-control',
        'placeholder':'Date',
        'name':'date',
        'id':'date'
      }
    )
  )
  Time = forms.CharField(
    max_length = 50,
    widget = forms.TextInput(
      attrs = {
        'class':'form-control',
        'placeholder':'Time',
        'name':'time',
        'id':'time'
      }
    )
  )
  ManyPeople = forms.CharField(
    max_length = 100,
    widget = forms.TextInput(
      attrs = {
        'class':'form-control',
        'placeholder':'# of people',
        'name':'people',
        'id':'people'
      }
    )
  )
  Message = forms.CharField(
    widget = forms.Textarea(
      attrs = {
        'class':'form-control',
        'placeholder':'Message',
        'name':'message',
        'id':'message',
        'style': 'background-color: #0c0b09; color: #625b4b; border: 3px solid #625b4b'
      }
    )
  )

class ContactUsForm(forms.Form):
  Name = forms.CharField(
    max_length = 255,
    widget = forms.TextInput(
      attrs = {
        'class':'form-control',
        'placeholder':'Your Name',
        'name':'name',
        'id':'name'
      }
    )
  )
  Email = forms.EmailField(
    widget = forms.TextInput(
      attrs = {
        'class':'form-control',
        'placeholder':'Your Email',
        'name':'email',
        'id':'email'
      }
    )
  )
  Subject = forms.CharField(
    max_length = 255,
    widget = forms.TextInput(
      attrs = {
        'class':'form-control',
        'placeholder':'Subject',
        'name':'subject',
        'id':'subject'
      }
    )
  )
  Message = forms.CharField(
    widget = forms.Textarea(
      attrs = {
        'class':'form-control',
        'placeholder':'Message',
        'name':'message',
        'id':'message',
        'style': 'background-color: #0c0b09; color: #625b4b; border: 3px solid #625b4b'
      }
    )
  )
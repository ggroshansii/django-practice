from re import I
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

def monthly_challenge(request, month):
    text = None
    if month == "january":
       text = "JANUARY" 
    elif month == "february":
        text = "FEBRUARY" 
    elif month == "march":
        text = "MARCH" 
    elif month == "april":
        text = "APRIL" 
    elif month == "may":
        text = "MAY" 
    elif month == "june":
        text = "JUNE" 
    elif month == "july":
        text = "JULY" 
    elif month == "august":
        text = "AUGUST" 
    elif month == "september":
        text = "SEPTEMBER" 
    elif month == "november":
        text = "NOVEMBER" 
    elif month == "december":
        text = "DECEMBER" 
    else:
        return HttpResponseNotFound("This month not supported")
    return HttpResponse(text)
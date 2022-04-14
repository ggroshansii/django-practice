from operator import truediv
from re import I
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

months = [
    {"january": "this is january"},
   { "february": "this is february"},
    {"march": "this is march"},
   { "april": "this is april"},
    {"may": "this is may"},
    {"june": "this is june"},
    {"july": "this is july"},
    {"august": "this is august"},
    {"september": "this is september"},
    {"october": "this is october"},
    {"november": "this is november"},
    {"december": "this is december"},
]

def monthly_challenge_number(request, month):
    test = month - 1
    try:
        return HttpResponse(months[test])
    except:
        return HttpResponseNotFound("This month not supported")

def monthly_challenge_string(request, month):
    
    def filter_month(a_month):
        print("fired")
        if a_month[month]: 
            return True
        else:
            return False
    # try:
    month_filter = list(filter(filter_month, months))

    print()
    return HttpResponse("month_filteHr")
    # except:
    #     return HttpResponseNotFound("This month not supported")

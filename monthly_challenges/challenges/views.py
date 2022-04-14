from re import I
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

# Create your views here.

months = {
    "january": "this is january",
    "february": "this is february",
    "march": "this is march",
    "april": "this is april",
    "may": "this is may",
    "june": "this is june",
    "july": "this is july",
    "august": "this is august",
    "september": "this is september",
    "october": "this is october",
    "november": "this is november",
    "december": "this is december"
}

def monthly_challenge_number(request, month):
    try:
        keys = list(months.keys())
        forward_month = keys[month-1]
        return HttpResponseRedirect("/challenges/" + forward_month)
    except:
        return HttpResponseNotFound("This month not supported")

def monthly_challenge_string(request, month):
    try:
        return HttpResponse(months[month])
    except:
        return HttpResponseNotFound("This month not supported")

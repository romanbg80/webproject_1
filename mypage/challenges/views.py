from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

monthly_challenges = {
    "january": "Eat no meat",
    "february": "Walk for 20 minutes",
    "march": "Learn django",
    "april": "Eat no meat",
    "may": "Walk for 20 minutes",
    "june": "Learn django",
    "july": "Eat no meat",
    "august": "Walk for 20 minutes",
    "september": "Learn django",
    "october": "Eat no meat",
    "november": "Walk for 20 minutes",
    "december": "Learn django"
}

# Create your views here.


def monthly_challenge_by_number(request, month):
    return HttpResponse(month)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("not a month")




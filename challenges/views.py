from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse


monthly_challenges={
    "january":"Minimize unnecessary screen times.",
    "feburary":"Walk for 30 mins a day.",
    "march":"Learn Django for 1 hour daily.",
    "april":'Eat healthy food and avoid the junk ones.',
    "may":"Go out hiking once a week.",
    "june":"Try some new food cusines.",
    "july":"Learn some new skills.",
    "august":"Go out to new places far away.",
    "september":"Buy some new threads.",
    "october":"Try some new games",
    "november":"Make some new dishes",
    "december":"Have some great time with family and friends.",
}


def index(request):
    months =list(monthly_challenges.keys())
    return render(request, "challenges/index.html", {
        "months": months,
    })


def monthly_challenge_by_number(request, month):
    if month > 0 and month <= len(monthly_challenges):
        months = list(monthly_challenges.keys())
        redirect_month = months[month - 1]
        redirect_path = reverse('monthly-challenge', args=[redirect_month])
        return HttpResponseRedirect(redirect_path)
    else:
        return HttpResponse(f"<h1>Enter a valid month.</h1>")


def monthly_challenge(request, month):
    challenge_text = None
    try:
        challenge_text=monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month_name": month,
        })
    except:
        raise Http404()
    
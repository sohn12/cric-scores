from django.shortcuts import render
from django.http import JsonResponse, HttpResponseBadRequest
from pycricbuzz import Cricbuzz

c = Cricbuzz()

# Create your views here.
def all_matches(request):
    try:
        matches = c.matches()
        return JsonResponse({"data": matches})
    except:
        return HttpResponseBadRequest("Error occurred")


def match_scores(request, mid):
    try:
        info = c.livescore(mid)
        return JsonResponse({"data": info})
    except:
        return HttpResponseBadRequest("Error occurred")


# def match_info
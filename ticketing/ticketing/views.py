
from django.shortcuts import render, HttpResponse

from ticketing.models import Ticket
import random
import string

def randomString(stringLength=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


def index(request):
    return render(request,"ticketing/index.html")

def submit(request):
    if request.method == "POST":
        username = request.POST.get("username")
        body = request.POST.get("body")
        new_ticket = Ticket(submitter=username, body=body)
        new_ticket.save()
        return HttpResponse("Succesfully submitted ticket!")
    return render(request,"ticketing/submit.html")

def tickets(request):
    all_tickets = Ticket.objects.all()
    return render(request,"ticketing/tickets.html", {'tickets': all_tickets})
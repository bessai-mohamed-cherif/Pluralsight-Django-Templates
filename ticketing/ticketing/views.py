
from django.shortcuts import render

from ticketing.models import Ticket
import random
import string

def randomString(stringLength=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


def index(request):
    return render(request,"ticketing/index.html")

def submit(request):
    new_ticket = Ticket(submitter=randomString(), body="Help!")
    new_ticket.save()
    return render(request,"ticketing/submit.html")

def tickets(request):
    all_tickets = Ticket.objects.all()
    return render(request,"ticketing/tickets.html", {'tickets': all_tickets})
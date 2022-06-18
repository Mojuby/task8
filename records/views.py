from django.shortcuts import render
from .forms import InfoForm
from .models import Cust_Info
# Create your views here.

def reservations(request):
    booked_rooms = Cust_Info.objects.all()
    return render(request, 'records/reservations.html',{'booked_rooms':booked_rooms})

def book_a_room(request):
    form = InfoForm()
    if request.method == 'POST':
        form = InfoForm(request.POST)
        if form.is_valid():
            form.save()
        return reservations(request)
    return render(request, 'records/book_a_rooom.html',{'form':form})

from django.shortcuts import render, redirect
from efinalapp.models import Contact, Myregister, Inquiry, Booking, House, Management
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def agent(request):
    return render(request,'agents.html')
def register(request):
    if request.method == 'POST':
        myregistrer = Myregister(
            username = request.POST['username'],
            email = request.POST['email'],
            password = request.POST['password'],
        )
        myregistrer.save()
        return redirect('login')
    else:
        return render(request, 'registration.html')
def login_view(request):
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            print(f"POST data received:username={username}, password={password}")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                print("Invalid login or password")
                return render(request,'login.html',{'error':'Invalid username or password'})
        else:
            print("GET request,rendering login form")
            return render(request,'login.html')

def contact(request):
    if request.method == "POST":
        mycontact = Contact(
            name = request.POST.get('name'),
            phone = request.POST.get('phone'),
            email = request.POST.get('email'),
            message = request.POST.get('message'),
        )
        mycontact.save()
        return redirect('/contact')
    else:
        return render(request,'contact.html')

def community(request):
    return render(request,'community.html')
def services(request):
    return render(request,'service.html')
def home(request):
    houses = House.objects.all()
    return render(request, 'home.html', {'houses': houses})

@login_required
def book_house(request, house_id):
    house = House.objects.get(id=house_id)
    Booking.objects.create(user=request.user, house=house)
    return redirect('home')

@login_required
def view_bookings(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'bookings.html', {'bookings': bookings})

@login_required
def delete_booking(request, booking_id):
    booking = Booking.objects.get(id=booking_id)
    if booking.user == request.user:
        booking.delete()
    return redirect('view_bookings')

def post_inquiry(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        Inquiry.objects.create(name=name, email=email, message=message)
        return redirect('post_inquiry')
    return render(request, 'inquiry.html')
def base(request):
    return render(request,'base.html')


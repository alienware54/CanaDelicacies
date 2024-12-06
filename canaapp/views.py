import json

import requests
from django.http import HttpResponse
from django.shortcuts import render,redirect
from requests.auth import HTTPBasicAuth

from canaapp.credentials import MpesaAccessToken, LipanaMpesaPpassword
from canaapp.models import Reservation, User, ImageModel, Manager
from canaapp.models import Contact
from canaapp.forms import ReservationForm, ImageUploadForm


# Create your views here.
def index(request):
   if request.method == 'POST':
       if User.objects.filter(
           username=request.POST['username'],
           password=request.POST['password']
       ).exists():
           return render(request,'index.html')
       else:
           return render(request,'login.html')
   else:return render(request,'login.html')



def starter(request):
    return render(request,'starter-page.html')

def about(request):
    return render(request,'about.html')


def menu(request):
    return render(request,'menu.html')

def make(request):
    return render(request,'make.html')



def specials(request):
    return render(request,'specials.html')

def events(request):
    return render(request,'events.html')

def chefs(request):
    return render(request,'chefs.html')

def gallery(request):
    return render(request,'gallery.html')

def contact(request):
    return render(request,'contact.html')

def received(request):
    return render(request,'received.html')


def thanks(request):
    return render(request,'thanks.html')

def rooms(request):
    return render(request,'rooms.html')

def reservations(request):
    if request.method == 'POST':
        # Save the reservation data
        myreservations = Reservation(
            name=request.POST['name'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            date=request.POST['date'],
            room=request.POST['room'],
            message=request.POST['message']
        )
        myreservations.save()


        return render(request, 'thanks.html')

    return render(request, 'reservations.html')


def show(request):
    allreservation=Reservation.objects.all()
    return render(request,'show.html',{'reservation':allreservation})

def delete(request,id):
    reserve=Reservation.objects.get(id=id)
    reserve.delete()
    return redirect('/show')


def contact(request):
    if request.method == 'POST':
        mycontact=Contact(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            email=request.POST['email'],
            message=request.POST['message']

        )
        mycontact.save()

        return render(request, 'received.html')

    return render(request, 'contact.html')


def edit(request,id):
    editreserve=Reservation.objects.get(id=id)
    return render(request,'edit.html',{'reservation':editreserve})

def update(request,id):
    updateinfo =Reservation.objects.get(id=id)
    form=ReservationForm(request.POST,instance =updateinfo)
    if form.is_valid():
        form.save()
        return redirect('/show')
    else:
        return render(request,'edit.html')


def register(request):
    if request.method == 'POST':
         members = User(
            username=request.POST['username'],
            name=request.POST['name'],
            password=request.POST['password']
        )
         members.save()
         return redirect('/login')
    else:
        return render(request,'register.html')




def login(request):
    return render(request,'login.html')



def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/showimage')
    else:
        form = ImageUploadForm()
    return render(request, 'upload_image.html', {'form': form})



def show_image(request):
    images = ImageModel.objects.all()
    return render(request, 'show_image.html', {'images': images})

def token(request):
    consumer_key = 'aIVPIcFkuTM8xUPJUa2HcW5oNlmhhkNntNqoan2FDpfsrnn7'
    consumer_secret = 'Ob8V1xVCbUGaginAnhGWJQC6Rv23L6wJS2mGbOsqNkBn7mnyaVulDcTT7rJAMulp'
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'

    r = requests.get(api_URL, auth=HTTPBasicAuth(
        consumer_key, consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token["access_token"]

    return render(request, 'token.html', {"token":validated_mpesa_access_token})

def pay(request):
   return render(request, 'pay.html')



def stk(request):
    if request.method =="POST":
        phone = request.POST['phone']
        amount = request.POST['amount']
        access_token = MpesaAccessToken.validated_mpesa_access_token
        api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
        headers = {"Authorization": "Bearer %s" % access_token}
        request = {
            "BusinessShortCode": LipanaMpesaPpassword.Business_short_code,
            "Password": LipanaMpesaPpassword.decode_password,
            "Timestamp": LipanaMpesaPpassword.lipa_time,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": amount,
            "PartyA": phone,
            "PartyB": LipanaMpesaPpassword.Business_short_code,
            "PhoneNumber": phone,
            "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",
            "AccountReference": "cana delicacies",
            "TransactionDesc": "Web Development Charges"
        }
        response = requests.post(api_url, json=request, headers=headers)
        return HttpResponse("Success")







def manager(request):
    if request.method == 'POST':
        workers = Manager(
            username=request.POST['username'],
            name=request.POST['name'],
            password=request.POST['password']

        )
        workers.save()
        return redirect('cana')
    else:
        return render(request,'manager.html')


def cana(request):
   return render(request, 'cana.html')



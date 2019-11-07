import twitter
import facebook
from django.shortcuts import render
from django.db import connection
from django.shortcuts import redirect
from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect
from django.conf import settings
from django.contrib.auth.decorators import login_required
from donation.models import donatemoney,donatevaluables
from donation.forms import donatemoneyform,donatevaluablesform
from paypal.standard.forms import PayPalPaymentsForm
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def donatemoneyview(request):
    if request.method =='POST':
        print('a')
        user_name = request.POST.get('user_name')
        transfer = request.POST.get('transfer')
        amount = request.POST.get('amount')
        orphanage=request.POST.get('orphanage')
        description= request.POST.get('description')
        saveform = donatemoney.objects.create(user_name=user_name,transfer=transfer, amount=amount,orphanage=orphanage,description=description)
        saveform.save()
        print(orphanage)
        tid=donatemoney.objects.latest('tid')
        tidstring=tid.tid
        print(tidstring)
        user_name.replace(" ", "9")
        if transfer=="paypal":
            user_name.replace(" ", "9")
            return HttpResponseRedirect(reverse('donation:inprogress',args=(tidstring,amount,user_name,orphanage)))
    else:
        form = donatemoneyform()
    return render(request,'donation/money.html',{'form': form})

def donation_completedview(request):
    return render(request,'donation/donation_completed.html')


def donatevaluablesview(request):
    if request.method =='POST':
        user_name=request.POST.get('user_name')
        type=request.POST.get('type')
        weight=request.POST.get('weight')
        length=request.POST.get('length')
        width =request.POST.get('width')
        height =request.POST.get('height')
        breadth =request.POST.get('breadth')
        description= request.POST.get('description')
        status='0'
        saveform = donatevaluables.objects.create(user_name=user_name,donation_type=type,weight=weight,height=height,length=length,breadth=breadth,description=description,status=status)
        saveform.save()
        return HttpResponseRedirect(reverse('donation:completed'))
    else:
        form = donatevaluablesform()
        return render(request, 'donation/valuables.html',{'form': form})

def paypal_home(request,tid,amount,user_name,orphanage): 
    account=""
    if orphanage=='Hyderabad child care':
        account="harshab"
    elif orphanage=='Kukatpally health organ':
        account="harshab"
    elif orphanage=='Pragathi orphanage':
        account="harshab"
    else:
        account="test"
    account=account+str("@harsha.com")
    print(account)
    paypal_dict = {
        "business": account,
        "amount": amount,
        "currency-code":"USD",
        "item_name": tid,
        "invoice": tid,
        "notify_url": "http://57e8e544.ngrok.io/donation/HaSHinGLinKK/",
        "return": "http://127.0.0.1:8000/paypal_return/",
        "cancel_return": "http://127.0.0.1:8000/paypal_cancel/",
    }
    form = PayPalPaymentsForm(initial=paypal_dict)
    data=donatemoney.objects.latest()
    context = {"form": form,"data":data,"user_name":user_name,"orphanage":orphanage}
    return render(request, "donation/gatewaypage.html", context)

def paypal_cancel(request):
     return render(request,'donation/paypalcancel.html')

@csrf_exempt
def paypal_return(request):
   # consumer_key=''
   # consumer_secret=''
   # access_token=''
   # access_secret=''

   # api = twitter.Api(consumer_key=consumer_key,
   #                   consumer_secret=consumer_secret,
   #                   access_token_key=access_token,
   #                   access_token_secret=access_secret)
    
   # post_update = api.PostUpdates(status='My first tweet through django')
   return render(request,'donation/paypalreturn.html')

def facebookview(request):
    token='EAALOtHuxZAWUBAMZCC0uefyOq0ZCwN9CKi402YpNuc16UnjhCQovj8LXEuZCFCibPh6vPID7ZAhT4uXiRFsSWTnCycHVTMhgGfVlc1vGULC7ZA2ZB54rVPjZA1iMZAUNA7ZBpaNLWHveGHOu0t5HWE8GF4ssBfVyNl26MBHynbPFP6t0iXwnWk2ColCtlZCdzXAZCkAzKoROFOagtF5b8pIkT0Eb'
    fb = facebook.GraphAPI(access_token=token)
    #faceb = OpenFacebook(access_token=token)
    fb.put_object(parent_object='me',connection_name='feed',message='Test1')
    #faceb.set('me/feed', message='Test1',url='http://www.something')
   




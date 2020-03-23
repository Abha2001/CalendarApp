from django.shortcuts import render,get_object_or_404
import datetime
import calendar
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.utils.safestring import mark_safe
from .models import *
from .utils import EventCalendar
from .forms import EventForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout,authenticate

class CalendarView(generic.ListView):
    model = Event
    template_name = 'cal/calendar.html'

    def get_context_data(self,**kwargs):
        context =super().get_context_data(**kwargs)
        
        day= self.request.GET.get('day_gte', None)
        
        if not day:
        	d=datetime.date.today()
        else:
        	try:
        		split_day=day.split('-')
        		d=datetime.date(year=int(split_day[0]),month=int(split_day[1]),day=1)
        	except:
        		d=datetime.date.today()

        cal = EventCalendar()
        html_cal = cal.formatmonth(d.year,d.month,withyear=True)
        html_cal=html_cal.replace('<td','<td width="500" height="80"')
        context['calendar']= mark_safe(html_cal)
        context['prev_month']=str(prev_month(d))
        context['next_month']=str(next_month(d))
        return context
def index(request):
    return render(request,'cal/base.html')

def prev_month(d):
    first=d.replace(day=1)
    prev_month=first-datetime.timedelta(days=1)
    month=str(prev_month.year)+'-'+str(prev_month.month)
    return month

def next_month(d):
    days_in_month=calendar.monthrange(d.year,d.month)[1]
    last=d.replace(day=days_in_month)
    next_month=last+datetime.timedelta(days=1)
    month=str(next_month.year)+'-'+str(next_month.month)
    return month

@login_required(login_url='/cal/login')
def new_event(request):
    form=EventForm()
    if request.method=='POST':
        form=EventForm(request.POST or None)
        if request.POST and form.is_valid():
            form.save(user_id=request.user.pk)
            return redirect('cal:calendar')
    return render(request,'cal/event.html',{'form':form})

@login_required(login_url='/cal/login')
def edit_event(request,event_id):
    instance=get_object_or_404(Event,id=event_id)
    form=EventForm(request.POST or None,instance=instance)
    if request.method=='POST':
        if form.is_valid() and instance.name.pk==request.user.pk:
            form.save(user_id=request.user.pk)
            return redirect('cal:calendar')
    return render(request,'cal/event.html',{'form':form})

def signup(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('cal:calendar')
    else:
        form = UserCreationForm()
    return render(request,'cal/signup.html',{'form':form})

def login_view(request):
    message=False
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('cal:calendar')
        else:
            message='Invalid Username or Password'
    return render(request,'cal/login.html',{'message':message})

def logout_views(request):
    logout(request)
    return redirect('cal:calendar') 


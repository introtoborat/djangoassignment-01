from django.shortcuts import render, redirect
from activities.models import Category, EventModel, Participant
from activities.forms import CategoryModelForm, EventModelForm,ParticipantsModelForm
from django.contrib import messages
from django.utils.timezone import now

def view_category(request):
    categories = Category.objects.all()
    return render(request, "show_event.html", {"categories": categories})

def view_participants(request):
    participants = Participant.objects.all()
    return render(request, "view_participants.html", {"participants": participants})

def view_events(request):
    events = Category.objects.all()
    return render(request, "view_events.html", {"events": events})
    
def dashboard(request):
    return render(request, "dashboard.html")


def event_list(request):
    events=EventModel.objects.all()
    categories=Category.objects.all()
    participants_count={event.id:event.participants.count() for event in events}
    context={
        "events":events,
        "categories": categories,
        "participants_count":participants_count
    }
    return render(request,"event_list.html", context)

def event_detail(request,event_id):
    event=EventModel.objects.get(id=event_id)
    return render(request,'event_detail.html',{'event':event})

# def dashboard(request):    
#     return render(request,'dashboard.html')


def create_event(request):
    category_form = CategoryModelForm()
    event_form = EventModelForm()

    if request.method == "POST":
        category_form = CategoryModelForm(request.POST)
        event_form = EventModelForm(request.POST)
        
        if category_form.is_valid() and event_form.is_valid():
            category = category_form.save()  

            event = event_form.save(commit=False)  
            event.category = category  
            event.save()  

            messages.success(request, "Event Created Successfully")
            return redirect("create-event")  
    
    return render(request, "create_event.html", {"category_form": category_form, "event_form": event_form})



def create_category(request):
    category_form=CategoryModelForm()

    if request.method=="POST":
        category_form=CategoryModelForm(request.POST)

        if category_form.is_valid():
            category_form.save()

            messages.success(request,"Category Created Successfully")
            return redirect("create-category")

    return render(request, "create-category.html",{"category_form":category_form})


def create_participant(request):
    if request.method == "POST":
        participant_form = ParticipantsModelForm(request.POST)
        
        if participant_form.is_valid():
            par = participant_form.save(commit=False)
            par.save() 

            event_id = request.POST.get("event")  
            
            if event_id:
                event_instance = EventModel.objects.get(id=event_id) 
                par.event.add(event_instance)  
                
                messages.success(request, "Participant Created Successfully")
                return redirect("create-participant")  
            else: 
                messages.error(request, "Selected event does not exist.")
    else:
        participant_form = ParticipantsModelForm()

    return render(request, "create_par.html", {"participant_form": participant_form})

def update_event(request, event_id):
    event=EventModel.objects.get(id=event_id)
    if request.method=="POST":
        form=EventModelForm(request.POST,instance=event)
        if form.is_valid():
            form.save()
            messages.success(request,"Event Updated Successfully")
            return redirect("event_list")
    
    else:
        form=EventModelForm(instance=event)
    return render(request, "update_event.html", {"form": form})


def dashboard_event_list(request):
    event_type = request.GET.get('type', 'all') 
    today = now().date()

   
    all_events = EventModel.objects.all()
    
   
    if event_type == 'today':
        events = all_events.filter(date=today) 
    elif event_type == 'past_event': 
        events = all_events.filter(date__lt=today)
    elif event_type == 'future_event':  
        events = all_events.filter(date__gt=today)
    elif event_type == 'total_event':  
        events = all_events
    else:
        events = all_events.filter(date=today) 


    context = {
        'events': events, 
        'all_event_count': all_events.count(),
        'past_event_count': all_events.filter(date__lt=today).count(),
        'future_event_count': all_events.filter(date__gt=today).count(),
        'participant_count': Participant.objects.count(),
    }
    return render(request, "dashboard_event_list.html", context)
from django.shortcuts import render
from .models import EventModel

def search(request):
    search_query = request.GET.get('search', '')
    events = []
    category=[]

    if search_query:
        events = EventModel.objects.filter(name__icontains=search_query) 
        category = Category.objects.filter(name__icontains=search_query) 

    
    return render(request, 'event_list.html', {'events': events, 'category':category})



def delete_event(request, event_id):
    if request.method == 'POST':  
        event = EventModel.objects.get(id=event_id)  
        event.delete()
        messages.success(request, 'Event deleted successfully.')
    else:
        messages.error(request, 'Invalid request method.')

    return redirect('event_list')  

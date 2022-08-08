from django.views.generic import ( ListView, CreateView, UpdateView, )
from django.urls import reverse_lazy
from .models import Card

# Create your views here.
class CardListView(ListView):
    model =  Card
    queryset = Card.objects.all().order_by("box", "-date_created") #the dash in front date created means descending order
    
class CardCreateView(CreateView):
    model = Card
    fields = ["question", "answer", "box"]
    success_url = reverse_lazy("card-create")

class CardUpdateView(CardCreateView, UpdateView):
    success_url = reverse_lazy("card-list")
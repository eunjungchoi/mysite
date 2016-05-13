from django.shortcuts import render

# Create your views here.
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView
from hangout.models import Place, City, Category, Visit

#TemplateView 

class HangoutModelView(TemplateView):
	template_name = 'hangout/index.html'

	def get_context_data(self, **kwargs):
		context = super(HangoutModelView, self).get_context_data(**kwargs)
		context['object_list']=['Place', 'City', 'Category', 'Visit']
		return context

# ListView

class PlaceList(ListView):
	model = Place

class CityList(ListView):
	model = City

class CategoryList(ListView):
	model = Category

class VisitList(ListView):
	model = Visit

# DetailView
class PlaceDetail(DetailView):
	model = Place

class CityDetail(DetailView):
	model = City

class CategoryDetail(DetailView):
	model = Category

class VisitDetail(DetailView):
	model = Visit
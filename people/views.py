from django.shortcuts import render
from django.conf import settings

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from django.template import loader
from datetime import datetime
from company.models import Company
from company.models import People
from company.models import Jobs
from django.contrib.auth.decorators import login_required

def people(request):
	people = People.objects.all().order_by('name')
	context = {
		'people' : people
	}
	return render(request, 'people/index.html', context)

def people_detail(request, people_id):
	if not request.user.is_authenticated():
		return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
	p = People.objects.get(pk=people_id)
	colleagues = People.objects.filter(company_id=p.company_id).exclude(id__in=[p.id])
	context = {
		'people' : p,
		'people_id': people_id,
		'colleagues': colleagues
	}

	return render(request, 'people/detail.html', context)

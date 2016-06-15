from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import os
from django.conf import settings


from datetime import datetime
from company.models import Company
from company.models import People
from company.models import Jobs


def index(request):
	companies = Company.objects.all().order_by('name')
	context = {
		'companies' : companies,
	}

	return render(request, 'company/index.html', context)

def loginform(request):
	return render(request, 'company/login.html')

def log_in(request):
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(username=username, password=password)
	
	if user is not None:
		login(request, user)
		return redirect('/company/')
	else:
		return redirect('/company/')

def log_out(request):
	logout(request)
	return redirect('/company/')

def signupform(request):
	return render(request, 'company/signupform.html')

def signup(request):
	username = request.POST['username']
	email = request.POST['email']
	password = request.POST['password']
	user = User.objects.create_user(username, email, password)
	user = authenticate(username=username, password=password)
	login(request, user)
	return redirect('/company/')
		
@login_required
def company_detail(request, company_id):
	if not request.user.is_authenticated():
		return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
		
	c = Company.objects.get(pk=company_id) # SELECT * FROM Company WHERE id = '3';
	people = People.objects.filter(company=c) # SELECT * FROM People WHERE company_id = '3';
	j = Jobs.objects.filter(company_id=company_id)
	context = {
		'company' : c,
		'company_id': company_id,
		'people' : people,
		'jobs' : j
	}
	template = loader.get_template('company/company_detail.html')
	return HttpResponse(template.render(context, request))

def news(request):
	template = loader.get_template('company/news.html')
	context = {
	}
	return HttpResponse(template.render(context, request))

def news_detail(request, news_id):
	template = loader.get_template('company/news_detail.html')
	context = {
		'news_id': news_id
	}
	return HttpResponse(template.render(context, request))

def form(request):
	template = loader.get_template('company/form.html')
	context = {
			}
	return HttpResponse(template.render(context, request))

def add(request):
	c = Company(
		name=request.POST['company_name'],
		intro=request.POST['company_intro'],
		date=request.POST['company_date'], 
		homepage=request.POST['company_homepage'],
		address=request.POST['company_address'],
		phone=request.POST['company_phone'],
		photo=request.FILES['image'])

	c.save()

	companies = Company.objects.all().order_by('name')
	context = {
		'companies' : companies,
	}

	return render(request, 'company/index.html', context)

	# handle_uploaded_file(request.FILES['image'], "company_" + str(c.id) + ".png")

	# c.photo.name = "static/" + "company_" + str(c.id) + ".png"
	# c.save()

	# return render(request, 'company/debug.html', {"file": request.FILES['image']})

	# context = {
	# 	'company_name' : request.POST['company_name'],
	# 	'company_intro' : request.POST['company_intro'],
	# 	'company_date' : request.POST['company_date'],
	# 	'company_homepage' : request.POST['company_homepage'],
	# 	'company_address' : request.POST['company_address'],
	# 	'company_phone' : request.POST['company_phone']
	# }
	# return HttpResponseRedirect("/company/" + str(c.id))
	#template = loader.get_template('company/add.html')

def delete(request, company_id):
	c = Company.objects.get(pk=company_id)
	c.delete()
	
	return HttpResponseRedirect("/company/")

def edit(request):
	company_id = request.POST['company_id']
	c = Company.objects.get(pk=company_id)
	c.name = request.POST['company_name']
	c.intro = request.POST['company_intro']
	c.date = request.POST['company_date']
	c.homepage = request.POST['company_homepage']
	c.address = request.POST['company_address']
	c.phone = request.POST['company_phone']
	c.save()
	return HttpResponseRedirect("/company/" + str(c.id))
	#template = loader.get_template('company/editform.html')
	#context = {
	#	'company' : c,
	#	'company_id': company_id
	#}
	#return HttpResponse(template.render(context, request))

def editform(request, company_id):
	c = Company.objects.get(pk=company_id)
	template = loader.get_template('company/editform.html')
	context = {
		'company' : c,
		'company_id': company_id
	}
	return HttpResponse(template.render(context, request))

def peopleform(request, company_id):
	template = loader.get_template('company/peopleform.html')
	c = Company.objects.get(pk=company_id)
	context = {
			'company_id': company_id,
			'company_name' : c.name
	}
	return HttpResponse(template.render(context, request))

def addpeople(request):
	c = People(company_id=request.POST['company_id'], name=request.POST['people_name'], position=request.POST['people_position'])
	c.save()

	return HttpResponseRedirect("/company/" + str(request.POST['company_id']))

def deletepeople(request, people_id):
	p = People.objects.get(pk=people_id)
	company_id = p.company.id
	p.delete()
	
	return HttpResponseRedirect("/company/" + str(company_id))

def editpeople(request, people_id):
	p = People.objects.get(pk=people_id)
	template = loader.get_template('company/editpeople.html')
	context = {
		'people' : p,
		'people_id': people_id
	}
	return HttpResponse(template.render(context, request))

def editp(request):
	people_id = request.POST['people_id']
	p = People.objects.get(pk=people_id)
	p.name = request.POST['people_name']
	p.position = request.POST['people_position']
	p.save()

	return HttpResponseRedirect("/company/people/" + str(p.id))

def position(request):
	people = People.objects.all()
	positions = []
	for i in people:
		if i.position in positions:
			pass
		else:
			positions.append(i.position)
	template = loader.get_template('company/position.html')
	context = {
		'people' : people,
		'positions' : positions
	}
	return HttpResponse(template.render(context, request))

def byposition(request, position_name):
	people = People.objects.filter(position=position_name)
	context = {
		'people' : people,
		'position' : position_name
	}
	return render(request, 'company/positiongroup.html', context)

# def swengineer(request):
# 	people = People.objects.filter(position='swengineer')
# 	one = people[0]
# 	template = loader.get_template('company/positiongroup.html')
# 	context = {
# 		'people' : people,
# 		'position' : one.position
# 	}
# 	return HttpResponse(template.render(context, request))



def jobs(request):
	jobs = Jobs.objects.all()
	template = loader.get_template('company/jobs.html')
	context = {
		'jobs' : jobs
	}
	return HttpResponse(template.render(context, request))

def job_detail(request, jobs_id):
	j = Jobs.objects.get(pk=jobs_id)
	c = Company.objects.get(company_id=j.company_id)
	colleagues = People.objects.filter(company_id=j.company_id)
	template = loader.get_template('company/job_detail.html')
	context = {
		'job' : j, 
		'company' : c, 
		'colleagues': colleagues
		}
	return HttpResponse(template.render(context, request))

def jobform(request, company_id):
	template = loader.get_template('company/jobform.html')
	c = Company.objects.get(pk=company_id)
	context = {
			'company_id': company_id,
			'company_name' : c.name
	}
	return HttpResponse(template.render(context, request))

def addjob(request):
	j = Jobs(company_id=request.POST['company_id'], title=request.POST['title'], position=request.POST['position'],
		jd=request.POST['jd'], qualification=request.POST['qualification'], deadline=request.POST['deadline'], 
		salary=request.POST['salary'])
	j.save()
	return HttpResponseRedirect("/company/" + str(request.POST['company_id']))


def current_datetime(request):
	now = datetime.datetime.now()
	html - "<html><body>It is now %s.</body></html>" % now
	return HttpResponse(html)

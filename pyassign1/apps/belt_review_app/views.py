from __future__ import unicode_literals
from models import *
from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt



def index(request):
	return render(request, 'belt_review_app/index.html')

def dashboard(request):
	###create objects with likes
	###get the users that you need
	
	context = {
	###get other users and their pokes
	"other_users" : User.objects.exclude(id= request.session['user_id']),
	"all_users": User.objects.all()
	}
	
	return render(request, 'belt_review_app/dashboard.html', context)


def poke(request, id):
	###keep tracked of how many times each person was poked
	were_poked = User.objects.get(id = id)
	####add +1 to their poke history
	were_poked.were_poked += 1
	were_poked.save()
	
	####you also gotta figure out who was poking
	poked_another = User.objects.get(id=request.session['user_id'])
	poked_another.poked_another += 1
	poked_another.save()

###subtract the number of times each person has poked the logged in user
###from the number of times the logged in user has been poked
	
	###first get all the non logged in users
	other_users =  User.objects.exclude(id=request.session['user_id'])
	for user in other_users:
		many_times_poked = user.poked_another - were_poked.were_poked
	
	return redirect('/dashboard')

################################################################################################################################################
def logout(request):
	request.session['user_id'] = 0
	return redirect('/main')
	

def register(request):
	###below comes from validate_reg in models.Manager
	errors = User.objects.validate_reg(request.POST)
	if errors:
		##for the exact error 
		for tag, error in errors.iteritems():
			messages.error(request, error, extra_tags=tag)
		return redirect('/main')
	else:
		####if the user has entered successfully log them in
		pass
		found_users = User.objects.filter(email=request.POST['email'])
		if found_users.count() > 0:
			##display an error if the email has already been taken
			messages.error(request, "email already taken", extra_tags="email")
			return redirect('/main')
		else:
			#register the user
			hashed_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
			created_user = User.objects.create(name=request.POST['name'], user_name =request.POST['user_name'], email=request.POST['email'], password=hashed_pw)
			request.session['user_id'] = created_user.id
			request.session['user_name'] = created_user.name
			print created_user
			return redirect('/dashboard')
		return redirect('/main')
def login(request):
	###se if email is in the database
	found_users = User.objects.filter(email=request.POST['email'])
	if found_users.count() > 0:
		#check passwords
		found_user = found_users.first()
		if bcrypt.checkpw(request.POST['password'].encode(), found_user.password.encode()) == True:
			#we are logged in
			request.session['user_id'] = found_user.id
			request.session['user_name'] = found_user.name
			print found_user
			return redirect('/dashboard')
		else:
			messages.error(request, "Login Failed", extra_tags="email")
			return redirect('/main')
	else:
		messages.error(request, "Login Failed", extra_tags="email")
		return redirect('/main')
			
			
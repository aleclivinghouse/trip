from __future__ import unicode_literals
from models import *
from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt

def re(request):
	return redirect("/main")

def index(request):
	return render(request, 'belt_review_app/index.html')

def dashboard(request):

	user_poked_you = Poke.objects.filter(user_poked__id = request.session['user_id']).all()
	context = {
	#get everyone except the user
	"other_users":User.objects.exclude(id = request.session['user_id']),
	"user_poked_you": Poke.objects.filter(user_poked__id = request.session['user_id']).all(),


	}
	return render(request, 'belt_review_app/dashboard.html', context)


def process(request, id):
	##get
	previous_history = User.objects.get(id = request.session['user_id'])
	user_poker = User.objects.get(id = request.session['user_id'])
	user_poked = User.objects.get(id = id)
	user_poker_1 = User.objects.filter(id = request.session['user_id'])
	Poke.objects.create(user_poker = user_poker, user_poked = user_poked)
	user_poker_1.update(poke_history = previous_history.poke_history + 1)
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

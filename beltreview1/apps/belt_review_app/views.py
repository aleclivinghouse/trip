from __future__ import unicode_literals
from models import *
from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt


def index(request):
	return render(request, 'belt_review_app/index.html')

def books(request):
	context = {
		'books': Book.objects.all(),
		'reviews': Review.objects.order_by('-id')[:3]
	}
	return render(request, 'belt_review_app/dashboard.html', context)

def booksadd(request):
	context = {
	'books': Book.objects.all()

	}
	return render(request, 'belt_review_app/addbook.html', context)

def viewbook(request, id):
	context = {
	'the_book': Book.objects.get(id = id),
	'reviews': Review.objects.filter(book__id = id).all()
	}
	return render(request, 'belt_review_app/showbook.html', context)
#these are the process routes
def add(request):
	the_user = User.objects.get(id = request.session['user_id'])
	new_book = Book.objects.create(title = request.POST['title'], author = request.POST['author'])
 	new_review = Review.objects.create(text = request.POST['text'], rating = request.POST['rating'], book = new_book, user = the_user)
	return redirect('/dashboard')

def showuser(request, id):
	count = 0
	reviewNum = Review.objects.filter(user__id = id).all()
	for x in reviewNum:
		count = count + 1
	context = {
	"the_user": User.objects.get(id = id),
	"reviews": Review.objects.filter(user__id = id).all(),
	"count": count
	}
	return render(request, 'belt_review_app/showuser.html', context)



def addreviewtobook(request, id):
	if request.method == "POST":
		book = Book.objects.get(id = id)
		user = User.objects.get(id = request.session['user_id'])
		new_review = Review.objects.create(text = request.POST['text'], rating = request.POST['rating'], book = book, user = user)
	return redirect('/books/' + id)


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

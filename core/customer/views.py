import stripe
import firebase_admin
from firebase_admin import credentials, auth

from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib import messages

from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

from core.customer import forms

cred = credentials.Certificate(settings.FIREBASE_ADMIN_CREDENTIAL)
firebase_admin.initialize_app(cred)

stripe.api_key = settings.STRIPE_API_SECRET_KEY

@login_required()
def home(request):
	return redirect(reverse('customer:profile'))	

@login_required(login_url="/sign-in/?next=/customer/")
def profile_page(request):
	user_form = forms.BasicUserForm(instance=request.user)
	customer_form = forms.BasicCustomerForm(instance=request.user.customer)
	password_form = PasswordChangeForm(request.user)
	
	if request.method == "POST":

		if request.POST.get('action') == 'update_profile':
			user_form = forms.BasicUserForm(request.POST, instance=request.user)
			customer_form = forms.BasicCustomerForm(request.POST, request.FILES, instance=request.user.customer)

			if user_form.is_valid() and customer_form.is_valid():
				user_form.save()
				customer_form.save()

				messages.success(request, 'Your profile has been updated')
				return redirect(reverse('customer:profile'))

		elif request.POST.get('action') == 'update_password':	
			password_form = PasswordChangeForm(request.user, request.POST)
			if password_form.is_valid():
				user = password_form.save()
				update_session_auth_hash(request, user)
				
				messages.success(request, 'Your password has been updated')
				return redirect(reverse('customer:profile'))

		elif request.POST.get('action') == 'update_phone':	
			# Get Firebase user data
			firebase_user = auth.verify_id_token(request.POST.get('id_token'))
			request.user.customer.phone_number = firebase_user['phone_number']
			request.user.customer.save()	
			return redirect(reverse('customer:profile'))

	return render(request, 'customer/profile.html', {
		"user_form": user_form,
		"customer_form": customer_form,
		"password_form": password_form
	})

@login_required(login_url="/sign-in/?next=/customer/")
def payment_method_page(request):
	return render(request, 'customer/payment_method.html')
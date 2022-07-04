from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import loader

from django.contrib.auth.models import User
from django.db.models import Q
from django.core.paginator import Paginator

# Create your views here.
@login_required
def Search(request):
	query = request.GET.get("q")
	context = {}

	if query:
		users = User.objects.filter(Q(username__icontains=query))

		# Pagination
		paginator = Paginator(users, 6)
		page_number = request.GET.get('page')
		users_paginator = paginator.get_page(page_number)

		context = {
			'users': users_paginator,
		}

	template = loader.get_template('search_account.html')

	return HttpResponse(template.render(context, request))
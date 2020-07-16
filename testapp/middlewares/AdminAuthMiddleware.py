from django.http import HttpResponseRedirect
from django.urls import resolve, reverse
from django.shortcuts import redirect

# @author Bergin
# used as middleware for Sporty admin
# created - july 31st
# Middleware applies to url starts with site_url/sporty-admin/ except login page
class AdminAuthMiddleware:

    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self,request):
        response = self.get_response(request)
        current_url = resolve(request.path_info).route
        print(current_url)
        if current_url.startswith('admin') and current_url!='admin/login/':
            if 'loggedin' in request.session :
                if request.session['usertype'] == 1:
                    return response
                else:
                    return redirect('/admin/login/')
            else:
                return redirect('/admin/login/')
        else:
            return response
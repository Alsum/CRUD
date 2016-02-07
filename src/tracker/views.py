from django.shortcuts import render
from django.contrib.auth.models import User
from models import UserProfile
from forms import ProfileForm,UserForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf


def home(request):
	if request.user.is_authenticated() and request.user.is_staff:
		queryset = UserProfile.objects.all().order_by('-timestamp') 
		context = {
			"queryset": queryset
		}
	else:
		context={"queryset": "welcome"}    
	return render(request, "home.html", context)


def edit(request,profile_id):
    profile=UserProfile.objects.get(id=profile_id) 
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            cd = form.cleaned_data
            UserProfile.objects.filter(id=profile_id).update(pic=cd['pic'],
                                                   url=cd['url'],
                                                   mobile=cd['mobile'])
            
            return HttpResponseRedirect('/')
    else:
        form = ProfileForm(initial={
                                 'id':profile.id,
                                 'pic':profile.pic,
                                 'url':profile.url,
                                 'mobile':profile.mobile})

    args = {}
    args.update(csrf(request))
    
    args['form'] = form    
        
    return render(request, "edit.html", args)

def del_user(request,profile_id):    
    user=User.objects.get(id=profile_id) 
    user.delete()
    return HttpResponseRedirect('/')    
		
def edit_core(request,user_id):
    user=User.objects.get(id=user_id) 
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            User.objects.filter(id=user_id).update(username=cd['username'],
                                                   email=cd['email'])
            
            return HttpResponseRedirect('/')
    else:
        form = UserForm(initial={'username':user.username,
                                 'email':user.email})

    args = {}
    args.update(csrf(request))
    
    args['form'] = form    
        
    return render(request, "editcore.html", args)
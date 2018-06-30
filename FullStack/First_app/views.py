from django.shortcuts import render
from django.http import HttpResponse
from First_app.models import Topic,Webpage,AccessRecord
from . import forms
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse , HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpages_list}
    return render (request,'first_app/index.html',context=date_dict)

def formview (request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)
        if form.is_valid():
            print('Valid form')
            print("NAME:" + form.cleaned_data['name'])
            print("EMAIL:" + form.cleaned_data['email'])
            print("TEXT:" + form.cleaned_data['text'])



    return render(request,'First_app/Form.html',{'form':form})


def formview1 (request):
    form = forms.FormName1()

    if request.method == 'POST':
        form = forms.FormName1(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)



    return render(request,'First_app/Form.html',{'form':form})





def register(request):

    registerd = False

    if request.method == "POST":
        user_form = forms.UserForm(data = request.POST)
        profile_form = forms.UserProfileInfoForm(data = request.POST)


        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit = False)
            profile.user = user


            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()

            registerd = True

        else:
            print('ERROR')
    else:
        user_form = forms.UserForm()
        profile_form = forms.UserProfileInfoForm()

    return render(request,'first_app/registration.html',
    {'registerd':registerd,'user_form':user_form,'profile_form':profile_form})



@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def user_login(request):

        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')


            user = authenticate(username=username , password=password)


            if user:
                if user.is_active:
                    login(request,user)
                    return HttpResponseRedirect(reverse('index'))

                else:
                    return HttpResponse("Not Active")

            else:
                print ("Wrong INFO")

        else :
            return render(request,'first_app/login.html')

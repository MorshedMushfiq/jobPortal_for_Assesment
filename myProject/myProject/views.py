from django.shortcuts import render,redirect

from myApp.models import *
from django.contrib.auth import authenticate,login,logout
from django.db.models import Q
from django.contrib.auth.decorators import login_required


def signupPage(request):
    
    if request.method=='POST':
        
        username=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("password")
        Confirm_password=request.POST.get("Confirm_password")
        user_type=request.POST.get("user_type")
        contact_no=request.POST.get("contact_no")
        Profile_Pic=request.FILES.get("Profile_Pic")
    
        
        if password==Confirm_password:
            
            
            user=customUser.objects.create_user(
                username=username,
                email=email,
                password=password,
                user_type=user_type,
                Profile_Pic=Profile_Pic,
                contact_no=contact_no,
            )
            if user_type=='seeker':
                seekerProfileModel.objects.create(user=user)
                
            elif user_type=='recruiter':
                recruiterProfileModel.objects.create(user=user)
            
            return redirect("signInPage")
            
    return render(request,"signupPage.html")


def signInPage(request):
    if request.method == 'POST':
        
        user_name=request.POST.get("username")
        pass_word=request.POST.get("password")

        try:
            user = authenticate(request, username=user_name, password=pass_word)

            if user is not None:
                login(request, user)
                return redirect('homePage') 
            else:
                return redirect('signInPage')

        except customUser.DoesNotExist:
            return redirect('signInPage')

    return render(request, 'signInPage.html')

@login_required
def homePage(request):
    
    
    return render(request,"homePage.html")


def logoutPage(request):
    
    logout(request)
    
    return redirect('signInPage')

@login_required
def profilePage(request):
    
    return render(request,"profilePage.html")

@login_required
def createdJobs(request):
    jobs = JobModel.objects.filter(user=request.user)
    context = {
        'jobs':jobs
    }

    return render(request, "createdJobs.html", context)

def deleteJob(request, id):
    JobModel.objects.get(id=id).delete()
    return redirect('createdJobs')

def editJob(request, id):
    edit_job = JobModel.objects.get(id=id)
    if request.method == "POST":
        id =  request.POST.get('job_id')
        title =  request.POST.get('title')
        openings = request.POST.get('openings')
        description = request.POST.get('description')
        category = request.POST.get('category')
        skills = request.POST.get('skills')
        new_job_image = request.FILES.get('new_job_image')
        old_job_image = request.POST.get('old_job_image')
        job = JobModel(id = id, user=request.user, title=title, openings=openings, description=description, skills=skills, category=category)
        if new_job_image:
            job.job_image = new_job_image
        else:
            job.job_image = old_job_image
        job.save()
        return redirect('createdJobs')
    context = {
        'data':edit_job,
        'category':JobModel.CATEGORY
    }

    return render(request, 'editJob.html', context)

def viewJob(request, id):
    view_job = JobModel.objects.get(id=id)
    context = {
        'jobs':view_job
    }

    return render(request, 'viewJob.html', context)

def addJob(request):
    

    if request.method == "POST":
        title =  request.POST.get('title')
        openings = request.POST.get('openings')
        description = request.POST.get('description')
        category = request.POST.get('category')
        skills = request.POST.get('skills')
        job_image = request.FILES.get('job_image')
        job = JobModel(user=request.user, title=title, openings=openings, description=description, skills=skills, 
                       category=category, job_image=job_image)
        job.save()
        return redirect('createdJobs')
    context = {
        "category": JobModel.CATEGORY
    }
    return render(request, 'addJob.html', context)



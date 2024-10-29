from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from myProject.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path('',signupPage,name="signupPage"),
    path("signInPage/", signInPage, name="signInPage"),
    path("homePage/", homePage, name="homePage"),
    path("logoutPage/", logoutPage, name="logoutPage"),
    path("ProfilePage/", profilePage, name="profilePage"),
    path("createdJobs/", createdJobs, name="createdJobs"),
    path("addJob/", addJob, name="addJob"),
    path("deleteJob/<int:id>", deleteJob, name="deleteJob"),
    path("editJob/<int:id>", editJob, name="editJob"),
    path("viewJob/<int:id>", viewJob, name="viewJob"),

    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

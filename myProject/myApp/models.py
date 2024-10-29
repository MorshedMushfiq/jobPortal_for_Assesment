from django.db import models
from django.contrib.auth.models import AbstractUser

class customUser(AbstractUser):
    
    USER=[
        ('recruiter','Recruiter'),
        ('seeker','Seeker'),
    ]
    user_type=models.CharField(choices=USER,max_length=100,null=True)
    skills=models.CharField(max_length=100,null=True)
    Profile_Pic=models.ImageField(upload_to='Media/Profile_Pic',null=True)
    contact_no=models.CharField(max_length=100,null=True)
    
    def __str__(self):   
        
        return f"{self.username}"
    
class seekerProfileModel(models.Model):
    
    user=models.OneToOneField(customUser,on_delete=models.CASCADE,related_name='seekerProfile')
   
    def __str__(self):
        return f"{self.user.username}"
    
    
class recruiterProfileModel(models.Model):
    
   
    user = models.OneToOneField(customUser, on_delete=models.CASCADE,related_name='recruiterProfile')
   
    def __str__(self):
        return f"{self.user.username}"
    

class JobModel(models.Model):
    
    CATEGORY=[
        ('full_time','Full Time'),
        ('part_time','Part Time'),
        ('project_based','Project Based'),
    ]

    skills=models.CharField(max_length=100,null=True)
    
    
    user = models.ForeignKey(customUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    openings = models.PositiveIntegerField()
    category=models.CharField(choices=CATEGORY,max_length=100,null=True)
    description = models.TextField()
    job_image=models.ImageField(upload_to='Media/Job_Image',null=True)
    
    def __str__(self):
        return f"{self.user.username} {self.title}"


class ApplyJob(models.Model):
    user = models.ForeignKey(customUser, on_delete=models.CASCADE, null=True)
    job = models.ForeignKey(JobModel, on_delete=models.CASCADE, null=True)
    resume = models.FileField(upload_to='Media/resume', max_length=100, null=True)
    coverLetter = models.TextField(null=True)

    def __str__(self):
        return f" Applying to - {self.job.title} - {self.user.username}"




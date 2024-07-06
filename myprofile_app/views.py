from django.shortcuts import redirect, render
from django.http import HttpResponse

from . models import Userdata

def edit_portfolio(request): 
    if request.POST:
        # Capture and print form data
        fullname = request.POST.get('fullname')
        about = request.POST.get('about')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        skills = request.POST.get('skills')
        workexperience = request.POST.get('workexperience')
        education = request.POST.get('education')
        certifications = request.POST.get('certifications')
        projecttitle = request.POST.get('projecttitle')
        projectdescription = request.POST.get('projectdescription')
        projectlink = request.POST.get('projectlink')
        
        user_obj = Userdata(fullname=fullname,about=about,email=email,mobile=mobile,skills=skills,workexperience=workexperience,education=education,certifications=certifications,projecttitle=projecttitle,projectdescription=projectdescription,projectlink=projectlink)
        user_obj.save()

        # Print the data to the terminal
        print("Full Name:", fullname)
        print("About:", about)
        print("Email:", email)
        print("Mobile:", mobile)
        print("Skills:", skills)
        print("Work Experience:", workexperience)
        print("Education:", education)
        print("Certifications:", certifications)
        print("Project Title:", projecttitle)
        print("Project Description:", projectdescription)
        print("Project Link:", projectlink)

        

        # Redirect or render a template

    return render(request, 'edit_portfolio.html')

   

    



    

def portfolio_view(request):
    return render(request, "portfolio.html")

def project_showcase_view(request):
    return render(request, 'project_showcase.html')


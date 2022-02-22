from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages


# Create your views here.
def home(request):
    status = False    
    if request.method=='POST':
        email_from = settings.EMAIL_HOST_USER
        to_email = [request.POST['email']]
        subject = request.POST['subject']
        content = request.POST['content']
        try:
            send_mail(subject=subject, message=content, from_email=email_from, recipient_list=to_email)
            print("Message has sent successfully!!!")
            status = True
            messages.success(request, "Email has sent successfully!!!")
        except Exception as e:
            # status = False
            print(e)
    return render(request, template_name='index.html', context={'success': status})
def about_page(request):
    return render(request, template_name='about.html')

def contact_page(request):
    return render(request, template_name='contact.html')


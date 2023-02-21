from django.shortcuts import render
from django.shortcuts import render,get_object_or_404, redirect
from .forms import SendEmail
from django.core.mail import send_mail

def FAQ(request):
    return render(request,'pages/basic/faq.html')

def contact_us(request):
    submitted = False
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        # send email
        send_mail(
            name,
            'Name:' + name + ',' + 'Email: ' + email + ',' + 'Subject: ' + subject + ',' + 'Message: ' + message,
            email,
            ['davortelisman@gmail.com'],
        )
        form = SendEmail(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "personal_page.html")
    form = SendEmail
    return render(request,'pages/basic/contact-us.html',{'form': form})

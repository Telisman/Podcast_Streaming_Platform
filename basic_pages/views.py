from django.shortcuts import render

def FAQ(request):
    return render(request,'pages/basic/faq.html')

def contact_us(request):
    return render(request,'pages/basic/contact-us.html')

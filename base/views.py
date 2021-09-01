from django.shortcuts import render, redirect

from django.core.mail import send_mail

from django.contrib import messages
from django.template import context

from .templatetags.custom_tags import anchor 

def home(request):

    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        company = request.POST.get('company')
        message = request.POST.get('message')
        service = request.POST.get('services')
        
        data = {    
            'fname' : fname,
            'lname' : lname,
            'email' : email,
            'company' : company,
            'message' : message,
            'service' : service,
        }

        global formcheck

        formcheck = all(data.values())

        print(formcheck)

        if formcheck :
        
            message = '''
            Nuevo mensaje: {}
            
            de: {}  {}

            empresa: {}

            email: {}

            servicio: {}
            '''.format(data['message'],data['fname'],data['lname'],data['company'],data['email'], data['service'])

            send_mail(data['lname'], message,'', ['alejandroalonso0306@gmail.com'])
            
            messages.success(request, 'Gracias por enviar su consulta {} {}'.format(fname,lname))
        
        else:
            messages.error(request,'Por favor ingrese todos los campos')
            return redirect('home')

    return render(request, 'base/home.html')


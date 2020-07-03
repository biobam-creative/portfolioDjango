from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail
from .models import Project

from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse


def home(request):
    projects = Project.objects.order_by('-pk')[:4]

    context = {
        'projects': projects,
    }
    return render(request, 'portfolio/home.html', context)


def about(request):
    return render(request, 'portfolio/about.html',)


def services(request):
    return render(request, 'portfolio/services.html',)


def portfolio(request):
    projects = Project.objects.all()

    context = {
        'projects': projects,
    }
    return render(request, 'portfolio/portfolio.html', context)


def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data["message"]
            name = form.cleaned_data["name"]
            email = f'Message from {form.cleaned_data["email"]}'
            subject = form.cleaned_data["subject"]
            recipients = ['eminentia.ea@gmail.com', ]
            sucess_message = f'Thank you {name}, Your email has been sent'
            failed_message = 'Your message was not delivered please try again!!!'

            try:
                send_mail(subject, message, email,
                          recipients,  fail_silently=True, )
            except BadHeaderError:
                return render(request, 'portfolio/contact.html', {'failed_message': failed_message, 'form': form})
            return render(request, 'portfolio/contact.html', {'sucess_message': sucess_message, 'form': form})
    return render(request, 'portfolio/contact.html', {'form': form})


def project_detail(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    context = {
        'project': project,
    }

    return render(request, 'portfolio/project_detail.html', context)


# Create your views here.

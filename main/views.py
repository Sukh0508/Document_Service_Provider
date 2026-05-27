from django.shortcuts import render ,redirect
from .models import Coreservices ,Document_img , Contact , Logo

# Create your views here.
def Home(request):

    coreservice = Coreservices.objects.all()

    doc_img = Document_img.objects.first()
    if request.method == "POST":
        service_type = request.POST.get("service_type")
        application_type = request.POST.get("application_type")
        name = request.POST.get("name")
        mobile = request.POST.get("mobile")
        email = request.POST.get("email")
        address = request.POST.get("address")
        dob = request.POST.get("dob")
        notes = request.POST.get("notes")
        
        Contact.objects.create(
            service_type = service_type,
            application_type  = application_type ,
            name = name,
            mobile = mobile,
            email = email,
            address = address,
            dob = dob,
            notes = notes
        )
        return redirect("/")
     
        
    return render(request,"index.html",{
        "coreservice": coreservice,
        "doc_img":doc_img,
        
                  
     })

def Gumasta(request,slug):
    return render(request ,f"{slug}.html")

def Apply(request):
    return render(request,"apply.html")

def dashboard(request):
    coreservice = Coreservices.objects.all()

    doc_img = Document_img.objects.first()

    services = Coreservices.objects.all()

    contacts = Contact.objects.all()

    logo = Logo.objects.first()

    return render(request,"admin/dashboard.html",{
        "services": services,
        "contacts": contacts,
        "logo": logo,
        "coreservice":coreservice,
        "doc_img":doc_img,
    })
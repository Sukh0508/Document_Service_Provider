from django.shortcuts import render ,redirect
from .models import Coreservices ,Document_img , Contact , Logo , Staff

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

    free = Staff.objects.filter(busy=False).first()

    print("FREE WORKER:", free)

    

    Contact.objects.create(
            service_type = service_type,
            application_type = application_type,
            name = name,
            mobile = mobile,
            email = email,
            address = address,
            dob = dob,
            notes = notes,
            assign = free if free else None,
            status = "assigned" if free else "pending"

    )
    if free:
        free.busy = True
        free.save()

    # else:

    #     Contact.objects.create(
    #         service_type = service_type,
    #         application_type = application_type,
    #         name = name,
    #         mobile = mobile,
    #         email = email,
    #         address = address,
    #         dob = dob,
    #         notes = notes
    #     )

        print("NO FREE WORKER")
 
        return redirect("/")
     
 return render(request,"index.html",{
    "coreservice": coreservice,
     "doc_img":doc_img,
 })

def auto_assign(staff):
   pending_request = Contact.objects.filter(status = "pending").first()
   if pending_request:
      pending_request.assign = staff
      pending_request.status = "assigned"
      pending_request.save()

      staff.busy = True
      staff.save()
      auto_assign(staff)

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
from .models import Logo

def global_data(request):
    return {
        "global_logo" : Logo.objects.first()
    }
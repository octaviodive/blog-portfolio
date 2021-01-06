from django.shortcuts import render

# Create your views here.
def about(request):
    return render(request, "about.html", {})
def contact(request):
    return render(request, "contact.html", {})
def privacy_policy(request):
    return render(request, "privacy_policy.html", {})
def terms_of_service(request):
    return render(request, "terms_of_service.html", {})

from django.shortcuts import render,redirect
from django.views.generic import View
from phone.forms import MobileForm
from phone.models import Mobilemodel

# Create your views here.
class MobileView(View):
    #the get method is a special method used to handle HTTP GET requests
    def get(self,request):
        
        form=MobileForm()

        return render(request,"phn.html",{"form":form})
    #Renders a form to create a new mobile phone entry.
    def post(self,request):
#the post method is used to handle HTTP POST requests. When a user submits a form on a webpage (typically created with the HTML 
        
        form=MobileForm(request.POST)
        if form.is_valid():#Handles the form submission. If the form is valid, it saves the new mobile phone entry
            form.save()
        else:
            print("get out")    
        return render(request,"phn.html",{"form":form}) 

class MobileList(View):
    def get(self,request):
        #Retrieves all mobile phone entries from the database and renders a template to display them.
        qs=Mobilemodel.objects.all()
        return render(request,"phnlist.html",{"qs":qs})
    

    def post(self,request):
        #Handles a search request based on the mobile phone name
        name=request.POST.get("text")
        qs=Mobilemodel.objects.filter(name=name)
        return render(request,"phnlist.html",{"qs":qs})
    

class Mobiledetail(View):
    def get(self,request,**kwargs):
# Retrieves the details of a specific mobile phone entry based on the provided ID and renders a template to display the details.
        print(kwargs)
        id=kwargs.get("k")
        qs=Mobilemodel.objects.get(id=id)
        return render(request,"phndetail.html",{"qs":qs})
    
class Mobileremove(View):
    def get(self,request,**kwargs):
        #Deletes a specific mobile phone entry based on the provided ID and redirects to the mobile phone list view.
        id=kwargs.get("k")
        qs=Mobilemodel.objects.get(id=id).delete()
        return redirect('lst')
    
class Mobileupdate(View):
    def get(self,request,**kwargs):
#Retrieves the details of a specific mobile phone entry based on the provided ID and renders a form to update the entry.
         id=kwargs.get("pk")
         qs=Mobilemodel.objects.get(id=id)
         form=MobileForm(instance=qs)
         return render(request,"phnedit.html",{"form":form})
    
    def post(self,request,**kwargs):
#Handles the form submission to update the mobile phone entry. If the form is valid, it saves the changes;
        id=kwargs.get("pk")
        qs=Mobilemodel.objects.get(id=id)
        form=MobileForm(request.POST,instance=qs)

        if form.is_valid():
            form.save()
        else:
            print("get out")
        return redirect('lst')    
    
    

    

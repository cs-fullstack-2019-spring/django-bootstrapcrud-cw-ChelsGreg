from django.shortcuts import render, redirect, get_object_or_404
from .forms import GarageForm
from .models import Garage

# Create your views here.


def index(request):
    # TO GRAB ITEMS IN GARAGE MODEL
    items = Garage.objects.all()
    # TO GRAB FORM
    itemForm = GarageForm(request.POST or None)
       # SAVE FORM INPUT
    if request.method == "POST":
        if itemForm.is_valid():
            itemForm.save()
            return redirect('index')

    context = {
        "items": items,
        "form": itemForm,
    }


    return render(request, 'BootCRUDApp/index.html', context)



# EDIT FUNCTION
def edit(request, id):
    # TO GRAB ITEMS IN GARAGE BY ID
    editItem = get_object_or_404(Garage, pk=id)
    # TO GRAB SELECTED ITEM IN editItem FOR FORM
    editForm = GarageForm(request.POST or None, instance=editItem)
           # TO SAVE IF FORM IS VALID
    if editForm.is_valid():
        editForm.save()
            # RETURNS/RELOADS INDEX
        return redirect('index')
     # DIRECT TO INDEX/ VARIABLE TO SYNC HTML AND VIEWS
    return render(request, 'BootCRUDApp/index.html', {"form": editForm})


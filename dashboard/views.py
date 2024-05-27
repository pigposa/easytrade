from django.shortcuts import render
from django.contrib.auth import logout

from item.models import Item


from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required

def index(request):
    items = Item.objects.filter(created_by=request.user)
    context={'items': items}
    return render(request,'dashboard/dashboard.html',context)


@login_required()    
def logout_user(request):
    logout(request)
    return render(request, 'dashboard/logout.html')

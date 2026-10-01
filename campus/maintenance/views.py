from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import MaintenanceRequest
from .forms import UserRegisterForm, MaintenanceRequestForm, StatusUpdateForm

def home(request):
    return render(request, 'home.html')

def register_view(request):
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        login(request, form.save())
        return redirect('home')
    return render(request, 'form.html', {'form': form, 'title': 'Register'})

def login_view(request):
    form = AuthenticationForm(request, data=request.POST or None)
    if form.is_valid():
        login(request, form.get_user())
        return redirect('home')
    return render(request, 'form.html', {'form': form, 'title': 'Login'})

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def submit_request(request):                      # CREATE
    form = MaintenanceRequestForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        return redirect('my_requests')
    return render(request, 'form.html', {'form': form, 'title': 'Submit Request'})

@login_required
def my_requests(request):                         # READ
    requests = MaintenanceRequest.objects.filter(user=request.user)
    return render(request, 'list.html', {'requests': requests, 'title': 'My Requests'})

@login_required
def edit_request(request, pk):                    # UPDATE
    obj = get_object_or_404(MaintenanceRequest, pk=pk, user=request.user)
    form = MaintenanceRequestForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('my_requests')
    return render(request, 'form.html', {'form': form, 'title': 'Edit Request'})

@login_required
def delete_request(request, pk):                  # DELETE
    obj = get_object_or_404(MaintenanceRequest, pk=pk, user=request.user)
    if request.method == 'POST':
        obj.delete()
    return redirect('my_requests')

@user_passes_test(lambda u: u.is_staff)
def staff_dashboard(request):                     # staff: see all
    requests = MaintenanceRequest.objects.all()
    return render(request, 'list.html',
                  {'requests': requests, 'title': 'All Requests', 'staff': True})

@user_passes_test(lambda u: u.is_staff)
def staff_update_status(request, pk):             # staff: change status
    obj = get_object_or_404(MaintenanceRequest, pk=pk)
    form = StatusUpdateForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('staff_dashboard')
    return render(request, 'form.html', {'form': form, 'title': 'Update Status'})

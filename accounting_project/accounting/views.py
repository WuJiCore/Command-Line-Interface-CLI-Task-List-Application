from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Profile

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

from .forms import UserCreationForm, SaleForm, PurchaseForm, ExpenseForm, get_dynamic_form
from .models import Sale, Purchase, Expense, EditRequest

@login_required
def home(request):
    return render(request, 'home.html')

from django.contrib.contenttypes.models import ContentType
from .forms import EditRequestForm

@login_required
def view_data(request):
    sales = Sale.objects.filter(employee=request.user)
    purchases = Purchase.objects.filter(employee=request.user)
    expenses = Expense.objects.filter(employee=request.user)
    context = {
        'sales': sales,
        'purchases': purchases,
        'expenses': expenses,
    }
    return render(request, 'view_data.html', context)

@login_required
def request_edit(request, model_name, object_id):
    model = None
    if model_name == 'sale':
        model = Sale
    elif model_name == 'purchase':
        model = Purchase
    elif model_name == 'expense':
        model = Expense

    obj = model.objects.get(pk=object_id)
    DynamicForm = get_dynamic_form(model)

    if request.method == 'POST':
        form = DynamicForm(request.POST, instance=obj)
        if form.is_valid():
            requested_changes = form.cleaned_data
            edit_request = EditRequest.objects.create(
                employee=request.user,
                content_object=obj,
                reason=request.POST.get('reason'),
                requested_changes=requested_changes
            )
            return redirect('view_data')
    else:
        form = DynamicForm(instance=obj)

    return render(request, 'request_edit.html', {'form': form, 'object': obj})

@login_required
def add_sale(request):
    if request.method == 'POST':
        form = SaleForm(request.POST)
        if form.is_valid():
            sale = form.save(commit=False)
            sale.employee = request.user
            sale.save()
            return redirect('home')
    else:
        form = SaleForm()
    return render(request, 'add_sale.html', {'form': form})

@login_required
def add_purchase(request):
    if request.method == 'POST':
        form = PurchaseForm(request.POST)
        if form.is_valid():
            purchase = form.save(commit=False)
            purchase.employee = request.user
            purchase.save()
            return redirect('home')
    else:
        form = PurchaseForm()
    return render(request, 'add_purchase.html', {'form': form})

@login_required
def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.employee = request.user
            expense.save()
            return redirect('home')
    else:
        form = ExpenseForm()
    return render(request, 'add_expense.html', {'form': form})

def is_admin(user):
    return user.profile.role == 'admin'

@user_passes_test(is_admin)
def create_employee(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'create_employee.html', {'form': form})

@user_passes_test(is_admin)
def admin_dashboard(request):
    edit_requests = EditRequest.objects.filter(status='pending')
    context = {
        'edit_requests': edit_requests,
    }
    return render(request, 'admin_dashboard.html', context)

@user_passes_test(is_admin)
def approve_request(request, request_id):
    edit_request = EditRequest.objects.get(pk=request_id)
    obj = edit_request.content_object
    for field, value in edit_request.requested_changes.items():
        setattr(obj, field, value)
    obj.save()
    edit_request.status = 'approved'
    edit_request.save()
    return redirect('admin_dashboard')

@user_passes_test(is_admin)
def deny_request(request, request_id):
    edit_request = EditRequest.objects.get(pk=request_id)
    edit_request.status = 'denied'
    edit_request.save()
    return redirect('admin_dashboard')

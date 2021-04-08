from django.shortcuts import render
from .models import Customer, Transfer

# Create your views here.
def home(request):
    return render(request, 'home.htm')


def all_customers(request):
    customers = Customer.objects.all()
    return render(request, 'all_customers.htm', {'customers' :customers, 'button':'View'})

def customer(request, id):
    customer = Customer.objects.filter(id = id)
    # print(customer[0])
    transfer_to = Transfer.objects.filter(from_customer=customer[0].name)
    # print(transfer_from)
    transfer_from = Transfer.objects.filter(to_customer =customer[0].name)
    return render(request, 'customer.htm', {'customer':customer, 'transfer_from': transfer_from, 'transfer_to': transfer_to})

def transfer(request,from_id):
    print(from_id)
    from_customer = Customer.objects.filter(id = from_id)
    # to_customer = Customer.objects.filter(id = to_id)
    customers = Customer.objects.exclude(id = from_id)
    return render(request, 'all_customers.htm', {'customers' :customers,'button':'Select'})

def money_transfer(request, from_id, to_id):
    # transfer = Transfer()
    # transfer.from_customer = Customer.objects.filter(id = from_id)[0].name
    # transfer.to_customer = Customer.objects.filter(id = to_id)[0].name
    # transfer.save()
    # print(transfer)
    from_customer = Customer.objects.filter(id = from_id)
    to_customer = Customer.objects.filter(id = to_id)
    return render(request, 'transfer.htm' ,{'from_customer':from_customer[0], 'to_customer': to_customer[0]})

def done(request):
    if request.method == 'POST':
        from_customer = request.POST['from_customer']
        to_customer = request.POST['to_customer']
        balance_transferred = request.POST['balance']
        transfer = Transfer()
        transfer.from_customer = from_customer
        transfer.to_customer = to_customer
        transfer.balance_transferred = balance_transferred
        transfer.save()
        from_cus = Customer.objects.get(name=from_customer)
        to_cus = Customer.objects.get(name = to_customer)
        from_cus.current_balance= from_cus.current_balance - float(balance_transferred)
        to_cus.current_balance = to_cus.current_balance + float(balance_transferred)
        from_cus.save()
        to_cus.save()
    return render(request, 'home.htm')


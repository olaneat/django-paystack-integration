from django.shortcuts import render
from .forms import CustomerInfoForm
from django.http import HttpResponse

# Create your views here.
def customer_info(request):
    if request.method == 'POST':
        customer_form = CustomerInfoForm(request.method)
        # print(customer_form.cleaned_data)
        # customer_form.save(commit=False)
        # return render(request, 'template_folder/payment.html', {'email':customer_form.email})
        # if customer_form.is_valid() and customer_form.cleaned_data:
        if customer_form.is_valid():
            email_val = customer_form.cleaned_data['email']
            print(customer_form.cleaned_data)
            # customer_form.save(commit=False)
            # return render(request, 'template_folder/payment.html', {'email':customer_form.email})

        # else:
        #     return HttpResponse('Invalid input, try again!!')
    else:
        customer_form = CustomerInfoForm()
    return render(request, 'template_folder/customer_info.html', {'customer_form':customer_form})
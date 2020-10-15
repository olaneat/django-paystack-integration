"""paystackInt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from customer import views
from dispatch import receiver
#from paystack.api import signals

@receiver(signals.successful_payment_signal)
def on_successful_payment(sender, **kwargs):
    import pdb

    pdb.set_trace()
    pass

urlpatterns = [
    path('admin/', admin.site.urls),
    path("paystack/", include(("paystack.urls", "paystack"), namespace="paystack")),
    path('', views.customer_info, name='customer_info'),
    #path("paystack/", include(("paystack.frameworks.django.urls", "paystack"), namespace="paystack")),

]
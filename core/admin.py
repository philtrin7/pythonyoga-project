from django.contrib import admin
from django.conf import settings
from paypalrestsdk import configure

from .models import *


configure({
    "mode": settings.PAYPAL_MODE,
    "client_id": settings.PAYPAL_CLIENT_ID,
    "client_secret": settings.PAYPAL_CLIENT_SECRET,
})


class CourierAdmin(admin.ModelAdmin):
    list_display = ['user_full_name', 'paypal_email', 'balance']

    def user_full_name(self, obj):
        return obj.user.get_full_name()

    def balance(self, obj):
        return round(sum(t.amount for t in Transaction.objects.filter(job__courier=obj, status=Transaction.IN_STATUS)) * 0.80, 2)


class TransactionAdmin(admin.ModelAdmin):
    list_display = ['stripe_payment_intent_id',
                    'courier_paypal_email', 'customer', 'courier', 'job', 'amount', 'status', 'created_at']
    list_filter = ['status', ]

    def customer(self, obj):
        return obj.job.customer

    def courier(self, obj):
        return obj.job.courier

    def courier_paypal_email(self, obj):
        return obj.job.courier.paypal_email if obj.job.courier else None


# Register your models here.
admin.site.register(Customer)
admin.site.register(Courier, CourierAdmin)
admin.site.register(Category)
admin.site.register(Job)
admin.site.register(Transaction, TransactionAdmin)

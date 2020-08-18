from django.contrib import admin
from .models import Item, OrderItem, Order, Payment, Coupon


class OrderAdmin(admin.ModelAdmin):
    list_display = ['user',
                    'ordered',
                    # 'being_delivered',
                    # 'received',
                    # 'refund_requested',
                    # 'refund_granted',
                    # 'shipping_address',
                    # 'billing_address',
                    # 'payment',
                    'coupon'
                    ]


admin.site.register(Item)
admin.site.register(OrderItem)
admin.site.register(Order, OrderAdmin)
admin.site.register(Payment)
admin.site.register(Coupon)

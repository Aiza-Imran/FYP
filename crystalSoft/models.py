from django.db import models
from django.contrib.auth.models import User

class Permissions(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    add_expense = models.BooleanField()
    add_edit_income = models.BooleanField()
    add_new_item = models.BooleanField()
    add_purchase = models.BooleanField()
    view_dashboard = models.BooleanField()
    view_sale_invoices = models.BooleanField()
    view_reports = models.BooleanField()
    view_stock = models.BooleanField()
    view_bill_profit = models.BooleanField()
    open_new_day = models.BooleanField()
    close_day = models.BooleanField()
    attendence_of_employee = models.BooleanField()
    day_summary = models.BooleanField()
    change_sale_price = models.BooleanField()
    change_price = models.BooleanField()
    edit_invoices = models.BooleanField()
    discount_in_sale_price = models.BooleanField()
    make_receipt_voucher = models.BooleanField()
    
    def __str__(self):
        return  f"{self.user} Permission Set"
    
        
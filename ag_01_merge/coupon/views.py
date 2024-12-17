from django.shortcuts import render




# @require_POST

# def add_coupon(request):
#   now = timezone.now()
#   form = AddCouponForm(request.POST)
#   if form.is_valid():
#     code = form.cleaned_data['code']

#     try:
#       coupon = Coupon.objects.get(code__iexact=code, use_from__lte=now,
#                                   use_to__gte=now, active=True)
   
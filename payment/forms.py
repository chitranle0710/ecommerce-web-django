from django import forms
from .models import ShippingAddress

class ShippingForm(forms.ModelForm):
	shipping_full_name = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Tên đầy đủ'}), required=True)
	shipping_email = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email'}), required=True)
	shipping_address1 = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Đia chỉ 1'}), required=True)
	shipping_address2 = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Địa chỉ 2'}), required=False)
	shipping_city = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Thành phố'}), required=True)
	shipping_state = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Quận'}), required=False)
	shipping_zipcode = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Mã bưu chính'}), required=False)
	shipping_country = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Quốc gia'}), required=True)

	class Meta:
		model = ShippingAddress
		fields = ['shipping_full_name', 'shipping_email', 'shipping_address1', 'shipping_address2', 'shipping_city', 'shipping_state', 'shipping_zipcode', 'shipping_country']

		exclude = ['user',]



class PaymentForm(forms.Form):
	card_name =  forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Tên trên thẻ'}), required=True)
	card_number =  forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Số thẻ'}), required=True)
	card_exp_date =  forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ngày hết hạn'}), required=True)
	card_cvv_number =  forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Mã CVV'}), required=True)
	card_address1 =  forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Hóa đơn địa chỉ 1'}), required=True)
	card_address2 =  forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Hóa đơn địa chỉ 2'}), required=False)
	card_city =  forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Thành phố'}), required=True)
	card_state = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Quận'}), required=True)
	card_zipcode =  forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Mã bưu chính'}), required=True)
	card_country =  forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Quốc gia'}), required=True)
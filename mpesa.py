from datetime import datetime
from pytz import timezone
import requests

# def lipa_na_mpesa_online(request):
#     access_token = MpesaAccessToken.validated_mpesa_access_token
#     api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
#     headers = {"Authorization": "Bearer %s" % access_token}
#     request = {
#         "BusinessShortCode": LipanaMpesaPpassword.Business_short_code,
#         "Password": LipanaMpesaPpassword.decode_password,
#         "Timestamp": LipanaMpesaPpassword.lipa_time,
#         "TransactionType": "CustomerBuyGoodsOnline",
#         "Amount": 1,
#         "PartyA": 254708374149,  # replace with your phone number to get stk push
#         "PartyB": LipanaMpesaPpassword.Business_short_code,
#         "PhoneNumber": 254708374149,  # replace with your phone number to get stk push
#         "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",
#         "AccountReference": "Henry",
#         "TransactionDesc": "Testing stk push"
#      }

#      response = requests.post(api_url, json=request, headers=headers)
#      return HttpResponse('success')

def send():
    time = str(datetime.now()).split(".")[0].replace(":","").replace("-","").replace(" ", "")
    headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer N4m4ck6B2g2iNwDVGJ8jgnaoninj'
    }

    payload = {
        # "BusinessShortCode": 174379,
        # "Password": "MTc0Mzc5YmZiMjc5ZjlhYTliZGJjZjE1OGU5N2RkNzFhNDY3Y2QyZTBjODkzMDU5YjEwZjc4ZTZiNzJhZGExZWQyYzkxOTIwMjIwNDE2MjMxNzMx",
        # "Timestamp": time,
        # "TransactionType": "CustomerPayBillOnline",
        # "Amount": 1,
        # "PartyA": 254725757067,
        # "PartyB": 174379,
        # "PhoneNumber": 254701872702,
        # "CallBackURL": "https://pulsar-2217f.uc.r.appspot.com/mpesa",
        # "AccountReference": "KwikSaf",
        # "TransactionDesc": "Soko" 
        "BusinessShortCode": 174379,
    "Password": "MTc0Mzc5YmZiMjc5ZjlhYTliZGJjZjE1OGU5N2RkNzFhNDY3Y2QyZTBjODkzMDU5YjEwZjc4ZTZiNzJhZGExZWQyYzkxOTIwMjIwNDE2MjM1ODA4",
    "Timestamp": "20220416235808",
    "TransactionType": "CustomerPayBillOnline",
    "Amount": 1,
    "PartyA": 254725757067,
    "PartyB": 174379,
    "PhoneNumber": 254701872702,
    "CallBackURL": "https://pulsar-2217f.uc.r.appspot.com/mpesa",
    "AccountReference": "CompanyXLTD",
    "TransactionDesc": "Payment of X" 
    }

    response = requests.post('https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest', headers = headers, json = payload)
    print(response.text)


send()
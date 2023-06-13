from django.shortcuts import render
import requests
import json
from django.http import JsonResponse

def index(request):
    country_codes_api = 'https://v6.exchangerate-api.com/v6/abe1b036f037ca2b7282affa/codes'
    data = {}

    if request.method == "POST":
        first_currency = request.POST.get('firstCurrency')
        second_currency = request.POST.get('secondCurrency')
        amount = float(request.POST.get('amount'))

        convert_api = f'https://v6.exchangerate-api.com/v6/abe1b036f037ca2b7282affa/pair/{first_currency}/{second_currency}/'

        get_response = requests.get(convert_api).text
        # get api response data
        convert_json = json.loads(get_response)
        # convert data from json to dictionary

        calculate = convert_json['conversion_rate'] * amount
        # calculate result based on amount entered by user

        data['result_convert'] = round(calculate, 2)
        # round a number to 2 decimal places

        data["success"] = True
        # create a dictionary value that indicates the operation was successful

        return JsonResponse(data)

    codes_response_text = requests.get(country_codes_api).text
    codes_json = json.loads(codes_response_text)

    context = {
        'codes': codes_json['supported_codes']
    }

    return render(request, 'index.html', context)

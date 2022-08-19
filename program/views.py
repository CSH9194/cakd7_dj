import re
from django.shortcuts import render


def inputdata(request):
    return render(
        request,
        'program/inputdata.html',
    )


def result(request):
    # lis=[]
    # lis.append(request.GET['a'])
    # lis.append(request.GET['b'])

    # sum = 0
    # for l in lis:
    #     sum += int(l)

    # ans = sum


    # bmi구하기 #
    a = int(request.GET['height'])
    b = int(request.GET['weight'])

    ans = round(b/((a/100)**2), 2)

    if ans >= 40:
        result = '초고도비만'
    elif ans >=30:
        result = '고도비만'
    elif ans >=25:
        result = '경도비만'
    elif ans >=23:
        result = '과체중'
    elif ans >=18.5:
        result = '정상체중'
    else:
        result = '저체중'

    return render(
        request,
        'program/result.html',
        {'ans':ans, 'result':result}
    )

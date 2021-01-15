#Django
from django.http import HttpResponse, JsonResponse
import json

def sort_ed(request):
    """ return  """

    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    sort_numbers = sorted(numbers)
    data = {
        'Status': 'ok',
        'numbers': sort_numbers,
        'message': 'Integers sorted successfully'
    }
    return JsonResponse(data, safe=False)

def say_hi(request, name, age):
    """ Say a greeting """
    if age < 12:
        message = 'Sorry {}, you are not alloweb here'.format(name)
    else:
        message = "Hello {}, Welcome tu platzigram".format(name)
    return HttpResponse(message)

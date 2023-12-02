from django.http import HttpResponse

def index(request):
    tabl = ''.join([''.join([f'{x*y}\t' for x in range(1,11)])+'\n' for y in range(1,11)])
    return HttpResponse(tabl)

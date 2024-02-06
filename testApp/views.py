from django.shortcuts import render
import datetime

# Create your views here.
def templateView(request):

    date = datetime.datetime.now()
    dict = {

        'date_msg':date
    }
    return render(request, 'testAppTemplates/wish.html', context=dict)

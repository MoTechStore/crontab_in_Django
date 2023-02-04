from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.db import connection


def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]




def index(request):
    """
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM feedback")
    feed = dictfetchall(cursor)



    cursor.execute("SELECT * FROM web_db.employee")
    emp = dictfetchall(cursor)


    context = {'feed':feed, 'emp':emp}
    
    return render(request, 'core\index.html', context)
    """
    return HttpResponse('Hello Django')


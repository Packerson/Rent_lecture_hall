from django.shortcuts import render
from django.http import HttpResponse, Http404
from hall_lecture.models import Hall, Booked
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime


# Create your views here.
def main_site(request):
    response = HttpResponse()
    response = render(request, 'main_site.html')
    return response


@csrf_exempt
def add_hall(request):
    response = HttpResponse()
    if request.method == "GET":
        response = render(request, 'add_hall.html')
        return response
    elif request.method == "POST":
        if request.POST.get("hall_name") and request.POST.get("hall_capacity"):
            # my_hall = Hall.objects.get()
            hall_name_check = request.POST.get("hall_name")
            try:
                if Hall.objects.get(hall_name=hall_name_check):
                    # if hall_name == hall_name_check:
                    response.write(f"{hall_name_check},  hall name has to be unique")
                    return response
            except:
                if request.POST.get("hall_capacity").isnumeric():
                    if int(request.POST.get("hall_capacity")) > 0:
                        hall_capacity = int(request.POST.get("hall_capacity"))
                    else:
                        response.write(f"Add hall capacity")
                        return response
                    if request.POST.get("projector"):
                        projector = True
                    else:
                        projector = False
                    new_hall = Hall()
                    hall_name = request.POST.get("hall_name")
                    new_hall.hall_name = hall_name
                    new_hall.hall_capacity = hall_capacity
                    new_hall.projector = projector
                    new_hall.save()
                    response = render(request, 'add_hall.html')
                    response.write(f"New lecture hall '{hall_name}' add to base!")
                    return response
                response.write(f"capacity need to be a natural number")
                return response
        response.write("add hall name")
        return response


def list_all_halls(request):
    response = HttpResponse()
    if request.method == "GET":
        args = {}
        if len(Hall.objects.all()) == 0:
            response.write("There is no lecture hall")
            return response
        args['hall_list'] = Hall.objects.all()
        response = render(request, 'list_all_halls.html', args)
        return response


@csrf_exempt
def hall_modify(request, hall_id):
    response = HttpResponse()
    if request.method == "GET":
        args = {}
        args['hall_to_edit'] = Hall.objects.get(pk=hall_id)
        response = render(request, 'modify_hall.html', args)
        return response
    elif request.method == "POST":
        if request.POST.get("hall_name") and request.POST.get("hall_capacity"):
            # my_hall = Hall.objects.get()
            hall_name_check = request.POST.get("hall_name")
            try:
                if Hall.objects.get(hall_name=hall_name_check):
                    response.write(f"{hall_name_check},  hall name has to be unique")
                    return response
            except:
                if int(request.POST.get("hall_capacity")) > 0:
                    hall_capacity = int(request.POST.get("hall_capacity"))
                else:
                    response.write(f"Add hall capacity")
                    return response
                if request.POST.get("projector"):
                    projector = True
                else:
                    projector = False
                new_hall = Hall.objects.get(pk=hall_id)
                new_hall.hall_name = hall_name_check
                new_hall.hall_capacity = hall_capacity
                new_hall.projector = projector
                new_hall.save()
                response.write(
                    f"Edited hall '{hall_name_check}'! <br> <a href='http://127.0.0.1:8000/room/list-all'>Hall list</a></label>")
                return response
        response.write("add hall name")
        return response


def hall_delete(request, hall_id):
    response = HttpResponse()
    if request.method == "GET":
        response.write(f"Hall of number {hall_id} is deleted")
        hall_to_delete = Hall.objects.get(pk=hall_id)
        hall_to_delete.delete()
        response.write(f'<label> <a href="http://127.0.0.1:8000/room/list-all">Hall list</a></label>')
        return response


@csrf_exempt
def hall_booked(request, hall_id):
    response = HttpResponse()
    args_details = {}
    # hall_to_booked = Hall.objects.get(pk=hall_id)
    hall = Hall.objects.get(pk=hall_id)
    args_details['hall_details_list'] = Hall.objects.get(pk=hall_id)
    args_details['hall_booking'] = (
        Booked.objects.filter(id_lecture_hall=hall).filter(booked_date__gte=datetime.today()).order_by('booked_date'))

    if request.method == "GET":
        response = render(request, 'hall_booked.html', args_details)
        return response
    elif request.method == "POST":
        comment_booked = request.POST.get('comment_booked')
        data_field = request.POST.get('date_field')
        if Booked.objects.filter(booked_date=data_field, id_lecture_hall=hall_id):
            response.write(f'Hall is already booked on this date')
            return response
        if data_field < str(datetime.today()):
            response.write(f'Cant booked old date')
            return response
        else:
            new_booked = Booked.objects.create(booked_date=data_field, comment=comment_booked,
                                               id_lecture_hall=hall)

            response = render(request, 'hall_booked.html', args_details)
            response.write(f"Booked on date {data_field} , hall id {hall_id}")
            response.write(f''
                           f'<label> <a href="http://127.0.0.1:8000/room/{hall_id}">Hall details</a></label>')

            return response


def hall_details(request, hall_id):
    response = HttpResponse()
    args_details = {}
    hall = Hall.objects.get(pk=hall_id)
    args_details['hall_details_list'] = Hall.objects.get(pk=hall_id)
    args_details['hall_booking'] = (
        Booked.objects.filter(id_lecture_hall=hall).filter(booked_date__gte=datetime.today()).order_by('booked_date'))
    response = render(request, 'hall_details.html', args_details)
    return response

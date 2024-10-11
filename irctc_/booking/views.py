# pylint: disable=no-member


from django.http import JsonResponse
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from django.db import transaction
from .models import Train, Booking

@csrf_exempt
def register_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            user = User.objects.create_user(username=username, password=password)
            return JsonResponse({'status': 'User registered successfully'}, status=201)
        return JsonResponse({'error': 'Invalid data'}, status=400)


@csrf_exempt
def add_train(request):
    if request.method == 'POST':
        train_name = request.POST.get('train_name')
        source = request.POST.get('source')
        destination = request.POST.get('destination')
        total_seats = request.POST.get('total_seats')

        if train_name and source and destination and total_seats:
            train = Train.objects.create(
                train_name=train_name,
                source=source,
                destination=destination,
                total_seats=total_seats,
                available_seats=total_seats
            )
            return JsonResponse({'status': 'Train added successfully'}, status=201)
        return JsonResponse({'error': 'Invalid data'}, status=400)


@csrf_exempt
def check_seat_availability(request):
    if request.method == 'GET':
        source = request.GET.get('source')
        destination = request.GET.get('destination')

        if source and destination:
            trains = Train.objects.filter(source=source, destination=destination)
            result = [{'train': train.train_name, 'available_seats': train.available_seats} for train in trains]
            return JsonResponse(result, safe=False)
        return JsonResponse({'error': 'Invalid source or destination'}, status=400)


@csrf_exempt
@transaction.atomic
def book_seat(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        train_id = request.POST.get('train_id')

        user = User.objects.get(id=user_id)
        train = Train.objects.get(id=train_id)

        if train.available_seats > 0:
            train.available_seats -= 1
            train.save()

            booking = Booking.objects.create(user=user, train=train, seat_number=train.total_seats - train.available_seats)
            return JsonResponse({'status': 'Seat booked successfully', 'seat_number': booking.seat_number}, status=201)
        return JsonResponse({'error': 'No seats available'}, status=400)

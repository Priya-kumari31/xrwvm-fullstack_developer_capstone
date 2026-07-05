from django.http import JsonResponse
from django.contrib.auth import login, authenticate
from django.views.decorators.csrf import csrf_exempt
import json

from .models import CarMake, CarModel, Dealer, Review
from .populate import initiate


# LOGIN
@csrf_exempt
def login_user(request):
    data = json.loads(request.body)
    user = authenticate(username=data['userName'], password=data['password'])

    if user:
        login(request, user)
        return JsonResponse({"userName": user.username, "status": "Authenticated"})

    return JsonResponse({"status": "Failed"})


# CARS (REAL DB)
def get_cars(request):
    if CarMake.objects.count() == 0:
        initiate()

    cars = CarModel.objects.select_related('car_make')

    data = [
        {
            "CarModel": c.name,
            "CarMake": c.car_make.name
        }
        for c in cars
    ]

    return JsonResponse({"CarModels": data})


# DEALERSHIPS (REAL DB)
def get_dealerships(request):
    dealers = Dealer.objects.all()

    data = [
        {"id": d.id, "name": d.name}
        for d in dealers
    ]

    return JsonResponse({"dealerships": data})


# REVIEWS (FILTER BY DEALER)
def get_dealer_reviews(request):
    dealer_id = request.GET.get('dealer_id')

    if dealer_id:
        reviews = Review.objects.filter(dealer_id=dealer_id)
    else:
        reviews = Review.objects.all()

    data = [
        {"id": r.id, "dealer": r.dealer_id, "review": r.review}
        for r in reviews
    ]

    return JsonResponse({"reviews": data})


# ADD REVIEW (POST API)
@csrf_exempt
def add_review(request):
    data = json.loads(request.body)

    review = Review.objects.create(
        dealer_id=data['dealer_id'],
        review=data['review']
    )

    return JsonResponse({
        "id": review.id,
        "status": "Review Added"
    })
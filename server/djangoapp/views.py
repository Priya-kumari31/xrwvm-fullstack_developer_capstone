from django.http import JsonResponse
from django.contrib.auth import login, authenticate
from django.views.decorators.csrf import csrf_exempt
import json

from .models import CarMake, CarModel, Dealer, Review
from .populate import initiate
from .restapis import get_request, sentiment_analyzer_url


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
    if "state" in request.GET:
        response = get_request("/fetchDealers/" + request.GET["state"])
    else:
        response = get_request("/fetchDealers")

    return JsonResponse({"dealerships": response}, safe=False)


# REVIEWS (FILTER BY DEALER)
def get_dealer_reviews(request):
    dealer_id = request.GET.get("dealer_id")

    reviews = Review.objects.filter(dealer_id=dealer_id)

    data = []

    for r in reviews:
        data.append({
            "id": r.id,
            "name": r.name,
            "dealership": int(dealer_id),
            "review": r.review,
            "car_make": r.car_make,
            "car_model": r.car_model,
            "car_year": r.car_year,
            "sentiment": r.sentiment
        })

    return JsonResponse({"reviews": data})


# ADD REVIEW (POST API)
@csrf_exempt
@csrf_exempt
def add_review(request):
    data = json.loads(request.body)

    review = Review.objects.create(
        dealer_id=data['dealership'],
        name=data['name'],
        review=data['review'],
        car_make=data['car_make'],
        car_model=data['car_model'],
        car_year=data['car_year'],
        sentiment="positive"
    )

    return JsonResponse({
        "id": review.id,
        "status": "Review Added",
        "sentiment": "positive"
    })
def get_dealer(request, dealer_id):
    response = get_request("/fetchDealer/" + str(dealer_id))
    return JsonResponse(response, safe=False)

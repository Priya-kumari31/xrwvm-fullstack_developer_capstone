from djangoapp.models import Dealer, CarMake, CarModel


def initiate():

    # Car Makes
    car_makes = [
        {
            "name": "Toyota",
            "description": "Toyota Cars"
        },
        {
            "name": "Honda",
            "description": "Honda Cars"
        },
        {
            "name": "BMW",
            "description": "BMW Cars"
        },
        {
            "name": "Ford",
            "description": "Ford Cars"
        }
    ]

    for make in car_makes:
        car_make, created = CarMake.objects.get_or_create(
            name=make["name"],
            description=make["description"]
        )

        models = {
            "Toyota": ["Camry", "Corolla"],
            "Honda": ["Civic", "Accord"],
            "BMW": ["X5", "X3"],
            "Ford": ["Mustang", "Explorer"]
        }

        for model in models[make["name"]]:
            CarModel.objects.get_or_create(
                car_make=car_make,
                name=model,
                type="Sedan",
                year=2023
            )


    # Dealers
    dealer_data = [
        {
            "full_name": "ABC Motors",
            "city": "Dallas",
            "address": "123 Main Street",
            "zip": "75001",
            "state": "Texas"
        },
        {
            "full_name": "XYZ Cars",
            "city": "Houston",
            "address": "456 Market Street",
            "zip": "77001",
            "state": "Texas"
        }
    ]

    for data in dealer_data:
        Dealer.objects.get_or_create(
            full_name=data["full_name"],
            city=data["city"],
            address=data["address"],
            zip=data["zip"],
            state=data["state"]
        )

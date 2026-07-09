from .models import Dealer

def initiate():
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
        },
        {
            "full_name": "Prime Auto",
            "city": "Austin",
            "address": "789 Lake Road",
            "zip": "73301",
            "state": "Texas"
        }
    ]

    for data in dealer_data:
        Dealer.objects.create(
            full_name=data["full_name"],
            city=data["city"],
            address=data["address"],
            zip=data["zip"],
            state=data["state"]
        )

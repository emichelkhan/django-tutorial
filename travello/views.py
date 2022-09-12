from django.shortcuts import render

from travello.models import Destination


# Create your views here.
def index(request):
    dest1 = Destination()
    dest1.name = 'Mumbai'
    dest1.desc = 'The City That Never Sleeps'
    dest1.price = 700
    dest1.img = 'destination_1.jpg'
    dest1.offer = False

    dest2 = Destination()
    dest2.name = 'Hyderabad'
    dest2.desc = 'Biriani City'
    dest2.price = 800
    dest2.img = 'destination_2.jpg'
    dest2.offer = True

    dest3 = Destination()
    dest3.name = 'Chennai'
    dest3.desc = 'City of Temples'
    dest3.price = 900
    dest3.img = 'destination_3.jpg'
    dest3.offer = False

    dest4 = Destination()
    dest4.name = 'Paris'
    dest4.desc = 'City of Eiffel Tower'
    dest4.price = 1150
    dest4.img = 'destination_4.jpg'
    dest4.offer = False

    dest5 = Destination()
    dest5.name = 'New York'
    dest5.desc = 'City of Hollywood'
    dest5.price = 1250
    dest5.img = 'destination_5.jpg'
    dest5.offer = True

    dest6 = Destination()
    dest6.name = 'London'
    dest6.desc = 'City of Big Ben'
    dest6.price = 1350
    dest6.img = 'destination_6.jpg'
    dest6.offer = False

    dest7 = Destination()
    dest7.name = 'Dubai'
    dest7.desc = 'City of Gold'
    dest7.price = 1450
    dest7.img = 'destination_7.jpg'
    dest7.offer = True

    dest8 = Destination()
    dest8.name = 'Singapore'
    dest8.desc = 'City of Gardens'
    dest8.price = 1550
    dest8.img = 'destination_8.jpg'
    dest8.offer = False

    dests = [dest1, dest2, dest3, dest4, dest5, dest6, dest7, dest8]

    return render(request, 'index.html', {'dests': dests})

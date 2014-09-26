__author__ = 'gabriele'

import os
from django.utils import timezone

def populate():

    jill = add_user('jill', 'jill@gmail.com', 'jill')
    john = add_user('john', 'john@gmail.com', 'john')
    jess = add_user('jess', 'jess@gmail.com', 'jess')

    add_user_profile(jill, 'Jesrsey')
    add_user_profile(john, 'NYC')
    add_user_profile(jess, 'Detroit')

    piscina = add_list('Piscina', timezone.now(), 0)
    checkin = add_list('Checkin', timezone.now(), 0)

    add_item(piscina, 'cuffia', False )
    add_item(piscina, 'costume', False)
    add_item(piscina, 'tessera', False)
    add_item(piscina, 'asciugamanano', False)

    add_item(checkin, 'passport', False)
    add_item(checkin, 'boarding pass', False)
    add_item(checkin, 'underwear', False)

    for u in UserProfile.objects.all():
        print u

def add_user(username, email, password):
    u = User.objects.create_user(username=username, email=email, password=password)
    return u

def add_user_profile(user, location):
    up = UserProfile.objects.get_or_create(user=user, location=location)[0]
    return up

def add_list(name, pub_date, total_check):
    l = List.objects.get_or_create(name=name, pub_date=pub_date, total_check=total_check)[0]

    return l

def add_item(list, item_text, done):
    i = Item.objects.get_or_create(list=list, item_text=item_text, done=done)[0]

    return i

if __name__ == '__main__':
    print "Starting Checkout population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'checkout_project.settings')
    from checkout.models import UserProfile, List, Item
    from django.contrib.auth.models import User
    populate()
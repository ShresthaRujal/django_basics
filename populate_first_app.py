import os
#need to configure setting LOGGING_CONFIG, therefore
#we must either define the environment variable
#DJANGO_SETTINGS_MODULE or call settings.configure() before accessing settings.
os.environ.setdefault('DJANGO_SETTINGs_MODULE', 'first_django.settings')

import django
django.setup()

import random
from first_app.models import AccessRecord,WebPage,Topic
from faker import Faker

fakegen = Faker()
topics = ['Search','Social','MarketPlace','News','Games']

def add_topic():
    t = Topic.objects.get_or_create(topic_name = random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    for entry in range(N):
        top = add_topic()
        fake_url = fakegen.url()
        fake_date =  fakegen.date()
        fake_name = fakegen.company()

        webpg = WebPage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]

        acc_rec = AccessRecord.objects.get_or_create(name= webpg,date = fake_date)[0]

if __name__=='__main__':
    print("populating script!")
    populate(20)
    print("populating complete!")

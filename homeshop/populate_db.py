import os
import sys

# script_path = os.path.dirname(__file__)
# project_dir = os.path.dirname(script_path)
# sys.path.insert(0, project_dir)

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'homeshop.settings')

import django
django.setup()

from shop.models import City, Region


regions = {
    'Minsk', 'Grodno', 'Gomel', 'Brest', 'Mogilev', 'Vitebsk'
}

cities = {
    'Minsk': {'Borisov', 'Sluck', 'Minsk', 'Molodechno', 'Uzda'},
    'Grodno': {'Grodno', 'Slonim', 'Lida', 'Volkovysk', 'Novogrudok', 'Shuchin'},
    'Gomel': {'Gomel', 'Mozyr', 'Kalinkovichi', 'Petrikov', 'Novoelna', },
    'Brest': {'Brest', 'Baranovichi', 'Pinsk', 'Kobrin', 'Bereza', 'Luninec'},
    'Mogilev': {'Mogilev', 'Bobruisk', 'Gorki', 'Osipovichi', 'Krichev', 'Shklov'},
    'Vitebsk': {'Vitebsk', 'Polotsk', 'Novopolotsk', 'Orsha', 'Postavy', 'Lepel'},
}


def populate():
    for region_name in regions:
        region = Region.objects.get_or_create(name=region_name)[0]
        if region:
            print("region" + region.name + "created")
            for city_name in cities[region_name]:
                city = City.objects.get_or_create(name=city_name, region=region)[0]
                if region:
                    print("city" + city.name + " created")
                else:
                    pass
                    # print(f"WARNING city {city.name} wsn't created")
        else:
            pass
            # print(f"WARNING region {region.name} wasn't created")


# Start execution here!
if __name__ == '__main__':
    print("Starting population script...")
    populate()

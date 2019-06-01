# Descriptions
this project works with geo points.
it search your inserted point and find nearest points.
you can improve it by adding more points to csv file.

# SETUP

create your own setting_local.py like setting_local.example.

## Installation

install requierementd
```bash
pip install -r requirements.txt
```

load data to database
```bash
python manage.py loaddata location/fixtures/locations.json
```

## Usage

```python
reverse_geocoder.RGeocoder(mode=2, verbose=True,
                     stream=io.StringIO(open('location/city_reverse_geo.csv', encoding='utf-8').read()))
coordinates = (latitude, longitude),
results = rg.search(coordinates)

ids = []
for result in results:
    ids.append(result['name'])

cities = City.objects.filter(pk__in=ids)
```

## Demo
location.developtools.ir/search/?place=33.481832,50.457210
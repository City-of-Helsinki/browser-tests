import pytest

ADDRESSES = [
    {
        'path': 'address/Espoo/Veräjäpellonkatu/15',
        'location': {
            'lat': 60.2257708,
            'lng': 24.8041296},
        'name': 'Veräjäpellonkatu 15, Espoo'

    },
    {
        'path': 'address/Espoo/Kamreerintie/3',
        'location': {
            'lat': 60.2042426,
            'lng': 24.6560127},
        'name': 'Kamreerintie 3, Espoo'}]

UNITS = [
    {
        'path': 'unit/41047',
        'name': 'Uimastadion / Maauimala',
        'location': {
            'lat': 60.188812,
            'lng': 24.930822
        }
    },
    {
        'path': 'unit/41047?bbox=60.18672,24.92038,60.19109,24.93742',
        'name': 'Uimastadion / Maauimala',
        'location': {
            'lat': 60.188812,
            'lng': 24.930822
        },
        'bbox': [
            [60.18672, 24.92038],
            [60.19109, 24.93742]
        ]
    },
    {
        'path': 'unit/40823',
        'name': 'Kumpulan maauimala',
        'location': {
            'lat': 60.208702,
            'lng': 24.958284
        }
    },
    {
        'path': 'unit/40823?bbox=60.20661,24.94783,60.21098,24.96489',
        'name': 'Kumpulan maauimala',
        'location': {
            'lat': 60.208702,
            'lng': 24.958284
        },
        'bbox': [
            [60.20661, 24.94783],
            [60.21098, 24.96489]
        ]
    }
]

SERVICES = [
    {
        'path': 'unit?service=25002&bbox=60.13744,24.77468,60.20935,25.04703&city=helsinki',
        'bbox': [
            [60.13744, 24.77468],
            [60.20935, 25.04703]
        ]
    },
    {
        'path': 'unit?service=25010&bbox=60.13744,24.77468,60.20935,25.04703&city=helsinki',
        'bbox': [
            [60.13744, 24.77468],
            [60.20935, 25.04703]
        ]
    }

]


@pytest.fixture(params=ADDRESSES)
def address_embed(request):
    return request.param


@pytest.fixture(params=UNITS)
def unit_embed(request):
    return request.param


@pytest.fixture(params=SERVICES)
def service_embed(request):
    return request.param

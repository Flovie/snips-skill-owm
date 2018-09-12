# -*- coding: utf-8 -*-
from enum import Enum


class SnipsWeatherConditions(Enum):
    HUMID = 0
    BLIZZARD = 1
    SNOWFALL = 2
    WINDY = 3
    CLOUD = 4
    RAINY = 5
    STORMY = 6
    SUN = 7
    SNOW = 8
    FOG = 9
    DEPRESSION = 10
    STORM = 11
    RAINFALL = 12
    SNOWY = 13
    SUNNY = 14
    RAIN = 15
    HAIL = 16
    FOGGY = 17
    OVERCAST = 18
    CLOUDY = 19
    HUMIDITY = 20
    SNOWSTORM = 21
    WIND = 22
    TRENCH_COAT = 23  # TODO REMOVE WHEN INTENT 'ITEM' WILL BE INDEPENDENTLY MANAGE
    PARKA = 24
    CARDIGAN = 25
    SUMMER_CLOTHING = 26
    GAMP = 27
    BROLLY = 28
    SUNSHADE = 29
    PARASOL = 30
    UMBRELLA = 31
    OPEN_TOED_SHOES = 32
    SHORTS = 33
    SKIRT = 34
    WARM_JUMPER = 35
    WARM_SOCKS = 36
    WARM_SWEATER = 37
    SCARF = 38
    STRAW_HAT = 39
    HAT = 40
    SUNBLOCK = 41
    SUNSCREEN = 42
    SUN_CREAM = 43
    WOOLEN_SWEATER = 44
    WOOLEN_JUMPER = 45
    WOOLEN_SOCKS = 46
    WOOLEN_TIGHTS = 47
    SLEEVELESS_SUNDRESS = 48
    SUNDRESS = 49
    CHUNKY_SWEATER = 50
    SUNGLASSES = 51
    RAINCOAT = 52


mappings = {
    SnipsWeatherConditions.HUMID: {
        'fr_FR': [u'humide'],
        'en_US': [u'humid'],
		'de_DE': [u'schwül']
    },
    SnipsWeatherConditions.BLIZZARD: {
        'fr_FR': [u'blizzard'],
        'en_US': [u'blizzard'],
		'de_DE': [u'Blitzeis']
    },
    SnipsWeatherConditions.SNOWFALL: {
        'fr_FR': [u'chutes de neige'],
        'en_US': [u'snowfall'],
		'de_DE': [u'Schneefall']
    },
    SnipsWeatherConditions.WINDY: {
        'fr_FR': [u''],
        'en_US': [u'windy'],
		'de_DE': [u'windig']
    },
    SnipsWeatherConditions.CLOUD: {
        'fr_FR': [u'nuage', u'nuages'],
        'en_US': [u'cloud', u'clouds'],
		'de_DE': [u'wolke', u'wolken']
    },
    SnipsWeatherConditions.RAINY: {
        'fr_FR': [u'pluvieux'],
        'en_US': [u'rainy'],
		'de_DE': [u'regnerisch']
    },
    SnipsWeatherConditions.STORMY: {
        'fr_FR': [u''],
        'en_US': [u'stormy'],
		'de_DE': [u'stürmisch']
    },
    SnipsWeatherConditions.SUN: {
        'fr_FR': [u'soleil'],
        'en_US': [u'sun'],
		'de_DE': [u'Sonne']
    },
    SnipsWeatherConditions.SNOW: {
        'fr_FR': [u'neige', u'neiger', u'neigera'],
        'en_US': [u'snow'],
		'de_DE': [u'Schnee']
    },
    SnipsWeatherConditions.FOG: {
        'fr_FR': [u'brouillard'],
        'en_US': [u'fog'],
		'de_DE': [u'Nebel']
    }, SnipsWeatherConditions.DEPRESSION: {
        'fr_FR': [u'dépression'],
        'en_US': [u'depression'],
		'de_DE': [u'Tief']
    },
    SnipsWeatherConditions.STORM: {
        'fr_FR': [u'tempête'],
        'en_US': [u'storm'],
		'de_DE': [u'Sturm']
    },
    SnipsWeatherConditions.RAINFALL: {
        'fr_FR': [u'précipitations'],
        'en_US': [u'rainfall'],
		'de_DE': [u'Niederschlag']
    },
    SnipsWeatherConditions.SNOWY: {
        'fr_FR': [u'neigeux'],
        'en_US': [u'snowy'],
		'de_DE': [u'schneeig']
    },
    SnipsWeatherConditions.SUNNY: {
        'fr_FR': [u'ensoleillé'],
        'en_US': [u'sunny'],
		'de_DE': [u'sonnig']
    },
    SnipsWeatherConditions.RAIN: {
        'fr_FR': [u'pluie'],
        'en_US': [u'rain'],
		'de_DE': [u'Regen']
    },
    SnipsWeatherConditions.HAIL: {
        'fr_FR': [u'grêle'],
        'en_US': [u'hail'],
		'de_DE': [u'Hagel']
    },
    SnipsWeatherConditions.FOGGY: {
        'fr_FR': [u''],
        'en_US': [u'foggy'],
		'de_DE': [u'neblig']
    },
    SnipsWeatherConditions.OVERCAST: {
        'fr_FR': [u'couvert'],
        'en_US': [u'overcast'],
		'de_DE': [u'bedeckt']
    },
    SnipsWeatherConditions.CLOUDY: {
        'fr_FR': [u'nuageux'],
        'en_US': [u'cloudy'],
		'de_DE': [u'bewölkt']
    },
    SnipsWeatherConditions.HUMIDITY: {
        'fr_FR': [u'humidité'],
        'en_US': [u'humidity'],
		'de_DE': [u'Luftfeuchte']
    }, SnipsWeatherConditions.SNOWSTORM: {
        'fr_FR': [u'tempête de neige'],
        'en_US': [u'snowstorm'],
		'de_DE': [u'Schneesturm']
    },
    SnipsWeatherConditions.WIND: {
        'fr_FR': [u'vent'],
        'en_US': [u'wind'],
		'de_DE': [u'Wind']
    },
    SnipsWeatherConditions.TRENCH_COAT: {
        'fr_FR': [u'trench'],
        'en_US': [u'trench coat'],
		'de_DE': [u'Regenmantel', u'Mantel']
    },
    SnipsWeatherConditions.PARKA: {
        'fr_FR': [u'parka'],
        'en_US': [u'parka'],
		'de_DE': [u'Anorak', u'Parka']
    },
    SnipsWeatherConditions.CARDIGAN: {
        'fr_FR': [u'cardigan'],
        'en_US': [u'cardigan'],
		'de_DE': [u'Strickjacke', u'Cardigan']
    },
    SnipsWeatherConditions.SUMMER_CLOTHING: {
        'fr_FR': [u''],
        'en_US': [u'summer clothing'],
		'de_DE': [u'Sommerkleidung']
    },
    SnipsWeatherConditions.GAMP: {
        'fr_FR': [u'parapluie'],
        'en_US': [u'gamp'],
		'de_DE': [u'Schirm']
    },
    SnipsWeatherConditions.BROLLY: {
        'fr_FR': [u'parapluie'],
        'en_US': [u'brolly'],
		'de_DE': [u'Regenschirm']
    },
    SnipsWeatherConditions.SUNSHADE: {
        'fr_FR': [u'parasol'],
        'en_US': [u'sunshade']
		'de_DE': [u'Sonnenschirm']
    },
    SnipsWeatherConditions.PARASOL: {
        'fr_FR': [u'parasol'],
        'en_US': [u'parasol'],
		'de_DE': [u'Sonnenschirm']
    },
    SnipsWeatherConditions.UMBRELLA: {
        'fr_FR': [u'parapluie'],
        'en_US': [u'umbrella'],
		'de_DE': [u'Regenschirm']
    }, SnipsWeatherConditions.OPEN_TOED_SHOES: {
        'fr_FR': [u'sandales'],
        'en_US': [u'open toed shoes'],
		'de_DE': [u'Sandalen']
    },
    SnipsWeatherConditions.SHORTS: {
        'fr_FR': [u'short'],
        'en_US': [u'shorts'],
		'de_DE': [u'kurze Hosen']
    },
    SnipsWeatherConditions.SKIRT: {
        'fr_FR': [u'jupe'],
        'en_US': [u'skirt'],
		'de_DE': [u'Rock']
    },
    SnipsWeatherConditions.WARM_JUMPER: {
        'fr_FR': [u''],
        'en_US': [u'warm jumper'],
		'de_DE': [u'']
    },
    SnipsWeatherConditions.WARM_SOCKS: {
        'fr_FR': [u'chausettes chaudes'],
        'en_US': [u'warm socks'],
		'de_DE': [u'warme Socken']
    },
    SnipsWeatherConditions.WARM_SWEATER: {
        'fr_FR': [u''],
        'en_US': [u'warm sweater'],
		'de_DE': [u'warmer Pullover']
    },
    SnipsWeatherConditions.SCARF: {
        'fr_FR': [u'écharpe'],
        'en_US': [u'scarf'],
		'de_DE': [u'Schal']
    },
    SnipsWeatherConditions.STRAW_HAT: {
        'fr_FR': [u'chapeau de paille'],
        'en_US': [u'straw hat'],
		'de_DE': [u'Strohhut']
    },
    SnipsWeatherConditions.HAT: {
        'fr_FR': [u'chapeau'],
        'en_US': [u'hat'],
		'de_DE': [u'Hut']
    },
    SnipsWeatherConditions.SUNBLOCK: {
        'fr_FR': [u'crème solaire'],
        'en_US': [u'sunblock'],
		'de_DE': [u'Sonnencreme']
    },
    SnipsWeatherConditions.SUNSCREEN: {
        'fr_FR': [u'écran solaire'],
        'en_US': [u'sunscreen'],
		'de_DE': [u'Sonnenschutz']
    }, SnipsWeatherConditions.SUN_CREAM: {
        'fr_FR': [u'crème solaire'],
        'en_US': [u'sun cream'],
		'de_DE': [u'Sonnencreme']
    },
    SnipsWeatherConditions.WOOLEN_SWEATER: {
        'fr_FR': [u''],
        'en_US': [u'woolen sweater'],
		'de_DE': [u'Wollpullover']
    },
    SnipsWeatherConditions.WOOLEN_JUMPER: {
        'fr_FR': [u''],
        'en_US': [u'woolen jumper'],
		'de_DE': [u'']
		},
    SnipsWeatherConditions.WOOLEN_TIGHTS: {
        'fr_FR': [u''],
        'en_US': [u'woolen tights'],
		'de_DE': [u'Strumpfhosen']
    },
    SnipsWeatherConditions.SLEEVELESS_SUNDRESS: {
        'fr_FR': [u''],
        'en_US': [u'sleeveless sundress'],
		'de_DE': [u'Sommerkleid']
    },
    SnipsWeatherConditions.SUNDRESS: {
        'fr_FR': [u''],
        'en_US': [u'sundress'],
		'de_DE': [u'']
    },
    SnipsWeatherConditions.CHUNKY_SWEATER: {
        'fr_FR': [u''],
        'en_US': [u'chunky sweater'],
		'de_DE': [u'dicker Pullover']
    },
    SnipsWeatherConditions.SUNGLASSES: {
        'fr_FR': [u'lunettes de soleil'],
        'en_US': [u'sunglasses'],
		'de_DE': [u'Sonnenbrille']
    },
    SnipsWeatherConditions.RAINCOAT: {
        'fr_FR': [u'manteau pour la pluie'],
        'en_US': [u'raincoat'],
		'de_DE': [u'Regenjacke']
    },
    SnipsWeatherConditions.WOOLEN_SOCKS: {
        'fr_FR': [u'chaussettes en laine'],
        'en_US': [u'woolen socks'],
		'de_DE': [u'Wintersocken']
    }
}

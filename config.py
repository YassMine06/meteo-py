"""
Configuration centralisée pour l'application météo
"""

# URLs des APIs
API_BASE_URL = "https://api.open-meteo.com/v1/forecast"
GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search"
AIR_QUALITY_URL = "https://air-quality-api.open-meteo.com/v1/air-quality"

# Configuration du cache (en secondes)
CACHE_TTL_WEATHER = 900  # 15 minutes
CACHE_TTL_GEOCODING = 3600  # 1 heure
CACHE_TTL_AIR_QUALITY = 3600  # 1 heure

# Villes prédéfinies
PREDEFINED_CITIES = [
    "Casablanca", "Rabat", "Marrakech", "Fès", "Tanger", "Agadir",
    "Paris", "London", "New York", "Tokyo", "Dubai", "Berlin",
    "Madrid", "Rome", "Cairo", "Istanbul", "Moscow", "Sydney",
    "Toronto", "Los Angeles", "Singapore", "Mumbai", "Beijing"
]

# Codes météo Open-Meteo
WEATHER_CODES = {
    0: {"desc": "☀️ Ciel dégagé", "category": "sunny"},
    1: {"desc": "🌤️ Principalement dégagé", "category": "sunny"},
    2: {"desc": "⛅ Partiellement nuageux", "category": "cloudy"},
    3: {"desc": "☁️ Couvert", "category": "cloudy"},
    45: {"desc": "🌫️ Brouillard", "category": "cloudy"},
    48: {"desc": "🌫️ Brouillard givrant", "category": "cloudy"},
    51: {"desc": "🌦️ Bruine légère", "category": "rainy"},
    53: {"desc": "🌦️ Bruine modérée", "category": "rainy"},
    55: {"desc": "🌦️ Bruine dense", "category": "rainy"},
    61: {"desc": "🌧️ Pluie légère", "category": "rainy"},
    63: {"desc": "🌧️ Pluie modérée", "category": "rainy"},
    65: {"desc": "🌧️ Pluie forte", "category": "rainy"},
    71: {"desc": "🌨️ Neige légère", "category": "snowy"},
    73: {"desc": "🌨️ Neige modérée", "category": "snowy"},
    75: {"desc": "❄️ Neige forte", "category": "snowy"},
    77: {"desc": "🌨️ Grêle", "category": "snowy"},
    80: {"desc": "🌦️ Averses légères", "category": "rainy"},
    81: {"desc": "⛈️ Averses modérées", "category": "rainy"},
    82: {"desc": "⛈️ Averses violentes", "category": "rainy"},
    85: {"desc": "🌨️ Averses de neige légères", "category": "snowy"},
    86: {"desc": "❄️ Averses de neige fortes", "category": "snowy"},
    95: {"desc": "⚡ Orage", "category": "stormy"},
    96: {"desc": "⚡ Orage avec grêle", "category": "stormy"},
    99: {"desc": "⚡ Orage violent avec grêle", "category": "stormy"}
}

# Thème Premium Unifié
THEME_COLORS = {
    "premium": {
        "primary": "#4facfe", # Bleu ciel vibrant
        "secondary": "#00f2fe", # Cyan vibrant
        "background": "rgba(20, 30, 48, 0.9)", # Bleu nuit profond
        "card": "rgba(255, 255, 255, 0.1)", # Blanc translucide
        "text": "#FFFFFF",
        "text_secondary": "rgba(255, 255, 255, 0.85)"
    }
}

# Gradients pour les backgrounds dynamiques (Plus subtils et élégants)
WEATHER_GRADIENTS = {
    "sunny": "linear-gradient(135deg, #fce38a 0%, #f38181 100%)", # Sunset warm
    "cloudy": "linear-gradient(135deg, #5f72bd 0%, #9b23ea 100%)", # Mystic purple
    "rainy": "linear-gradient(135deg, #3a6186 0%, #89253e 100%)", # Moody blue/red
    "snowy": "linear-gradient(135deg, #E0EAFC 0%, #CFDEF3 100%)", # Cold white/blue
    "stormy": "linear-gradient(135deg, #232526 0%, #414345 100%)"  # Dark storm
}

# Seuils pour les alertes
ALERT_THRESHOLDS = {
    "temp_high": 35,  # °C
    "temp_low": 0,    # °C
    "wind_high": 50,  # km/h
    "precipitation_high": 20,  # mm
    "aqi_poor": 80
}

# Configuration de l'export PDF
PDF_CONFIG = {
    "page_size": "A4",
    "margin": 50,
    "title_font_size": 24,
    "heading_font_size": 16,
    "body_font_size": 12
}

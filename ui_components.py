"""
Composants UI réutilisables pour l'application météo
"""

import streamlit as st
from typing import Dict, Any
from config import THEME_COLORS, WEATHER_GRADIENTS
from weather_analyzer import WeatherAnalyzer


def inject_custom_css(theme: str = 'premium', weather_category: str = 'sunny'):
    """
    Injecter le CSS personnalisé avec glassmorphism et animations
    
    Args:
        theme: 'premium' (unifié)
        weather_category: Catégorie météo pour le fond
    """
    # Force premium theme
    theme = 'premium'
    colors = THEME_COLORS[theme]
    gradient = WEATHER_GRADIENTS.get(weather_category, WEATHER_GRADIENTS['sunny'])
    
    st.markdown(f"""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');
        
        * {{
            font-family: 'Poppins', sans-serif;
        }}

        .stApp {{
            background: {gradient};
            background-size: cover;
            background-attachment: fixed;
        }}

        /* Overlay principal subtil pour unifier le contraste */
        .main {{
            background: linear-gradient(to bottom, rgba(0,0,0,0.2) 0%, rgba(0,0,0,0.6) 100%);
            min-height: 100vh;
        }}

        /* Animations */
        @keyframes fadeIn {{
            from {{ opacity: 0; transform: translateY(20px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}
        
        .animate-fadeIn {{
            animation: fadeIn 0.8s ease-out forwards;
        }}

        /* Glassmorphism Premium Unifié */
        .glass-card {{
            background: {colors['card']};
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            border: 1px solid rgba(255, 255, 255, 0.2);
            border-radius: 24px;
            padding: 2rem;
            color: {colors['text']};
            box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.2);
            transition: all 0.3s ease;
            margin-bottom: 2.5rem;
        }}

        .glass-card:hover {{
            background: rgba(255, 255, 255, 0.15);
            transform: translateY(-5px);
            border-color: rgba(255, 255, 255, 0.4);
            box-shadow: 0 15px 40px 0 rgba(0, 0, 0, 0.3);
        }}

        /* Hero Section */
        .hero-container {{
            text-align: center;
            padding: 3.5rem 1rem;
            margin-bottom: 6rem;
            border-radius: 40px;
            background: rgba(255, 255, 255, 0.05);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            animation: fadeIn 1.2s ease-out;
        }}

        .hero-title {{
            font-size: 4.5rem;
            font-weight: 700;
            margin: 0;
            letter-spacing: -1px;
            color: {colors['text']} !important;
            text-shadow: 0 4px 15px rgba(0,0,0,0.3);
        }}

        .hero-temp {{
            color: {colors['text']} !important;
            font-size: 7rem;
            font-weight: 200;
            margin: -15px 0;
            text-shadow: 0 4px 15px rgba(0,0,0,0.2);
        }}

        /* Tabs Stylisés */
        .stTabs [data-baseweb="tab-list"] {{
            gap: 20px;
            background-color: rgba(255, 255, 255, 0.1);
            padding: 15px;
            border-radius: 50px;
            border: 1px solid rgba(255, 255, 255, 0.15);
            margin-bottom: 6rem;
            justify-content: center;
        }}

        .stTabs [data-baseweb="tab"] {{
            height: 40px;
            background-color: transparent !important;
            border: none !important;
            color: rgba(255, 255, 255, 0.7) !important;
            font-weight: 500 !important;
            border-radius: 20px !important;
        }}

        .stTabs [aria-selected="true"] {{
            background-color: rgba(255, 255, 255, 0.25) !important;
            color: white !important;
            font-weight: 600 !important;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        }}

        /* Sidebar Glass */
        [data-testid="stSidebar"] {{
            background-color: rgba(10, 20, 35, 0.85);
            border-right: 1px solid rgba(255, 255, 255, 0.05);
            backdrop-filter: blur(20px);
        }}
        
        [data-testid="stSidebar"] * {{
            color: rgba(255, 255, 255, 0.9) !important;
        }}

        /* Scrollbar */
        ::-webkit-scrollbar {{
            width: 6px;
        }}
        ::-webkit-scrollbar-thumb {{
            background: rgba(255, 255, 255, 0.2);
            border-radius: 10px;
        }}

        /* Text shadows defaults */
        div.stMarkdown p, div.stMarkdown h1, div.stMarkdown h2, div.stMarkdown h3, 
        .stMetricValue, .stMetricLabel {{
            color: {colors['text']} !important;
            text-shadow: 0 2px 4px rgba(0,0,0,0.4);
        }}
    </style>
    """, unsafe_allow_html=True)


def create_hero_section(city_name: str, temp: float, weather_desc: str, unit: str = "°C"):
    """
    Créer la section hero avec la température
    
    Args:
        city_name: Nom de la ville
        temp: Température
        weather_desc: Description météo
        unit: Unité de température
    """
    st.markdown(f"""
    <div class="hero-container animate-fadeIn">
        <p style="font-size: 1rem; opacity: 0.8; letter-spacing: 3px; text-transform: uppercase; margin-bottom: 10px;">MÉTÉO ACTUELLE</p>
        <h1 class="hero-title">{city_name}</h1>
        <p class="hero-temp">{round(temp)}{unit}</p>
        <p style="font-size: 1.5rem; font-weight: 400; opacity: 0.9; margin-top: 5px;">{weather_desc}</p>
    </div>
    """, unsafe_allow_html=True)


def create_metric_card(icon: str, label: str, value: str, extra: str = ""):
    """
    Créer une carte de métrique glassmorphism
    """
    extra_html = f"<p style='margin: 5px 0; font-size: 0.85em; opacity: 0.7;'>{extra}</p>" if extra else ""
    
    st.markdown(f"""
    <div class="glass-card" style="margin-bottom: 20px; text-align: center; padding: 1.5rem;">
        <p style="margin:0; opacity:0.8; font-size: 0.9rem; letter-spacing: 1px; text-transform: uppercase;">{icon} {label}</p>
        <h2 style="margin: 10px 0; font-weight: 600;">{value}</h2>
        {extra_html}
    </div>
    """, unsafe_allow_html=True)


def create_forecast_card(date_str: str, day_str: str, temp_max: float, temp_min: float, precip: float, temp_color: str = "blue"):
    """
    Créer une carte de prévision quotidienne
    """
    # Gradient subtil pour les cartes de prévision
    bg_style = "background: rgba(255, 255, 255, 0.08);"
    if temp_max > 30:
        bg_style = "background: linear-gradient(135deg, rgba(255, 100, 100, 0.15), rgba(255, 255, 255, 0.05));"
    elif precip > 5:
        bg_style = "background: linear-gradient(135deg, rgba(100, 150, 255, 0.15), rgba(255, 255, 255, 0.05));"
    
    st.markdown(f"""
    <div class="glass-card" style='{bg_style} text-align: center; padding: 15px; margin-bottom: 10px; border: 1px solid rgba(255,255,255,0.15);'>
        <h4 style='margin:0; font-size: 1.1rem;'>{date_str}</h4>
        <p style='font-size: 0.85em; opacity: 0.7; text-transform: uppercase; letter-spacing: 1px;'>{day_str}</p>
        <div style="margin: 10px 0;">
            <span style="font-size: 1.4rem; font-weight: 600;">{round(temp_max)}°</span>
            <span style="font-size: 1rem; opacity: 0.6; margin-left: 5px;">{round(temp_min)}°</span>
        </div>
        <p style='font-size: 0.8em; margin-top: 5px; opacity: 0.8;'>💧 {precip}mm</p>
    </div>
    """, unsafe_allow_html=True)


def create_alert_box(alert: Dict[str, str]):
    """
    Créer une boîte d'alerte stylisée
    """
    color = "#FF9800" if alert['type'] == 'warning' else "#2196F3"
    icon = alert['icon']
    
    st.markdown(f"""
    <div class="glass-card" style="border-left: 5px solid {color}; background: rgba(0,0,0,0.2); margin-bottom: 15px; padding: 1.5rem;">
        <h4 style="margin: 0 0 0.5rem 0; color: {color}; display: flex; align-items: center; gap: 10px;">
            <span style="font-size: 1.5rem;">{icon}</span> {alert['title']}
        </h4>
        <p style="margin: 0; opacity: 0.9; font-size: 1.05rem;">{alert['message']}</p>
    </div>
    """, unsafe_allow_html=True)

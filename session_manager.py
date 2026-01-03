"""
Gestion de la session Streamlit pour les favoris, historique et préférences
"""

import streamlit as st
from typing import List, Dict, Any


class SessionManager:
    """Classe pour gérer l'état de session Streamlit"""
    
    @staticmethod
    def initialize():
        """Initialiser toutes les variables de session"""
        defaults = {
            'weather_data': None,
            'city_info': None,
            'aqi_data': None,
            'current_units': 'metric',
            'history': [],
            'theme': 'dark',
            'comparison_cities': [],
            'alerts_enabled': True
        }
        
        for key, value in defaults.items():
            if key not in st.session_state:
                st.session_state[key] = value
    
    @staticmethod
    def add_to_history(city_name: str, max_items: int = 10):
        """
        Ajouter une ville à l'historique
        
        Args:
            city_name: Nom de la ville
            max_items: Nombre maximum d'éléments dans l'historique
        """
        if 'history' not in st.session_state:
            st.session_state.history = []
        
        # Retirer si déjà présent
        if city_name in st.session_state.history:
            st.session_state.history.remove(city_name)
        
        # Ajouter au début
        st.session_state.history.insert(0, city_name)
        
        # Limiter la taille
        st.session_state.history = st.session_state.history[:max_items]
    
    @staticmethod
    def get_history() -> List[str]:
        """
        Obtenir l'historique des recherches
        
        Returns:
            Liste des villes recherchées (ordre chronologique inverse)
        """
        if 'history' not in st.session_state:
            st.session_state.history = []
        
        return st.session_state.history
    
    @staticmethod
    def clear_history():
        """Vider l'historique"""
        st.session_state.history = []
    
    @staticmethod
    def set_theme(theme: str):
        """
        Définir le thème
        
        Args:
            theme: 'dark' ou 'light'
        """
        st.session_state.theme = theme
    
    @staticmethod
    def get_theme() -> str:
        """
        Obtenir le thème actuel
        
        Returns:
            'dark' ou 'light'
        """
        if 'theme' not in st.session_state:
            st.session_state.theme = 'dark'
        
        return st.session_state.theme
    
    @staticmethod
    def toggle_theme() -> str:
        """
        Basculer entre dark et light
        
        Returns:
            Nouveau thème
        """
        current = SessionManager.get_theme()
        new_theme = 'light' if current == 'dark' else 'dark'
        SessionManager.set_theme(new_theme)
        return new_theme
    
    @staticmethod
    def set_comparison_cities(cities: List[str]):
        """
        Définir les villes pour la comparaison
        
        Args:
            cities: Liste des villes à comparer
        """
        st.session_state.comparison_cities = cities
    
    @staticmethod
    def get_comparison_cities() -> List[str]:
        """
        Obtenir les villes en comparaison
        
        Returns:
            Liste des villes
        """
        if 'comparison_cities' not in st.session_state:
            st.session_state.comparison_cities = []
        
        return st.session_state.comparison_cities

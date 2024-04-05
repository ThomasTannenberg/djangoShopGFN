"""
URL KLASSE von shop
djangoShopGFN/djangoShopGFN/shop/urls.py

Dieses Modul definiert die URL-Konfiguration für den 'shop'-Bereich
der Django-Anwendung djangoShopGFN. Es importiert Django's 'path'-Funktion
sowie die View-Funktionen aus dem aktuellen Modul, um die URL-Pfade mit den entsprechenden
Views zu verknüpfen. Die 'urlpatterns'-Liste enthält die Pfade, die definiert werden,
einschließlich der Hauptseite des Shops, des Warenkorbs und der Kasse.
Jeder Pfad ist mit einer spezifischen View-Funktion verbunden
und hat einen eindeutigen Namen, der für das Routing
und die Referenzierung in Templates und Views genutzt wird.

~ Thomas Tannenberg, 2024
"""

from django.urls import path
from . import views

urlpatterns = [
    # Der Root-Pfad ('') wird für die Hauptseite des Shops verwendet.
    # Ruft die 'shop'-View-Funktion auf, wenn die Basis-URL des Shops aufgerufen wird.
    path('', views.shop, name='shop'),

    # Definiert den Pfad für den Warenkorb. 'warenkorb/' führt zur 'warenkorb'-View,
    # die die Seite des Warenkorbs rendert.
    path('warenkorb/', views.warenkorb, name='warenkorb'),

    # Definiert den Pfad für die Kasse. 'kasse/' leitet die Anfrage an die 'kasse'-View weiter,
    # welche die Checkout-Seite des Shops anzeigt.
    path('kasse/', views.kasse, name='kasse'),
]

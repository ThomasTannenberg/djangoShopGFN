"""
HAUPT URL KLASSE
djangoShop/djangoShop/urls.py

Dieses Modul konfiguriert die zentralen URL-Routen der Django-Anwendung djangoShop.
Es ist dafür zuständig, die oberste Ebene der URL-Navigation zu definieren,
indem es sowohl die standardmäßigen Django-Admin-Pfade als auch die Anwendungs-spezifischen Pfade,
die in anderen Modulen definiert sind, einschließt.

Die 'urlpatterns'-Liste definiert hier zwei wesentliche Routen:
1. 'admin/': Leitet Anfragen an die Django-Admin-Oberfläche weiter.
Dies ermöglicht den administrativen Zugriff auf das Backend der Anwendung,
welches für die Verwaltung der Datenbankinhalte genutzt wird.

2. '': (leerer Pfad) - Dieser Pfad inkludiert die URL-Konfigurationen aus dem 'shop'-Modul,
was bedeutet, dass alle URLs, die im 'shop.urls'-Modul definiert sind,
als Unterpfade der Haupt-URL behandelt werden.
Dadurch wird eine klare Trennung der verschiedenen Anwendungsteile erreicht,
und die URL-Struktur bleibt organisiert und erweiterbar.

Das Einbinden der 'shop.urls' in die Haupt-URL-Konfiguration erlaubt
eine modulare Entwicklung der Anwendung,
indem spezifische Funktionen und Routen in separaten Modulen gehandhabt werden können.

~ Thomas Tannenberg, 2024
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [

    # Definiert den Zugriffspfad zur Django-Admin-Seite.
    # 'admin.site.urls' verweist auf eine Reihe von URLs,
    # die von Django für die Admin-Oberfläche vorgegeben sind.
    path('admin/', admin.site.urls),

    # Inkludiert die URL-Konfigurationen aus dem 'shop'-Modul.
    # Der leere String als Pfad bedeutet, dass alle im 'shop.urls'
    # definierten Pfade direkt unter dem Wurzelpfad der Anwendung verfügbar sind.
    path('', include('shop.urls')),
]


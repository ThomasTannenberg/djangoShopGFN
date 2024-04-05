"""
shop/views.py

Dieses Modul definiert die View-Funktionen für den Shop-Bereich der Django-Anwendung.
Jede Funktion ist zuständig für das Rendern einer spezifischen Seite innerhalb des Shops,
indem sie ein HTTP-Request-Objekt empfängt und als Antwort ein gerendertes HTML-Template zurückgibt.
Diese Funktionen sind direkt mit den URL-Pfaden im `urls.py`-Modul des Shop-Bereichs verknüpft,
was die Darstellung der entsprechenden Seiten im Webbrowser ermöglicht.

~ Thomas Tannenberg, 2024
"""

from django.shortcuts import render

def shop(request):
    """
    Rendert die Hauptseite des Shops.

    Nimmt ein HttpRequest-Objekt entgegen und gibt als Antwort das gerenderte Template 'shop.html' zurück.
    Dieses Template repräsentiert die Startseite des Shops, auf der Produkte oder Dienstleistungen angezeigt werden können.
    """
    return render(request, 'shop/shop.html')

def warenkorb(request):
    """
    Rendert die Warenkorb-Seite des Shops.

    Nimmt ein HttpRequest-Objekt entgegen und gibt als Antwort das gerenderte Template 'warenkorb.html' zurück.
    Auf dieser Seite können Benutzer die Produkte sehen, die sie zum Kauf ausgewählt haben, und Änderungen daran vornehmen.
    """
    return render(request, 'shop/warenkorb.html')

def kasse(request):
    """
    Rendert die Kasse-Seite des Shops.

    Nimmt ein HttpRequest-Objekt entgegen und gibt als Antwort das gerenderte Template 'warenkorb.html' zurück.
    """
    return render(request, 'shop/kasse.html')

# QR-Code-Generator und -Leser

Ein interaktives Python-Kommandozeilenprogramm zum Erstellen und Auslesen von QR-Codes. Die QR-Code-Verarbeitung erfolgt über die API von [QR Server](https://goqr.me/api/); deshalb wird eine Internetverbindung benötigt.

## Voraussetzungen

- Python 3
- Das Python-Paket `requests`
- Internetzugang

Installiere `requests`, falls es noch nicht vorhanden ist:

```bash
python3 -m pip install requests
```

Wenn du die vorhandene virtuelle Umgebung verwendest:

```bash
.venv/bin/python -m pip install requests
```

## Starten

Führe das Programm im Projektverzeichnis aus:

```bash
python3 python.py
```

Mit der virtuellen Umgebung:

```bash
.venv/bin/python python.py
```

## Menü

Gib eine der folgenden Optionen ein:

- `generate` erstellt einen QR-Code.
- `read` liest einen QR-Code aus einer lokalen Bilddatei.
- `help` zeigt die Hilfe im Programm an.
- `quit` beendet das Programm.

## QR-Code erstellen

Nach der Auswahl `generate` fragt das Programm nach Größe, Inhalt, Fehlerkorrektur, Dateiformat, Rand und Farben.

Beispielwerte:

| Eingabe | Beispiel | Hinweise |
| --- | --- | --- |
| Größe | `150x150` | Quadratisch; Rasterbilder von `10x10` bis `1000x1000` Pixeln. |
| Inhalt | `https://example.com` | Text oder Link, der im QR-Code gespeichert wird. |
| Fehlerkorrektur (`ecc`) | `M` | `L`, `M`, `Q` oder `H`; `L` ist der API-Standard. Höhere Stufen erlauben mehr Beschädigung, erzeugen aber dichtere Codes. |
| Format | `png` | `png`, `gif`, `jpeg`, `jpg`, `svg` oder `eps`. Für Rasterformate gilt maximal `1000x1000`; `svg` und `eps` sind Vektorformate. |
| Rand (`margin`) | `1` | Ganze Zahl von `0` bis `50`; API-Standard ist `1`. |
| Vordergrund (`color`) | `000000` | Hexfarbe oder RGB mit Bindestrichen, zum Beispiel `0-0-0`. |
| Hintergrund (`bgcolor`) | `ffffff` | Hexfarbe oder RGB mit Bindestrichen, zum Beispiel `255-255-255`. |

Für gute Scanbarkeit sollte der Vordergrund deutlich dunkler als der Hintergrund sein.

**Wichtig:** Das Programm speichert die Antwort derzeit immer als `qrcode.png`, auch wenn ein anderes Format ausgewählt wurde. Wähle deshalb `png`, damit Dateiendung und Bildformat übereinstimmen.

## QR-Code lesen

1. Wähle `read`.
2. Gib den Pfad zu einer lokalen Bilddatei ein, zum Beispiel `qrcode.png`.

Unterstützt werden PNG-, GIF- und JPEG-Bilder unter `1 MiB`. Das Bild wird zum Auslesen an QR Server hochgeladen. Bei Erfolg gibt das Programm den gespeicherten Inhalt aus.

## Datenschutz und API

Beim Erstellen wird der angegebene QR-Code-Inhalt an QR Server übermittelt. Beim Lesen wird die Bilddatei hochgeladen. Sende daher keine vertraulichen Inhalte oder Bilder, die du nicht an einen externen Dienst übertragen möchtest.

Weitere Parameter und API-Informationen: [goqr.me/api](https://goqr.me/api/).


Dieses Projekt ist unter der MIT-Lizens lizensiert (`LICENSE.md`)
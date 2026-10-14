import requests
import qrcode
import cv2

def main():
    choice = input("Do you want to generate a new QR code or read an existing one? (generate/read/help/quit): ")
    if choice.lower() == 'generate':
        generate_qr_code()
    elif choice.lower() == 'read':
        read_qr_code()
    elif choice.lower() == 'help':
        show_help()
    elif choice.lower() == 'quit':
        print("Goodbye!")
        quit()
    else:
        print("Invalid choice. Please enter 'generate' or 'read' or 'help' or 'quit'.")
        
        
        
        
def generate_qr_code():
    size = input("Enter the size of the QR code (e.g., 150x150): ")
    data = input("Enter the data for the QR code: ")
    ecc = input("Enter the error correction level (e.g., L, M, Q, H): ")
    qrformat = input("Enter the format for the QR code (e.g., png, svg): ")
    margin = input("Enter the margin for the QR code (e.g., 1): ")
    qrcolor = input("Enter the color for the QR code (e.g., 000000 for black): ")
    bgcolor = input("Enter the background color for the QR code (e.g., ffffff for white): ")
    api_url = "https://api.qrserver.com/v1/create-qr-code/?size=" + size + "&data=" + data + "&ecc=" + ecc + "&format=" + qrformat + "&margin=" + margin + "&color=" + qrcolor + "&bgcolor=" + bgcolor

        
        
    qr_export = qrcode.make(data)
    qr_export.save("qrcode.png")
    print("QR code generated and saved as 'qrcode.png'. You can also view it at the following URL:")
    print(api_url)
    
       
         
        
def read_qr_code():
    file_path = input("Enter the path to the QR code image file: ")
    try:
        with open(file_path, "rb") as image_file:
            response = requests.post(
                "https://api.qrserver.com/v1/read-qr-code/",
                files={"file": image_file},
                timeout=20,
            )
        response.raise_for_status()
        result = response.json()
        qr_data = result[0]["symbol"][0].get("data") if result else None
        if qr_data:
            print("Data in QR code:", qr_data)
        else:
            print("No data found in the QR code.")
    except OSError as error:
        print("Could not open the image file:", error)
    except requests.RequestException as error:
        print("Could not read the QR code:", error)
        
        
    load_picture = cv2.imread(file_path)
    detector = cv2.QRCodeDetector()
    data, bbox, _ = detector.detectAndDecode(load_picture)
    if data:
        print("Data in QR code (using OpenCV):", data)
    else:
        print("No data found in the QR code (using OpenCV).")
        
        
def show_help():
    print("\nQR-Code-Hilfe")
    print("Waehle im Menue 'generate', 'read' oder 'help'. Mit Ctrl+C beendest du das Programm.\n")
    print("QR-Code erstellen (generate):")
    print("  data: Der Text oder Link, der im QR-Code gespeichert werden soll (Pflichtfeld).")
    print("  size: Quadratische Groesse im Format BREITExHOEHE, z. B. 150x150.")
    print("        Erlaubt: 10x10 bis 1000x1000; beide Seiten muessen gleich sein.")
    print("        Standard der API: 200x200.")
    print("  ecc:  Fehlerkorrektur: L (niedrig), M (mittel), Q (hoch) oder H (sehr hoch).")
    print("        Standard: L. Hoehere Korrektur macht den QR-Code dichter.")
    print("  format: png, gif, jpeg, jpg, svg oder eps (klein schreiben).")
    print("          Rasterformate maximal 1000x1000; svg/eps sind Vektorformate.")
    print("  margin: Rand in Pixeln, ganze Zahl von 0 bis 50; Standard: 1.")
    print("  color / bgcolor: Vorder- und Hintergrundfarbe als Hexwert, z. B. 000000")
    print("                  und ffffff, oder RGB mit Bindestrichen, z. B. 0-0-0.")
    print("                  Fuer gute Lesbarkeit muss der Vordergrund dunkler sein.")
    print("  Das Ergebnis wird als qrcode.png gespeichert.\n")
    print("QR-Code lesen (read):")
    print("  Gib den Pfad zu einer lokalen PNG-, GIF- oder JPG-Datei ein.")
    print("  Die Bilddatei muss kleiner als 1 MiB sein und einen lesbaren QR-Code enthalten.\n")
    print("Die Erstellung und das Lesen verwenden den QR Server und benoetigen Internetzugang.")
    print("Details: https://goqr.me/api/")
    

while True:
    main()
        

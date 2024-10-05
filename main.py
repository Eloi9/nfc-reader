import nfc

def on_connect(tag): # Quan es conecta la NFC
    print(f"ID de la tarjeta: " + tag.identifier.hex())
    return True  # Mantén la connexió 

def main():
    with nfc.ContactlessFrontend('usb') as clf:
        print("Apropeu la tarjeta NFC...")
        clf.connect(rdwr={'on-connect': on_connect})

if __name__ == "__main__":
    main()

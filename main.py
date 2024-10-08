import nfc

class Rfid_Lector:
	def __init__(self): #Inicialitza el lector NFC
		self.clf = nfc.ContactlessFrontend('usb')
	
	def read_uid(self): #Lectura del uid i es torna en un string hex
		tag = None
		
		try:
			tag = self.clf.connect(rdwr={'on-connect': lambda tag: False})
		except Exception as e:
			print("Error al llegir la targeta: " + e)
			
		if tag:
			uid = tag.identifier.hex()
			return uid
		else:
			return None	

if __name__ =="__main__":
	rf = Rfid_Lector()
	print("Esperant targeta NFC...")
	uid = rf.read_uid()
	if uid:
		print("UID de la targeta: "+ uid.upper())
	else:
		print("No s'ha pogut llegir la targerta correctament")	

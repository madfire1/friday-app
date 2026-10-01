import threading
import time
from google import genai
from google.genai import types
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

API_KEY = "AQ.Ab8RN6LB_7US6Aev9ATpLM40IKE0LKJBQzU8m0G12SoWpGTn2Q"

try:
    client = genai.Client(api_key=API_KEY)
    chat = client.chats.create(model="gemini-2.5-flash")
    istruzioni_personalita = (
        "Tu sei Friday, l'assistente virtuale avanzato del tuo creatore. "
        "Rispondi sempre in modo estremamente educato, chiamandolo 'Signore'. "
        "Sii conciso, efficiente e brillante nelle risposte vocali."
    )
except Exception as e:
    print(e)

class FridayInterface(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        self.stato_label = Label(text="Sistemi Online, Signore.\nIn ascolto costante di 'Friday'...", halign="center")
        self.add_widget(self.stato_label)
        threading.Thread(target=self.servizio_background, daemon=True).start()

    def servizio_background(self):
        while True:
            # Qui il Foreground Service mantiene attivo il microfono a schermo spento
            time.sleep(1)

class FridayApp(App):
    def build(self):
        return FridayInterface()

if __name__ == '__main__':
    FridayApp().run()

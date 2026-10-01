import threading
import time
from google import genai
from google.genai import types
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.clock import Clock

# === CONFIGURAZIONE CERVELLO (GEMINI) ===
API_KEY = "AQ.Ab8RN6LB_7US6Aev9ATpLM40IKE0LKJBQzU8m0G12SoWpGTn2Q"

class FridayInterface(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        self.stato_label = Label(
            text="Sistemi Online, Signore.\nIn ascolto costante di 'Friday'...", 
            halign="center",
            valign="middle"
        )
        self.stato_label.bind(size=self.stato_label.setter('text_size'))
        self.add_widget(self.stato_label)
        
        # Inizializziamo il client Gemini in modo sicuro
        try:
            self.client = genai.Client(api_key=API_KEY)
            self.chat = self.client.chats.create(model="gemini-2.5-flash")
        except Exception as e:
            self.stato_label.text = f"Errore Connessione Cervello:\n{str(e)}"

        # Avviamo il timer di Kivy anziché un ciclo True distruttivo
        Clock.schedule_once(self.avvia_ascolto_sicuro, 1)

    def avvia_ascolto_sicuro(self, dt):
        # Questo thread gestisce l'ascolto senza congelare l'applicazione
        threading.Thread(target=self.ascolto_loop, daemon=True).start()

    def ascolto_loop(self):
        while True:
            # Qui si posizionerà l'ascolto in background
            time.sleep(2)

class FridayApp(App):
    def build(self):
        return FridayInterface()

if __name__ == '__main__':
    FridayApp().run()
    

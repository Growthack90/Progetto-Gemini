import google.generativeai as genai
import sys

# 1. Configurazione - Inserisci qui la tua API Key tra le virgolette
API_KEY = "IL_TUO_API_KEY_QUI"

def inizializza_gemini(key):
    try:
        genai.configure(api_key=key)
        # Utilizziamo 1.5 Flash: veloce, economico e perfetto per testi
        return genai.GenerativeModel('gemini-1.5-flash')
    except Exception as e:
        print(f"Errore durante la configurazione: {e}")
        sys.exit(1)

def analizzatore_creativo(modello, testo_input):
    prompt = f"""
    Agisci come un esperto di comunicazione. Analizza il testo fornito e restituisci:
    
    1. Un TITOLO accattivante.
    2. Un RIASSUNTO breve (massimo 3 punti elenco).
    3. Un POST per LinkedIn basato sul contenuto, usando emoji e hashtag pertinenti.
    
    Testo da analizzare:
    ---
    {testo_input}
    ---
    """
    
    try:
        response = modello.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Errore durante la generazione: {e}"

def main():
    # Verifica che la chiave non sia quella di default
    if API_KEY == "IL_TUO_API_KEY_QUI":
        print("Attenzione: Devi inserire la tua API Key nel codice!")
        return

    model = inizializza_gemini(API_KEY)

    # Testo di esempio (puoi sostituirlo con qualsiasi contenuto)
    testo_da_elaborare = """
    L'esplorazione spaziale sta vivendo una nuova epoca d'oro grazie alla collaborazione 
    tra agenzie governative e aziende private. L'obiettivo non è più solo la Luna, 
    ma la creazione di basi sostenibili su Marte e lo sfruttamento delle risorse minerarie 
    degli asteroidi, aprendo la strada a un'economia extra-terrestre.
    """

    print("\n--- ELABORAZIONE IN CORSO ---\n")
    
    risultato = analizzatore_creativo(model, testo_da_elaborare)
    
    print(risultato)
    print("\n--- OPERAZIONE COMPLETATA ---")

if __name__ == "__main__":
    main()
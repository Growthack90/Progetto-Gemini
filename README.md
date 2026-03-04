# Analizzatore di Testi con Gemini AI

Questo progetto utilizza le API di Google Gemini per analizzare testi, generare riassunti e creare contenuti per i social media in modo automatico.

Dai un occhiata alla guida seguente:
https://ai.google.dev/gemini-api/docs?hl=it

## 🚀 Installazione e Configurazione

Segui questi passaggi per configurare l'ambiente di lavoro sul tuo PC.

### 1. Clonazione o Creazione Progetto
Posizionati nella cartella del progetto:
```bash
cd <YOUR-LOCAL-PATH>\progetto-gemini

```

### 2. Creazione dell'Ambiente Virtuale

Crea un ambiente isolato per evitare conflitti con altre versioni di Python:

```bash
# Nota: usa la versione 3.11 come specificato
py -3.11 -m venv venv

```

### 3. Attivazione dell'Ambiente

* **Windows (PowerShell/CMD):**
```powershell
venv\Scripts\activate

```


*Nota: Se ricevi un errore di protezione in PowerShell, esegui: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser*`

### 4. Installazione Librerie

Una volta attivato l'ambiente (vedrai `(venv)` nel terminale), installa il pacchetto ufficiale:

```bash
pip install -U google-generativeai

```

*(Opzionale per PC Aziendali)* Se riscontri errori di certificato SSL, prova:

```bash
pip install pip-system-certs

```

## 🔑 Configurazione API Key

1. Ottieni una chiave da [Google AI Studio](https://aistudio.google.com/).
2. Apri il file `app.py`.
3. Sostituisci `IL_TUO_API_KEY_QUI` con la tua chiave reale.

## 🛠️ Test dello Script

Per verificare che tutto funzioni correttamente, esegui:

```bash
python app.py

```

### Cosa fa lo script:

* Invia un testo di esempio ai server Google.
* Genera un titolo accattivante.
* Crea un riassunto in 3 punti.
* Formatta un post pronto per LinkedIn.

---

**Nota per l'ambiente aziendale:** Se la rotellina di caricamento in AI Studio si blocca, prova a generare la chiave da un dispositivo non collegato alla rete ufficio (es. smartphone) e caricala manualmente nello script.

```
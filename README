# 🔐 Einfaches Authentifizierungssystem mit konfigurierbarem Hashing (Umschulungsaufgabe)

Dieses Projekt demonstriert ein sicheres Login-System in Python mit Unterstützung für Salt, Pepper und verschiedenen Hash-Algorithmen.

## 📁 Struktur

- `auth_system.py` – Kernlogik: Registrierung, Hashing, Verifikation
- `main.py` – Einfaches Konsolenmenü zur Benutzerverwaltung
- `config.json` – Konfiguration von Pepper und Hash-Verfahren
- `users.json` – Mini-Datenbank zur Speicherung von Benutzerdaten
- `requirements.txt` – Enthält alle nötigen Abhängigkeiten

---

## ⚙️ Konfiguration (`config.json`)

```json
{
  "pepper": "SUPERGEHEIMER_PEPPER_WERT",
  "algorithm": "bcrypt"
}
```

### Unterstützte Algorithmen:
- `"sha256"` – einfacher, schneller, weniger sicher
- `"bcrypt"` – bewährter Standard, langsam & sicher
- `"argon2"` – moderner & empfohlener Standard (speicherintensiver)

**Hinweis:** Der Pepper wird nicht in der Datenbank gespeichert und muss geheim bleiben!

---

## 🚀 Einrichtung

### 1. Python-Umgebung (optional)
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 2. Abhängigkeiten installieren
```bash
pip install -r requirements.txt
```

---

## 🧪 Ausführen

### Registrierung & Login über Konsole
```bash
python main.py
```

---

## 🧠 Sicherheitshinweis

> Dieses Beispiel dient der Veranschaulichung. In echten Anwendungen solltest du:
> - das `users.json` durch eine echte Datenbank ersetzen,
> - das `config.json` und besonders den Pepper sicher speichern (z. B. via Umgebungsvariablen),
> - und ggf. eine Passwort-Policy sowie Zwei-Faktor-Authentifizierung integrieren.

---

Happy Hacking! 🔒

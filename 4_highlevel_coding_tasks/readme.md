# Highlevel Coding Tasks mit Skills

In diesem Abschnitt geht es um Skills für **Coding-nahe Workflows**:

1. den `mcp-builder` Skill von skills.sh nutzen,
2. einen eigenen Skill mit Unterordnern + Python-Skript aufbauen.
3. teste den neuesten research --> skill hype: Caveman || Karpathy Skillset

---

## Das Konzept

Wie in den anderen Workshop-Teilen:

1. Aufgabe zuerst **OHNE** Skill probieren (Baseline)
2. Dann passenden Skill nutzen
3. Gleiches Ziel erneut **MIT** Skill umsetzen
4. Vergleich: Zeit, Qualität, Konsistenz, Wartbarkeit

So wird klar, wann ein Skill wirklich hilft und wo er zu starr ist.

---

## Teil A - MCP-Builder Skill testen

Skill-Link:
`https://skills.sh/anthropics/skills/mcp-builder`

### Ziel

Verstehen, wie der Skill beim Aufsetzen eines MCP-bezogenen Projekts
(Struktur, Komponenten, naechste Schritte) hilft oder gar als Einstieg in MCP dienen kann. Schaut dazu gerne auch mal in [unseren Workshop zu MCP](https://github.com/ScaDSAILLLE/meetup-workshop-mcp) von einst.

### Hinweise:

Nutze gerne Ollama lokal oder frag bzgl. Zugriff via API / openai-compatible-endpoint zum ScaDS.AI HPC-LLM-Cluster.

### Schritt 1: Ohne Skill (Baseline)

Prompt-Beispiel:

```text
Ich möchte einen einfachen MCP-Service planen, der auf lokale Dateien zugreift.
Erstelle mir eine sinnvolle Projektstruktur und erklaere die Kernkomponenten.
```

Notiere kurz:

- Wie konkret ist der Plan?
- Fehlen wichtige Bausteine?
- Wie viel Nachfragen sind noetig?

### Schritt 2: MCP-Builder installieren

Option A (empfohlen):

```text
/find-skills installiere mir den anthropic mcp-builder skill
```

Option B (manuell):

```bash
npx skills add anthropics/skills@mcp-builder -g -y
```

Danach OpenCode neu starten und mit `/skills` pruefen.

### Schritt 3: Mit Skill

Prompt-Beispiel:

```text
Nutze den mcp-builder Skill.
Ich moechte ein kleines MCP-Projekt fuer lokale Dateien planen.
Bitte liefere: Projektstruktur, Kernmodule, Implementierungsschritte,
Validierung und typische Fehlerquellen.
```

### Schritt 4: Vergleich ohne/mit Skill

Teste das Projekt mal- hat es geklappt? Konntest du ein Sprachmodell anbinden, mit deinem MCP ausstatten und war alles erfolgreich?
Teile gerne mit allen, was du erreicht hast!

Bewerte in 4 Punkten:

- **Qualität**: Ist die Architektur klarer?
- **Tempo**: Kommt man schneller zum brauchbaren Plan?
- **Konsistenz**: Ist das Ergebnis strukturierter/reproduzierbarer?
- **Flexibilität**: Wo war der freie Ansatz besser?

Für den Austausch in der Runde: Wie kann das deine alltägliche Arbeit erleichtern? Siehst du hier einen Nutzen für dich?

---

## Teil B - Eigener Skill mit Unterordnern + Python-Skript

### Use Case: Focus-Break Helper (Bildschirmpause-Reminder)

Idee: Ein Skill startet ein Python-Skript, das in festen Intervallen
an kurze Blick-/Bewegungspausen erinnert.

### Beispiel-Struktur

Wichtig: Der Kern ist immer eine Datei `SKILL.md` (Grossschreibung).
Darunter koennen beliebige Unterordner liegen (z. B. `scripts/`, `templates/`,
`references/`, `assets/`).

```text
focus-break-helper/
├── SKILL.md
├── scripts/
│   └── break_reminder.py
├── templates/
│   └── usage.md
└── references/
    └── troubleshooting.md
```

### Beispiel: `SKILL.md`

```markdown
---
name: focus-break-helper
description: Startet einen einfachen Fokus-/Pausen-Reminder per Python. Use when Nutzer lange Bildschirmarbeit machen und regelmaessige Break-Notifications wollen. Produces eine laufende Reminder-Session mit konfigurierbarem Intervall.
---

# Focus Break Helper

## When to Use This Skill
- Bei langen Coding-/Office-Sessions
- Wenn regelmaessige Mikropausen vergessen werden

## Prerequisites
- uv package manager installiert installiert
- Zugriff auf lokales Terminal

## Step-by-Step Workflow
1. Frage Intervall (in Minuten) und Anzahl Reminder ab
2. Starte `scripts/break_reminder.py` mit diesen Parametern
3. Gib kurze Abschlussmeldung mit Empfehlungen aus

## Validation Checklist
- Script wurde mit korrekten Parametern gestartet
- Reminder liefen in den erwarteten Abstaenden
- Session endet sauber ohne Fehler

## Troubleshooting
- Wenn uv / Python fehlt: Installationshinweis geben
- Wenn Notification nicht sichtbar: auf Terminal-Ausgabe ausweichen
```

### Beispiel: `scripts/break_reminder.py`

```python
import argparse
import platform
import subprocess
import time


def notify(message: str) -> None:
    system = platform.system().lower()
    if "linux" in system:
        subprocess.run(["notify-send", "Focus Break", message], check=False)
    elif "darwin" in system:
        subprocess.run(
            ["osascript", "-e", f'display notification "{message}" with title "Focus Break"'],
            check=False,
        )
    else:
        print(f"[REMINDER] {message}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Focus break reminder")
    parser.add_argument("--minutes", type=int, default=20)
    parser.add_argument("--count", type=int, default=3)
    args = parser.parse_args()

    for index in range(1, args.count + 1):
        time.sleep(args.minutes * 60)
        notify(f"Pause {index}/{args.count}: 20 Sekunden in die Ferne schauen.")

    print("Session beendet. Gut gemacht.")


if __name__ == "__main__":
    main()
```

### Test-Prompt fuer den eigenen Skill

```text
Nutze den Skill focus-break-helper.
Starte eine kurze Demo mit 1 Minute Intervall und 2 Erinnerungen.
Erklaere danach knapp, wie ich Intervall und Anzahl anpasse.
```

---

## Sicherheits- und Praxis-Hinweise

- Externe Skills und Skripte immer reviewen (Quelle, Berechtigungen, Verhalten, prompt-injection, zusätzliche Online-Recherche etc.).
- Lokale Skripte klein halten, klar benennen, Fehlerfälle dokumentieren.

## Teil C / Goodies: *Let LLMs talk like a caveman*

- Installiere diesen Skill: [Link zum GitHub Repo von **Caveman**](https://github.com/JuliusBrussee/caveman?tab=readme-ov-file).
- Teste mal aus, wie das so funktioniert und ob das Vorteile bringt.
- Bei Interesse lies in das verlinkte Paper rein, das Grundlage hierfür ist.

Außerdem kannst du mal schauen, ob dir die Beobachtungen und Lösungen von Andrej Karpathy für dein Setup helfen und besser Ergebnisse liefern: [Link](https://github.com/forrestchang/andrej-karpathy-skills)  


### Viel Erfolg beim weiteren Einsatz von Agent-Skills! 

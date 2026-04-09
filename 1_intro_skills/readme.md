# Intro Skills - Workshop Einstieg

## Ziel dieses Abschnitts

Nach dieser Intro-Einheit sollst du:

- verstehen, was Agent Skills sind,
- wissen, wann man **mit** und wann man **ohne** Skill arbeitet,
- den Unterschied zwischen Skills und z.B. MCP grob einordnen,
- Risiken kennen, z.B. beim installieren von fremden Skills (wie z.b. von [skills.sh](skills.sh),
- und vorbereitet in `2_skill_basics/` starten.

## Was sind Skills?

Skills sind wiederverwendbare, spezialisierte Anleitungen fuer einen Agenten.
Sie helfen bei wiederkehrenden Aufgaben, z. B.:

- standardisierte Workflows Schritt fuer Schritt durchfuehren,
- bspw. strukturiert Briefe zu erstellen,
- Excel/PowerPoint-Dateien erzeugen (frei od. nach Template),
- Code in einer gewissen Struktur zu schreiben, zu testen oder einem bestimmten "Pattern" zu folgen (z.B. Test-driven-development)

Ein Skill ist **kein neues Modell**, sondern ein kuratierter Arbeitsablauf geschrieben in mindestens einem Textfile ([Markdown](https://de.wikipedia.org/wiki/Markdown)-File) aber auch ziemlich erweiterbar (bspw. ausführbarer (Python-) Code) mit klaren Triggern, Regeln und Outputs, so dass ein Sprachmodell nicht nur weiß wie es das nutzen kann/soll, sondern auch wann.

## Mit Skill vs. Ohne Skill

### Ohne Skill

- flexibel und frei, gut für offene Exploration, Chat, Ideenentwicklung (ja, auch hier könnte man Skills nutzen- hast du ein "mentales" Template für Ideen entwickeln od. *brainstormen*, dann versuch das doch mal im Laufe des Workshops in einen Skill zu übertragen zusammen mit Opencode),
- **ABER** Qualität/Struktur und damit das Ergebnis schwankt stärker, d.h. mehr Prompt-Design/Engineering-Aufwand bei Einsteiger:innen.

### Mit Skill

- schneller reproduzierbare Ergebnisse,
- klare Schrittfolge und definierter Output,
- gut für wiederholende (gleiche) Abläufe, für Teams, die gewisse Templates und *"Guidelines"* nutzen, Standards und onboarding (hier kann man vom Vorteil profitieren, dass ein onboarding in gewisse Arbeitsabläufe erleichtert wird, das Workflows bereits strukturiert sind und zusammen mit Agents einfacher anzuwenden sind),
- **ABER** weniger flexibel bei Sonderfällen (hier warten womöglich dann die Fehlerquellen).

## Wann sind Skills gut - wann eher nicht?

### Gute Faelle fuer Skills

- wiederkehrende Aufgaben mit aehnlichem Muster,
- konkrete Artefakte als Ziel (Datei, Diagramm, Bericht, Strukturtext, Code-Struktur/Pattern etc.),
- einheitliche Qualität.

### Eher ohne Skill arbeiten

- stark kreative, komplett neue Problemstellungen,
- Research ohne klares Endformat,
- Ideenfindung, Chat,
- Situationen, in denen schnelle Iteration wichtiger ist als Standardisierung.

## Skills vs. MCP (kurz), falls das hilft, die Abgrenzung nicht ganz klar ist und eine Unterscheidung das ganze auf anderer Ebene besser erklärt:

- **Skill**: Prompt-/Workflow-Ebene; steuert, *wie* der Agent arbeitet.
- **MCP**: Tool-/System-Ebene; ermöglicht Zugriff auf Daten, APIs, lokale Dienste.

Merksatz:

- Skill = "Arbeitsanweisung"
- MCP = "Werkzeuganschluss"

## Vor- und Nachteile im Überblick

### Vorteile

- schnellere Einstiege für Unerfahrene,
- besser vergleichbare Ergebnisse,
- weniger Prompt-Chaos,
- dokumentierbare *Best Practices*.

### Nachteile

- kann zu starr sein,
- falscher Skill kann Aufgaben verkomplizieren,
- Qualitaet hängt stark von Skill-Design und Pflege ab (ja, Skills müssen u.U. gepflegt werden: ändert sich was am Workflow, muss auch ein damit zusammenhängender Skill geändert werden).

## Skill-Struktur verstehen

Der Kern eines Skills ist immer eine Datei namens `SKILL.md` (**Großschreibung beachten**).
Je nach Skill können darunter auch weitere Unterordner liegen, z. B. für
Skripte, Programme, Referenzen, Assets oder Templates.

```text
my-first-skill/
├── SKILL.md
├── templates/
│   └── output-template.md
├── scripts/
│   └── helper.py
├── references/
│   └── checklist.md
└── assets/
    └── example-input.txt
```

```markdown
---
name: demo-skill
description: Erzeugt aus Stichpunkten eine kurze Meeting-Zusammenfassung. Use when Nutzer nach schneller Zusammenfassung, Meeting Notes oder Follow-up fragen. Produces einen klar strukturierten Kurztext mit naechsten Schritten.
---

# Demo Skill

## When to Use This Skill
- Wenn aus Notizen schnell ein Ergebnis entstehen soll
- Wenn ein einheitliches Format gebraucht wird

## Prerequisites
- Eingabe liegt als Stichpunkte vor
- Sprache ist Deutsch oder Englisch

## Step-by-Step Workflow
1. Notizen kurz auf Ziel und Kontext pruefen
2. 3-5 Kernpunkte extrahieren
3. Kurzfassung in festem Ausgabeformat schreiben
4. Offene Punkte und naechste Schritte markieren

## Validation Checklist
- Ergebnis ist knapp und klar
- Wichtige Entscheidungen sind enthalten
- Naechste Schritte sind konkret benannt

## Troubleshooting
- Wenn Input zu vage ist: 2-3 Rueckfragen stellen
- Wenn Kontext fehlt: Annahmen transparent machen
```

Hinweis: In `2_skill_basics/` kannst du selbst anhand des *klassischen* Skill-Templates einen ersten Skill bauen. Sogar einen *guided-skill-builder* Skill ist vorbereitet.

## Wo findet man Skills?

- über `/skills` in OpenCode (**Achtung**: nur vorkonfigurierte oder bereits installierte Skills- das ist **keine** Skill-Bibliothek),
- über Discovery-Workflows wie `/find-skills` (das haben wir von [skills.sh](skills.sh) bezogen, um den Umgang und das Beziehen neuer (fremder/externer) Skills von Dritten zu erleichtern),
- über kuratierte Quellen wie `https://skills.sh/`.

## Sicherheits-Disclaimer (**Achtung:** wichtig!)

Externe Skills sind Drittinhalte.

- Ein Skill kann unsichere oder ungeeignete Anweisungen enthalten.
- Downloadzahlen sind bspw. **kein** Garant für Qualitaet oder Sicherheit.
- Vor Nutzung kurz prüfen: Quelle, Zweck, benötigte Berechtigungen,
  erwarteter Output, evtl. Code im Skill checken, zusätzliche Online-Recherche usw.!

Ein Beispiel gefällig, warum man das so machen sollte: [From Magic to Malware: How OpenClaws Agent Skills become an attack surface](https://1password.com/blog/from-magic-to-malware-how-openclaws-agent-skills-become-an-attack-surface), [hier eine dt. Quelle](https://www.linux-magazin.de/news/virus-total-entdeckt-hunderte-boesartige-erweiterungen-fuer-openclaw/).
Nicht überzeugt? Schaut mal [hier](https://www.mitiga.io/blog/ai-agent-supply-chain-risk-silent-codebase-exfiltration-via-skills) oder [hier](https://embracethered.com/blog/posts/2026/scary-agent-skills/)...

## Setup für heute

1. Opencode (Website)[opencode.ai]; schaut gerne in die Docs und wer es eigens installieren möchte oder eine Einführung in die Nutzung braucht schaut [hier](../0_opencode/README.md)
2. Spitzen Workshop-Material, klar :)
3. Vorbereitete Laptops samt Zugriff auf unser ScaDS.AI LLM-Cluster am ZIH/HPC an der TU Dresden [Link](https://llm.scads.ai/docs/) mit [folgenden Modellen](https://llm.scads.ai/status/)


## Workshop-Fahrplan

Bis hierher hast du Begriffe, Grundstruktur, Pro/Con etc. eingecheckt. 

- Wenn du bereit bist, kannst du mit `2_skill_basics/`: erster eigener Skill + Vergleich ohne/mit Skill usw.

- Wer Skills schon grundlegend kennt oder sogar nutzt kann sich in `3_midlevel_office_tasks/`: fortgeschrittene Office-Workflows inspirieren lassen oder eigene Skills erstellen, testen usw.

- Für die Erfahrenen unter euch und insb. Coder haben wir `4_highlevel_coding_tasks/`: Skills mit Code/MCP-Anbindung vorbereitet- quasi der *Blick über den Tellerrand*. 

### Let's go!


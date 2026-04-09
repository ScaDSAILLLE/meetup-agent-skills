# Excel-Skill – Step-by-Step

## Was kann der Skill?

Der Excel-Skill hilft dir, Excel-Dateien (.xlsx) direkt zu erstellen, zu bearbeiten und zu formatieren.

Wir verwenden den Excel-Skill von Anthropic:
https://skills.sh/anthropics/skills/xlsx

---

## Kreative Beispiel-Prompts

Hier sind Ideen, die du ausprobieren kannst:

```
Erstelle eine Excel-Datei für einen Monats-Einkaufsplan.
Spalten: Produkt, Kategorie, Menge, geschätzter Preis, Summe
Füge 8 typische Einkaufsartikel hinzu
```

```
Erstelle eine Excel-Datei @projekttracker.xlsx für ein Projekt.
Spalten: Aufgabe, Status, Verantwortlich, Deadline, Tage bis Deadline
Füge 5 Beispielaufgaben hinzu
```

```
Erstelle eine Umsatzübersicht @quartal.xlsx.
Spalten: Monat, Umsatz, Kosten, Gewinn
Formeln für Gewinn (Umsatz - Kosten) einrichten
```

---

## Step-by-Step

### Schritt 1: Erst OHNE Skill

Teste diese Aufgabe ZUERST ohne installierten Skill:

```
Erstelle eine Excel-Datei mit monatlichen Ausgaben.
Die Tabelle soll Spalten haben für: Kategorie, Betrag, Datum
Füge 5 Beispieldatensätze hinzu
```

### Schritt 2: Skill installieren

**Option 1: Über /find-skills**

```
/find-skills installiere mir den anthropic xlsx skill
```

**Option 2: Manuell**

```bash
npx skills add anthropics/skills@xlsx -g -y
```

**Danach:**
- OpenCode neu starten
- Skill-Verfügbarkeit prüfen mit `/skills`
TODO: Wie wollen wir das machen? schon vorbereiten? über vercel installieren?
*******

### Schritt 3: Skill aufrufen

**CLI:**
- Nach Installation: `/skills` → Skill aktivieren
- Oder: Skill wird automatisch erkannt bei Excel-Prompts

**GUI:**
- `/{skillname}` eingeben (z.B. `/excel`)
- Oder: Slash-Command im Menü auswählen

### Schritt 4: MIT Skill

Wiederhole die gleiche Aufgabe nur dass du zu Beginn des Prompts den Skill aufrufst:

```
Erstelle eine Excel-Datei mit monatlichen Ausgaben.
Die Tabelle soll Spalten haben für: Kategorie, Betrag, Datum
Füge 5 Beispieldatensätze hinzu
```

### Schritt 5: Vergleichen

- Was hat besser funktioniert?
- Was war anders?
- Was war einfacher?

---

## Weitere Prompts zum Ausprobieren

### Daten formatieren
```
Formatiere @tabelle.xlsx:
- Header fett
- Rahmen um die Tabelle
- Zahlen mit 2 Dezimalstellen
```

### Diagramme erstellen
```
Füge zu @daten.xlsx ein Balkendiagramm hinzu:
Umsatz pro Monat
```

### Bedingte Formatierung
```
Markiere in @ausgaben.xlsx alle Zellen in der Spalte "Betrag",
die über 100 Euro liegen, mit rotem Hintergrund
```

---

## Mehr Infos

- Link zum Skill: https://skills.sh/anthropics/skills/xlsx

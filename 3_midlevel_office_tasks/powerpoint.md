# PowerPoint-Skill – Step-by-Step

## Was kann der Skill?

Der PowerPoint-Skill hilft dir, Präsentationen (.pptx) zu erstellen, zu bearbeiten und zu gestalten.

Wir verwenden den Powerpoint-Skill von Anthropic:
https://skills.sh/anthropics/skills/pptx

---

## Kreative Beispiel-Prompts

Hier sind Ideen, die du ausprobieren kannst:

```
Erstelle eine Präsentation zum Treibhauseffekt und seine Auswirkungen auf den Klimawandel.
```

```
Erstelle eine Präsentation @hundoderkatze.pptx, die ein für alle Mal klärt, ob Hunde oder Katzen besser sind.
```

```
Erstelle eine Präsentation zu Datenschutz- und Urheberrechtsproblemen im Bezug auf KI.
```

---

## Step-by-Step

### Schritt 1: Erst OHNE Skill

Teste diese Aufgabe ZUERST ohne installierten Skill:
```
Erstelle eine Präsentation zum Triebhauseffekt und seine Auswirkungen auf den Klimawandel.
```

### Schritt 2: Skill installieren

**Option 1: Über /find-skills**

```
/find-skills installiere mir den anthropic pptx skill
```

**Option 2: Manuell**

```bash
npx skills add anthropics/skills@pptx -g -y
```

**Danach:**
- OpenCode neu starten
- Skill-Verfügbarkeit prüfen mit `/skills`
TODO: Wie wollen wir das machen? schon vorbereiten? über vercel installieren?
*******

### Schritt 3: Skill aufrufen

**CLI:**
- Nach Installation: `/skills` → Skill aktivieren
- Oder: Skill wird automatisch erkannt bei PowerPoint-Prompts

**GUI:**
- `/{skillname}` eingeben (z.B. `/powerpoint`)
- Oder: Slash-Command im Menü auswählen

### Schritt 4: MIT Skill

Wiederhole die gleiche Aufgabe nur dass du zu Beginn des Prompts den Skill aufrufst:
```
Erstelle eine Präsentation zum Triebhauseffekt und seine Auswirkungen auf den Klimawandel.
```

### Schritt 5: Vergleichen

- Was hat besser funktioniert?
- Was war anders?
- Was war einfacher?

---

## Weitere Prompts zum Ausprobieren

### Folien hinzufügen
```
Füge zu @praesentation.pptx eine neue Folie hinzu: "Nächste Schritte"
```

### Layout ändern
```
Ändere Layout von Folie 2 auf "Text links, Bild rechts"
```

### Design anwenden
```
Wende auf @praesentation.pptx ein modernes, dunkles Design an
```

### Präsentationen kombinieren
```
Kombiniere @teil1.pptx und @teil2.pptx zu @kombiniert.pptx
```


### Ergebnis Überprüfen (Wichtig!)

Nach dem Erstellen:
```
Prüfe @praesentation.pptx auf:
- Platzhalter-Text entfernt?
- Überlappende Elemente?
- Text abgeschnitten?
```

---

## Mehr Infos

- Link zum Skill: https://skills.sh/anthropics/skills/pptx

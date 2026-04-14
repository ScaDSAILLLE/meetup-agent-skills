# Skill Basics - Schritt-für-Schritt Guide

## Ziel dieses Abschnitts

In diesem Teil lernst du praktisch:

- wie man einen ersten Skill erstellt,
- wie man Skills in OpenCode prüft und nutzt,
- was der Unterschied zwischen bspw. im Output **ohne Skill** und **mit Skill** ist,
- welche Vor- und Nachteile Skills im Alltag oder für deinen Workflow haben,
- und wie man auf eigene Faust einen einfachen Skill aufsetzt.

## Voraussetzungen (2 Minuten)

- OpenCode ist installiert und startet. Falls es nicht geöffnet ist, gehe wie folgt vor:
    - Öffne VSCode! (Unten in der Taskleiste solltest du ein blaues Logo finden.)
    - Links im *Explorer* klicke mit Rechtsklick auf  den Ordner "meetup-agent-skills",
    - wähle "Open in Integrated Terminal" --> es öffnet sich unten ein Terminal-Fenster,
    - gib ein `wsl`,
    - gib ein `opencode`.
    Und schon kann es losgehen! (Beenden geht mit STRG + C)
- Wenn Unsicherheiten bei Setup oder Bedienung bestehen, frag die Kursleiter, frag einfach in die Runde oder sieh hier nach:
  - `0_opencode/setup.md`
  - `0_opencode/README.md`
- Falls du nochmal nachlesen willst zu Skills i.A., kannst du nochmal die Intro lesen:
  - `1_intro_skills/readme.md`
  - sowie den Foliensatz (PDF).

## Vorgehen im Workshop

Wir arbeiten bewusst in zwei Modi:

1. **Ohne Skill** (Baseline)
2. **Mit Skill** (strukturierter Workflow)

Nach jedem Schritt kurz vergleichen:

- Was war schneller?
- Was war präziser?
- Wo war mehr Nacharbeit nötig?
- Hatte ich einen *"Aha-"* oder sogar einen *"Wow-"* Effekt?


## Schritt 0 - Ein erster Skill:  Wikipedia-Skill testen 

### Ziel

Erleben, wie ein klarer, enger Skill eine Aufgabe zuverlässig durchführt. Sogar mit *computer use* also dem eigenständigen Bedienen des PCs durch ein Sprachmodell... magisch! 

### Beispielprompt

```text
Öffne Wikipedia und suche nach "Prompt Engineering".
```

### Reflexion ohne/mit Skill

- **Ohne Skill:**: Teste das doch mal mit z.B. einer anderen Website oder dem öffnen eines anderen Programms. Vermutlich kommen oft Rückfragen oder eine weniger klare Ausführung zustande.
- **Mit Skill:** zielgerichteter Ablauf mit weniger bis keiner Prompt-Feinjustierung. Wenn, dann nur nötige Rückfragen, wobei man Skills auch so gestalten kann, dass annahmen getroffen werden oder Minimal-Workflows gefahren werden: vgl. Wikipedia-Skill: gibt man keinen Suchbegriff an, öffnet der Skill einfach nur Wikipedia im Standardbrowser. 

## Schritt 1 - Ersten Skill mit guided-skill-builder bauen

### Ziel

Verstehen, wie ein Skill strukturiert ist und einen ersten Entwurf erstellen.

### Prompt (Beispiel)

```text
Ich möchte einen Skill bauen, der aus Stichpunkten eine kurze, klare
Meeting-Zusammenfassung schreibt.
Führe mich als Einsteiger:in Schritt für Schritt durch den Skill-Aufbau und die Skill-Erstellung.
Nutze den guided-skill-builder!
```

*Prüft auch mal ob das klappt, wenn ihr am Ende nicht explizit nach dem betreffenden Skill fragt. Klappt das auch?*

### Worauf achten?

- `name` klar und achtet auf **kleinschreibung mit Bindestrichen**,
- `description` mit Was + Wann + Output,
- Workflow in wenigen klaren Schritten,
- Validation und Troubleshooting nicht vergessen.

*Der guided-skill-builder führt euch hier durch und fragt gewisse Infos eigens ab. Schaut dir das genau an und erhalte ein grobes Gefühl, welche Infos nützlich und nötig sind für einen funktionierenden Skill*

### Ergebnischeck

Am Ende liegt ein verständlicher Skill-Entwurf vor, der ohne Platzhalter
benutzbar ist.


## Schritt 2 - OpenCode neu starten und Skill prüfen

### Ziel

Sicherstellen, dass der Skill korrekt erkannt wird.

### Ablauf

1. Frage im Chat nach dem erstellen des ersten eigene Skills, ob Opencode bzw. der Sprachmodell-Agent den Skill bereits installiert hat und wenn nicht, dass das getan werden soll (im *build-mode*).
2. OpenCode danach neu starten. (Nur so werden die neu-installierten Skills beim Opencode-Start auch neu registriert und sind verfügbar. Etwas ungelenk aber das machen die meisten Agents derzeit (noch) so...)
3. über /sessions die letzte Konversation wieder öffnen oder einfach neustarten
4. Mit `/skills` prüfen, ob der Skill sichtbar ist.
5. Einen kleinen Testprompt ausführen.

### Wenn etwas nicht klappt

- Opencode-Agent oder in die Runde fragen, 
- Dateiname/Struktur prüfen,
- Trigger-Formulierungen in der Description konkretisieren...


## Schritt 3 - Eigene Mini-Idee umsetzen (auf eigene Faust)

### Ziel

Selbstständig Skills entwerfen und testen.

### Aufgabe

Wähle eine wiederkehrende Alltagsaufgabe und baue dazu einen Mini-Skill,
z. B.:

- To-do-Liste aus Meeting-Notizen,
- kurze Projektstatus-Updates,
- standardisierte E-Mail-Antworten.

Du kannst natürlich auch kreativ sein und eine verwegene Idee testen, die dir in den Sinn kommt!
Oder, *Profi-Tipp*: brainstorme doch mit dem Opencode-Agent über mögliche Skill-Ideen?

### Varianten

- mit guided-skill-builder,
- oder ohne Builder direkt per Chat versuchen zum Ziel zu kommen.


## Prompt-Playbook fuer Einsteiger:innen

Nutze diese Prompt-Formel:

`Kontext + Ziel + Eingaben + Grenzen + Ausgabeformat`

### Starter-Prompt

```text
Ich bin Einsteiger:in und möchte eigene Skills entwickeln. Führe mich in kleinen Schritten.
Stelle nur eine Frage gleichzeitig.
Gib mir am Ende eine klare Checkliste und Zusammenfassung.
Wenn bereit und gemeinsam finalisiert: installiere den Skill, so dass ich neustarten kann.
```

### Prompt zum Skill-Vergleich

```text
Löse die Aufgabe zuerst ohne Skill und dann mit passendem Skill.
Vergleiche beide Ergebnisse in 4 Punkten: Qualität, Zeit, Konsistenz,
manueller Aufwand.
```

### Prompt zur Selbstpruefung

```text
Prüfe meinen Skill-Entwurf auf fehlende Teile.
Nenne konkrete Verbesserungen für name, description, workflow,
validation und troubleshooting.
```


## Troubleshooting (kurz)

- Skill wird nicht erkannt: Name/Frontmatter/Ordnerstruktur prüfen. Oder schauen, ob der Skill noch registriert werden muss. Im Zweifel nach Erstellung den Opencode-Agent fragen oder neustarten (STRG + C und dann wieder `opencode` eingeben).
- Ergebnis ist unklar: Description und Outputformat praezisieren.
- Bedienung unklar: in `0_opencode/` nachsehen.

## Brücke zum weiteren Workshop-Material

- Nach den Basics geht es weiter mit `3_midlevel_office_tasks/` hier lernst du, wie du nützliche externe Skills mit dem `find-skills` Skill beziehen kannst und kannst mal komplexere Tasks wie z.B. in Excel oder Powerpoint testen.
- Später in `4_highlevel_coding_tasks/` geht es um Skills mit Code,
  z. B. Python-Workflows und MCP-nahe Aufgaben.

Wichtig: Das Ziel ist nicht nur Skills zu nutzen, sondern zu verstehen,
wie ihr sie selbst entwerft, testet und verbessert. Nimm dir also Zeit. :)

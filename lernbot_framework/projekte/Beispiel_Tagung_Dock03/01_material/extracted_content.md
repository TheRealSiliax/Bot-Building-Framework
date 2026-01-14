Tagung im Hotel Dock 03 – strukturierte, maschinenlesbare Version (kompaktes Chatbot-Layout)
0. Dokument-Metadaten
SIM_ID: SIM_TAGUNG_DOCK03_2026_01
Titel: Tagung im Hotel Dock 03 (Material 1–3c)
Version: v1.1 (kompakt)
Datum: 2026-01-14
Autor/Team: {{eintragen}}
Zielgruppe: {{eintragen}}
Dauer gesamt: {{eintragen}}
Fächer/Kompetenzen: {{eintragen}}
Voraussetzungen: {{eintragen}}
Lizenz/Quellen: {{eintragen}}
Chatbot-Ausgabe-Layout (global)
Ziel: Die Chat-Ausgabe soll kompakt sein, ohne Aufgabeninhalte zu kürzen.
Rollen werden im Chat nicht angezeigt (Rollen sind intern für Steuerung/Didaktik).
Keine Checkfragen wie „Bist du bereit?“ / „Kannst du loslegen?“. Direkter Einstieg.
In jeder TASK-Ausgabe: Lernziele → (Orientierungsfilter: Rubrik-Kriterien kurz) → Aufgabe → Eingabeaufforderung.
Hinweise/Teilhinweise und Rubrik-Feedback werden frühestens nach dem 1. Lösungsversuch ausgegeben.
P0_BRIEF ist eine Sonderphase („Startlayout“): etwas umfangreicher, enthält das vollständige Szenario + Gesamtauftrag + Ablaufüberblick.
1. Ablaufübersicht (Phasen)
PHASE_ID: P0_BRIEF | Name: Briefing / Startlayout | Zeit: {{10–15 Min}} | Kurzbeschreibung: Szenario verstehen, Ziele klären, Regeln, Gesamtauftrag.
PHASE_ID: P1_BEDARF | Name: Bedarf ermitteln | Zeit: {{25–40 Min}} | Kurzbeschreibung: Rezepte/Speisenplan → Warenbedarf für 50 Personen.
PHASE_ID: P2_BESTAND | Name: Bestand abgleichen & Bestellung bereinigen | Zeit: {{20–30 Min}} | Kurzbeschreibung: Lagerbestand prüfen, Bestellung korrigieren.
PHASE_ID: P3_ANGEBOT | Name: Angebote vergleichen & Lieferant auswählen | Zeit: {{25–40 Min}} | Kurzbeschreibung: Kriterien anwenden, Entscheidung begründen.
PHASE_ID: P4_DEBRIEF | Name: Debriefing / Reflexion & Transfer | Zeit: {{10–15 Min}} | Kurzbeschreibung: Lernen sichern, Transfer herstellen.
2. Rollen (intern – nicht im Chat ausgeben)
Hinweis: Rollen dienen dem Bot zur Steuerung und zur didaktischen Perspektive. Sie werden im Chat nicht angezeigt.
[ROLE-BLOCK]
ROLE_ID: ROLE_STUDENT_EINKAUF
Rollenname: Schüler*in – Küche/Wareneinkauf
Ziele/Motivation: Sicherstellen, dass die Tagung versorgt ist; korrekte Mengen; wirtschaftliche Entscheidung.
Informationen (öffentlich): {{eintragen/aus Material ableiten}}
Informationen (geheim/optional): {{optional}}
[/ROLE-BLOCK]
[ROLE-BLOCK]
ROLE_ID: ROLE_LEHRKRAFT_SPIELLEITUNG
Rollenname: Lehrkraft/Spielleitung
Ziele/Motivation: Moderiert, gibt Material frei, steuert Zeit und Reflexion.
Informationen (öffentlich): {{eintragen/aus Material ableiten}}
Informationen (geheim/optional): {{optional}}
[/ROLE-BLOCK]
3. Materialien / Ressourcen
[RESOURCE-BLOCK]
RESOURCE_ID: R_TEXT_SITUATION
Typ: Input
Titel: Situationsbeschreibung (Zeitdruck durch Krankheitsausfall)
Beschreibung/Zweck: {{kurz ergänzen, falls nötig}}
Verwendung in Tasks: T0_1_AUFTRAGSKLAERUNG
Quelle: intern (Tagung_003)
Datei/Anhang: Anhang A (Originalmaterial)
Maschinenhinweise: {{Einheiten/Spaltennamen/Notation}}
[/RESOURCE-BLOCK]
[RESOURCE-BLOCK]
RESOURCE_ID: R_BRIEF_VERANSTALTER
Typ: Input
Titel: Veranstalter-Infos / Eckdaten Tagung
Beschreibung/Zweck: {{kurz ergänzen, falls nötig}}
Verwendung in Tasks: T0_1_AUFTRAGSKLAERUNG
Quelle: intern (Tagung_003)
Datei/Anhang: Anhang A (Originalmaterial)
Maschinenhinweise: {{Einheiten/Spaltennamen/Notation}}
[/RESOURCE-BLOCK]
[RESOURCE-BLOCK]
RESOURCE_ID: R_RECHERCHE_MOEHRENSUPPE
Typ: Aufgabe
Titel: Möhrensuppe – Rezept muss recherchiert werden
Beschreibung/Zweck: {{kurz ergänzen, falls nötig}}
Verwendung in Tasks: T1_1_BEDARF
Quelle: intern (Tagung_003)
Datei/Anhang: Anhang A (Originalmaterial)
Maschinenhinweise: {{Einheiten/Spaltennamen/Notation}}
[/RESOURCE-BLOCK]
[RESOURCE-BLOCK]
RESOURCE_ID: R_REZEPT_PANNFISCH
Typ: Rezept
Titel: Hamburger Pannfisch (für 5 Personen)
Beschreibung/Zweck: {{kurz ergänzen, falls nötig}}
Verwendung in Tasks: T1_1_BEDARF
Quelle: intern (Tagung_003)
Datei/Anhang: Anhang A (Originalmaterial)
Maschinenhinweise: {{Einheiten/Spaltennamen/Notation}}
[/RESOURCE-BLOCK]
[RESOURCE-BLOCK]
RESOURCE_ID: R_REZEPT_ROTEGRUETZE
Typ: Rezept
Titel: Hamburger Rote Grütze (für 10 Personen)
Beschreibung/Zweck: {{kurz ergänzen, falls nötig}}
Verwendung in Tasks: T1_1_BEDARF
Quelle: intern (Tagung_003)
Datei/Anhang: Anhang A (Originalmaterial)
Maschinenhinweise: {{Einheiten/Spaltennamen/Notation}}
[/RESOURCE-BLOCK]
[RESOURCE-BLOCK]
RESOURCE_ID: R_FUNC_SHEET
Typ: Worksheet
Titel: Function Sheet / Warengruppen-Überblick
Beschreibung/Zweck: {{kurz ergänzen, falls nötig}}
Verwendung in Tasks: T1_1_BEDARF
Quelle: intern (Tagung_003)
Datei/Anhang: Anhang A (Originalmaterial)
Maschinenhinweise: {{Einheiten/Spaltennamen/Notation}}
[/RESOURCE-BLOCK]
[RESOURCE-BLOCK]
RESOURCE_ID: R_WORKSHEET_ANGEBOT
Typ: Worksheet
Titel: Angebotsvergleich (Preis, Transportkosten, Rabatte, ...)
Beschreibung/Zweck: {{kurz ergänzen, falls nötig}}
Verwendung in Tasks: T3_1_ANGEBOT
Quelle: intern (Tagung_003)
Datei/Anhang: Anhang A (Originalmaterial)
Maschinenhinweise: {{Einheiten/Spaltennamen/Notation}}
[/RESOURCE-BLOCK]
[RESOURCE-BLOCK]
RESOURCE_ID: R_CRITERIA_LIEFERANT
Typ: Input
Titel: Kriterien zur Lieferantenentscheidung (Termintreue, Qualität, ...)
Beschreibung/Zweck: {{kurz ergänzen, falls nötig}}
Verwendung in Tasks: T3_1_ANGEBOT
Quelle: intern (Tagung_003)
Datei/Anhang: Anhang A (Originalmaterial)
Maschinenhinweise: {{Einheiten/Spaltennamen/Notation}}
[/RESOURCE-BLOCK]
[RESOURCE-BLOCK]
RESOURCE_ID: R_PARTNER_BRAINSTORM
Typ: Worksheet
Titel: Brainstorm: Handelspartner im Raum Hamburg
Beschreibung/Zweck: {{kurz ergänzen, falls nötig}}
Verwendung in Tasks: T3_1_ANGEBOT
Quelle: intern (Tagung_003)
Datei/Anhang: Anhang A (Originalmaterial)
Maschinenhinweise: {{Einheiten/Spaltennamen/Notation}}
[/RESOURCE-BLOCK]
[RESOURCE-BLOCK]
RESOURCE_ID: R_TEXT_TASKS
Typ: Input
Titel: Arbeitsaufträge / Leitfragen aus Material (Textteile)
Beschreibung/Zweck: {{kurz ergänzen, falls nötig}}
Verwendung in Tasks: T0_1_AUFTRAGSKLAERUNG, T1_1_BEDARF, T2_1_BESTAND, T3_1_ANGEBOT
Quelle: intern (Tagung_003)
Datei/Anhang: Anhang A (Originalmaterial)
Maschinenhinweise: {{Einheiten/Spaltennamen/Notation}}
[/RESOURCE-BLOCK]
4. Phasen (Detail)
[PHASE-BLOCK]
PHASE_ID: P0_BRIEF
Name: Briefing / Startlayout (Sonderphase)
Ziel der Phase: Szenario vollständig verstehen, Gesamtauftrag erfassen, Arbeitsmodus klären (ohne Checkfragen).
Zeit: {{10–15 Min}}
Startlayout (Chat-Ausgabe): Enthält: Kontext + vollständige Aufgabenstellung (Gesamtüberblick) + Ablauf + Abgabeprodukte + Start mit T0_1.
Übergang/Nächste Phase (Bedingung): Wenn T0_1 abgeschlossen → P1_BEDARF.
[/PHASE-BLOCK]
[PHASE-BLOCK]
PHASE_ID: P1_BEDARF
Name: Bedarf ermitteln
Ziel der Phase: Rezepte/Speisenplan → Warenbedarf für 50 Personen.
Zeit: {{eintragen}}
Übergang/Nächste Phase (Bedingung): {{eintragen}}
[/PHASE-BLOCK]
[PHASE-BLOCK]
PHASE_ID: P2_BESTAND
Name: Bestand abgleichen & Bestellung bereinigen
Ziel der Phase: Lagerbestand prüfen, Bestellung korrigieren.
Zeit: {{eintragen}}
Übergang/Nächste Phase (Bedingung): {{eintragen}}
[/PHASE-BLOCK]
[PHASE-BLOCK]
PHASE_ID: P3_ANGEBOT
Name: Angebote vergleichen & Lieferant auswählen
Ziel der Phase: Kriterien anwenden, Entscheidung begründen.
Zeit: {{eintragen}}
Übergang/Nächste Phase (Bedingung): {{eintragen}}
[/PHASE-BLOCK]
[PHASE-BLOCK]
PHASE_ID: P4_DEBRIEF
Name: Debriefing / Reflexion & Transfer
Ziel der Phase: Lernen sichern, Transfer herstellen.
Zeit: {{eintragen}}
Übergang/Nächste Phase (Bedingung): {{eintragen}}
[/PHASE-BLOCK]
5. Aufgaben (Tasks) – kompaktes Chatbot-Layout
Hinweis: Pro Task sind die „Nach 1. Versuch“-Elemente (Hinweise, Rubrik-Feedback) als separater Abschnitt markiert und dürfen erst nach der ersten Eingabe gezeigt werden.
[TASK-BLOCK]
TASK_ID: T0_1_AUFTRAGSKLAERUNG
Phase: P0_BRIEF
Lernziele: Handlungssituation verstehen; Aufgaben erkennen; Lösungsweg gemeinsam klären.
Orientierungsfilter (Rubrik-Kriterien kurz): RB_T0_1 | C1 Situationsverständnis, C2 Aufgabenerkennung, C3 Lösungsansatz
Aufgabe: Handlungssituation

Die Firma „Love it? Save it!" hat in zwei Wochen im Hotel DOCK 03 einen Veranstaltungsraum für eine große Tagung gebucht.

Alle Abteilungen des Hotels DOCK 03 arbeiten unter Hochdruck an den Vorbereitungen, um einen reibungslosen Ablauf zu garantieren.

Für die Tagung ist ein Mittagslunch in Form eines 3-Gang-Menüs vorgesehen:
- Möhrensuppe mit Croutons
- Hamburger Pannfisch vom Kabeljau mit Blattspinat und Bratkartoffeln
- Rote Grütze mit Vanilleeis

Auch hier müssen entsprechende Vorbereitungen getroffen werden. Vor allem müssen die benötigten Lebensmittel bestellt werden. Da der zuständige Koch länger erkrankt ist, seid ihr dafür zuständig.

Eingabeaufforderung: Ziel- und Auftragsklärung: „Was ist nun zu tun und wie können wir die neue Situation bewältigen?"
— Nach 1. Lösungsversuch ausgeben (nicht in der Erst-Ausgabe) —
Input/Material (intern): R_TEXT_SITUATION, R_BRIEF_VERANSTALTER, R_TEXT_TASKS
Rubrik (für Feedback): RB_T0_1
Teilhinweise (Scaffolds): Hint1: Was muss alles organisiert werden? | Hint2: Welche Schritte sind nötig? | Hint3: Was brauchen wir, bevor wir bestellen können?
Typische Fehler (optional): {{eintragen}}
Abgabeformat (Output): {{eintragen (aus Aufgabe ableiten)}}
Zeit/Umfang: {{eintragen}}
[/TASK-BLOCK]
[TASK-BLOCK]
TASK_ID: T1_1_BEDARF
Phase: P1_BEDARF
Lernziele: Warenbedarf für 50 Personen korrekt ableiten (Skalierung, Vollständigkeit, Einheiten).
Orientierungsfilter (Rubrik-Kriterien kurz): RB_T1_1 | C1 Skalierung, C2 Vollständigkeit, C3 Einheiten, C4 Quelle Möhrensuppe
Aufgabe: Warenanforderung feststellen
Im Folgenden sollst du den Warenbedarf (Lebensmittel und Getränke) für die Tagung im Hotel Dock 03 ermitteln.
Für die Tagung sollen die folgenden Speisen angeboten werden:
- Möhrensuppe mit Croutons (Rezept muss recherchiert werden)
- Hamburger Pannfisch mit Blattspinat und Bratkartoffeln (Rezept für 5 Personen)
- Hamburger Rote Grütze mit Vanilleeis (Rezept für 10 Personen)
Getränke:
- Wasser
- Apfelsaft
- Kaffee

a) Ermittel die Warenanforderung der Tagung und fülle die Tabelle aus.
Eingabeaufforderung: Gib jetzt deine berechnete Warenanforderung ein (als Liste oder Tabelle) inkl. Einheiten und nenne deine Quelle für das Möhrensuppe-Rezept.
— Nach 1. Lösungsversuch ausgeben (nicht in der Erst-Ausgabe) —
Input/Material (intern): R_RECHERCHE_MOEHRENSUPPE, R_REZEPT_PANNFISCH, R_REZEPT_ROTEGRUETZE, R_FUNC_SHEET, R_TEXT_TASKS
Rubrik (für Feedback): RB_T1_1
Teilhinweise (Scaffolds): Hint1: Rezepte auf 50 skalieren | Hint2: Einheiten prüfen | Hint3: Plausibilität (Portionen)
Typische Fehler (optional): {{eintragen}}
Abgabeformat (Output): {{eintragen (aus Aufgabe ableiten)}}
Zeit/Umfang: {{eintragen}}
[/TASK-BLOCK]
[TASK-BLOCK]
TASK_ID: T2_1_BESTAND
Phase: P2_BESTAND
Lernziele: Bedarf und Bestand korrekt abgleichen; Bestellung logisch bereinigen und dokumentieren.
Orientierungsfilter (Rubrik-Kriterien kurz): RB_T2_1 | C1 Korrekte Abzüge, C2 Plausibilität, C3 Dokumentation
Aufgabe: Bestand abgleichen
Nachdem du die Warenanforderung ermittelt hast, sollst du im Folgenden noch den Bestand prüfen.
b) Prüfe den Bestand und gleiche ihn mit der ermittelten Warenanforderung ab.
c) Bereinige die Bestellung, indem du alle vorhandenen Waren aus der Bestellung streichst oder Mengen anpasst.
Eingabeaufforderung: Gib jetzt deine bereinigte Bestellung ein (Liste/Tabelle) und erkläre in 3–5 Sätzen deine wichtigsten Änderungen.
— Nach 1. Lösungsversuch ausgeben (nicht in der Erst-Ausgabe) —
Input/Material (intern): R_TEXT_TASKS
Rubrik (für Feedback): RB_T2_1
Teilhinweise (Scaffolds): Hint1: Bestand markieren | Hint2: Bedarf - Bestand | Hint3: sinnvoll runden (Gebinde)
Typische Fehler (optional): {{eintragen}}
Abgabeformat (Output): {{eintragen (aus Aufgabe ableiten)}}
Zeit/Umfang: {{eintragen}}
[/TASK-BLOCK]
[TASK-BLOCK]
TASK_ID: T3_1_ANGEBOT
Phase: P3_ANGEBOT
Lernziele: Angebote systematisch vergleichen; Kriterien anwenden; Lieferant nachvollziehbar begründen.
Orientierungsfilter (Rubrik-Kriterien kurz): RB_T3_1 | C1 Kriterienanwendung, C2 Nachvollziehbarkeit, C3 Wirtschaftlichkeit, C4 Qualität/Risiko
Aufgabe: Anfrage und Angebot
Da du die Bestellung bereinigt hast, sollst du nun einen passenden Lieferanten finden.
d) Recherchiere mögliche Handelspartner im Raum Hamburg und trage diese ein.
e) Vergleiche Angebote anhand der Kriterien.
f) Entscheide dich für einen Lieferanten und begründe deine Entscheidung anhand der Kriterien.
Eingabeaufforderung: Gib jetzt deinen Angebotsvergleich (oder die wichtigsten Zahlen/Infos) ein und formuliere danach deine Lieferantenentscheidung in 8–12 Sätzen mit Kriterienbezug.
— Nach 1. Lösungsversuch ausgeben (nicht in der Erst-Ausgabe) —
Input/Material (intern): R_WORKSHEET_ANGEBOT, R_CRITERIA_LIEFERANT, R_PARTNER_BRAINSTORM, R_TEXT_TASKS
Rubrik (für Feedback): RB_T3_1
Teilhinweise (Scaffolds): Hint1: Kriterienliste systematisch nutzen | Hint2: harte/weiche Kriterien trennen | Hint3: 2–3 Belege aus Tabelle
Typische Fehler (optional): {{eintragen}}
Abgabeformat (Output): {{eintragen (aus Aufgabe ableiten)}}
Zeit/Umfang: {{eintragen}}
[/TASK-BLOCK]
6. Bewertungsrubriken (Rubrics – für Feedback nach 1. Versuch)
Hinweis: Rubrik-Details (Levels/Anker) werden für Feedback genutzt und sollen im Chat erst nach dem 1. Lösungsversuch angewandt/ausgegeben werden. Vorher werden nur die Orientierungsfilter (Kriterien kurz) gezeigt.
[RUBRIC-BLOCK]
RUBRIC_ID: RB_T0_1
Gilt für TASK_ID: T0_1_AUFTRAGSKLAERUNG
Skala: 0–2 (0 = nicht erfüllt, 1 = teilweise, 2 = erfüllt)
Hinweise zur Bewertung: Kriteriumsbezogen, mit Belegen aus der Schülerantwort. Kurz und konstruktiv.
Kriterien:
Kriterium_ID: C1_Situationsverstaendnis | Kriterium: Situation vollständig verstanden
Level 0: Situation nicht verstanden
Level 1: Teilweise verstanden (nur Teile erfasst)
Level 2: Vollständig verstanden (Event, Menü, Verantwortung)
Kriterium_ID: C2_Aufgabenerkennung | Kriterium: Notwendige Aufgaben erkannt
Level 0: Keine konkreten Aufgaben genannt
Level 1: Einige Aufgaben erkannt
Level 2: Hauptaufgaben klar erkannt (Bedarf ermitteln, bestellen, organisieren)
Kriterium_ID: C3_Loesungsansatz | Kriterium: Lösungsweg skizziert
Level 0: Kein Lösungsansatz
Level 1: Vager Ansatz
Level 2: Konkreter, logischer Lösungsweg skizziert
[/RUBRIC-BLOCK]
[RUBRIC-BLOCK]
RUBRIC_ID: RB_T1_1
Gilt für TASK_ID: T1_1_BEDARF
Skala: 0–2 (0 = nicht erfüllt, 1 = teilweise, 2 = erfüllt)
Hinweise zur Bewertung: Kriteriumsbezogen, mit Belegen aus der Schülerantwort. Kurz und konstruktiv.
Kriterien (Platzhalter-Levels bitte ausfüllen):
Kriterium_ID: C1_Skalierung | Kriterium: {{Beschreibung}}
Level 0: {{...}}
Level 1: {{...}}
Level 2: {{...}}
Ankerbeispiele: {{...}}
Kriterium_ID: C2_Vollstaendigkeit | Kriterium: {{Beschreibung}}
Level 0: {{...}}
Level 1: {{...}}
Level 2: {{...}}
Ankerbeispiele: {{...}}
Kriterium_ID: C3_Einheiten | Kriterium: {{Beschreibung}}
Level 0: {{...}}
Level 1: {{...}}
Level 2: {{...}}
Ankerbeispiele: {{...}}
Kriterium_ID: C4_Quelle_Moehrensuppe | Kriterium: {{Beschreibung}}
Level 0: {{...}}
Level 1: {{...}}
Level 2: {{...}}
Ankerbeispiele: {{...}}
[/RUBRIC-BLOCK]
[RUBRIC-BLOCK]
RUBRIC_ID: RB_T2_1
Gilt für TASK_ID: T2_1_BESTAND
Skala: 0–2 (0 = nicht erfüllt, 1 = teilweise, 2 = erfüllt)
Hinweise zur Bewertung: Kriteriumsbezogen, mit Belegen aus der Schülerantwort. Kurz und konstruktiv.
Kriterien (Platzhalter-Levels bitte ausfüllen):
Kriterium_ID: C1_Korrekte_Abzuege | Kriterium: {{Beschreibung}}
Level 0: {{...}}
Level 1: {{...}}
Level 2: {{...}}
Ankerbeispiele: {{...}}
Kriterium_ID: C2_Plausibilitaet | Kriterium: {{Beschreibung}}
Level 0: {{...}}
Level 1: {{...}}
Level 2: {{...}}
Ankerbeispiele: {{...}}
Kriterium_ID: C3_Dokumentation | Kriterium: {{Beschreibung}}
Level 0: {{...}}
Level 1: {{...}}
Level 2: {{...}}
Ankerbeispiele: {{...}}
[/RUBRIC-BLOCK]
[RUBRIC-BLOCK]
RUBRIC_ID: RB_T3_1
Gilt für TASK_ID: T3_1_ANGEBOT
Skala: 0–2 (0 = nicht erfüllt, 1 = teilweise, 2 = erfüllt)
Hinweise zur Bewertung: Kriteriumsbezogen, mit Belegen aus der Schülerantwort. Kurz und konstruktiv.
Kriterien (Platzhalter-Levels bitte ausfüllen):
Kriterium_ID: C1_Kriterienanwendung | Kriterium: {{Beschreibung}}
Level 0: {{...}}
Level 1: {{...}}
Level 2: {{...}}
Ankerbeispiele: {{...}}
Kriterium_ID: C2_Nachvollziehbarkeit | Kriterium: {{Beschreibung}}
Level 0: {{...}}
Level 1: {{...}}
Level 2: {{...}}
Ankerbeispiele: {{...}}
Kriterium_ID: C3_Wirtschaftlichkeit | Kriterium: {{Beschreibung}}
Level 0: {{...}}
Level 1: {{...}}
Level 2: {{...}}
Ankerbeispiele: {{...}}
Kriterium_ID: C4_Qualitaet_Risiko | Kriterium: {{Beschreibung}}
Level 0: {{...}}
Level 1: {{...}}
Level 2: {{...}}
Ankerbeispiele: {{...}}
[/RUBRIC-BLOCK]
7. Musterlösungen (optional, später ergänzen)
Hinweis: Musterlösungen erst nach bestandenem Maschinenlesbarkeits-Test ergänzen. Im Schüler*innen-Chat nur nach Versuch oder im Lehrkraft-Modus vollständig zeigen.
8. Debriefing (Reflexion & Transfer)
[DEBRIEF-BLOCK]
DEBRIEF_ID: D_P4
Zugehörige Phase(n): P0_BRIEF, P1_BEDARF, P2_BESTAND, P3_ANGEBOT
Ziel: Entscheidungen reflektieren, Fehlerquellen erkennen, Transfer in reale Einkaufs-/Küchenpraxis herstellen.
Beschreibung – Was ist passiert?
Welche Entscheidung war am schwierigsten und warum?
Wo gab es Unsicherheiten (Einheiten, Mengen, Lieferantenwahl)?
Analyse – Warum ist es passiert?
Welche Daten/Tabellen waren entscheidend?
Welche Annahmen habt ihr getroffen?
Transfer – Was bedeutet das in der Praxis?
Welche Routine/Checkliste würdet ihr für echte Wareneinkäufe ableiten?
Alternative Handlungen
Welche andere Lieferantenentscheidung wäre vertretbar – unter welchen Bedingungen?
Abschlussprodukt: 6–8 Sätze Reflexion + 3 Learnings (Bulletpoints)
[/DEBRIEF-BLOCK]
9. Änderungslog
Datum: 2026-01-14 | Version: v1.1 (kompakt) | Änderung: Chatbot-Ausgabe komprimiert (Rolle/Checkfragen entfernt; Lernziel→Aufgabe→Eingabeaufforderung; Feedback/Hints erst nach 1. Versuch; P0 Startlayout erweitert). | Bearbeiter: Prompti (ChatGPT)
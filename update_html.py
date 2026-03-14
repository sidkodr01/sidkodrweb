import sys

replacements = {
    '[DE] Microland': 'Microland',
    '[DE] Technical Operations Intern': 'Praktikant im technischen Betrieb',
    '[DE] Jan 2026 – Present': 'Jan. 2026 – heute',
    '[DE] Bangalore, KA': 'Bangalore, KA',
    '[DE] Internship': 'Praktikum',
    '[DE] Closing the Loop on Automated Escalation': 'Den Kreislauf der automatisierten Eskalation schließen',
    "[DE] When a support ticket arrives in an enterprise environment, the first question an engineer asks is: what has already been tried? Without a clear answer, they duplicate effort, lose time, and often start from scratch on problems that were partially solved. That gap — between what an automated system does and what a human engineer can see — was the problem I was brought in to address.": "Wenn ein Support-Ticket in einer Unternehmensumgebung eingeht, lautet die erste Frage eines Ingenieurs: Was wurde bereits versucht? Ohne eine klare Antwort wird Aufwand doppelt betrieben, Zeit verloren und oft von vorne begonnen bei Problemen, die bereits teilweise gelöst waren. Diese Lücke — zwischen dem, was ein automatisiertes System tut, und dem, was ein menschlicher Ingenieur sehen kann — war das Problem, das ich lösen sollte.",
    "[DE] The system I worked on sits between the client and the engineer. A bot handles initial troubleshooting autonomously and escalates only when it cannot resolve the issue. The problem was that when escalation happened, the bot's entire decision trail was invisible. Engineers had no way of knowing which steps had been attempted, which had failed, or why the bot had given up. Every handoff started blind.": "Das System, an dem ich arbeitete, sitzt zwischen dem Kunden und dem Ingenieur. Ein Bot übernimmt die erste Fehlersuche eigenständig und eskaliert nur, wenn er das Problem nicht lösen kann. Das Problem war, dass beim Eskalieren die gesamte Entscheidungskette des Bots unsichtbar war. Ingenieure hatten keine Möglichkeit zu wissen, welche Schritte versucht wurden, welche fehlgeschlagen waren oder warum der Bot aufgegeben hatte. Jede Übergabe begann blind.",
    "[DE] My work was to fix that. I built out the logging layer that made the bot's reasoning visible and traceable — so that by the time a ticket reached a human engineer, they had a complete record of what the bot had already tried. The handoff became informative rather than abrupt.": "Meine Aufgabe war es, das zu beheben. Ich baute die Logging-Schicht auf, die das Denken des Bots sichtbar und nachvollziehbar machte — sodass ein Ingenieur beim Eingang eines Tickets eine vollständige Aufzeichnung dessen hatte, was der Bot bereits versucht hatte. Die Übergabe wurde informativ statt abrupt.",
    "[DE] Enterprise networking and the codebase were both new to me when I started. I treated the first few weeks as a structured orientation — knowledge transfer sessions, research into the problem space, and studying how similar automation challenges had been approached elsewhere. I also spent time learning the IT Infrastructure Library and IT Service Management frameworks that govern how enterprise service operations actually run — not just the technical mechanics, but how organisations formally think about incidents, escalation, and service continuity. Understanding that process layer shaped how I approached the logging design, because the output had to be useful to engineers operating within those frameworks, not just technically correct.": "Enterprise-Netzwerke und die Codebasis waren beide neu für mich, als ich anfing. Ich behandelte die ersten Wochen als strukturierte Einarbeitung — Wissenstransfersitzungen, Recherche im Problembereich und das Studium, wie ähnliche Automatisierungsherausforderungen anderswo angegangen wurden. Ich verbrachte auch Zeit damit, die IT Infrastructure Library und IT Service Management-Frameworks zu lernen, die den tatsächlichen Betrieb von Unternehmensservices regeln — nicht nur die technischen Mechanismen, sondern wie Organisationen formal über Vorfälle, Eskalation und Servicekontinuität nachdenken. Das Verständnis dieser Prozessschicht prägte meinen Ansatz beim Logging-Design, da die Ausgabe für Ingenieure, die in diesen Frameworks arbeiten, nützlich sein musste — nicht nur technisch korrekt.",
    "[DE] Networking": "Netzwerke",
    "[DE] The practice of connecting computers and devices so they can communicate and share resources.": "Die Praxis, Computer und Geräte zu verbinden, damit sie kommunizieren und Ressourcen teilen können.",
    "[DE] &lt;strong&gt;Beispiel:&lt;/strong&gt; Configuring routers and switches so that different departments in an office can access the same servers securely.": "&lt;strong&gt;Beispiel:&lt;/strong&gt; Router und Switches konfigurieren, damit verschiedene Abteilungen in einem Büro sicher auf dieselben Server zugreifen können.",
    "[DE] IT Infrastructure": "IT-Infrastruktur",
    "[DE] The collective hardware, software, networks, and facilities that an organisation uses to deliver IT services.": "Die Gesamtheit der Hardware, Software, Netzwerke und Einrichtungen, die eine Organisation zur Bereitstellung von IT-Diensten nutzt.",
    "[DE] &lt;strong&gt;Beispiel:&lt;/strong&gt; Managing the servers, storage systems, and network equipment that keep a company's digital operations running 24/7.": "&lt;strong&gt;Beispiel:&lt;/strong&gt; Verwaltung der Server, Speichersysteme und Netzwerkgeräte, die den digitalen Betrieb eines Unternehmens rund um die Uhr aufrechterhalten.",
    "[DE] Automation": "Automatisierung",
    "[DE] Using software or scripts to perform repetitive tasks without human intervention.": "Software oder Skripte nutzen, um wiederkehrende Aufgaben ohne menschliches Eingreifen auszuführen.",
    "[DE] &lt;strong&gt;Beispiel:&lt;/strong&gt; A bot that automatically attempts to resolve common network issues before escalating them to an engineer.": "&lt;strong&gt;Beispiel:&lt;/strong&gt; Ein Bot, der automatisch versucht, häufige Netzwerkprobleme zu lösen, bevor er sie an einen Ingenieur eskaliert.",
    "[DE] Logging": "Protokollierung",
    "[DE] Recording a system's actions and decisions in a structured, traceable log for debugging and auditing.": "Die Aktionen und Entscheidungen eines Systems in einem strukturierten, nachvollziehbaren Protokoll für Debugging und Auditing aufzeichnen.",
    "[DE] &lt;strong&gt;Beispiel:&lt;/strong&gt; Capturing every step a troubleshooting bot takes so engineers can see exactly what was tried before a ticket reaches them.": "&lt;strong&gt;Beispiel:&lt;/strong&gt; Jeden Schritt eines Fehlerbehebungs-Bots erfassen, damit Ingenieure genau sehen, was versucht wurde, bevor ein Ticket sie erreicht.",
    "[DE] Troubleshooting": "Fehlerbehebung",
    "[DE] The systematic process of identifying and resolving problems in a system or network.": "Der systematische Prozess zur Identifikation und Behebung von Problemen in einem System oder Netzwerk.",
    "[DE] &lt;strong&gt;Beispiel:&lt;/strong&gt; Analysing incident logs to diagnose why a client's network connection keeps dropping during peak hours.": "&lt;strong&gt;Beispiel:&lt;/strong&gt; Vorfallsprotokolle analysieren, um zu diagnostizieren, warum die Netzwerkverbindung eines Kunden zu Stoßzeiten immer wieder abbricht.",
    "[DE] Python": "Python",
    "[DE] A versatile, beginner-friendly programming language widely used for automation, data analysis, and AI development.": "Eine vielseitige, einsteigerfreundliche Programmiersprache, die häufig für Automatisierung, Datenanalyse und KI-Entwicklung verwendet.",
    "[DE] &lt;strong&gt;Beispiel:&lt;/strong&gt; Writing scripts to automate log parsing and generate structured reports from raw system data.": "&lt;strong&gt;Beispiel:&lt;/strong&gt; Skripte schreiben, um Log-Parsing zu automatisieren und strukturierte Berichte aus rohen Systemdaten zu generieren."
}

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

for k, v in replacements.items():
    # Only replace data-de attributes
    content = content.replace(f'data-de="{k}"', f'data-de="{v}"')
    
with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)


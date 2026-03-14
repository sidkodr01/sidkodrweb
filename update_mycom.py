import codecs

with codecs.open("index.html", "r", encoding="utf-8") as f:
    text = f.read()

replacements = {
    '[DE] MyCom': 'MyCom',
    '[DE] R&amp;D Intern': 'F&amp;E-Praktikant',
    '[DE] May 2025 – Oct 2025': 'Mai 2025 – Okt. 2025',
    '[DE] Automating SBOM Extraction and Version Compliance in Container Deployments': 'SBOM-Extraktion und Versions-Compliance in Container-Deployments automatisieren',
    '[DE] In enterprise software deployment, version mismatch is one of the most silent failure modes. A single dependency running one version off from what the requirements document specifies can break systems in ways that are difficult to trace and expensive to fix after the fact. At MyCom, that risk was being managed entirely by hand — before every deployment, engineers manually cross-checked every package version across every file against the requirements document. The process was slow, dependent on individual thoroughness, and fundamentally unscalable.': 'Bei der Bereitstellung von Unternehmenssoftware ist Versionskonflikt eine der lautlosesten Fehlerquellen. Eine einzige Abhängigkeit, die eine Version abweicht von dem, was das Anforderungsdokument vorschreibt, kann Systeme auf schwer nachvollziehbare und nachträglich teure Weise beschädigen. Bei MyCom wurde dieses Risiko vollständig manuell verwaltet — vor jeder Bereitstellung prüften Ingenieure manuell jede Paketversion in jeder Datei gegen das Anforderungsdokument. Der Prozess war langsam, von individueller Sorgfalt abhängig und grundlegend nicht skalierbar.',
    '[DE] The problem I was asked to solve was straightforward to state but non-trivial to build: eliminate that manual check entirely, and replace it with something automatic, reliable, and fast.': 'Das Problem, das ich lösen sollte, war einfach zu formulieren, aber nicht trivial umzusetzen: den manuellen Check vollständig eliminieren und durch etwas Automatisches, Zuverlässiges und Schnelles ersetzen.',
    '[DE] I built a system that extracts a Software Bill of Materials from container images, compares every package version against the requirements document automatically, flags every mismatch, and compiles the results into a structured report — in a fraction of the time the manual process required. A version comparison script existed in a basic form when I arrived, but the final system was so fundamentally rearchitected that it was effectively built from scratch.': 'Ich baute ein System, das eine Software Bill of Materials aus Container-Images extrahiert, jede Paketversion automatisch gegen das Anforderungsdokument vergleicht, jeden Konflikt markiert und die Ergebnisse in einem strukturierten Bericht zusammenfasst — in einem Bruchteil der Zeit, die der manuelle Prozess erforderte. Ein grundlegendes Versionsvergleichsskript existierte bereits, aber das finale System war so grundlegend neu architektiert, dass es praktisch von Grund auf neu gebaut wurde.',
    '[DE] The part I\'m most satisfied with wasn\'t in the original brief. Beyond the core compliance check, I added individual package-level breakdowns, an overall compliance summary table, and additional codebase health metrics that gave the team a richer picture of their deployment readiness. These additions weren\'t requested — I included them because the data was already there and the insight seemed worth surfacing. They became the most referenced sections of the report.': 'Der Teil, mit dem ich am zufriedensten bin, stand nicht im ursprünglichen Auftrag. Über die Kern-Compliance-Prüfung hinaus fügte ich individuelle Aufschlüsselungen auf Paketebene, eine Gesamtkompliance-Übersichtstabelle und zusätzliche Codebase-Gesundheitsmetriken hinzu, die dem Team ein umfassenderes Bild ihrer Bereitstellungsbereitschaft gaben. Diese Ergänzungen wurden nicht angefordert — ich fügte sie hinzu, weil die Daten bereits vorhanden waren und die Erkenntnisse es wert schienen, sichtbar gemacht zu werden. Sie wurden zu den meistzitierten Abschnitten des Berichts.',
    '[DE] The next stage was integrating the system into GitLab CI/CD so compliance checks would run automatically on every build — making version verification a permanent, invisible layer of the deployment pipeline rather than a pre-deployment ritual. The internship ended before that integration was complete, but the architecture was designed for it and the foundation was in place.': 'Der nächste Schritt war die Integration des Systems in GitLab CI/CD, damit Compliance-Prüfungen bei jedem Build automatisch ausgeführt werden — und die Versionsverifizierung zu einer dauerhaften, unsichtbaren Schicht der Deployment-Pipeline statt eines Vor-Deployment-Rituals zu machen. Das Praktikum endete, bevor diese Integration abgeschlossen war, aber die Architektur war darauf ausgelegt und die Grundlage war vorhanden.',
    '[DE] Python': 'Python',
    '[DE] A versatile programming language widely used for automation, data processing, and building AI-powered tools.': 'Eine vielseitige Programmiersprache, die häufig für Automatisierung, Datenverarbeitung und den Aufbau KI-gestützter Tools verwendet wird.',
    '[DE] &lt;strong&gt;Beispiel:&lt;/strong&gt; Writing the scripts that extract package metadata from container images and automatically compare versions against requirements documents.': '&lt;strong&gt;Beispiel:&lt;/strong&gt; Skripte schreiben, die Paketmetadaten aus Container-Images extrahieren und Versionen automatisch gegen Anforderungsdokumente vergleichen.',
    '[DE] Bash': 'Bash',
    '[DE] A command-line scripting language used to automate tasks and interact directly with the operating system.': 'Eine Kommandozeilen-Skriptsprache, die zur Automatisierung von Aufgaben und zur direkten Interaktion mit dem Betriebssystem verwendet wird.',
    '[DE] &lt;strong&gt;Beispiel:&lt;/strong&gt; Writing shell scripts to trigger SBOM extraction and feed the output into the Python comparison pipeline.': '&lt;strong&gt;Beispiel:&lt;/strong&gt; Shell-Skripte schreiben, um die SBOM-Extraktion auszulösen und die Ausgabe in die Python-Vergleichspipeline einzuspeisen.',
    '[DE] SBOM': 'SBOM',
    '[DE] Software Bill of Materials — a complete, structured list of every package, library, and dependency inside a software system.': 'Software Bill of Materials — eine vollständige, strukturierte Liste aller Pakete, Bibliotheken und Abhängigkeiten innerhalb eines Softwaresystems.',
    '[DE] &lt;strong&gt;Beispiel:&lt;/strong&gt; Extracting the full list of packages inside a Docker container image to verify every version matches deployment requirements.': '&lt;strong&gt;Beispiel:&lt;/strong&gt; Die vollständige Paketliste eines Docker-Container-Images extrahieren, um zu überprüfen, ob jede Version den Deployment-Anforderungen entspricht.',
    '[DE] Docker': 'Docker',
    '[DE] A platform that packages software into isolated containers so it runs consistently across different environments.': 'Eine Plattform, die Software in isolierte Container verpackt, damit sie in verschiedenen Umgebungen konsistent läuft.',
    '[DE] &lt;strong&gt;Beispiel:&lt;/strong&gt; Pulling container images and extracting their package manifests to feed into the version comparison and compliance pipeline.': '&lt;strong&gt;Beispiel:&lt;/strong&gt; Container-Images abrufen und ihre Paketmanifeste extrahieren, um sie in die Versionsvergleichs- und Compliance-Pipeline einzuspeisen.',
    '[DE] Version Control': 'Versionskontrolle',
    '[DE] The practice of tracking and managing changes to software over time so teams can collaborate without overwriting each other\'s work.': 'Die Praxis, Änderungen an Software im Laufe der Zeit zu verfolgen und zu verwalten, damit Teams zusammenarbeiten können, ohne die Arbeit des anderen zu überschreiben.',
    '[DE] &lt;strong&gt;Beispiel:&lt;/strong&gt; Managing the SBOM comparison scripts in Git so changes were tracked and the team could review the history of every update.': '&lt;strong&gt;Beispiel:&lt;/strong&gt; Die SBOM-Vergleichsskripte in Git verwalten, damit Änderungen nachverfolgt und das Team die Historie jedes Updates einsehen konnte.',
    '[DE] Compliance Automation': 'Compliance-Automatisierung',
    '[DE] Using software to automatically verify that a system meets required standards or specifications — replacing manual checks.': 'Software verwenden, um automatisch zu überprüfen, ob ein System die erforderlichen Standards oder Spezifikationen erfüllt — und manuelle Prüfungen ersetzen.',
    '[DE] &lt;strong&gt;Beispiel:&lt;/strong&gt; Automatically comparing every package version in a deployment against the requirements document and flagging mismatches before anything goes live.': '&lt;strong&gt;Beispiel:&lt;/strong&gt; Jede Paketversion eines Deployments automatisch gegen das Anforderungsdokument vergleichen und Konflikte markieren, bevor etwas live geht.',
    '[DE] Excel Reporting': 'Excel-Berichterstellung',
    '[DE] Generating structured, formatted spreadsheet reports that make complex data easy to read and act on.': 'Strukturierte, formatierte Tabellenberichte erstellen, die komplexe Daten leicht lesbar und handlungsorientiert machen.',
    '[DE] &lt;strong&gt;Beispiel:&lt;/strong&gt; Producing multi-sheet Excel reports with individual package comparisons, overall compliance summaries, and version mismatch highlights for the internal team.': '&lt;strong&gt;Beispiel:&lt;/strong&gt; Mehrseitige Excel-Berichte mit individuellen Paketvergleichen, Gesamtkompliance-Zusammenfassungen und hervorgehobenen Versionskonflikten für das interne Team erstellen.',
    '[DE] GitLab CI/CD': 'GitLab CI/CD',
    '[DE] A continuous integration and deployment platform that automatically builds, tests, and deploys code every time a change is pushed.': 'Eine Plattform für kontinuierliche Integration und Bereitstellung, die bei jeder Code-Änderung automatisch baut, testet und deployt.',
    '[DE] &lt;strong&gt;Beispiel:&lt;/strong&gt; The planned next stage — integrating the compliance pipeline into GitLab so version checks would run automatically on every deployment without human intervention.': '&lt;strong&gt;Beispiel:&lt;/strong&gt; Der geplante nächste Schritt — die Compliance-Pipeline in GitLab integrieren, damit Versionskontrollen bei jedem Deployment automatisch ohne manuellen Eingriff ausgeführt werden.',
    '[DE] DevOps': 'DevOps',
    '[DE] A set of practices that combines software development and IT operations to deliver software faster and more reliably.': 'Eine Reihe von Praktiken, die Softwareentwicklung und IT-Betrieb kombiniert, um Software schneller und zuverlässiger bereitzustellen.',
    '[DE] &lt;strong&gt;Beispiel:&lt;/strong&gt; Building automated compliance tooling that sits between the development team and production deployments, reducing manual overhead and deployment risk.': '&lt;strong&gt;Beispiel:&lt;/strong&gt; Automatisierte Compliance-Tools aufbauen, die zwischen dem Entwicklungsteam und Produktions-Deployments sitzen und manuellen Aufwand sowie Deployment-Risiken reduzieren.'
}

import re

for k, v in replacements.items():
    text = text.replace(f'data-de="{k}"', f'data-de="{v}"')
    text = text.replace(f'data-de-html="{k}"', f'data-de-html="{v}"')

def replace_mycom_internship(m):
    return m.group(0).replace('data-de="[DE] Internship"', 'data-de="Praktikum"')

pattern = re.compile(r'(<h3[^>]+data-de="(?:\[DE\] )?MyCom".*?)(<span class="proj-category-badge" data-en="Internship" data-de="\[DE\] Internship">Internship</span>)', re.DOTALL)
text = pattern.sub(replace_mycom_internship, text)

with codecs.open("index.html", "w", encoding="utf-8") as f:
    f.write(text)

print("Updates applied to index.html successfully.")

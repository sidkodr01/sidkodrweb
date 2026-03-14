import codecs
import re

with codecs.open("index.html", "r", encoding="utf-8") as f:
    text = f.read()

replacements = {
    '[DE] Aster Digital Health': 'Aster Digital Health',
    '[DE] Product Management Intern': 'Praktikant im Produktmanagement',
    '[DE] May 2024 – Jun 2024': 'Mai 2024 – Jun. 2024',
    '[DE] Finding What Slips Through: Software Quality Assurance at Scale': 'Was durchrutscht: Software-Qualitätssicherung im großen Maßstab',
    '[DE] Production bugs in web platforms rarely originate from core functionality — they surface in edge cases, incomplete user flows, and untested state transitions that pass code review but fail under real usage conditions. At Aster Digital Health, the problem was identifying these failure points in a live healthcare web platform before they reached end users.': 'Produktionsfehler in Web-Plattformen entstehen selten aus der Kernfunktionalität — sie tauchen in Randfällen, unvollständigen Benutzerflüssen und nicht getesteten Zustandsübergängen auf, die den Code-Review bestehen, aber unter realen Nutzungsbedingungen versagen. Bei Aster Digital Health bestand das Problem darin, diese Schwachstellen in einer live Healthcare-Web-Plattform zu identifizieren, bevor sie die Endnutzer erreichten.',
    '[DE] My role was systematic black-box testing across the platform. This involved mapping user flows, designing test cases around boundary conditions and edge cases, reproducing reported and discovered bugs, isolating root causes, and producing structured defect reports that development teams could action directly.': 'Meine Aufgabe war systematisches Black-Box-Testing der gesamten Plattform. Dazu gehörten das Kartografieren von Benutzerflüssen, das Entwerfen von Testfällen rund um Grenzbedingungen und Randfälle, das Reproduzieren gemeldeter und entdeckter Fehler, das Isolieren von Grundursachen und das Erstellen strukturierter Fehlerberichte, die Entwicklungsteams direkt umsetzen konnten.',
    '[DE] The work built a testing mindset that has carried into every technical role since — treating every assumption in a system design as a potential failure point, and verifying rather than inferring how a system behaves under conditions it wasn\'t explicitly built for.': 'Die Arbeit formte eine Testmentalität, die sich in jede seitdem folgende technische Rolle übertragen hat — jede Annahme in einem Systemdesign als potenziellen Fehlerpunkt zu behandeln und zu verifizieren statt zu schlussfolgern, wie sich ein System unter Bedingungen verhält, für die es nicht explizit gebaut wurde.',
    '[DE] Software Testing': 'Softwaretests',
    '[DE] The process of evaluating a software application to find bugs, inconsistencies, or anything that doesn\'t work as intended.': 'Der Prozess der Bewertung einer Softwareanwendung, um Fehler, Inkonsistenzen oder alles zu finden, was nicht wie beabsichtigt funktioniert.',
    '[DE] &lt;strong&gt;Beispiel:&lt;/strong&gt; Systematically navigating through Aster\'s web platform to identify broken flows, UI issues, and edge cases before they reached real users.': '&lt;strong&gt;Beispiel:&lt;/strong&gt; Systematisch durch Asters Web-Plattform navigieren, um fehlerhafte Flüsse, UI-Probleme und Randfälle zu identifizieren, bevor sie echte Nutzer erreichen.',
    '[DE] Quality Assurance': 'Qualitätssicherung',
    '[DE] The practice of ensuring a product meets defined standards of quality before it is released.': 'Die Praxis sicherzustellen, dass ein Produkt definierte Qualitätsstandards erfüllt, bevor es veröffentlicht wird.',
    '[DE] &lt;strong&gt;Beispiel:&lt;/strong&gt; Reviewing deployed features to catch small errors and inconsistencies that slipped through the development process.': '&lt;strong&gt;Beispiel:&lt;/strong&gt; Bereitgestellte Funktionen überprüfen, um kleine Fehler und Inkonsistenzen zu entdecken, die durch den Entwicklungsprozess geschlüpft sind.',
    '[DE] Bug Reporting': 'Fehlermeldung',
    '[DE] Documenting identified issues in a software system in a clear, reproducible way so developers can find and fix them.': 'Identifizierte Probleme in einem Softwaresystem klar und reproduzierbar dokumentieren, damit Entwickler sie finden und beheben können.',
    '[DE] &lt;strong&gt;Beispiel:&lt;/strong&gt; Logging discovered issues with steps to reproduce, expected behaviour, and actual behaviour so the development team could act on them efficiently.': '&lt;strong&gt;Beispiel:&lt;/strong&gt; Entdeckte Probleme mit Reproduktionsschritten, erwartetem Verhalten und tatsächlichem Verhalten protokollieren, damit das Entwicklungsteam effizient handeln kann.',
    '[DE] Web Platform Testing': 'Web-Plattform-Testing',
    '[DE] Testing a web-based application across different browsers, devices, and user flows to ensure it works correctly for all users.': 'Eine webbasierte Anwendung über verschiedene Browser, Geräte und Benutzerflüsse hinweg testen, um sicherzustellen, dass sie für alle Nutzer korrekt funktioniert.',
    '[DE] &lt;strong&gt;Beispiel:&lt;/strong&gt; Testing Aster\'s digital health platform across different scenarios to ensure patients and healthcare providers had a seamless experience.': '&lt;strong&gt;Beispiel:&lt;/strong&gt; Asters digitale Gesundheitsplattform in verschiedenen Szenarien testen, um sicherzustellen, dass Patienten und Gesundheitsdienstleister eine reibungslose Erfahrung haben.',
    '[DE] Healthcare Tech': 'Gesundheitstechnologie',
    '[DE] Technology products and platforms built specifically for the healthcare industry — covering everything from patient management to digital diagnostics.': 'Technologieprodukte und -plattformen, die speziell für die Gesundheitsbranche entwickelt wurden — von der Patientenverwaltung bis zur digitalen Diagnostik.',
    '[DE] &lt;strong&gt;Beispiel:&lt;/strong&gt; Working within a digital health company whose platform directly impacts how patients and providers interact with healthcare services.': '&lt;strong&gt;Beispiel:&lt;/strong&gt; In einem digitalen Gesundheitsunternehmen arbeiten, dessen Plattform direkt beeinflusst, wie Patienten und Anbieter mit Gesundheitsdiensten interagieren.'
}

for k, v in replacements.items():
    text = text.replace(f'data-de="{k}"', f'data-de="{v}"')
    text = text.replace(f'data-de-html="{k}"', f'data-de-html="{v}"')

def replace_aster_internship(m):
    return m.group(0).replace('data-de="[DE] Internship"', 'data-de="Praktikum"')

pattern = re.compile(r'(<h3[^>]+data-de="(?:\[DE\] )?Aster Digital Health".*?)(<span class="proj-category-badge" data-en="Internship" data-de="\[DE\] Internship">Internship</span>)', re.DOTALL)
text = pattern.sub(replace_aster_internship, text)

with codecs.open("index.html", "w", encoding="utf-8") as f:
    f.write(text)

print("Updates applied to index.html successfully.")

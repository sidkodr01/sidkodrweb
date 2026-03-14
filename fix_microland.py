import re

with open("index.html", "r", encoding="utf-8") as f:
    text = f.read()

replacements = {
    '[DE] ITIL': 'ITIL',
    '[DE] IT Infrastructure Library — a framework of best practices for delivering IT services.': 'IT Infrastructure Library — ein Framework von Best Practices für die Bereitstellung von IT-Services.',
    '[DE] &lt;strong&gt;Beispiel:&lt;/strong&gt; Using ITIL\'s incident management process to ensure every client issue is logged, prioritised, and resolved within agreed timeframes.': '&lt;strong&gt;Beispiel:&lt;/strong&gt; Anwendung des ITIL-Incident-Management-Prozesses, um sicherzustellen, dass jedes Kundenproblem protokolliert, priorisiert und innerhalb vereinbarter Fristen gelöst wird.',
    '[DE] ITSM': 'ITSM',
    '[DE] IT Service Management — the practice of designing, delivering, and improving IT services to meet business needs.': 'IT Service Management — die Praxis der Gestaltung, Bereitstellung und Verbesserung von IT-Services, um geschäftliche Anforderungen zu erfüllen.',
    '[DE] &lt;strong&gt;Beispiel:&lt;/strong&gt; Building a ticketing system that routes client issues through defined workflows so nothing falls through the cracks.': '&lt;strong&gt;Beispiel:&lt;/strong&gt; Aufbau eines Ticketing-Systems, das Kundenprobleme durch definierte Workflows steuert, damit nichts übersehen wird.'
}

for k, v in replacements.items():
    text = text.replace(f'data-de="{k}"', f'data-de="{v}"')

def replacer(match):
    attr = match.group(1)
    val = match.group(2)
    if "&lt;" in val and "&gt;" in val:
        return f'{attr}-html="{val}"'
    return match.group(0)

# Replace data-en="..." with data-en-html="..." if it contains &lt; or &gt;
# And replace data-de="..." with data-de-html="..." if it contains &lt; or &gt;
text = re.sub(r'(data-(?:en|de))="([^"]*)"', replacer, text)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(text)
print("Fixes applied successfully.")

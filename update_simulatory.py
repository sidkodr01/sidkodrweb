import re

with open("index.html", "r", encoding="utf-8") as f:
    text = f.read()

replacements = {
    '[DE] Simulatory AG': 'Simulatory AG',
    r'\[DE\] Software Developer (?:&amp;|&) ML Intern': 'Softwareentwickler &amp; ML-Praktikant',
    '[DE] Jun 2025 – Jan 2026': 'Jun. 2025 – Jan. 2026',
    # We only want to replace Internship for the Simulatory type-badge. We will do this carefully below.
    '[DE] From Raw Simulation Data to Structured Surgical Coaching': 'Von rohen Simulationsdaten zu strukturiertem chirurgischem Coaching',
    '[DE] Surgical simulation generates enormous amounts of raw performance data. The problem is that data alone tells a trainee surgeon very little — it doesn\'t explain what went wrong, why it went wrong, or what to do differently. At Simulatory, which builds robotic surgical simulators for spinal procedures, that gap between raw output and actionable insight was the problem I was asked to solve.': 'Chirurgische Simulationen erzeugen enorme Mengen an rohen Leistungsdaten. Das Problem ist, dass Daten allein einem angehenden Chirurgen wenig sagen — sie erklären nicht, was schiefgelaufen ist, warum es schiefgelaufen ist oder was man anders machen sollte. Bei Simulatory, das robotische Chirurgiesimulator für Wirbelsäuleneingriffe entwickelt, war diese Lücke zwischen rohem Output und verwertbaren Erkenntnissen das Problem, das ich lösen sollte.',
    '[DE] I built a pipeline that ingests the raw data produced by each simulation, processes and structures it, and generates coaching feedback that tells trainee surgeons specifically where they performed well and where they need to improve. The system is now in production and actively used in surgical training. The feedback it generates is the kind that previously didn\'t exist in a structured form — surgeons had intuition, but not a systematic, data-driven account of each trainee\'s performance.': 'Ich baute eine Pipeline, die die von jeder Simulation erzeugten Rohdaten aufnimmt, verarbeitet und strukturiert und Coaching-Feedback generiert, das angehenden Chirurgen genau sagt, wo sie gut abgeschnitten haben und wo sie sich verbessern müssen. Das System ist jetzt in Produktion und wird aktiv in der chirurgischen Ausbildung eingesetzt. Das generierte Feedback existierte zuvor nicht in strukturierter Form — Chirurgen hatten Intuition, aber keine systematische, datengestützte Auswertung der Leistung jedes Auszubildenden.',
    '[DE] The technical challenge was significant, but the harder problem was organisational. I was the only person in the company who could build this. No senior engineer to review my architecture, no technical peers to pressure-test my thinking, no safety net for the decisions I got wrong. In that environment, being mostly confident wasn\'t enough — every architectural and technical decision had to be fully stress-tested before I committed to it. That constraint changed how I approach problems. I stopped looking only for solutions and started looking for the failure modes in my solutions before anyone else could find them.': 'Die technische Herausforderung war erheblich, aber das schwierigere Problem war organisatorischer Natur. Ich war die einzige Person im Unternehmen, die das aufbauen konnte. Kein erfahrener Ingenieur, der meine Architektur überprüfte, keine technischen Kollegen, die mein Denken auf die Probe stellten, kein Sicherheitsnetz für falsche Entscheidungen. In diesem Umfeld reichte es nicht, größtenteils sicher zu sein — jede architektonische und technische Entscheidung musste vollständig stress-getestet werden, bevor ich sie umsetzte. Diese Einschränkung veränderte meinen Umgang mit Problemen. Ich hörte auf, nur nach Lösungen zu suchen, und begann, die Schwachstellen meiner Lösungen zu finden, bevor es jemand anderes konnte.',
    '[DE] Alongside the core pipeline, I built an annotation model that identifies anatomical structures on screen during simulations in real time, and explored generative medical imaging as a route to synthesising training data — though resource constraints kept that work at the research stage.': 'Neben der Kernpipeline baute ich ein Annotationsmodell, das anatomische Strukturen auf dem Bildschirm während Simulationen in Echtzeit erkennt, und erkundete generative medizinische Bildgebung als Weg zur Synthese von Trainingsdaten — obwohl Ressourcenbeschränkungen diese Arbeit auf der Forschungsebene hielten.',
    '[DE] Working in medical technology also recalibrated my sense of pace. In a domain where the end user is a surgeon and the product is someone\'s spine, speed is never the primary objective. Every change went through rigorous testing before deployment. Knowing when to slow down and verify — not just how to move fast — turned out to be the more important skill.': 'Die Arbeit in der Medizintechnik kalibrierte auch mein Gefühl für Tempo neu. In einem Bereich, in dem der Endnutzer ein Chirurg und das Produkt jemandes Wirbelsäule ist, ist Geschwindigkeit nie das primäre Ziel. Jede Änderung durchlief rigorose Tests vor der Bereitstellung. Zu wissen, wann man langsamer werden und überprüfen muss — nicht nur, wie man sich schnell bewegt — erwies sich als die wichtigere Fähigkeit.',
    '[DE] Python': 'Python',
    '[DE] A versatile programming language widely used for building AI pipelines, automation scripts, and data processing systems.': 'Eine vielseitige Programmiersprache, die häufig für den Aufbau von KI-Pipelines, Automatisierungsskripten und Datenverarbeitungssystemen verwendet wird.',
    '[DE] &lt;strong&gt;Beispiel:&lt;/strong&gt; Writing the end-to-end pipeline that ingests surgical simulation logs, processes them, and sends structured data to a Large Language Model for feedback generation.': '&lt;strong&gt;Beispiel:&lt;/strong&gt; Die End-to-End-Pipeline schreiben, die chirurgische Simulationsprotokolle aufnimmt, verarbeitet und strukturierte Daten zur Feedback-Generierung an ein Large Language Model sendet.',
    '[DE] Large Language Models': 'Große Sprachmodelle',
    '[DE] Advanced AI models trained on vast amounts of text that can understand, reason about, and generate human-like language.': 'Fortschrittliche KI-Modelle, die auf riesigen Textmengen trainiert wurden und menschenähnliche Sprache verstehen, darüber nachdenken und generieren können.',
    '[DE] &lt;strong&gt;Beispiel:&lt;/strong&gt; Using GPT to interpret raw surgical performance data and generate structured, meaningful coaching feedback for trainee surgeons.': '&lt;strong&gt;Beispiel:&lt;/strong&gt; GPT verwenden, um rohe chirurgische Leistungsdaten zu interpretieren und strukturiertes, aussagekräftiges Coaching-Feedback für angehende Chirurgen zu generieren.',
    '[DE] Medical AI': 'Medizinische KI',
    '[DE] The application of artificial intelligence to healthcare problems — from diagnostics to training to drug discovery.': 'Die Anwendung künstlicher Intelligenz auf Gesundheitsprobleme — von der Diagnostik über die Ausbildung bis zur Medikamentenentwicklung.',
    '[DE] &lt;strong&gt;Beispiel:&lt;/strong&gt; Building AI systems that analyse surgical simulation data to help trainee surgeons improve their technique in a safe, controlled environment.': '&lt;strong&gt;Beispiel:&lt;/strong&gt; KI-Systeme aufbauen, die chirurgische Simulationsdaten analysieren, um angehenden Chirurgen zu helfen, ihre Technik in einer sicheren, kontrollierten Umgebung zu verbessern.',
    '[DE] Surgical Simulation': 'Chirurgische Simulation',
    '[DE] Virtual reality or software-based systems that replicate real surgical procedures for training purposes without risk to real patients.': 'Virtual-Reality- oder softwarebasierte Systeme, die echte chirurgische Eingriffe zu Ausbildungszwecken nachbilden, ohne echte Patienten zu gefährden.',
    '[DE] &lt;strong&gt;Beispiel:&lt;/strong&gt; The VR-based spinal surgery simulators built by Simulatory, where every trainee action is logged and analysed for performance feedback.': '&lt;strong&gt;Beispiel:&lt;/strong&gt; Die VR-basierten Wirbelsäulenchirurgie-Simulatoren von Simulatory, bei denen jede Aktion des Auszubildenden protokolliert und für Leistungs-Feedback analysiert wird.',
    '[DE] Annotation Models': 'Annotationsmodelle'
}

# Apply most replacements
for k, v in replacements.items():
    if k.endswith("ML Intern"):
        text = re.sub(f'data-de="{k}"', f'data-de="{v}"', text)
    else:
        text = text.replace(f'data-de="{k}"', f'data-de="{v}"')
        text = text.replace(f'data-de-html="{k}"', f'data-de-html="{v}"')
        
# Be careful with Simulatory's type-badge "[DE] Internship" -> "Praktikum"
# To do this safely, we will look for `<span class="proj-category-badge" data-en="Internship" data-de="[DE] Internship">Internship</span>` close to `data-de="Simulatory AG"`
def replace_simulatory_internship(m):
    return m.group(0).replace('data-de="[DE] Internship"', 'data-de="Praktikum"')

pattern = re.compile(r'(<h3[^>]+data-de="(?:\[DE\] )?Simulatory AG".*?)(<span class="proj-category-badge" data-en="Internship" data-de="\[DE\] Internship">Internship</span>)', re.DOTALL)
text = pattern.sub(replace_simulatory_internship, text)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(text)

print("Replacement applied")

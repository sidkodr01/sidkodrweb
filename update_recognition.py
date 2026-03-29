import codecs

with codecs.open("index.html", "r", encoding="utf-8") as f:
    text = f.read()

replacements = {
    # GRID CARDS
    'data-de="[DE] Enhanced Apicultural Threat Detection System"': 'data-de="Verbessertes Bedrohungserkennungssystem"',
    'data-de="[DE] Patent"': 'data-de="Patent"',
    'data-de="[DE] ₹10 Lakh Government Research Grant"': 'data-de="₹10 Lakh Forschungsstipendium"',
    'data-de="[DE] Grant"': 'data-de="Förderung"',
    'data-de="[DE] Virtual Boundary Detection for Industrial Safety"': 'data-de="Virtuelle Grenzenerkennung"',
    'data-de="[DE] Conference Paper"': 'data-de="Konferenzbeitrag"',
    'data-de="[DE] Harnessing the Power of Deep Learning"': 'data-de="Deep Learning in der Praxis"',
    'data-de="[DE] Journal Publication"': 'data-de="Fachzeitschrift"',
    'data-de="[DE] Comprehensive Analysis of Advanced ML Techniques"': 'data-de="Analyse fortgeschrittener ML-Methoden"',

    # PATENT DETAIL
    # Note: "[DE] Enhanced Apicultural Threat Detection System" in detail name needs a more specific match or handle both.
    # The user specifies: data-de="[DE] Enhanced Apicultural Threat Detection System" (detail name) -> data-de="Verbessertes Imkerei-Bedrohungserkennungssystem"
    # I will use specific replacements for detail name vs grid card if they differ.
    
    'data-de="[DE] Application Number"': 'data-de="Antragsnummer"',
    'data-de="[DE] 202441071459"': 'data-de="202441071459"',
    'data-de="[DE] Type"': 'data-de="Typ"',
    'data-de="[DE] Indian Patent Application"': 'data-de="Indische Patentanmeldung"',
    'data-de="[DE] Field"': 'data-de="Fachgebiet"',
    'data-de="[DE] Computer Vision, Edge AI, Agricultural Technology"': 'data-de="Computer Vision, Edge-KI, Agrartechnologie"',
    'data-de="[DE] Status"': 'data-de="Status"',
    'data-de="[DE] Filed"': 'data-de="Eingereicht"',
    'data-de="[DE] Filed a patent for an intelligent apiculture monitoring system that uses computer vision to detect threats around beehives — including hornets, wasps, and other predators — in real time. The system runs on edge hardware (Jetson Nano) without cloud dependency, making it suitable for remote agricultural deployments. Combined with an acoustic monitoring module using CNN + BiLSTM models to detect colony stress and prevent colony collapse disorder."': 'data-de="Ein Patent für ein intelligentes Imkerei-Überwachungssystem eingereicht, das Computer Vision nutzt, um Bedrohungen rund um Bienenstöcke — einschließlich Hornissen, Wespen und anderer Räuber — in Echtzeit zu erkennen. Das System läuft auf Edge-Hardware (Jetson Nano) ohne Cloud-Abhängigkeit, was es für abgelegene landwirtschaftliche Einsätze geeignet macht. Kombiniert mit einem akustischen Überwachungsmodul mit CNN + BiLSTM-Modellen zur Erkennung von Koloniestress und Vorbeugung des Bienensterbens."',

    # GRANT DETAIL
    'data-de="[DE] Amount"': 'data-de="Betrag"',
    'data-de="[DE] ₹10,00,000 (10 Lakhs)"': 'data-de="₹10,00,000 (10 Lakh)"',
    'data-de="[DE] Issued By"': 'data-de="Ausgestellt von"',
    'data-de="[DE] Government of Andhra Pradesh"': 'data-de="Regierung von Andhra Pradesh"',
    'data-de="[DE] Purpose"': 'data-de="Zweck"',
    'data-de="[DE] Enhancement and further development of the ML-Driven Apiculture Monitoring System"': 'data-de="Weiterentwicklung des ML-gestützten Imkerei-Überwachungssystems"',
    'data-de="[DE] State Government Research Grant"': 'data-de="Staatliches Forschungsstipendium"',
    'data-de="[DE] Received a ₹10 lakh research grant from the Government of Andhra Pradesh to further develop and scale the ML-driven apiculture monitoring system. The grant recognises the project\'s potential impact on agricultural sustainability and bee population preservation in India. Funding supports hardware procurement, field deployment, and continued model development."': 'data-de="Ein Forschungsstipendium von ₹10 Lakh von der Regierung von Andhra Pradesh erhalten, um das ML-gestützte Imkerei-Überwachungssystem weiterzuentwickeln und zu skalieren. Das Stipendium erkennt die potenzielle Wirkung des Projekts auf landwirtschaftliche Nachhaltigkeit und die Erhaltung der Bienenpopulation in Indien an. Die Finanzierung unterstützt die Hardware-Beschaffung, den Feldeinsatz und die kontinuierliche Modellentwicklung."',

    # ICICC
    'data-de="[DE] Full Title"': 'data-de="Vollständiger Titel"',
    'data-de="[DE] System and Method for Virtual Boundary Detection and Warning of Safety Zone Violations in Construction and Industrial Environments"': 'data-de="System und Methode zur virtuellen Grenzenerkennung und Warnung bei Sicherheitszonen-Verstößen in Bau- und Industrieumgebungen"',
    'data-de="[DE] Conference"': 'data-de="Konferenz"',
    'data-de="[DE] ICICC 2025 (8th International Conference on Innovative Computing and Communication)"': 'data-de="ICICC 2025 (8. Internationale Konferenz für innovatives Computing und Kommunikation)"',
    'data-de="[DE] Paper ID"': 'data-de="Paper-ID"',
    'data-de="[DE] 1346"': 'data-de="1346"',
    'data-de="[DE] Accepted &amp; Presented"': 'data-de="Angenommen &amp; Präsentiert"',
    'data-de="[DE] Presented a research paper at ICICC 2025 detailing the design and implementation of a YOLOv5-based computer vision system for real-time safety zone enforcement in construction and industrial environments. The system uses virtual boundary detection via ROI and bounding boxes to monitor worker proximity to hazardous areas and trigger instant alerts — reducing reliance on manual supervision and physical barriers."': 'data-de="Eine Forschungsarbeit auf der ICICC 2025 präsentiert, die den Entwurf und die Implementierung eines YOLOv5-basierten Computer-Vision-Systems zur Echtzeit-Sicherheitszonen-Durchsetzung in Bau- und Industrieumgebungen beschreibt. Das System nutzt virtuelle Grenzenerkennung über ROI und Bounding Boxes, um die Nähe von Arbeitern zu Gefahrenbereichen zu überwachen und sofortige Alarme auszulösen — wodurch die Abhängigkeit von manueller Überwachung und physischen Barrieren reduziert wird."',

    # IJARCCE DEEP LEARNING
    'data-de="[DE] Journal"': 'data-de="Zeitschrift"',
    'data-de="[DE] DOI"': 'data-de="DOI"',
    'data-de="[DE] Peer-reviewed Journal Article"': 'data-de="Begutachteter Zeitschriftenartikel"',
    'data-de="[DE] Published a comprehensive review and analysis of advanced deep learning techniques applied to computer vision tasks. Covers state-of-the-art architectures, training methodologies, and real-world applications across object detection, image segmentation, and visual recognition — with insights drawn from hands-on project experience."': 'data-de="Eine umfassende Übersicht und Analyse fortgeschrittener Deep-Learning-Techniken für Computer-Vision-Aufgaben veröffentlicht. Behandelt modernste Architekturen, Trainingsmethoden und reale Anwendungen in Objekterkennung, Bildsegmentierung und visueller Erkennung — mit Erkenntnissen aus praktischer Projekterfahrung."',

    # IJARCCE ML
    'data-de="[DE] Published a comprehensive analysis of advanced machine learning techniques covering supervised, unsupervised, and reinforcement learning paradigms. Reviews cutting-edge algorithms, model architectures, and optimization strategies, with practical perspectives on applying these techniques to real-world engineering problems."': 'data-de="Eine umfassende Analyse fortgeschrittener Techniken des maschinellen Lernens veröffentlicht, die überwachte, unüberwachte und Verstärkungslern-Paradigmen abdeckt. Bewertet modernste Algorithmen, Modellarchitekturen und Optimierungsstrategien mit praktischen Perspektiven zur Anwendung dieser Techniken auf reale Ingenieurprobleme."',
}

# Specific logic for detailed vs grid titles
# Patent title: Grid card: Verbessertes Bedrohungserkennungssystem vs Detail: Verbessertes Imkerei-Bedrohungserkennungssystem
# I'll use context to replace these.

import re

# Replace Patent titles separately
# Grid card (usually inside recog-grid-view)
# Detail name (usually inside recog-detail-view)

# I'll use a safer approach: direct find/replace for the ones that don't collide.
for k, v in replacements.items():
    text = text.replace(k, v)

# Now handle the specific collisions or unique markers if needed.
# Patent title in grid:
# <span class="recog-grid-name" data-en="Enhanced Apicultural Threat Detection System" data-de="[DE] Enhanced Apicultural Threat Detection System">
text = text.replace('class="recog-grid-name" data-en="Enhanced Apicultural Threat Detection System" data-de="[DE] Enhanced Apicultural Threat Detection System"', 
                    'class="recog-grid-name" data-en="Enhanced Apicultural Threat Detection System" data-de="Verbessertes Bedrohungserkennungssystem"')

# Patent title in detail:
# <h3 class="recog-detail-name" data-en="Enhanced Apicultural Threat Detection System" data-de="[DE] Enhanced Apicultural Threat Detection System">
text = text.replace('class="recog-detail-name" data-en="Enhanced Apicultural Threat Detection System" data-de="[DE] Enhanced Apicultural Threat Detection System"', 
                    'class="recog-detail-name" data-en="Enhanced Apicultural Threat Detection System" data-de="Verbessertes Imkerei-Bedrohungserkennungssystem"')

# Grant title in grid:
text = text.replace('class="recog-grid-name" data-en="₹10 Lakh Government Research Grant" data-de="[DE] ₹10 Lakh Government Research Grant"',
                    'class="recog-grid-name" data-en="₹10 Lakh Government Research Grant" data-de="₹10 Lakh Forschungsstipendium"')

# Grant title in detail:
text = text.replace('class="recog-detail-name" data-en="₹10 Lakh Government Research Grant" data-de="[DE] ₹10 Lakh Government Research Grant"',
                    'class="recog-detail-name" data-en="₹10 Lakh Government Research Grant" data-de="₹10 Lakh staatliches Forschungsstipendium"')

# Virtual Boundary in grid:
text = text.replace('class="recog-grid-name" data-en="Virtual Boundary Detection for Industrial Safety" data-de="[DE] Virtual Boundary Detection for Industrial Safety"',
                    'class="recog-grid-name" data-en="Virtual Boundary Detection for Industrial Safety" data-de="Virtuelle Grenzenerkennung"')

# Virtual Boundary in detail:
text = text.replace('class="recog-detail-name" data-en="Virtual Boundary Detection for Industrial Safety" data-de="[DE] Virtual Boundary Detection for Industrial Safety"',
                    'class="recog-detail-name" data-en="Virtual Boundary Detection for Industrial Safety" data-de="Virtuelle Grenzenerkennung für industrielle Sicherheit"')

# Deep Learning title in grid:
text = text.replace('class="recog-grid-name" data-en="Harnessing the Power of Deep Learning" data-de="[DE] Harnessing the Power of Deep Learning"',
                    'class="recog-grid-name" data-en="Harnessing the Power of Deep Learning" data-de="Deep Learning in der Praxis"')

# Deep Learning title in detail:
text = text.replace('class="recog-detail-name" data-en="Harnessing the Power of Deep Learning" data-de="[DE] Harnessing the Power of Deep Learning"',
                    'class="recog-detail-name" data-en="Harnessing the Power of Deep Learning" data-de="Die Kraft des Deep Learning nutzen"')

# ML Techniques title in grid:
text = text.replace('class="recog-grid-name" data-en="Comprehensive Analysis of Advanced ML Techniques" data-de="[DE] Comprehensive Analysis of Advanced ML Techniques"',
                    'class="recog-grid-name" data-en="Comprehensive Analysis of Advanced ML Techniques" data-de="Analyse fortgeschrittener ML-Methoden"')

# ML Techniques title in detail:
text = text.replace('class="recog-detail-name" data-en="Comprehensive Analysis of Advanced ML Techniques" data-de="[DE] Comprehensive Analysis of Advanced ML Techniques"',
                    'class="recog-detail-name" data-en="Comprehensive Analysis of Advanced ML Techniques" data-de="Umfassende Analyse fortgeschrittener ML-Techniken"')


# Final cleanup for DOI strings if they are formatted differently
text = text.replace('data-de="[DE] DOI"', 'data-de="DOI"')

# Journal Publication in details
text = text.replace('class="type-badge" data-en="Journal Publication" data-de="[DE] Journal Publication"',
                    'class="type-badge" data-en="Journal Publication" data-de="Fachzeitschriften-Publikation"')

# Journal Publication in grid
text = text.replace('class="recog-grid-badge" data-en="Journal Publication" data-de="[DE] Journal Publication"',
                    'class="recog-grid-badge" data-en="Journal Publication" data-de="Fachzeitschrift"')

# DOI specific instances if they exist
text = text.replace('data-de="[DE] 10.17148/IJARCCE.2024.13614"', 'data-de="10.17148/IJARCCE.2024.13614"')
text = text.replace('data-de="[DE] 10.17148/IJARCCE.2024.13611"', 'data-de="10.17148/IJARCCE.2024.13611"')

with codecs.open("index.html", "w", encoding="utf-8") as f:
    f.write(text)

print("Recognition section updated successfully.")

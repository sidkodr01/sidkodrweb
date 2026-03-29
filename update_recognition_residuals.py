import codecs

with codecs.open("index.html", "r", encoding="utf-8") as f:
    text = f.read()

# Residuals / Smart Quotes / Entities
residuals = {
    # Grant description with smart quote
    'data-de="[DE] Received a ₹10 lakh research grant from the Government of Andhra Pradesh to further develop and scale the ML-driven apiculture monitoring system. The grant recognises the project’s potential impact on agricultural sustainability and bee population preservation in India. Funding supports hardware procurement, field deployment, and continued model development."': 
    'data-de="Ein Forschungsstipendium von ₹10 Lakh von der Regierung von Andhra Pradesh erhalten, um das ML-gestützte Imkerei-Überwachungssystem weiterzuentwickeln und zu skalieren. Das Stipendium erkennt die potenzielle Wirkung des Projekts auf landwirtschaftliche Nachhaltigkeit und die Erhaltung der Bienenpopulation in Indien an. Die Finanzierung unterstützt die Hardware-Beschaffung, den Feldeinsatz und die kontinuierliche Modellentwicklung."',
    
    # ICICC Status with double encoded ampersand maybe?
    'data-de="[DE] Accepted &amp;amp; Presented"': 'data-de="Angenommen &amp; Präsentiert"',
    
    # Deep Learning Title in Detail
    'data-de="[DE] Harnessing the Power of Deep Learning: Advanced Techniques in Computer Vision"': 'data-de="Die Kraft des Deep Learning nutzen: Fortgeschrittene Techniken in Computer Vision"',
    
    # IJARCCE Journal Title in Detail
    'data-de="[DE] IJARCCE (International Journal of Advanced Research in Computer and Communication Engineering)"': 'data-de="IJARCCE (International Journal of Advanced Research in Computer and Communication Engineering)"',
    
    # ML Techniques Title in Detail
    'data-de="[DE] Comprehensive Analysis of Advanced Techniques in Machine Learning"': 'data-de="Umfassende Analyse fortgeschrittener Techniken im maschinellen Lernen"',
}

for k, v in residuals.items():
    text = text.replace(k, v)

with codecs.open("index.html", "w", encoding="utf-8") as f:
    f.write(text)

print("Residual Recognition updates applied.")

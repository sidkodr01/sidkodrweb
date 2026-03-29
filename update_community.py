import codecs

with codecs.open("index.html", "r", encoding="utf-8") as f:
    text = f.read()

replacements = {
    # GRID CARDS
    'data-de="[DE] Women Empowerment Program"': 'data-de="Frauenförderungsprogramm"',
    'data-de="[DE] Social Impact"': 'data-de="Soziale Wirkung"',
    'data-de="[DE] 80 Hours"': 'data-de="80 Stunden"',
    'data-de="[DE] Water Management Initiative"': 'data-de="Wasserwirtschafts-Initiative"',
    'data-de="[DE] Environmental"': 'data-de="Umwelt"',
    'data-de="[DE] Waste Management Initiative"': 'data-de="Abfallmanagement-Initiative"',
    'data-de="[DE] Swachh Bharat Initiative"': 'data-de="Swachh-Bharat-Initiative"',
    'data-de="[DE] Civic"': 'data-de="Bürgerschaftlich"',
    'data-de="[DE] Health Awareness Program"': 'data-de="Gesundheitsbewusstseinsprogramm"',
    'data-de="[DE] Healthcare"': 'data-de="Gesundheitswesen"',

    # SHARED DETAIL LABELS
    'data-de="[DE] 📝 What I Did"': 'data-de="📝 Was ich getan habe"',
    'data-de="[DE] 📋 Key Activities"': 'data-de="📋 Hauptaktivitäten"',
    'data-de="[DE] ✨ Impact"': 'data-de="✨ Wirkung"',

    # DETAIL 0: WOMEN EMPOWERMENT
    'data-de="[DE] Participated in and helped organise a series of workshops aimed at empowering women through education, awareness, and skill-building. Contributed to sessions on financial independence and digital tools as part of a broader community outreach program."': 'data-de="An einer Reihe von Workshops teilgenommen und bei deren Organisation geholfen, die darauf abzielen, Frauen durch Bildung, Bewusstsein und Kompetenzaufbau zu stärken. Zu Sitzungen über finanzielle Unabhängigkeit und digitale Tools im Rahmen eines breiteren Gemeinschafts-Outreach-Programms beigetragen."',
    'data-de="[DE] Helped create a more informed and confident community of women with improved awareness of digital tools and financial independence."': 'data-de="Dazu beigetragen, eine besser informierte und selbstbewusstere Gemeinschaft von Frauen mit verbessertem Bewusstsein für digitale Tools und finanzielle Unabhängigkeit zu schaffen."',

    # DETAIL 1: WATER MANAGEMENT
    'data-de="[DE] Took part in a community initiative focused on educating people about water scarcity and sustainable water management. Helped spread awareness about modern water conservation techniques and smart technologies in water systems."': 'data-de="An einer Gemeinschaftsinitiative teilgenommen, die sich auf die Aufklärung über Wasserknappheit und nachhaltiges Wassermanagement konzentriert. Geholfen, Bewusstsein für moderne Wassereinsparmethoden und intelligente Technologien in Wassersystemen zu verbreiten."',
    'data-de="[DE] Contributed to building environmental consciousness around water usage and introduced communities to technology-driven conservation solutions."': 'data-de="Dazu beigetragen, Umweltbewusstsein rund um den Wasserverbrauch aufzubauen und Gemeinden mit technologiegestützten Erhaltungslösungen vertraut zu machen."',

    # DETAIL 2: WASTE MANAGEMENT
    'data-de="[DE] Participated in a structured waste management awareness program focused on practical, everyday actions that reduce environmental impact. Helped communicate the importance of proper waste segregation and circular economy concepts to the community."': 'data-de="An einem strukturierten Abfallmanagement-Aufklärungsprogramm teilgenommen, das sich auf praktische, alltägliche Maßnahmen zur Reduzierung der Umweltauswirkungen konzentriert. Geholfen, die Bedeutung ordnungsgemäßer Abfalltrennung und Kreislaufwirtschaftskonzepte in der Gemeinschaft zu vermitteln."',
    'data-de="[DE] Encouraged practical, actionable waste reduction habits in the local community, contributing to cleaner and more sustainable living environments."': 'data-de="Praktische, umsetzbare Gewohnheiten zur Abfallreduzierung in der lokalen Gemeinschaft gefördert und zu saubereren und nachhaltigeren Lebensumgebungen beigetragen."',

    # DETAIL 3: SWACHH BHARAT
    'data-de="[DE] Volunteered in Swachh Bharat-aligned community programs promoting public sanitation, hygiene, and cleanliness. Participated in awareness drives targeting plastic pollution and community-led cleanliness efforts."': 'data-de="In Swachh-Bharat-orientierten Gemeinschaftsprogrammen zur Förderung öffentlicher Hygiene und Sauberkeit ehrenamtlich mitgewirkt. An Aufklärungsaktionen gegen Plastikverschmutzung und gemeinschaftsgeführten Reinigungsaktionen teilgenommen."',
    'data-de="[DE] Contributed to national cleanliness goals at the grassroots level, helping shift community attitudes toward public hygiene and responsible waste disposal."': 'data-de="Zu nationalen Sauberkeitszielen auf Basisebene beigetragen und dazu geholfen, die Einstellung der Gemeinschaft gegenüber öffentlicher Hygiene und verantwortungsvoller Abfallentsorgung zu verändern."',

    # DETAIL 4: HEALTH AWARENESS
    'data-de="[DE] Participated in rural community outreach programs focused on basic health education. Helped conduct awareness sessions and assisted in organising health screenings for underserved communities with limited access to healthcare information."': 'data-de="An ländlichen Gemeinschafts-Outreach-Programmen mit Schwerpunkt auf grundlegender Gesundheitsaufklärung teilgenommen. Geholfen, Aufklärungssitzungen durchzuführen und Gesundheitsuntersuchungen für unterversorgte Gemeinschaften mit begrenztem Zugang zu Gesundheitsinformationen zu organisieren."',
    'data-de="[DE] Helped improve health literacy in rural communities, empowering individuals to make better health decisions and access available healthcare resources."': 'data-de="Dazu beigetragen, die Gesundheitskompetenz in ländlichen Gemeinden zu verbessern und Einzelpersonen zu befähigen, bessere Gesundheitsentscheidungen zu treffen und verfügbare Gesundheitsressourcen zu nutzen."',

}

for k, v in replacements.items():
    if k in text:
        text = text.replace(k, v)
    else:
        print(f"Warning: Could not find target: {k}")

with codecs.open("index.html", "w", encoding="utf-8") as f:
    f.write(text)

print("Community section updated successfully.")

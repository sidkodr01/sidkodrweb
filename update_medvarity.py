import codecs
import re

with codecs.open("index.html", "r", encoding="utf-8") as f:
    text = f.read()

replacements = {
    '[DE] Medvarity Online Ltd.': 'Medvarity Online Ltd.',
    '[DE] Marketing Intern': 'Marketing-Praktikant',
    '[DE] Audience Segmentation and Paid Campaign Management for a Niche Medical Education Platform': 'Zielgruppensegmentierung und Verwaltung bezahlter Kampagnen für eine Nischen-Medizinbildungsplattform',
    '[DE] Reaching medical professionals with online advertising is a distinct and difficult problem. The audience is highly educated, time-poor, and resistant to generic marketing — broad reach strategies don\'t work because the signal-to-noise ratio for this demographic is extremely low. At Medvarsity, which produces online courses for medical professionals, the problem was designing and executing campaigns precise enough to cut through to a highly specific audience without wasting budget on irrelevant reach.': 'Mediziner mit Online-Werbung zu erreichen ist ein spezifisches und schwieriges Problem. Das Publikum ist hochgebildet, zeitarm und resistent gegenüber generischem Marketing — breite Reichweitenstrategien funktionieren nicht, weil das Signal-Rausch-Verhältnis für diese Zielgruppe extrem niedrig ist. Bei Medvarsity, das Online-Kurse für Mediziner anbietet, bestand das Problem darin, Kampagnen präzise genug zu gestalten und durchzuführen, um eine hochspezifische Zielgruppe zu erreichen, ohne Budget für irrelevante Reichweite zu verschwenden.',
    '[DE] Before running anything live, I spent the first phase of the internship building the technical foundation properly — Google Ads certification, Facebook AdSense, Search Engine Optimisation strategy, and keyword research methodology. The objective was to understand the mechanics of each platform well enough to make deliberate decisions rather than default ones.': 'Bevor ich etwas live schaltete, verbrachte ich die erste Phase des Praktikums damit, das technische Fundament richtig aufzubauen — Google-Ads-Zertifizierung, Facebook AdSense, Suchmaschinenoptimierungsstrategie und Keyword-Recherche-Methodik. Das Ziel war, die Mechanismen jeder Plattform gut genug zu verstehen, um bewusste statt automatischer Entscheidungen zu treffen.',
    '[DE] By the end of the internship I was managing a live campaign independently with a real allocated budget — applying audience segmentation, keyword targeting, and conversion-focused copy to reach Medvarsity\'s target demographic. The work required thinking precisely about who the audience was, what they were searching for, and how to position the product in a way that was relevant to their specific professional context.': 'Gegen Ende des Praktikums verwaltete ich selbstständig eine Live-Kampagne mit einem echten Budget — Zielgruppensegmentierung, Keyword-Targeting und konversionsorientierte Texte anwenden, um Medvarsitys Zielgruppe zu erreichen. Die Arbeit erforderte präzises Nachdenken darüber, wer das Publikum war, wonach es suchte und wie das Produkt so positioniert werden konnte, dass es für den spezifischen beruflichen Kontext relevant war.',
    '[DE] Google Ads': 'Google Ads',
    '[DE] Google\'s online advertising platform that lets businesses show ads to people searching for relevant terms on Google.': 'Googles Online-Werbeplattform, die es Unternehmen ermöglicht, Anzeigen für Personen zu schalten, die nach relevanten Begriffen bei Google suchen.',
    '[DE] &lt;strong&gt;Beispiel:&lt;/strong&gt; Running a live campaign on Google Ads to reach medical professionals searching for online continuing education courses — targeting by keyword, profession, and intent.': '&lt;strong&gt;Beispiel:&lt;/strong&gt; Eine Live-Kampagne auf Google Ads schalten, um Mediziner zu erreichen, die nach Online-Fortbildungskursen suchen — Targeting nach Keyword, Beruf und Absicht.',
    '[DE] Facebook AdSense': 'Facebook AdSense',
    '[DE] Meta\'s advertising platform that allows businesses to run targeted ads across Facebook and Instagram based on user demographics and behaviour.': 'Metas Werbeplattform, die es Unternehmen ermöglicht, zielgerichtete Anzeigen auf Facebook und Instagram basierend auf Nutzerdemografie und -verhalten zu schalten.',
    '[DE] &lt;strong&gt;Beispiel:&lt;/strong&gt; Creating targeted ad campaigns on Facebook to reach Medvarsity\'s audience of healthcare professionals with course recommendations relevant to their specialty.': '&lt;strong&gt;Beispiel:&lt;/strong&gt; Zielgerichtete Werbekampagnen auf Facebook erstellen, um Medvarsitys Zielgruppe von Gesundheitsfachleuten mit für ihre Fachrichtung relevanten Kursempfehlungen zu erreichen.',
    '[DE] SEO': 'SEO',
    '[DE] Search Engine Optimisation — the practice of improving a website\'s visibility in search engine results to attract more organic traffic.': 'Suchmaschinenoptimierung — die Praxis, die Sichtbarkeit einer Website in Suchmaschinenergebnissen zu verbessern, um mehr organischen Traffic anzuziehen.',
    '[DE] &lt;strong&gt;Beispiel:&lt;/strong&gt; Researching keywords that medical professionals use when searching for online courses and applying on-page SEO strategies to improve Medvarsity\'s search rankings.': '&lt;strong&gt;Beispiel:&lt;/strong&gt; Keywords recherchieren, die Mediziner bei der Suche nach Online-Kursen verwenden, und On-Page-SEO-Strategien anwenden, um Medvarsitys Suchranking zu verbessern.',
    '[DE] Digital Marketing': 'Digitales Marketing',
    '[DE] The use of online channels — search engines, social media, email, and more — to promote products or services to a target audience.': 'Die Nutzung von Online-Kanälen — Suchmaschinen, Social Media, E-Mail und mehr — um Produkte oder Dienstleistungen einer Zielgruppe zu bewerben.',
    '[DE] &lt;strong&gt;Beispiel:&lt;/strong&gt; Designing and executing a digital marketing strategy for a medical education platform, balancing paid advertising with organic growth tactics.': '&lt;strong&gt;Beispiel:&lt;/strong&gt; Eine digitale Marketingstrategie für eine Medizinbildungsplattform entwerfen und umsetzen, die bezahlte Werbung mit organischen Wachstumstaktiken in Einklang bringt.',
    '[DE] Campaign Management': 'Kampagnenmanagement',
    '[DE] The end-to-end process of planning, launching, monitoring, and optimising a marketing campaign to achieve specific goals.': 'Der End-to-End-Prozess der Planung, Einführung, Überwachung und Optimierung einer Marketingkampagne zur Erreichung spezifischer Ziele.',
    '[DE] &lt;strong&gt;Beispiel:&lt;/strong&gt; Managing a live Google Ads campaign independently with a real budget — setting targeting parameters, writing ad copy, monitoring performance, and adjusting based on results.': '&lt;strong&gt;Beispiel:&lt;/strong&gt; Eine Live-Google-Ads-Kampagne selbstständig mit echtem Budget verwalten — Targeting-Parameter festlegen, Anzeigentexte schreiben, Leistung überwachen und basierend auf Ergebnissen anpassen.',
    '[DE] Google Ads Certified': 'Google Ads zertifiziert',
    '[DE] An official Google certification that validates proficiency in creating and managing Google Ads campaigns.': 'Eine offizielle Google-Zertifizierung, die Kompetenz bei der Erstellung und Verwaltung von Google-Ads-Kampagnen bestätigt.',
    '[DE] &lt;strong&gt;Beispiel:&lt;/strong&gt; Completing the Google Ads certification and immediately applying the strategies learned to a live campaign for Medvarsity\'s medical professional audience.': '&lt;strong&gt;Beispiel:&lt;/strong&gt; Die Google-Ads-Zertifizierung abschließen und die erlernten Strategien sofort auf eine Live-Kampagne für Medvarsitys medizinische Fachpublikum anwenden.'
}

for k, v in replacements.items():
    text = text.replace(f'data-de="{k}"', f'data-de="{v}"')
    text = text.replace(f'data-de-html="{k}"', f'data-de-html="{v}"')

def replace_medvarsity_date(m):
    return m.group(0).replace('data-de="[DE] Jun 2023 – Dec 2023"', 'data-de="Jun. 2023 – Dez. 2023"')

# Replace the Date span for Medvarsity only
pattern_date = re.compile(r'(<h3[^>]+data-de="(?:\[DE\] )?Medvarity Online Ltd\.".*?)(<span data-en="Jun 2023 – Dec 2023"[^>]*>Jun 2023 – Dec 2023</span>)', re.DOTALL)
text = pattern_date.sub(replace_medvarsity_date, text)


def replace_medvarsity_date_grid(m):
    return m.group(0).replace('data-de="[DE] Jun 2023 – Dec 2023"', 'data-de="Jun. 2023 – Dez. 2023"')

# Grid view replacement for Medvarsity date specifically
pattern_date_grid = re.compile(r'(<span class="exp-grid-name" data-en="Medvarity Online Ltd\.".*?)(<span class="exp-grid-duration"[^>]*>Jun 2023 – Dec 2023</span>)', re.DOTALL)
text = pattern_date_grid.sub(replace_medvarsity_date_grid, text)


def replace_medvarsity_internship(m):
    return m.group(0).replace('data-de="[DE] Internship"', 'data-de="Praktikum"')

pattern_badge = re.compile(r'(<h3[^>]+data-de="(?:\[DE\] )?Medvarity Online Ltd\.".*?)(<span class="type-badge"[^>]*>Internship</span>)', re.DOTALL)
text = pattern_badge.sub(replace_medvarsity_internship, text)


with codecs.open("index.html", "w", encoding="utf-8") as f:
    f.write(text)

print("Updates applied to Medvarity sections successfully.")

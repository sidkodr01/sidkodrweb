import codecs
import re

with codecs.open("index.html", "r", encoding="utf-8") as f:
    text = f.read()

replacements = {
    '[DE] Indimotard': 'Indimotard',
    '[DE] Social Media Manager': 'Social-Media-Manager',
    '[DE] Part-time': 'Teilzeit',
    '[DE] Content Strategy and Digital Presence Management for a Specialist Motorcycle Service Workshop': 'Content-Strategie und digitales Präsenzmanagement für eine Motorrad-Fachwerkstatt',
    '[DE] Indimotard had an audience worth reaching — serious motorcycle enthusiasts who treat high-end bikes as a lifestyle, not just a vehicle. The problem was that their social media presence wasn\'t converting that potential into measurable growth or consistent footfall. The brand had a story worth telling, but no systematic approach to telling it across platforms.': 'Indimotard hatte ein Publikum, das es wert war, erreicht zu werden — ernsthafte Motorradbegeisterte, die hochwertige Bikes als Lebensstil und nicht nur als Fahrzeug betrachten. Das Problem war, dass ihre Social-Media-Präsenz dieses Potenzial nicht in messbares Wachstum oder konstante Kundschaft umwandelte. Die Marke hatte eine Geschichte, die es wert war, erzählt zu werden, aber keinen systematischen Ansatz, sie plattformübergreifend zu erzählen.',
    '[DE] I took over their social media operations across Instagram, Facebook, and YouTube with a clear objective: grow an engaged following and translate that following into customers walking through the door.': 'Ich übernahm ihre Social-Media-Aktivitäten auf Instagram, Facebook und YouTube mit einem klaren Ziel: eine engagierte Followerschaft aufbauen und diese in Kunden umwandeln, die durch die Tür kommen.',
    '[DE] The approach was strategic before it was creative. That meant identifying what content resonated with the target audience — documentation of high-end service work, behind-the-scenes garage content, and brand collaboration posts — and building a consistent publishing cadence across platforms. Each piece of content was planned around what to shoot, how to frame it, and when to publish it to maximise reach and engagement within a niche but highly engaged audience segment.': 'Der Ansatz war strategisch, bevor er kreativ war. Das bedeutete, herauszufinden, welche Inhalte bei der Zielgruppe ankamen — Dokumentation hochwertiger Servicearbeiten, Garage-Inhalte hinter den Kulissen und Markenkooperationsbeiträge — und einen konsistenten Veröffentlichungsrhythmus über alle Plattformen hinweg aufzubauen. Jedes Stück Content wurde darum geplant, was gefilmt, wie gerahmt und wann veröffentlicht werden sollte, um Reichweite und Engagement innerhalb eines Nischen-, aber hochengagierten Publikumssegments zu maximieren.',
    '[DE] The results were concrete. Instagram following grew from 6,000 to 13,000 in six months. More significantly, inbound footfall attributable directly to Instagram increased over the same period — the follower growth translated into real customer acquisition, not just reach metrics.': 'Die Ergebnisse waren konkret. Die Instagram-Followerschaft wuchs in sechs Monaten von 6.000 auf 13.000. Noch bedeutsamer: Der direkt auf Instagram zurückzuführende Kundenzulauf stieg im gleichen Zeitraum — das Followerwachstum übersetzte sich in echte Kundengewinnung, nicht nur in Reichweite-Metriken.',
    '[DE] Social Media Strategy': 'Social-Media-Strategie',
    '[DE] The plan behind a brand\'s social media presence — deciding what to post, when to post it, and how to grow an engaged audience.': 'Der Plan hinter der Social-Media-Präsenz einer Marke — entscheiden, was, wann und wie gepostet wird, um ein engagiertes Publikum aufzubauen.',
    '[DE] &lt;strong&gt;Beispiel:&lt;/strong&gt; Developing a content strategy for Indimotard that balanced garage documentation, bike showcases, and brand collaborations to build a loyal community of motorcycle enthusiasts.': '&lt;strong&gt;Beispiel:&lt;/strong&gt; Eine Content-Strategie für Indimotard entwickeln, die Garagendokumentation, Bike-Präsentationen und Markenkooperationen in Einklang brachte, um eine treue Community von Motorradbegeisterten aufzubauen.',
    '[DE] Content Creation': 'Content-Erstellung',
    '[DE] Producing original photos, videos, and written material that represents a brand\'s identity and engages its audience.': 'Originale Fotos, Videos und schriftliche Inhalte produzieren, die die Identität einer Marke repräsentieren und ihr Publikum ansprechen.',
    '[DE] &lt;strong&gt;Beispiel:&lt;/strong&gt; Capturing daily garage activity, documenting services on high-end motorcycles, and creating visually compelling posts that reflected the premium, enthusiast culture of Indimotard.': '&lt;strong&gt;Beispiel:&lt;/strong&gt; Tägliche Garagenaktivitäten festhalten, Servicearbeiten an hochwertigen Motorrädern dokumentieren und visuell ansprechende Beiträge erstellen, die die Premium-Enthusiasten-Kultur von Indimotard widerspiegelten.',
    '[DE] Brand Collaborations': 'Markenkooperationen',
    '[DE] Partnerships between a brand and external companies or creators to produce content that benefits both parties.': 'Partnerschaften zwischen einer Marke und externen Unternehmen oder Kreativen, um Inhalte zu produzieren, die beiden Parteien nützen.',
    '[DE] &lt;strong&gt;Beispiel:&lt;/strong&gt; Working with motorcycle and lifestyle brands on co-branded posts that expanded Indimotard\'s reach while aligning with their identity as a destination for serious bike enthusiasts.': '&lt;strong&gt;Beispiel:&lt;/strong&gt; Mit Motorrad- und Lifestyle-Marken an Co-Branding-Beiträgen arbeiten, die Indimotards Reichweite erweiterten und gleichzeitig ihre Identität als Anlaufstelle für ernsthafte Bike-Begeisterte stärkten.',
    '[DE] Instagram Growth': 'Instagram-Wachstum',
    '[DE] The strategic process of growing a brand\'s Instagram following and engagement through consistent, quality content and community interaction.': 'Der strategische Prozess, die Instagram-Followerschaft und das Engagement einer Marke durch konsistente, qualitativ hochwertige Inhalte und Community-Interaktion zu steigern.',
    '[DE] &lt;strong&gt;Beispiel:&lt;/strong&gt; Growing Indimotard\'s Instagram following from 6,000 to 13,000 in six months — with a measurable increase in customers walking in directly from Instagram.': '&lt;strong&gt;Beispiel:&lt;/strong&gt; Indimotards Instagram-Followerschaft in sechs Monaten von 6.000 auf 13.000 steigern — mit einem messbaren Anstieg von Kunden, die direkt über Instagram kamen.',
    '[DE] Community Building': 'Community-Aufbau',
    '[DE] Creating a sense of belonging and loyalty around a brand so that followers become genuine advocates rather than passive consumers.': 'Ein Gefühl von Zugehörigkeit und Loyalität rund um eine Marke schaffen, damit Follower zu echten Fürsprechern statt zu passiven Konsumenten werden.',
    '[DE] &lt;strong&gt;Beispiel:&lt;/strong&gt; Positioning Indimotard not just as a garage but as a community hub for motorcycle enthusiasts — making the Instagram page feel like a place people wanted to follow, not just a business account.': '&lt;strong&gt;Beispiel:&lt;/strong&gt; Indimotard nicht nur als Werkstatt, sondern als Community-Hub für Motorradbegeisterte positionieren — die Instagram-Seite so gestalten, dass sie sich wie ein Ort anfühlt, dem man folgen möchte, nicht nur wie ein Unternehmenskonto.',
    '[DE] Creative Direction': 'Kreative Leitung',
    '[DE] The process of defining the visual and narrative identity of a brand\'s content — deciding how it looks, feels, and communicates.': 'Der Prozess der Definition der visuellen und narrativen Identität der Inhalte einer Marke — entscheiden, wie sie aussehen, sich anfühlen und kommunizieren.',
    '[DE] &lt;strong&gt;Beispiel:&lt;/strong&gt; Making consistent creative decisions about how to shoot, frame, and present Indimotard\'s content so that every post felt cohesive and on-brand.': '&lt;strong&gt;Beispiel:&lt;/strong&gt; Konsistente kreative Entscheidungen darüber treffen, wie Indimotards Inhalte aufgenommen, gerahmt und präsentiert werden, damit jeder Beitrag kohärent und markenkonform wirkte.'
}

for k, v in replacements.items():
    text = text.replace(f'data-de="{k}"', f'data-de="{v}"')
    text = text.replace(f'data-de-html="{k}"', f'data-de-html="{v}"')

def replace_indimotard_date(m):
    return m.group(0).replace('data-de="[DE] Jun 2023 – Dec 2023"', 'data-de="Jun. 2023 – Dez. 2023"')

# Replace the Date span for Indimotard only
pattern_date = re.compile(r'(<h3[^>]+data-de="(?:\[DE\] )?Indimotard".*?)(<span data-en="Jun 2023 – Dec 2023"[^>]*>Jun 2023 – Dec 2023</span>)', re.DOTALL)
text = pattern_date.sub(replace_indimotard_date, text)

# Grid view replacement for indimotard date specifically
pattern_date_grid = re.compile(r'(<span class="exp-grid-name" data-en="Indimotard".*?)(<span class="exp-grid-duration"[^>]*>Jun 2023 – Dec 2023</span>)', re.DOTALL)
text = pattern_date_grid.sub(replace_indimotard_date, text)

with codecs.open("index.html", "w", encoding="utf-8") as f:
    f.write(text)

print("Updates applied to Indimotard sections successfully.")

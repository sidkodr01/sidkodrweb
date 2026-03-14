import codecs
import re

with codecs.open("index.html", "r", encoding="utf-8") as f:
    text = f.read()

replacements = {
    '[DE] Flipick': 'Flipick',
    '[DE] AI Intern': 'KI-Praktikant',
    '[DE] Ground-Up Chatbot Development: Neural Architecture to Client Deployment': 'Chatbot-Entwicklung von Grund auf: Von der neuronalen Architektur zur Client-Bereitstellung',
    '[DE] In 2023, most teams building with Large Language Models were focused on what they could ship. The harder problem — and the more important one — was understanding what was actually happening inside these systems: how information flows through transformer layers, where models fail, and what architectural decisions determine whether something is robust enough to deploy to a real client.': 'Im Jahr 2023 konzentrierten sich die meisten Teams, die mit Large Language Models bauten, auf das, was sie liefern konnten. Das schwierigere Problem — und das wichtigere — war zu verstehen, was tatsächlich in diesen Systemen passierte: wie Informationen durch Transformer-Schichten fließen, wo Modelle versagen und welche Architekturentscheidungen bestimmen, ob etwas robust genug für den Einsatz bei einem echten Kunden ist.',
    '[DE] At Flipick, that was the problem I set out to solve for myself before writing a single line of production code. The internship was structured around deep technical grounding first — neural network architectures, attention mechanisms, how information propagates through layers, and how chatbot frameworks function beneath their abstractions. Not as background reading, but as the foundation every subsequent decision would rest on.': 'Bei Flipick war das das Problem, das ich für mich selbst lösen wollte, bevor ich eine einzige Zeile Produktionscode schrieb. Das Praktikum war zunächst auf tiefes technisches Fundament ausgerichtet — neuronale Netzwerkarchitekturen, Aufmerksamkeitsmechanismen, wie Informationen durch Schichten propagieren und wie Chatbot-Frameworks unter ihren Abstraktionen funktionieren. Nicht als Hintergrundlektüre, sondern als Grundlage, auf der jede nachfolgende Entscheidung ruhen würde.',
    '[DE] The culminating project was building a client-deployable chatbot from scratch — designing the architecture, handling failure modes, and making the system robust enough to hand off to an external client. The system didn\'t go into production, but the objective was never deployment. It was building something that could be deployed, and understanding every decision that distinction requires.': 'Das abschließende Projekt war der Aufbau eines für Kunden einsatzfähigen Chatbots von Grund auf — die Architektur entwerfen, Fehlermodi behandeln und das System robust genug machen, um es an einen externen Kunden übergeben zu können. Das System ging nicht in Produktion, aber das Ziel war nie die Bereitstellung. Es ging darum, etwas zu bauen, das bereitgestellt werden könnte, und jede Entscheidung zu verstehen, die diesen Unterschied erfordert.',
    '[DE] That architectural foundation has carried directly into every system I\'ve built since — Large Language Model feedback pipelines, annotation models, Retrieval-Augmented Generation systems. The difference between knowing how to use a tool and understanding how it works is the difference between building something that functions in a demo and building something that holds up in production.': 'Dieses architektonische Fundament hat sich direkt in jedes System übertragen, das ich seitdem gebaut habe — Large-Language-Model-Feedback-Pipelines, Annotationsmodelle, Retrieval-Augmented-Generation-Systeme. Der Unterschied zwischen dem Wissen, wie man ein Tool benutzt, und dem Verstehen, wie es funktioniert, ist der Unterschied zwischen dem Bauen von etwas, das in einer Demo funktioniert, und dem Bauen von etwas, das in der Produktion standhält.',
    '[DE] Chatbot Development': 'Chatbot-Entwicklung',
    '[DE] The process of designing and building conversational AI systems that can interact with users through natural language.': 'Der Prozess des Entwerfens und Aufbauens konversationeller KI-Systeme, die mit Nutzern in natürlicher Sprache interagieren können.',
    '[DE] &lt;strong&gt;Beispiel:&lt;/strong&gt; Building a client-deployable chatbot from scratch — designing the conversation flow, integrating the language model, and making it robust enough to handle real user interactions.': '&lt;strong&gt;Beispiel:&lt;/strong&gt; Einen für Kunden einsatzfähigen Chatbot von Grund auf bauen — den Gesprächsfluss entwerfen, das Sprachmodell integrieren und ihn robust genug machen, um echte Nutzerinteraktionen zu bewältigen.',
    '[DE] Neural Networks': 'Neuronale Netze',
    '[DE] Computational systems loosely inspired by the human brain, made up of layers of interconnected nodes that learn patterns from data.': 'Rechensysteme, die lose vom menschlichen Gehirn inspiriert sind und aus Schichten miteinander verbundener Knoten bestehen, die Muster aus Daten lernen.',
    '[DE] &lt;strong&gt;Beispiel:&lt;/strong&gt; Studying how different neural network architectures process and distribute information across layers to understand why certain models perform better for conversational tasks.': '&lt;strong&gt;Beispiel:&lt;/strong&gt; Untersuchen, wie verschiedene neuronale Netzwerkarchitekturen Informationen über Schichten hinweg verarbeiten und verteilen, um zu verstehen, warum bestimmte Modelle bei konversationellen Aufgaben besser abschneiden.',
    '[DE] Large Language Models': 'Große Sprachmodelle',
    '[DE] Advanced AI models trained on vast amounts of text that can understand, reason about, and generate human-like language at scale.': 'Fortschrittliche KI-Modelle, die auf riesigen Textmengen trainiert wurden und menschenähnliche Sprache in großem Maßstab verstehen, darüber nachdenken und generieren können.',
    '[DE] &lt;strong&gt;Beispiel:&lt;/strong&gt; Understanding how Large Language Models power modern chatbots — and how to build systems around them that are reliable enough to deploy to real clients.': '&lt;strong&gt;Beispiel:&lt;/strong&gt; Verstehen, wie Große Sprachmodelle moderne Chatbots antreiben — und wie man Systeme um sie herum baut, die zuverlässig genug sind, um bei echten Kunden eingesetzt zu werden.',
    '[DE] AI Frameworks': 'KI-Frameworks',
    '[DE] Software libraries and tools that provide pre-built components for building, training, and deploying artificial intelligence systems.': 'Softwarebibliotheken und Tools, die vorgefertigte Komponenten für den Aufbau, das Training und die Bereitstellung von KI-Systemen bereitstellen.',
    '[DE] &lt;strong&gt;Beispiel:&lt;/strong&gt; Learning how different chatbot and AI frameworks structure their pipelines, and how to choose the right one based on client requirements.': '&lt;strong&gt;Beispiel:&lt;/strong&gt; Lernen, wie verschiedene Chatbot- und KI-Frameworks ihre Pipelines strukturieren, und wie man das richtige basierend auf Kundenanforderungen auswählt.',
    '[DE] Natural Language Processing': 'Natürliche Sprachverarbeitung',
    '[DE] A branch of AI focused on enabling computers to understand, interpret, and generate human language in a meaningful way.': 'Ein Teilbereich der KI, der sich darauf konzentriert, Computer in die Lage zu versetzen, menschliche Sprache auf sinnvolle Weise zu verstehen, zu interpretieren und zu generieren.',
    '[DE] &lt;strong&gt;Beispiel:&lt;/strong&gt; Understanding how text is tokenised, embedded, and interpreted by language models to generate relevant, contextually appropriate responses.': '&lt;strong&gt;Beispiel:&lt;/strong&gt; Verstehen, wie Text von Sprachmodellen tokenisiert, eingebettet und interpretiert wird, um relevante, kontextuell angemessene Antworten zu generieren.',
    '[DE] Conversational AI': 'Konversations-KI',
    '[DE] AI systems designed to simulate natural human conversation — understanding user intent and responding in a coherent, helpful way.': 'KI-Systeme, die darauf ausgelegt sind, natürliche menschliche Gespräche zu simulieren — die Absicht des Nutzers zu verstehen und kohärent und hilfreich zu antworten.',
    '[DE] &lt;strong&gt;Beispiel:&lt;/strong&gt; Designing chatbot flows that handle diverse user inputs gracefully, including unexpected questions and edge cases that real users inevitably throw at any deployed system.': '&lt;strong&gt;Beispiel:&lt;/strong&gt; Chatbot-Flüsse entwerfen, die vielfältige Nutzereingaben elegant behandeln, einschließlich unerwarteter Fragen und Randfälle, die echte Nutzer unweigerlich an jedes bereitgestellte System stellen.'
}

for k, v in replacements.items():
    text = text.replace(f'data-de="{k}"', f'data-de="{v}"')
    text = text.replace(f'data-de-html="{k}"', f'data-de-html="{v}"')

def replace_flipick_internship(m):
    # This matches the `<span class="proj-category-badge"...` near Flipick and sets Praktikum
    return m.group(0).replace('data-de="[DE] Internship"', 'data-de="Praktikum"')

def replace_flipick_date(m):
    # This matches `<span class="exp-grid-duration"...` near Flipick and sets Jun. ... Dez.
    return m.group(0).replace('data-de="[DE] Jun 2023 – Dec 2023"', 'data-de="Jun. 2023 – Dez. 2023"')

# Replace the Internship badge for Flipick only
pattern_badge = re.compile(r'(<h3[^>]+data-de="(?:\[DE\] )?Flipick".*?)(<span class="proj-category-badge"[^>]*>Internship</span>)', re.DOTALL)
text = pattern_badge.sub(replace_flipick_internship, text)

# Replace the Date span for Flipick only
pattern_date = re.compile(r'(<h3[^>]+data-de="(?:\[DE\] )?Flipick".*?)(<span class="exp-grid-duration"[^>]*>Jun 2023 – Dec 2023</span>)', re.DOTALL)
text = pattern_date.sub(replace_flipick_date, text)

with codecs.open("index.html", "w", encoding="utf-8") as f:
    f.write(text)

print("Updates applied to Flipick sections successfully.")

import codecs

with codecs.open("index.html", "r", encoding="utf-8") as f:
    text = f.read()

replacements = {
    '[DE] Machine learning models trained to identify, label, and highlight specific objects or regions within images or video frames.': 'Machine-Learning-Modelle, die darauf trainiert sind, bestimmte Objekte oder Bereiche in Bildern oder Videoframes zu identifizieren, zu beschriften und hervorzuheben.',
    '[DE] &lt;strong&gt;Beispiel:&lt;/strong&gt; A model that detects which part of the spine is visible on screen during a simulation and highlights it in real time for the trainee.': '&lt;strong&gt;Beispiel:&lt;/strong&gt; Ein Modell, das erkennt, welcher Teil der Wirbelsäule während einer Simulation auf dem Bildschirm sichtbar ist, und ihn in Echtzeit für den Auszubildenden hervorhebt.',
    '[DE] Generative AI': 'Generative KI',
    '[DE] A class of AI models that can create new content — images, text, audio — by learning patterns from existing data.': 'Eine Klasse von KI-Modellen, die neue Inhalte — Bilder, Text, Audio — erstellen können, indem sie Muster aus vorhandenen Daten lernen.',
    '[DE] &lt;strong&gt;Beispiel:&lt;/strong&gt; Using Stable Diffusion to generate synthetic medical images of spine pathologies to supplement limited real training data.': '&lt;strong&gt;Beispiel:&lt;/strong&gt; Stable Diffusion verwenden, um synthetische medizinische Bilder von Wirbelsäulenpathologien zu generieren, um begrenzte echte Trainingsdaten zu ergänzen.',
    '[DE] Stable Diffusion': 'Stable Diffusion',
    '[DE] An open-source generative AI model capable of producing realistic images from text descriptions or by learning from existing image datasets.': 'Ein Open-Source-generatives KI-Modell, das realistische Bilder aus Textbeschreibungen oder durch Lernen aus vorhandenen Bilddatensätzen erzeugen kann.',
    '[DE] &lt;strong&gt;Beispiel:&lt;/strong&gt; Experimenting with fine-tuned Stable Diffusion models to synthesise MRI scan images of spinal conditions for use as training data.': '&lt;strong&gt;Beispiel:&lt;/strong&gt; Mit fein abgestimmten Stable-Diffusion-Modellen experimentieren, um MRT-Bilder von Wirbelsäulenerkrankungen als Trainingsdaten zu synthetisieren.',
    '[DE] API Integration': 'API-Integration',
    '[DE] Connecting different software systems together through their Application Programming Interfaces so they can communicate and share data.': 'Verschiedene Softwaresysteme über ihre Application Programming Interfaces verbinden, damit sie kommunizieren und Daten austauschen können.',
    '[DE] &lt;strong&gt;Beispiel:&lt;/strong&gt; Integrating the OpenAI API into the surgical feedback pipeline so that processed simulation data could be sent to GPT and structured responses returned automatically.': '&lt;strong&gt;Beispiel:&lt;/strong&gt; Die OpenAI-API in die chirurgische Feedback-Pipeline integrieren, damit verarbeitete Simulationsdaten an GPT gesendet und strukturierte Antworten automatisch zurückgegeben werden konnten.',
    '[DE] Solo Engineering': 'Alleinentwicklung',
    '[DE] Designing, building, testing, and deploying a complete technical system independently without a supporting engineering team.': 'Ein vollständiges technisches System unabhängig entwerfen, aufbauen, testen und bereitstellen, ohne ein unterstützendes Ingenieurteam.',
    '[DE] &lt;strong&gt;Beispiel:&lt;/strong&gt; Being the sole technical person responsible for the entire Machine Learning stack at Simulatory — from architecture decisions to production deployment.': '&lt;strong&gt;Beispiel:&lt;/strong&gt; Die einzige technische Person sein, die für den gesamten Machine-Learning-Stack bei Simulatory verantwortlich ist — von Architekturentscheidungen bis zur Produktionsbereitstellung.'
}

for k, v in replacements.items():
    text = text.replace(f'data-de="{k}"', f'data-de="{v}"')
    text = text.replace(f'data-de-html="{k}"', f'data-de-html="{v}"')

with codecs.open("index.html", "w", encoding="utf-8") as f:
    f.write(text)
print("Updates applied to index.html successfully.")

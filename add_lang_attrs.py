#!/usr/bin/env python3
"""
Add data-en / data-de attributes to every text element in index.html.
Uses known translations where available; prefixes "[DE] " for placeholders.
Also injects toggle button, tooltip, CSS, and JavaScript.
"""
import re, html as htmlmod

FILE = "index.html"

with open(FILE, "r", encoding="utf-8") as f:
    content = f.read()

# ── Exact text translations that are known ───────────────────────────────
KNOWN = {
    # Nav links
    "About": "Über mich",
    "Experience": "Erfahrung",
    "Projects": "Projekte",
    "Recognition": "Auszeichnungen",
    "Community": "Gemeinschaft",
    "Interests": "Interessen",
    # Section titles (h2)
    "Interests &amp; Skills": "Interessen &amp; Fähigkeiten",
    "Community &amp; Social Impact": "Gemeinschaft &amp; Soziales Engagement",
    # Buttons
    "Click to know more →": "Klicken Sie für mehr →",
    "Back to Experience": "Zurück zur Erfahrung",
    "Back to Projects": "Zurück zu den Projekten",
    "Back to Recognition": "Zurück zu den Auszeichnungen",
    "Back to Community": "Zurück zur Gemeinschaft",
    "View Publication": "Publikation ansehen",
    # Hero
    "AI/ML Engineer": "KI/ML-Ingenieur",
    # Duration label
    "Duration": "Dauer",
    "80 Hours": "80 Stunden",
}

# ── Tag popup labels ─────────────────────────────────────────────────────
# Definition: stays as Definition:
# Example: → Beispiel:


def attr_escape(s):
    """Escape for use inside a double-quoted HTML attribute."""
    return s.replace("&", "&amp;").replace('"', "&quot;").replace("<", "&lt;").replace(">", "&gt;")


def add_data_attrs(line, en_text, de_text):
    """Given a line and the English/German texts, add data-en and data-de to the opening tag."""
    en_escaped = attr_escape(en_text)
    de_escaped = attr_escape(de_text)
    # Find the first > that starts the tag content
    # We need to insert before the first > of the element's opening tag
    # But we need to be careful with self-closing tags, SVGs, etc.
    return line


# ──────────────────────────────────────────────────────────────────────────
# Instead of fragile regex, we'll use a line-by-line approach with specific patterns
# ──────────────────────────────────────────────────────────────────────────

lines = content.split('\n')
output_lines = []

# Track state
i = 0
while i < len(lines):
    line = lines[i]
    modified = False
    
    # ── 1. Sidebar nav links ─────────────────────────────────────────────
    # Pattern: <li><a href="#about" class="active">About</a></li>
    m = re.match(r'^(\s*<li><a\s[^>]*>)(About|Experience|Projects|Recognition|Community|Interests)(</a></li>)$', line)
    if m:
        prefix, text, suffix = m.groups()
        de = KNOWN.get(text, f"[DE] {text}")
        en_esc = attr_escape(text)
        de_esc = attr_escape(de)
        # Insert data-en and data-de into the <a> tag
        prefix_new = prefix.rstrip('>').rstrip()  # remove trailing >
        # Actually the prefix includes the > at the end before text
        # Let's re-match more carefully
        tag_m = re.match(r'^(\s*<li><a\s[^>]*)(>)', prefix)
        if tag_m:
            before_close = tag_m.group(1)
            line = f'{before_close} data-en="{en_esc}" data-de="{de_esc}">{text}{suffix}'
            modified = True

    # ── 2. Section headers (h2) ──────────────────────────────────────────
    if not modified:
        m = re.match(r'^(\s*<h2)(>)(.+?)(</h2>)$', line)
        if m:
            before, gt, text, close = m.groups()
            text_stripped = text.strip()
            de = KNOWN.get(text_stripped, f"[DE] {text_stripped}")
            en_esc = attr_escape(text_stripped)
            de_esc = attr_escape(de)
            line = f'{before} data-en="{en_esc}" data-de="{de_esc}">{text}{close}'
            modified = True

    # ── 3. Card CTAs ─────────────────────────────────────────────────────
    if not modified:
        m = re.match(r'^(\s*<span class="card-cta")(>)(Click to know more →)(</span>)$', line)
        if m:
            before, gt, text, close = m.groups()
            de = KNOWN.get(text, f"[DE] {text}")
            en_esc = attr_escape(text)
            de_esc = attr_escape(de)
            line = f'{before} data-en="{en_esc}" data-de="{de_esc}">{text}{close}'
            modified = True

    # ── 4. Back buttons (multi-line — text is on next line) ──────────────
    # Pattern:
    #   </svg>
    #   Back to Experience
    # </button>
    if not modified:
        stripped = line.strip()
        if stripped in ["Back to Experience", "Back to Projects", "Back to Recognition", "Back to Community"]:
            de = KNOWN.get(stripped, f"[DE] {stripped}")
            # Wrap in a span with data attrs
            indent = line[:len(line) - len(line.lstrip())]
            line = f'{indent}<span data-en="{attr_escape(stripped)}" data-de="{attr_escape(de)}">{stripped}</span>'
            modified = True

    # ── 5. Hero subheading ───────────────────────────────────────────────
    if not modified:
        m = re.match(r'^(\s*<p class="hero-subheading[^"]*"[^>]*)(>)(AI/ML Engineer)(</p>)$', line)
        if m:
            before, gt, text, close = m.groups()
            de = KNOWN.get(text, f"[DE] {text}")
            en_esc = attr_escape(text)
            de_esc = attr_escape(de)
            line = f'{before} data-en="{en_esc}" data-de="{de_esc}">{text}{close}'
            modified = True

    # ── 6. Role badge in sidebar ─────────────────────────────────────────
    if not modified:
        m = re.match(r'^(\s*<span class="role-badge")(>)(AI/ML Engineer)(</span>)$', line)
        if m:
            before, gt, text, close = m.groups()
            de = KNOWN.get(text, f"[DE] {text}")
            en_esc = attr_escape(text)
            de_esc = attr_escape(de)
            line = f'{before} data-en="{en_esc}" data-de="{de_esc}">{text}{close}'
            modified = True

    # ── 7. Sidebar bio ───────────────────────────────────────────────────
    if not modified:
        m = re.match(r'^(\s*<p class="sidebar-bio")(>)', line)
        if m and "Building practical AI systems" in line:
            # This is a multi-line element, need to handle carefully
            # For now, just add attrs to the opening tag
            full_text = "Building practical AI systems at the intersection of computer vision, edge AI, and real-world hardware."
            de = f"[DE] {full_text}"
            line = line.replace('<p class="sidebar-bio">', f'<p class="sidebar-bio" data-en="{attr_escape(full_text)}" data-de="{attr_escape(de)}">')
            modified = True

    # ── 8. About bio paragraphs (.about-bio) ─────────────────────────────
    if not modified:
        m = re.match(r'^(\s*<p class="about-bio")(>)$', line)
        if m:
            # Multi-line paragraph - collect full text
            j = i + 1
            para_lines = []
            while j < len(lines) and '</p>' not in lines[j]:
                para_lines.append(lines[j].strip())
                j += 1
            if j < len(lines):
                # Last line has </p>
                last = lines[j].strip().replace('</p>', '').strip()
                if last:
                    para_lines.append(last)
            full_text = ' '.join(para_lines)
            # Clean up whitespace
            full_text = re.sub(r'\s+', ' ', full_text).strip()
            de = f"[DE] {full_text}"
            line = f'{m.group(1)} data-en="{attr_escape(full_text)}" data-de="{attr_escape(de)}">'
            modified = True

    # ── 9. Hero college info ─────────────────────────────────────────────
    if not modified:
        if 'class="hero-college' in line:
            # Multi-line, has <strong> inside
            # We'll add data attrs but need innerHTML handling
            # For this element, we need special handling since it has mixed content
            # Skip for now — will handle with innerHTML approach in JS
            pass

    # ── 10. Company names, roles, durations in exp grid cards ────────────
    if not modified:
        # exp-grid-name
        m = re.match(r'^(\s*<span class="exp-grid-name")(>)(.+?)(</span>)$', line)
        if m:
            before, gt, text, close = m.groups()
            de = f"[DE] {text}"
            line = f'{before} data-en="{attr_escape(text)}" data-de="{attr_escape(de)}">{text}{close}'
            modified = True
    
    if not modified:
        # exp-grid-role
        m = re.match(r'^(\s*<span class="exp-grid-role")(>)(.+?)(</span>)$', line)
        if m:
            before, gt, text, close = m.groups()
            de = f"[DE] {text}"
            line = f'{before} data-en="{attr_escape(text)}" data-de="{attr_escape(de)}">{text}{close}'
            modified = True

    if not modified:
        # exp-grid-duration
        m = re.match(r'^(\s*<span class="exp-grid-duration")(>)(.+?)(</span>)$', line)
        if m:
            before, gt, text, close = m.groups()
            de = f"[DE] {text}"
            line = f'{before} data-en="{attr_escape(text)}" data-de="{attr_escape(de)}">{text}{close}'
            modified = True

    # ── 11. Detail view: company name (h3), role (p), meta spans ─────────
    if not modified:
        m = re.match(r'^(\s*<h3 class="exp-detail-company")(>)(.+?)(</h3>)$', line)
        if m:
            before, gt, text, close = m.groups()
            de = f"[DE] {text}"
            line = f'{before} data-en="{attr_escape(text)}" data-de="{attr_escape(de)}">{text}{close}'
            modified = True

    if not modified:
        m = re.match(r'^(\s*<p class="exp-detail-role")(>)(.+?)(</p>)$', line)
        if m:
            before, gt, text, close = m.groups()
            de = f"[DE] {text}"
            line = f'{before} data-en="{attr_escape(text)}" data-de="{attr_escape(de)}">{text}{close}'
            modified = True

    # ── 12. Detail description headings (h4) ─────────────────────────────
    if not modified:
        m = re.match(r'^(\s*<h4)(>)(.+?)(</h4>)$', line)
        if m:
            before, gt, text, close = m.groups()
            de = f"[DE] {text}"
            line = f'{before} data-en="{attr_escape(text)}" data-de="{attr_escape(de)}">{text}{close}'
            modified = True

    # ── 13. Detail description paragraphs ────────────────────────────────
    if not modified:
        # Match paragraphs inside exp-detail-desc, proj-detail sections etc.
        # These are <p> tags that contain long text
        m = re.match(r'^(\s*<p)(>)(.+?)(</p>)$', line)
        if m:
            before, gt, text, close = m.groups()
            text_stripped = text.strip()
            # Skip if it already has data-en or if it's a structural element
            if 'class=' not in before and 'data-en' not in before and len(text_stripped) > 10:
                de = f"[DE] {text_stripped}"
                line = f'{before} data-en="{attr_escape(text_stripped)}" data-de="{attr_escape(de)}">{text}{close}'
                modified = True

    # ── 14. Tag names (span.tag) ─────────────────────────────────────────
    if not modified:
        m = re.match(r'^(\s*<span class="tag"[^>]*)(>)(.+?)(</span>)$', line)
        if m:
            before, gt, text, close = m.groups()
            de = f"[DE] {text}"
            line = f'{before} data-en="{attr_escape(text)}" data-de="{attr_escape(de)}">{text}{close}'
            modified = True

    # ── 15. Tag popup titles ─────────────────────────────────────────────
    if not modified:
        m = re.match(r'^(\s*<div class="tag-popup-title")(>)(.+?)(</div>)$', line)
        if m:
            before, gt, text, close = m.groups()
            de = f"[DE] {text}"
            line = f'{before} data-en="{attr_escape(text)}" data-de="{attr_escape(de)}">{text}{close}'
            modified = True

    # ── 16. Tag popup descriptions ───────────────────────────────────────
    if not modified:
        m = re.match(r'^(\s*<div class="tag-popup-desc")(>)(.+)', line)
        if m:
            before = m.group(1)
            rest = m.group(3)
            # Could be single or multi-line
            full = rest
            j = i
            while '</div>' not in full and j + 1 < len(lines):
                j += 1
                full += ' ' + lines[j].strip()
            # Extract text between > and </div>
            text_content = re.sub(r'</div>$', '', full).strip()
            text_clean = re.sub(r'\s+', ' ', text_content).strip()
            de = f"[DE] {text_clean}"
            # Add attrs to opening tag only
            line = f'{before} data-en="{attr_escape(text_clean)}" data-de="{attr_escape(de)}">{rest}'
            modified = True

    # ── 17. Tag popup examples ───────────────────────────────────────────
    if not modified:
        m = re.match(r'^(\s*<div class="tag-popup-example")(>)(.+)', line)
        if m:
            before = m.group(1)
            rest = m.group(3)
            full = rest
            j = i
            while '</div>' not in full and j + 1 < len(lines):
                j += 1
                full += ' ' + lines[j].strip()
            text_content = re.sub(r'</div>$', '', full).strip()
            text_clean = re.sub(r'\s+', ' ', text_content).strip()
            # For examples, replace "Example:" label prefix with "Beispiel:" in DE
            de_text = text_clean.replace('<strong>Example:</strong>', '<strong>Beispiel:</strong>')
            de = f"[DE] {de_text}"
            line = f'{before} data-en="{attr_escape(text_clean)}" data-de="{attr_escape(de)}">{rest}'
            modified = True

    # ── 18. Type badges ──────────────────────────────────────────────────
    if not modified:
        m = re.match(r'^(\s*<span class="type-badge")(>)(.+?)(</span>)$', line)
        if m:
            before, gt, text, close = m.groups()
            de = f"[DE] {text}"
            line = f'{before} data-en="{attr_escape(text)}" data-de="{attr_escape(de)}">{text}{close}'
            modified = True

    # ── 19. Meta spans (dates, locations) ────────────────────────────────
    if not modified:
        # Date spans inside exp-detail-meta
        m = re.match(r'^(\s*<span)(>)((?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s.+?)(</span>)$', line)
        if m:
            before, gt, text, close = m.groups()
            de = f"[DE] {text}"
            line = f'{before} data-en="{attr_escape(text)}" data-de="{attr_escape(de)}">{text}{close}'
            modified = True
    
    if not modified:
        # Location spans
        m = re.match(r'^(\s*<span)(>)(Bangalore, KA)(</span>)$', line)
        if m:
            before, gt, text, close = m.groups()
            de = f"[DE] {text}"
            line = f'{before} data-en="{attr_escape(text)}" data-de="{attr_escape(de)}">{text}{close}'
            modified = True

    # ── 20. Project grid cards ───────────────────────────────────────────
    if not modified:
        # proj-grid-name
        m = re.match(r'^(\s*<span class="proj-grid-name")(>)(.+?)(</span>)$', line)
        if m:
            before, gt, text, close = m.groups()
            de = f"[DE] {text}"
            line = f'{before} data-en="{attr_escape(text)}" data-de="{attr_escape(de)}">{text}{close}'
            modified = True
    
    if not modified:
        # proj-grid-tagline  
        m = re.match(r'^(\s*<span class="proj-grid-tagline")(>)(.+?)(</span>)$', line)
        if m:
            before, gt, text, close = m.groups()
            de = f"[DE] {text}"
            line = f'{before} data-en="{attr_escape(text)}" data-de="{attr_escape(de)}">{text}{close}'
            modified = True

    # ── 21. Project detail names (h3) ────────────────────────────────────
    if not modified:
        m = re.match(r'^(\s*<h3 class="proj-detail-name")(>)(.+?)(</h3>)$', line)
        if m:
            before, gt, text, close = m.groups()
            de = f"[DE] {text}"
            line = f'{before} data-en="{attr_escape(text)}" data-de="{attr_escape(de)}">{text}{close}'
            modified = True

    # ── 22. Project sections (Problem/Solution/Outcome labels) ───────────
    if not modified:
        m = re.match(r'^(\s*<span class="pso-label")(>)(.+?)(</span>)$', line)
        if m:
            before, gt, text, close = m.groups()
            de = f"[DE] {text}"
            line = f'{before} data-en="{attr_escape(text)}" data-de="{attr_escape(de)}">{text}{close}'
            modified = True

    if not modified:
        m = re.match(r'^(\s*<p class="pso-text")(>)(.+?)(</p>)$', line)
        if m:
            before, gt, text, close = m.groups()
            de = f"[DE] {text}"
            line = f'{before} data-en="{attr_escape(text)}" data-de="{attr_escape(de)}">{text}{close}'
            modified = True

    # ── 23. Recognition detail elements ──────────────────────────────────
    if not modified:
        m = re.match(r'^(\s*<h3 class="recog-detail-name")(>)(.+?)(</h3>)$', line)
        if m:
            before, gt, text, close = m.groups()
            de = f"[DE] {text}"
            line = f'{before} data-en="{attr_escape(text)}" data-de="{attr_escape(de)}">{text}{close}'
            modified = True

    if not modified:
        m = re.match(r'^(\s*<span class="recog-grid-name")(>)(.+?)(</span>)$', line)
        if m:
            before, gt, text, close = m.groups()
            de = f"[DE] {text}"
            line = f'{before} data-en="{attr_escape(text)}" data-de="{attr_escape(de)}">{text}{close}'
            modified = True

    if not modified:
        m = re.match(r'^(\s*<span class="recog-grid-tagline")(>)(.+?)(</span>)$', line)
        if m:
            before, gt, text, close = m.groups()
            de = f"[DE] {text}"
            line = f'{before} data-en="{attr_escape(text)}" data-de="{attr_escape(de)}">{text}{close}'
            modified = True

    # ── 24. Recognition KV pairs ─────────────────────────────────────────
    if not modified:
        m = re.match(r'^(\s*<span class="recog-kv-label")(>)(.+?)(</span>)$', line)
        if m:
            before, gt, text, close = m.groups()
            de = f"[DE] {text}"
            line = f'{before} data-en="{attr_escape(text)}" data-de="{attr_escape(de)}">{text}{close}'
            modified = True

    if not modified:
        m = re.match(r'^(\s*<span class="recog-kv-value")(>)(.+?)(</span>)$', line)
        if m:
            before, gt, text, close = m.groups()
            de = f"[DE] {text}"
            line = f'{before} data-en="{attr_escape(text)}" data-de="{attr_escape(de)}">{text}{close}'
            modified = True

    # ── 25. Recognition description ──────────────────────────────────────
    if not modified:
        m = re.match(r'^(\s*<p class="recog-desc-text")(>)(.+?)(</p>)$', line)
        if m:
            before, gt, text, close = m.groups()
            de = f"[DE] {text}"
            line = f'{before} data-en="{attr_escape(text)}" data-de="{attr_escape(de)}">{text}{close}'
            modified = True

    # ── 26. View Publication button text ─────────────────────────────────
    if not modified:
        stripped = line.strip()
        if stripped == "View Publication":
            de = KNOWN.get(stripped, f"[DE] {stripped}")
            indent = line[:len(line) - len(line.lstrip())]
            line = f'{indent}<span data-en="{attr_escape(stripped)}" data-de="{attr_escape(de)}">{stripped}</span>'
            modified = True

    # ── 27. Community elements ───────────────────────────────────────────
    if not modified:
        m = re.match(r'^(\s*<span class="comm-grid-name")(>)(.+?)(</span>)$', line)
        if m:
            before, gt, text, close = m.groups()
            de = f"[DE] {text}"
            line = f'{before} data-en="{attr_escape(text)}" data-de="{attr_escape(de)}">{text}{close}'
            modified = True

    if not modified:
        m = re.match(r'^(\s*<h3 class="comm-detail-name")(>)(.+?)(</h3>)$', line)
        if m:
            before, gt, text, close = m.groups()
            de = f"[DE] {text}"
            line = f'{before} data-en="{attr_escape(text)}" data-de="{attr_escape(de)}">{text}{close}'
            modified = True

    # ── 28. Duration label and value ─────────────────────────────────────
    if not modified:
        stripped = line.strip()
        if stripped == "Duration":
            de = KNOWN.get(stripped, f"[DE] {stripped}")
            indent = line[:len(line) - len(line.lstrip())]
            line = f'{indent}<span data-en="{attr_escape(stripped)}" data-de="{attr_escape(de)}">{stripped}</span>'
            modified = True

    if not modified:
        stripped = line.strip()
        if stripped == "80 Hours":
            de = KNOWN.get(stripped, f"[DE] {stripped}")
            indent = line[:len(line) - len(line.lstrip())]
            line = f'{indent}<span data-en="{attr_escape(stripped)}" data-de="{attr_escape(de)}">{stripped}</span>'
            modified = True

    # ── 29. Project tagline (p.proj-detail-tagline) ──────────────────────
    if not modified:
        m = re.match(r'^(\s*<p class="proj-detail-tagline")(>)(.+?)(</p>)$', line)
        if m:
            before, gt, text, close = m.groups()
            de = f"[DE] {text}"
            line = f'{before} data-en="{attr_escape(text)}" data-de="{attr_escape(de)}">{text}{close}'
            modified = True

    # ── 30. Hero quote ───────────────────────────────────────────────────
    if not modified:
        if '"A Vision without execution is a hallucination."' in line:
            m = re.match(r'^(\s*<p[^>]*)(>)', line)
            if m:
                text = '"A Vision without execution is a hallucination."'
                de = f'[DE] {text}'
                line = line.replace(m.group(1) + '>', f'{m.group(1)} data-en="{attr_escape(text)}" data-de="{attr_escape(de)}">')
                modified = True

    # ── 31. Community detail sections ────────────────────────────────────
    if not modified:
        m = re.match(r'^(\s*<span class="comm-detail-badge")(>)(.+?)(</span>)$', line)
        if m:
            before, gt, text, close = m.groups()
            de = f"[DE] {text}"
            line = f'{before} data-en="{attr_escape(text)}" data-de="{attr_escape(de)}">{text}{close}'
            modified = True

    if not modified:
        m = re.match(r'^(\s*<span class="comm-detail-duration")(>)(.+?)(</span>)$', line)
        if m:
            before, gt, text, close = m.groups()
            de = f"[DE] {text}"
            line = f'{before} data-en="{attr_escape(text)}" data-de="{attr_escape(de)}">{text}{close}'
            modified = True

    # ── 32. Recognition badges ───────────────────────────────────────────
    if not modified:
        m = re.match(r'^(\s*<span class="recog-badge")(>)(.+?)(</span>)$', line)
        if m:
            before, gt, text, close = m.groups()
            de = f"[DE] {text}"
            line = f'{before} data-en="{attr_escape(text)}" data-de="{attr_escape(de)}">{text}{close}'
            modified = True

    if not modified:
        m = re.match(r'^(\s*<span class="recog-detail-badge")(>)(.+?)(</span>)$', line)
        if m:
            before, gt, text, close = m.groups()
            de = f"[DE] {text}"
            line = f'{before} data-en="{attr_escape(text)}" data-de="{attr_escape(de)}">{text}{close}'
            modified = True

    # ── 33. Project type badges ──────────────────────────────────────────
    if not modified:
        m = re.match(r'^(\s*<span class="proj-badge")(>)(.+?)(</span>)$', line)
        if m:
            before, gt, text, close = m.groups()
            de = f"[DE] {text}"
            line = f'{before} data-en="{attr_escape(text)}" data-de="{attr_escape(de)}">{text}{close}'
            modified = True

    if not modified:
        m = re.match(r'^(\s*<span class="proj-detail-badge")(>)(.+?)(</span>)$', line)
        if m:
            before, gt, text, close = m.groups()
            de = f"[DE] {text}"
            line = f'{before} data-en="{attr_escape(text)}" data-de="{attr_escape(de)}">{text}{close}'
            modified = True

    # ── 34. Community section labels (What I Did/Key Activities/Impact) ──
    if not modified:
        m = re.match(r'^(\s*<h4 class="comm-section-title")(>)(.+?)(</h4>)$', line)
        if m:
            before, gt, text, close = m.groups()
            de = f"[DE] {text}"
            line = f'{before} data-en="{attr_escape(text)}" data-de="{attr_escape(de)}">{text}{close}'
            modified = True

    # ── 35. Community text paragraphs ────────────────────────────────────
    if not modified:
        m = re.match(r'^(\s*<p class="comm-section-text")(>)(.+?)(</p>)$', line)
        if m:
            before, gt, text, close = m.groups()
            de = f"[DE] {text}"
            line = f'{before} data-en="{attr_escape(text)}" data-de="{attr_escape(de)}">{text}{close}'
            modified = True

    # ── 36. Community list items ─────────────────────────────────────────
    if not modified:
        m = re.match(r'^(\s*<li class="comm-activity-item")(>)(.+?)(</li>)$', line)
        if m:
            before, gt, text, close = m.groups()
            de = f"[DE] {text}"
            line = f'{before} data-en="{attr_escape(text)}" data-de="{attr_escape(de)}">{text}{close}'
            modified = True

    # ── 37. Project detail section labels ────────────────────────────────
    if not modified:
        m = re.match(r'^(\s*<span class="proj-section-label")(>)(.+?)(</span>)$', line)
        if m:
            before, gt, text, close = m.groups()
            de = f"[DE] {text}"
            line = f'{before} data-en="{attr_escape(text)}" data-de="{attr_escape(de)}">{text}{close}'
            modified = True

    # ── 38. Recognition year/date spans ──────────────────────────────────
    if not modified:
        m = re.match(r'^(\s*<span class="recog-grid-year")(>)(.+?)(</span>)$', line)
        if m:
            before, gt, text, close = m.groups()
            de = f"[DE] {text}"
            line = f'{before} data-en="{attr_escape(text)}" data-de="{attr_escape(de)}">{text}{close}'
            modified = True

    if not modified:
        m = re.match(r'^(\s*<span class="recog-detail-year")(>)(.+?)(</span>)$', line)
        if m:
            before, gt, text, close = m.groups()
            de = f"[DE] {text}"
            line = f'{before} data-en="{attr_escape(text)}" data-de="{attr_escape(de)}">{text}{close}'
            modified = True

    output_lines.append(line)
    i += 1

content = '\n'.join(output_lines)

# ──────────────────────────────────────────────────────────────────────────
# Now handle the hero-college paragraph which has mixed content (<strong>)
# We'll use innerHTML approach in JS for this one, adding data attributes
# ──────────────────────────────────────────────────────────────────────────
hero_college_en = '<strong>New Horizon College of Engineering</strong>, Bengaluru — B.E. in Artificial Intelligence and Machine Learning (Expected May 2026) · GPA: 8.66 / 10.0'
hero_college_de = '<strong>New Horizon College of Engineering</strong>, Bengaluru — B.E. in Künstlicher Intelligenz und maschinellem Lernen (Voraussichtlich Mai 2026) · GPA: 8,66/10,0'

content = content.replace(
    '<p class="hero-college fade-in fade-in-d3">',
    f'<p class="hero-college fade-in fade-in-d3" data-en-html="{attr_escape(hero_college_en)}" data-de-html="{attr_escape(hero_college_de)}">'
)

# ──────────────────────────────────────────────────────────────────────────
# Inject the toggle button and tooltip HTML before </body>
# ──────────────────────────────────────────────────────────────────────────
toggle_html = '''
  <!-- Language Toggle Button -->
  <div id="langToggle" style="position:fixed;bottom:28px;right:28px;z-index:9998;background:#fff;border:1px solid #e6e2db;border-radius:99px;padding:8px 16px;cursor:pointer;font-family:'DM Sans',sans-serif;font-size:13px;box-shadow:0 2px 8px rgba(0,0,0,0.06);user-select:none;transition:box-shadow 0.2s ease;" onmouseenter="this.style.boxShadow='0 4px 16px rgba(0,0,0,0.10)'" onmouseleave="this.style.boxShadow='0 2px 8px rgba(0,0,0,0.06)'">
    <span id="langEN" style="font-weight:700;color:#c85a2a;">EN</span>
    <span style="color:#a09c97;margin:0 4px;">|</span>
    <span id="langDE" style="font-weight:400;color:#a09c97;">DE</span>
  </div>

  <!-- Language Hint Tooltip -->
  <div id="langTooltip" style="position:fixed;bottom:80px;right:28px;z-index:9999;background:#fff;border:1px solid #e6e2db;border-radius:12px;padding:12px 16px;box-shadow:0 8px 24px rgba(0,0,0,0.10);font-family:'DM Sans',sans-serif;font-size:13px;max-width:220px;opacity:0;transform:translateY(8px);transition:opacity 0.3s ease,transform 0.3s ease;pointer-events:none;">
    <div>🌐 You can switch this site to German!</div>
    <div style="font-size:11px;color:#a09c97;margin-top:4px;">Diese Seite ist auch auf Deutsch verfügbar.</div>
    <div style="position:absolute;bottom:-7px;right:24px;width:14px;height:14px;background:#fff;border-right:1px solid #e6e2db;border-bottom:1px solid #e6e2db;transform:rotate(45deg);"></div>
  </div>
'''

content = content.replace('</body>', toggle_html + '\n</body>')

# ──────────────────────────────────────────────────────────────────────────
# Inject the language switching JavaScript before </script>
# ──────────────────────────────────────────────────────────────────────────
lang_js = '''
    /* ── Language Toggle System ─────────────────── */
    function switchLanguage(lang) {
      // Fade out
      document.body.style.transition = 'opacity 0.2s ease';
      document.body.style.opacity = '0';
      
      setTimeout(() => {
        // Switch text content for elements with data-en / data-de
        document.querySelectorAll('[data-en][data-de]').forEach(el => {
          el.textContent = lang === 'de' ? el.getAttribute('data-de') : el.getAttribute('data-en');
        });
        
        // Switch innerHTML for elements with data-en-html / data-de-html
        document.querySelectorAll('[data-en-html][data-de-html]').forEach(el => {
          el.innerHTML = lang === 'de' ? el.getAttribute('data-de-html') : el.getAttribute('data-en-html');
        });
        
        // Update toggle button styling
        const enSpan = document.getElementById('langEN');
        const deSpan = document.getElementById('langDE');
        if (lang === 'de') {
          enSpan.style.fontWeight = '400';
          enSpan.style.color = '#a09c97';
          deSpan.style.fontWeight = '700';
          deSpan.style.color = '#c85a2a';
        } else {
          enSpan.style.fontWeight = '700';
          enSpan.style.color = '#c85a2a';
          deSpan.style.fontWeight = '400';
          deSpan.style.color = '#a09c97';
        }
        
        // Store preference
        localStorage.setItem('siteLang', lang);
        
        // Fade in
        document.body.style.opacity = '1';
      }, 200);
    }
    
    // Toggle click handler
    document.getElementById('langToggle').addEventListener('click', () => {
      const current = localStorage.getItem('siteLang') || 'en';
      switchLanguage(current === 'en' ? 'de' : 'en');
    });
    
    // Restore language on load
    const savedLang = localStorage.getItem('siteLang');
    if (savedLang && savedLang !== 'en') {
      switchLanguage(savedLang);
    }
    
    // Language hint tooltip
    (function() {
      if (sessionStorage.getItem('langTooltipShown')) return;
      sessionStorage.setItem('langTooltipShown', 'true');
      
      const tooltip = document.getElementById('langTooltip');
      
      // Show after 1 second
      setTimeout(() => {
        tooltip.style.opacity = '1';
        tooltip.style.transform = 'translateY(0)';
        tooltip.style.pointerEvents = 'auto';
      }, 1000);
      
      // Hide after 5 seconds total
      setTimeout(() => {
        tooltip.style.opacity = '0';
        tooltip.style.transform = 'translateY(8px)';
        tooltip.style.pointerEvents = 'none';
        
        setTimeout(() => {
          tooltip.remove();
        }, 300);
      }, 5000);
    })();
'''

content = content.replace('  </script>', lang_js + '\n  </script>')

with open(FILE, 'w', encoding='utf-8') as f:
    f.write(content)

print("Done! Language toggle system added.")

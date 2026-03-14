#!/usr/bin/env python3
"""
Second pass: annotate remaining multi-line text elements that the first pass missed.
Handles: multi-line <p>, multi-line .pso-text, multi-line .proj-detail-tagline,
multi-line .pso-label, community detail content, li items, etc.
"""
import re

FILE = "index.html"

with open(FILE, "r", encoding="utf-8") as f:
    content = f.read()


def attr_escape(s):
    return s.replace("&", "&amp;").replace('"', "&quot;").replace("<", "&lt;").replace(">", "&gt;")


def collect_text_to_close(lines, start_idx, close_tag='</p>'):
    """Collect text content from start_idx until close tag is found. Returns (text, end_idx)."""
    full = []
    j = start_idx
    while j < len(lines):
        full.append(lines[j].strip())
        if close_tag in lines[j]:
            break
        j += 1
    joined = ' '.join(full)
    # Extract text between > and close_tag
    # Remove tags for text content
    text = re.sub(r'<[^>]+>', '', joined)
    text = re.sub(r'\s+', ' ', text).strip()
    return text, j


lines = content.split('\n')
output_lines = []

i = 0
while i < len(lines):
    line = lines[i]
    stripped = line.strip()
    modified = False

    # ── Multi-line <p> tags without class and without data-en ────────────
    if not modified:
        m = re.match(r'^(\s*)<p>(.*)', line)
        if m and 'data-en' not in line and '</p>' not in line:
            indent = m.group(1)
            rest = m.group(2)
            # Collect full text
            text_parts = [rest.strip()]
            j = i + 1
            while j < len(lines) and '</p>' not in lines[j]:
                text_parts.append(lines[j].strip())
                j += 1
            if j < len(lines):
                last = lines[j].strip().replace('</p>', '').strip()
                if last:
                    text_parts.append(last)
            full_text = ' '.join(text_parts)
            full_text = re.sub(r'\s+', ' ', full_text).strip()
            if len(full_text) > 5:
                de = f"[DE] {full_text}"
                line = f'{indent}<p data-en="{attr_escape(full_text)}" data-de="{attr_escape(de)}">{rest}'
                modified = True

    # ── Multi-line <p class="pso-text"> without data-en ──────────────────
    if not modified:
        m = re.match(r'^(\s*)<p class="pso-text">(.*)', line)
        if m and 'data-en' not in line and '</p>' not in line:
            indent = m.group(1)
            rest = m.group(2)
            text_parts = [rest.strip()]
            j = i + 1
            while j < len(lines) and '</p>' not in lines[j]:
                text_parts.append(lines[j].strip())
                j += 1
            if j < len(lines):
                last = lines[j].strip().replace('</p>', '').strip()
                if last:
                    text_parts.append(last)
            full_text = ' '.join(text_parts)
            full_text = re.sub(r'\s+', ' ', full_text).strip()
            de = f"[DE] {full_text}"
            line = f'{indent}<p class="pso-text" data-en="{attr_escape(full_text)}" data-de="{attr_escape(de)}">{rest}'
            modified = True

    # ── Multi-line <p class="proj-detail-tagline" ...> ───────────────────
    if not modified:
        m = re.match(r'^(\s*)<p class="proj-detail-tagline"', line)
        if m and 'data-en' not in line and '</p>' not in line:
            indent = m.group(1)
            # Collect full text from this line onward
            full_lines = [line.strip()]
            j = i + 1
            while j < len(lines) and '</p>' not in lines[j]:
                full_lines.append(lines[j].strip())
                j += 1
            if j < len(lines):
                full_lines.append(lines[j].strip())
            joined = ' '.join(full_lines)
            # Extract text content
            text = re.sub(r'<[^>]+>', '', joined)
            text = re.sub(r'\s+', ' ', text).strip()
            # Unescape &amp; for text content
            de = f"[DE] {text}"
            # Add attrs to opening tag
            line = line.replace('<p class="proj-detail-tagline"',
                              f'<p class="proj-detail-tagline" data-en="{attr_escape(text)}" data-de="{attr_escape(de)}"')
            modified = True

    # ── Multi-line <p class="hero-college ..."> ──────────────────────────
    # Already handled with data-en-html in first pass

    # ── <div class="pso-label"> with mixed emoji content ─────────────────
    if not modified:
        m = re.match(r'^(\s*)<div class="pso-label">(.*)</div>$', stripped)
        if m and 'data-en' not in stripped:
            content_text = m.group(2)
            # Extract just the text
            text = re.sub(r'<[^>]+>', '', content_text).strip()
            de = f"[DE] {text}"
            indent = line[:len(line) - len(line.lstrip())]
            line = f'{indent}<div class="pso-label" data-en="{attr_escape(text)}" data-de="{attr_escape(de)}">{content_text}</div>'
            modified = True

    # ── Community section labels (.comm-section-title as h4) ─────────────
    if not modified:
        m = re.match(r'^(\s*)<h4 class="comm-section-title">(.*?)</h4>$', stripped)
        if m and 'data-en' not in stripped:
            text = m.group(2).strip()
            de = f"[DE] {text}"
            indent = line[:len(line) - len(line.lstrip())]
            line = f'{indent}<h4 class="comm-section-title" data-en="{attr_escape(text)}" data-de="{attr_escape(de)}">{text}</h4>'
            modified = True

    # ── Community text paragraphs (.comm-section-text) ───────────────────
    if not modified:
        m = re.match(r'^(\s*)<p class="comm-section-text">(.*)', line)
        if m and 'data-en' not in line:
            indent = m.group(1)
            rest = m.group(2)
            if '</p>' in line:
                text = re.sub(r'<[^>]+>', '', rest).strip()
                text = text.replace('</p>', '').strip()
                de = f"[DE] {text}"
                line = f'{indent}<p class="comm-section-text" data-en="{attr_escape(text)}" data-de="{attr_escape(de)}">{rest}'
            else:
                text_parts = [rest.strip()]
                j = i + 1
                while j < len(lines) and '</p>' not in lines[j]:
                    text_parts.append(lines[j].strip())
                    j += 1
                if j < len(lines):
                    last = lines[j].strip().replace('</p>', '').strip()
                    if last:
                        text_parts.append(last)
                full_text = ' '.join(text_parts)
                full_text = re.sub(r'\s+', ' ', full_text).strip()
                de = f"[DE] {full_text}"
                line = f'{indent}<p class="comm-section-text" data-en="{attr_escape(full_text)}" data-de="{attr_escape(de)}">{rest}'
            modified = True

    # ── Community activity list items ────────────────────────────────────
    if not modified:
        m = re.match(r'^(\s*)<li class="comm-activity-item">(.*?)</li>$', stripped)
        if m and 'data-en' not in stripped:
            text = m.group(2).strip()
            de = f"[DE] {text}"
            indent = line[:len(line) - len(line.lstrip())]
            line = f'{indent}<li class="comm-activity-item" data-en="{attr_escape(text)}" data-de="{attr_escape(de)}">{text}</li>'
            modified = True

    # ── Community grid badges ────────────────────────────────────────────
    if not modified:
        m = re.match(r'^(\s*)<span class="comm-grid-badge">(.*?)</span>$', stripped)
        if m and 'data-en' not in stripped:
            text = m.group(2).strip()
            de = f"[DE] {text}"
            indent = line[:len(line) - len(line.lstrip())]
            line = f'{indent}<span class="comm-grid-badge" data-en="{attr_escape(text)}" data-de="{attr_escape(de)}">{text}</span>'
            modified = True

    # ── Project category badges ──────────────────────────────────────────
    if not modified:
        m = re.match(r'^(\s*)<span class="proj-category-badge">(.*?)</span>$', stripped)
        if m and 'data-en' not in stripped:
            text = m.group(2).strip()
            de = f"[DE] {text}"
            indent = line[:len(line) - len(line.lstrip())]
            line = f'{indent}<span class="proj-category-badge" data-en="{attr_escape(text)}" data-de="{attr_escape(de)}">{text}</span>'
            modified = True

    # ── proj-tag-label (DEVOPS, LANGUAGES etc.) ──────────────────────────
    if not modified:
        m = re.match(r'^(\s*)<span class="proj-tag-label">(.*?)</span>$', stripped)
        if m and 'data-en' not in stripped:
            text = m.group(2).strip()
            de = f"[DE] {text}"
            indent = line[:len(line) - len(line.lstrip())]
            line = f'{indent}<span class="proj-tag-label" data-en="{attr_escape(text)}" data-de="{attr_escape(de)}">{text}</span>'
            modified = True

    # ── proj-tag items ───────────────────────────────────────────────────
    if not modified:
        m = re.match(r'^(\s*)<span class="proj-tag">(.*?)</span>$', stripped)
        if m and 'data-en' not in stripped:
            text = m.group(2).strip()
            de = f"[DE] {text}"
            indent = line[:len(line) - len(line.lstrip())]
            line = f'{indent}<span class="proj-tag" data-en="{attr_escape(text)}" data-de="{attr_escape(de)}">{text}</span>'
            modified = True

    # ── Recognition detail elements ──────────────────────────────────────
    if not modified:
        for cls in ['recog-detail-tagline', 'recog-kv-label', 'recog-kv-value', 'recog-desc-text']:
            m = re.match(r'^(\s*)<(?:p|span) class="' + cls + r'">(.*)', line)
            if m and 'data-en' not in line:
                indent = m.group(1)
                rest = m.group(2)
                tag = 'p' if cls in ['recog-desc-text', 'recog-detail-tagline'] else 'span'
                close = f'</{tag}>'
                if close in line:
                    text = re.sub(r'<[^>]+>', '', rest).strip()
                    text = text.replace(close.replace('<', '').replace('>', '').replace('/', ''), '').strip()
                    de = f"[DE] {text}"
                    line = line.replace(f'<{tag} class="{cls}">', f'<{tag} class="{cls}" data-en="{attr_escape(text)}" data-de="{attr_escape(de)}">')
                else:
                    text_parts = [rest.strip()]
                    j = i + 1
                    while j < len(lines) and close not in lines[j]:
                        text_parts.append(lines[j].strip())
                        j += 1
                    if j < len(lines):
                        last = lines[j].strip().replace(close, '').strip()
                        if last:
                            text_parts.append(last)
                    full_text = ' '.join(text_parts)
                    full_text = re.sub(r'<[^>]+>', '', full_text)
                    full_text = re.sub(r'\s+', ' ', full_text).strip()
                    de = f"[DE] {full_text}"
                    line = line.replace(f'<{tag} class="{cls}">', f'<{tag} class="{cls}" data-en="{attr_escape(full_text)}" data-de="{attr_escape(de)}">')
                modified = True
                break

    # ── Sidebar name ─────────────────────────────────────────────────────
    if not modified:
        m = re.match(r'^(\s*)<p class="sidebar-name">(.*?)</p>$', stripped)
        if m and 'data-en' not in stripped:
            text = m.group(2).strip()
            de = f"[DE] {text}"
            indent = line[:len(line) - len(line.lstrip())]
            line = f'{indent}<p class="sidebar-name" data-en="{attr_escape(text)}" data-de="{attr_escape(de)}">{text}</p>'
            modified = True

    # ── Hero heading (h1) ────────────────────────────────────────────────
    if not modified:
        m = re.match(r'^(\s*)<h1 class="hero-heading[^"]*"[^>]*>(.*?)</h1>$', stripped)
        if m and 'data-en' not in stripped:
            text = m.group(2).strip()
            de = f"[DE] {text}"
            line = line.replace('>' + text + '</h1>', f' data-en="{attr_escape(text)}" data-de="{attr_escape(de)}">{text}</h1>')
            modified = True

    output_lines.append(line)
    i += 1

content = '\n'.join(output_lines)

with open(FILE, 'w', encoding='utf-8') as f:
    f.write(content)

print("Second pass complete!")

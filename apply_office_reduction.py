with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace the office_compact_css block
marker = "/* 10% Height Reduction for Head Office & Branch Office Boxes */"
start_idx = css.find(marker)
if start_idx != -1:
    css = css[:start_idx]

office_compact_css = """/* 10% Height Reduction for Head Office & Branch Office Boxes */
.contact-grid > .office-card-1,
.contact-grid > .office-card-2 {
    padding: clamp(1.2rem, 1.5vw, 1.45rem) clamp(1rem, 1.6vw, 1.45rem) !important;
}

.contact-grid .office-name {
    margin-bottom: 0.45rem !important;
}

.contact-grid .office-reviews {
    margin-bottom: 1rem !important;
}

.contact-grid .office-detail {
    margin-bottom: 0.85rem !important;
    gap: 0.95rem !important;
    font-size: 1rem !important;
    line-height: 1.45 !important;
    min-height: 0 !important;
}

.contact-grid .fort-gallery {
    margin-top: 1.1rem !important;
    max-width: 95% !important;
    margin-inline: auto !important;
}

.contact-grid .kotavila-gallery {
    margin-top: 1.1rem !important;
    width: min(100%, 265px) !important;
}

.contact-grid .map-container,
.contact-grid .map-container-square {
    margin-top: 1.1rem !important;
    width: min(100%, 225px) !important;
    height: min(100%, 225px) !important;
    max-width: 225px !important;
}

.contact-grid .action-buttons {
    margin-top: 1.25rem !important;
    gap: 0.9rem !important;
}
"""

css += "\n" + office_compact_css

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("SUCCESS: Calibrated office boxes for precise 10% reduction.")

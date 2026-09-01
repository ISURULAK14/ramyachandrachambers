with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Enforce strict opacity:0 and visibility:hidden for all inactive map pins
# Clean up any conflicting .map-pin rules
css = css.replace('.map-pin{position:absolute;width:12px;height:12px;background-color:#5ce1e6;border:1.5px solid #ffffff;border-radius:50%;transform:translate(-50%,-50%);transition:all .4s var(--smooth);box-shadow:0 0 10px rgba(92,225,230,.85),0 0 20px rgba(92,225,230,.4);z-index:15;cursor:pointer}',
                  '.map-pin{position:absolute;width:12px;height:12px;opacity:0 !important;visibility:hidden !important;pointer-events:none !important;border-radius:50%;transform:translate(-50%,-50%);transition:opacity .4s ease,transform .4s ease,visibility .4s ease;z-index:15}')

# Remove old office reduction block if present
marker = "/* 10% Height Reduction for Head Office & Branch Office Boxes */"
start_idx = css.find(marker)
if start_idx != -1:
    css = css[:start_idx]

compact_css = """/* Additional 10% Height Reduction & Strict Inactive Pin Invisibility */
.map-pin {
    position: absolute !important;
    width: 10px !important;
    height: 10px !important;
    background-color: #6ed6d2 !important;
    opacity: 0 !important;
    visibility: hidden !important;
    pointer-events: none !important;
    border-radius: 50% !important;
    transform: translate(-50%, -50%) !important;
    transition: opacity .35s ease, transform .35s ease, visibility .35s ease !important;
    box-shadow: 0 0 8px rgba(110,214,210,0.6) !important;
    z-index: 2 !important;
}

.map-pin.active,
.map-pin:hover {
    opacity: 1 !important;
    visibility: visible !important;
    pointer-events: auto !important;
    background-color: #f2c879 !important;
    box-shadow: 0 0 18px #f2c879, 0 0 30px rgba(242,200,121,0.85) !important;
    transform: translate(-50%, -50%) scale(1.35) !important;
    z-index: 50 !important;
    cursor: pointer !important;
}

.map-pin.active .pin-label,
.map-pin:hover .pin-label {
    opacity: 1 !important;
    visibility: visible !important;
    pointer-events: auto !important;
}

/* Office Boxes ~10% Height Reduction */
.contact-grid > .office-card-1,
.contact-grid > .office-card-2 {
    padding: clamp(1rem, 1.2vw, 1.25rem) clamp(0.9rem, 1.3vw, 1.25rem) !important;
}

.contact-grid .office-tag {
    padding: 0.35rem 1.1rem !important;
    font-size: 0.72rem !important;
    margin-bottom: 0.5rem !important;
}

.contact-grid .office-name {
    font-size: 1.85rem !important;
    margin-bottom: 0.3rem !important;
}

.contact-grid .office-reviews {
    margin-bottom: 0.75rem !important;
    font-size: 0.88rem !important;
}

.contact-grid .office-detail {
    margin-bottom: 0.55rem !important;
    gap: 0.75rem !important;
    font-size: 0.94rem !important;
    line-height: 1.38 !important;
    min-height: 0 !important;
}

.contact-grid .fort-gallery {
    margin-top: 0.85rem !important;
    max-width: 82% !important;
    margin-inline: auto !important;
}

.contact-grid .kotavila-gallery {
    margin-top: 0.85rem !important;
    width: min(100%, 215px) !important;
}

.contact-grid .map-container,
.contact-grid .map-container-square {
    margin-top: 0.85rem !important;
    width: min(100%, 190px) !important;
    height: min(100%, 190px) !important;
    max-width: 190px !important;
}

.contact-grid .action-buttons {
    margin-top: 1rem !important;
    gap: 0.75rem !important;
}

.contact-grid .action-buttons .btn {
    padding: 0.65rem 1.2rem !important;
    font-size: 0.85rem !important;
}
"""

css += "\n" + compact_css

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("SUCCESS: Updated css/style.css with strict inactive pin invisibility and 10% office height reduction!")

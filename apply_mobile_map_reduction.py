with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

mobile_map_css = """
/* ==========================================================================
   MOBILE WORLD MAP 40% HEIGHT REDUCTION
   ========================================================================== */
@media (max-width: 900px) {
    .map-wrapper {
        width: 100% !important;
        height: clamp(210px, 32vh, 250px) !important;
        min-height: 200px !important;
        max-height: 250px !important;
        margin: 0 auto 2.5rem auto !important;
        border-radius: 12px !important;
        background-size: 100% 100% !important;
    }

    .map-bg-img {
        width: 100% !important;
        height: 100% !important;
        object-fit: fill !important;
    }

    .map-pin {
        width: 7px !important;
        height: 7px !important;
    }

    .map-pin.active,
    .map-pin:hover {
        transform: translate(-50%, -50%) scale(1.3) !important;
    }

    .map-pin.active .pin-label,
    .map-pin:hover .pin-label {
        font-size: 0.52rem !important;
        padding: 0.2rem 0.42rem !important;
        letter-spacing: 0.3px !important;
    }

    /* Directional offsets scaled for compact mobile map */
    .pin-uk .pin-label, .pin-ireland .pin-label, .pin-france .pin-label, .pin-portugal .pin-label, .pin-belgium .pin-label, .pin-australia .pin-label, .pin-nz .pin-label {
        right: 120% !important; left: auto !important; top: 50% !important; bottom: auto !important;
    }
    .pin-slovakia .pin-label, .pin-romania .pin-label, .pin-latvia .pin-label, .pin-japan .pin-label, .pin-korea .pin-label, .pin-israel .pin-label, .pin-uae .pin-label, .pin-bangladesh .pin-label, .pin-china .pin-label {
        left: 120% !important; right: auto !important; top: 50% !important; bottom: auto !important;
    }
    .pin-greece .pin-label, .pin-italy .pin-label, .pin-malta .pin-label, .pin-srilanka .pin-label, .pin-zanzibar .pin-label, .pin-malaysia .pin-label, .pin-maldives .pin-label, .pin-mali .pin-label, .pin-singapore .pin-label {
        top: 120% !important; bottom: auto !important; left: 50% !important; right: auto !important;
    }
    .pin-norway .pin-label, .pin-sweden .pin-label, .pin-denmark .pin-label, .pin-netherlands .pin-label, .pin-germany .pin-label, .pin-usa .pin-label, .pin-india .pin-label, .pin-austria .pin-label, .pin-switzerland .pin-label, .pin-luxembourg .pin-label {
        bottom: 120% !important; top: auto !important; left: 50% !important; right: auto !important;
    }
}

@media (max-width: 480px) {
    .map-wrapper {
        height: clamp(180px, 28vh, 220px) !important;
        min-height: 180px !important;
        max-height: 220px !important;
        margin: 0 auto 2rem auto !important;
    }

    .map-pin {
        width: 6px !important;
        height: 6px !important;
    }

    .map-pin.active .pin-label,
    .map-pin:hover .pin-label {
        font-size: 0.48rem !important;
        padding: 0.15rem 0.35rem !important;
    }
}
"""

css += "\n" + mobile_map_css

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("SUCCESS: Added 40% height reduction for world map on mobile.")

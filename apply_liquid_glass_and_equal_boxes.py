with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

liquid_and_equal_css = """
/* ==========================================================================
   LIQUID GLASS OPAQUE HEADER & FOOTER
   ========================================================================== */
.site-nav,
.site-nav.scrolled {
    background: rgba(6, 17, 29, 0.94) !important;
    backdrop-filter: blur(28px) saturate(190%) contrast(105%) !important;
    -webkit-backdrop-filter: blur(28px) saturate(190%) contrast(105%) !important;
    border-bottom: 1px solid rgba(242, 200, 121, 0.25) !important;
    box-shadow: 0 12px 35px rgba(0, 0, 0, 0.65), inset 0 1px 0 rgba(255, 255, 255, 0.14), inset 0 -1px 0 rgba(242, 200, 121, 0.15) !important;
}

.site-footer {
    background: rgba(5, 14, 25, 0.96) !important;
    backdrop-filter: blur(28px) saturate(190%) contrast(105%) !important;
    -webkit-backdrop-filter: blur(28px) saturate(190%) contrast(105%) !important;
    border-top: 1px solid rgba(242, 200, 121, 0.25) !important;
    box-shadow: 0 -12px 35px rgba(0, 0, 0, 0.65), inset 0 1px 0 rgba(255, 255, 255, 0.12), inset 0 -1px 0 rgba(0, 0, 0, 0.5) !important;
}

/* ==========================================================================
   EQUAL & BALANCED OFFICE BOXES (HEAD OFFICE & BRANCH OFFICE)
   ========================================================================== */
.contact-grid {
    display: grid !important;
    grid-template-columns: repeat(2, minmax(0, 1fr)) !important;
    gap: clamp(1.2rem, 2vw, 2rem) !important;
    align-items: stretch !important;
}

.contact-grid > .office-card-1,
.contact-grid > .office-card-2 {
    display: flex !important;
    flex-direction: column !important;
    justify-content: space-between !important;
    height: 100% !important;
    max-width: 580px !important;
    width: 100% !important;
    padding: clamp(1.1rem, 1.4vw, 1.35rem) clamp(1rem, 1.5vw, 1.4rem) !important;
    border-radius: 16px !important;
    box-sizing: border-box !important;
}

.contact-grid .office-tag {
    display: inline-block !important;
    align-self: flex-start !important;
    padding: 0.35rem 1.1rem !important;
    font-size: 0.72rem !important;
    margin-bottom: 0.4rem !important;
}

.contact-grid .office-name {
    font-size: 1.85rem !important;
    margin-bottom: 0.25rem !important;
}

.contact-grid .office-reviews {
    margin-bottom: 0.75rem !important;
    font-size: 0.88rem !important;
}

.contact-grid .office-detail {
    margin-bottom: 0.5rem !important;
    gap: 0.75rem !important;
    font-size: 0.94rem !important;
    line-height: 1.38 !important;
    min-height: 0 !important;
}

.contact-grid .fort-gallery,
.contact-grid .kotavila-gallery {
    width: 100% !important;
    max-width: 320px !important;
    height: 140px !important;
    aspect-ratio: auto !important;
    margin: 0.85rem auto 0 !important;
    border-radius: 12px !important;
    overflow: hidden !important;
    border: 1px solid rgba(255, 255, 255, 0.22) !important;
    box-shadow: 0 12px 30px rgba(0, 0, 0, 0.3) !important;
    position: relative !important;
}

.contact-grid .fort-gallery picture,
.contact-grid .fort-gallery picture img {
    width: 100% !important;
    height: 100% !important;
    object-fit: cover !important;
    display: block !important;
}

.contact-grid .kotavila-gallery {
    display: grid !important;
    grid-template-columns: 1fr 1fr !important;
    gap: 6px !important;
    perspective: none !important;
}

.contact-grid .kotavila-gallery::after {
    display: none !important;
}

.contact-grid .kotavila-gallery picture {
    position: static !important;
    width: 100% !important;
    height: 100% !important;
    transform: none !important;
    border: none !important;
    box-shadow: none !important;
    border-radius: 0 !important;
}

.contact-grid .kotavila-gallery picture img {
    width: 100% !important;
    height: 100% !important;
    object-fit: cover !important;
    display: block !important;
}

.contact-grid .map-container,
.contact-grid .map-container-square {
    width: 100% !important;
    max-width: 320px !important;
    height: 140px !important;
    aspect-ratio: auto !important;
    margin: 0.85rem auto 0 !important;
    border-radius: 12px !important;
    overflow: hidden !important;
}

.contact-grid .map-container iframe,
.contact-grid .map-container-square iframe {
    width: 100% !important;
    height: 100% !important;
    display: block !important;
}

.contact-grid .action-buttons {
    margin-top: 1rem !important;
    display: grid !important;
    grid-template-columns: 1fr 1fr !important;
    gap: 0.75rem !important;
    width: 100% !important;
    max-width: 320px !important;
    margin-inline: auto !important;
}

.contact-grid .action-buttons .btn {
    padding: 0.65rem 1rem !important;
    font-size: 0.85rem !important;
    text-align: center !important;
    white-space: nowrap !important;
}

/* ==========================================================================
   MOBILE RESPONSIVENESS OPTIMIZATIONS
   ========================================================================== */
@media (max-width: 900px) {
    .contact-grid {
        grid-template-columns: 1fr !important;
        gap: 1.5rem !important;
    }
    .contact-grid > .office-card-1,
    .contact-grid > .office-card-2 {
        max-width: 100% !important;
    }
    .reviews-grid {
        grid-template-columns: 1fr !important;
        gap: 1.5rem !important;
    }
    .reviews-grid > .review-card {
        width: 100% !important;
    }
    .map-wrapper {
        border-radius: 12px !important;
    }
    .site-nav {
        padding: max(0.4rem, env(safe-area-inset-top)) 0.5rem 0.4rem !important;
    }
    .nav-container {
        padding: 0 !important;
    }
    .nav-links {
        padding: 0.2rem 0.5rem 0.35rem !important;
    }
    .site-footer {
        padding: 2.2rem 1.25rem max(1.2rem, env(safe-area-inset-bottom)) !important;
    }
    .footer-container {
        flex-direction: column !important;
        align-items: center !important;
        text-align: center !important;
        gap: 1.4rem !important;
    }
}

@media (max-width: 480px) {
    .contact-grid .fort-gallery,
    .contact-grid .kotavila-gallery,
    .contact-grid .map-container,
    .contact-grid .map-container-square,
    .contact-grid .action-buttons {
        max-width: 100% !important;
    }
    .hero-title {
        font-size: clamp(2.2rem, 9vw, 3.2rem) !important;
    }
    .section-title {
        font-size: clamp(2rem, 7.5vw, 2.8rem) !important;
    }
}
"""

css += "\n" + liquid_and_equal_css

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("SUCCESS: Added Liquid Glass Header/Footer, 100% Equal Office Boxes, and Mobile Optimizations!")

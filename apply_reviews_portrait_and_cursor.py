import re

# 1. Update css/style.css with portrait review boxes and cursor pixel animation
with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Add cursor animation CSS & portrait review boxes CSS
cursor_and_review_css = """
/* ==========================================================================
   CURSOR PIXEL ILLUMINATION ANIMATION (RESTORED)
   ========================================================================== */
.cursor-pixel-field {
    position: fixed !important;
    left: 0 !important;
    top: 0 !important;
    width: 112px !important;
    height: 112px !important;
    pointer-events: none !important;
    z-index: 9998 !important;
    opacity: 0 !important;
    transform: translate3d(-200px, -200px, 0);
    background-image:
        radial-gradient(circle at center, rgba(214, 183, 124, .38) 0, rgba(214, 183, 124, .18) 22%, rgba(103, 202, 198, .12) 44%, transparent 70%),
        radial-gradient(circle 2px at 56px 56px, rgba(255, 255, 255, .95) 0, transparent 100%) !important;
    border-radius: 50% !important;
    mix-blend-mode: screen !important;
    will-change: transform, opacity !important;
    transition: opacity .22s ease !important;
}

body.pixel-cursor-ready .cursor-pixel-field {
    opacity: 0.75 !important;
}

@media (max-width: 900px), (pointer: coarse) {
    .cursor-pixel-field {
        display: none !important;
    }
}

@media (prefers-reduced-motion: reduce) {
    .cursor-pixel-field {
        display: none !important;
    }
}

/* ==========================================================================
   PORTRAIT ORIENTATION REVIEW BOXES (MATCHING OFFICE BOXES)
   ========================================================================== */
.reviews-grid {
    display: grid !important;
    grid-template-columns: repeat(2, minmax(0, 1fr)) !important;
    gap: clamp(1.2rem, 2vw, 2rem) !important;
    align-items: stretch !important;
    max-width: 1200px !important;
    margin: 3rem auto 0 !important;
}

.reviews-grid > .review-card,
.review-card-google,
.review-card-direct {
    width: 100% !important;
    max-width: 580px !important;
    justify-self: center !important;
    display: flex !important;
    flex-direction: column !important;
    justify-content: space-between !important;
    min-height: 440px !important;
    height: 100% !important;
    padding: clamp(1.4rem, 1.8vw, 1.8rem) clamp(1.2rem, 1.6vw, 1.6rem) !important;
    border-radius: 16px !important;
    background: var(--slab-surface) !important;
    border: 1px solid var(--slab-border) !important;
    border-top-color: var(--slab-highlight) !important;
    border-left-color: rgba(202, 239, 231, 0.28) !important;
    box-shadow: var(--slab-shadow) !important;
    backdrop-filter: blur(26px) saturate(125%) !important;
    -webkit-backdrop-filter: blur(26px) saturate(125%) !important;
    box-sizing: border-box !important;
    position: relative !important;
    overflow: hidden !important;
}

.review-card-google .google-review-header {
    display: flex !important;
    align-items: center !important;
    justify-content: space-between !important;
    flex-wrap: wrap !important;
    gap: 0.75rem !important;
    padding-bottom: 1.1rem !important;
    margin-bottom: 1.1rem !important;
    border-bottom: 1px solid rgba(214, 183, 124, 0.15) !important;
}

.review-card-google .google-badge-left {
    display: flex !important;
    align-items: center !important;
    gap: 0.65rem !important;
}

.review-card-google .google-title {
    font-size: 0.82rem !important;
    text-transform: uppercase !important;
    letter-spacing: 1px !important;
    color: var(--text-muted) !important;
    font-weight: 600 !important;
}

.review-card-google .google-score {
    font-size: 1.15rem !important;
    font-weight: 700 !important;
    color: #fff !important;
}

.review-card-google .google-stars {
    color: #fbbf24 !important;
    font-size: 0.95rem !important;
    letter-spacing: 1px !important;
}

.review-card-google .google-maps-btn {
    display: inline-flex !important;
    align-items: center !important;
    gap: 0.4rem !important;
    font-size: 0.76rem !important;
    text-transform: uppercase !important;
    letter-spacing: 1px !important;
    color: var(--accent-main) !important;
    text-decoration: none !important;
    border: 1px solid rgba(214, 183, 124, 0.35) !important;
    padding: 0.35rem 0.75rem !important;
    border-radius: 20px !important;
    background: rgba(214, 183, 124, 0.08) !important;
    transition: all 0.3s ease !important;
}

.review-card-google .google-maps-btn:hover {
    background: rgba(214, 183, 124, 0.2) !important;
    color: #fff !important;
    border-color: var(--accent-main) !important;
}

.google-reviews-carousel {
    position: relative !important;
    flex: 1 !important;
    display: flex !important;
    flex-direction: column !important;
    justify-content: center !important;
}

.google-review-slide {
    display: none !important;
    animation: fadeInSlide 0.45s cubic-bezier(0.16, 1, 0.3, 1) forwards !important;
}

.google-review-slide.is-active {
    display: block !important;
}

.review-meta {
    display: flex !important;
    align-items: center !important;
    gap: 0.85rem !important;
    margin-bottom: 0.9rem !important;
}

.reviewer-avatar {
    width: 42px !important;
    height: 42px !important;
    border-radius: 50% !important;
    background: linear-gradient(135deg, #1d4ed8, #0284c7) !important;
    color: #fff !important;
    font-size: 0.95rem !important;
    font-weight: 700 !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3) !important;
    flex-shrink: 0 !important;
}

.reviewer-info {
    flex: 1 !important;
}

.reviewer-name {
    font-size: 1rem !important;
    font-weight: 600 !important;
    color: #fff !important;
    margin-bottom: 0.15rem !important;
}

.review-date {
    font-size: 0.76rem !important;
    color: var(--text-muted) !important;
}

.review-stars-single {
    color: #fbbf24 !important;
    font-size: 0.95rem !important;
    letter-spacing: 1px !important;
}

.review-body {
    font-size: 0.96rem !important;
    color: var(--text-primary) !important;
    line-height: 1.65 !important;
    font-style: italic !important;
    margin-top: 0.6rem !important;
}

.carousel-nav {
    display: flex !important;
    justify-content: center !important;
    align-items: center !important;
    gap: 12px !important;
    margin-top: 1.4rem !important;
    padding-top: 0.8rem !important;
    border-top: 1px solid rgba(255, 255, 255, 0.08) !important;
}

.carousel-dot {
    width: 28px !important;
    height: 6px !important;
    border-radius: 3px !important;
    background: rgba(255, 255, 255, 0.2) !important;
    border: none !important;
    cursor: pointer !important;
    transition: all 0.35s ease !important;
    padding: 0 !important;
}

.carousel-dot.is-active {
    width: 42px !important;
    background: var(--accent-main) !important;
    box-shadow: 0 0 10px rgba(214, 183, 124, 0.6) !important;
}

/* Review Card 2: Institutional Testimonial in Portrait */
.review-card-direct .review-source {
    font-size: 0.78rem !important;
    text-transform: uppercase !important;
    letter-spacing: 1.5px !important;
    color: var(--accent-main) !important;
    margin-bottom: 0.75rem !important;
    display: flex !important;
    align-items: center !important;
    gap: 8px !important;
    padding-bottom: 0.85rem !important;
    border-bottom: 1px solid rgba(214, 183, 124, 0.15) !important;
}

.review-card-direct .review-stars {
    color: #fbbf24 !important;
    font-size: 1.1rem !important;
    letter-spacing: 2px !important;
    margin-bottom: 1rem !important;
}

.review-card-direct .review-text {
    font-family: 'Cormorant Garamond', Georgia, serif !important;
    font-size: 1.35rem !important;
    font-style: italic !important;
    color: var(--text-primary) !important;
    line-height: 1.6 !important;
    flex: 1 !important;
    display: flex !important;
    align-items: center !important;
}

.direct-client-footer {
    margin-top: 1.4rem !important;
    padding-top: 0.8rem !important;
    border-top: 1px solid rgba(255, 255, 255, 0.08) !important;
    display: flex !important;
    align-items: center !important;
    gap: 0.85rem !important;
}
"""

css += "\n" + cursor_and_review_css

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("SUCCESS: Updated css/style.css with portrait review boxes and cursor animation styles.")

with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Remove any .ambient-cosmos-canvas { display: none !important }
css = css.replace('.ambient-cosmos-canvas{display:none !important}', '.ambient-cosmos-canvas{display:block !important}')
css = css.replace('.ambient-cosmos-canvas { display: none !important; }', '.ambient-cosmos-canvas { display: block !important; }')

mobile_bg_and_opt_css = """
/* ==========================================================================
   GLOBAL LIVING AMBIENT BACKGROUND ANIMATION (MOBILE + DESKTOP UNIFIED)
   ========================================================================== */
.global-ambient-system {
    position: fixed !important;
    inset: 0 !important;
    width: 100vw !important;
    height: 100vh !important;
    pointer-events: none !important;
    z-index: 0 !important;
    overflow: hidden !important;
    opacity: 1 !important;
    transform: translateZ(0) !important;
    animation: ambientBreathePulse 10s cubic-bezier(0.42, 0, 0.58, 1) infinite alternate !important;
}

.ambient-layer {
    position: absolute !important;
    border-radius: 50% !important;
    filter: blur(60px) !important;
    mix-blend-mode: screen !important;
    pointer-events: none !important;
    will-change: transform, opacity !important;
}

.ambient-blob-1 {
    width: clamp(380px, 75vw, 900px) !important;
    height: clamp(380px, 75vw, 900px) !important;
    top: 5% !important;
    left: -10% !important;
    background: radial-gradient(circle at 45% 45%, rgba(45, 120, 225, 0.52) 0%, rgba(20, 56, 125, 0.26) 45%, transparent 72%) !important;
    animation: globalDrift1 26s cubic-bezier(0.4, 0, 0.6, 1) infinite alternate, blobGlowPulse1 8s ease-in-out infinite alternate !important;
}

.ambient-blob-2 {
    width: clamp(360px, 70vw, 850px) !important;
    height: clamp(360px, 70vw, 850px) !important;
    top: 35% !important;
    right: -8% !important;
    background: radial-gradient(circle at 50% 50%, rgba(223, 179, 93, 0.42) 0%, rgba(197, 168, 112, 0.18) 45%, transparent 70%) !important;
    animation: globalDrift2 28s cubic-bezier(0.4, 0, 0.6, 1) infinite alternate, blobGlowPulse2 8.5s ease-in-out infinite alternate !important;
}

.ambient-blob-3 {
    width: clamp(400px, 80vw, 950px) !important;
    height: clamp(400px, 80vw, 950px) !important;
    top: 65% !important;
    left: -5% !important;
    background: radial-gradient(circle at 45% 45%, rgba(30, 150, 185, 0.48) 0%, rgba(16, 75, 105, 0.22) 50%, transparent 74%) !important;
    animation: globalDrift3 30s cubic-bezier(0.4, 0, 0.6, 1) infinite alternate, blobGlowPulse3 9s ease-in-out infinite alternate !important;
}

.ambient-blob-4 {
    width: clamp(340px, 68vw, 800px) !important;
    height: clamp(340px, 68vw, 800px) !important;
    top: 20% !important;
    right: 15% !important;
    background: radial-gradient(circle at 50% 50%, rgba(244, 208, 138, 0.35) 0%, rgba(186, 102, 90, 0.15) 48%, transparent 70%) !important;
    animation: globalDrift4 24s cubic-bezier(0.4, 0, 0.6, 1) infinite alternate, blobGlowPulse4 7.5s ease-in-out infinite alternate !important;
}

.ambient-cosmos-canvas {
    position: fixed !important;
    inset: 0 !important;
    width: 100vw !important;
    height: 100vh !important;
    pointer-events: none !important;
    opacity: 0.72 !important;
    display: block !important;
    z-index: 1 !important;
}

/* Ensure all content layers sit crisply above ambient canvas */
main, section, header, nav, footer, .site-footer {
    position: relative !important;
    z-index: 2 !important;
}

/* ==========================================================================
   MOBILE VIEW OPTIMIZATION ENHANCEMENTS (<= 900px & <= 480px)
   ========================================================================== */
@media (max-width: 900px) {
    .ambient-layer {
        filter: blur(45px) !important;
    }
    
    .ambient-cosmos-canvas {
        display: block !important;
        opacity: 0.7 !important;
    }

    /* Container & Section Padding */
    .section-container,
    section {
        padding-left: clamp(1rem, 4vw, 2rem) !important;
        padding-right: clamp(1rem, 4vw, 2rem) !important;
    }

    /* Hero Typography */
    .hero-title {
        font-size: clamp(2.2rem, 8.5vw, 3.4rem) !important;
        line-height: 1.15 !important;
    }

    .hero-subtitle {
        font-size: clamp(1rem, 3.8vw, 1.25rem) !important;
        margin-bottom: 2rem !important;
    }

    /* Banner Stats on Mobile */
    .banner-stats {
        width: 100% !important;
        max-width: 100% !important;
        padding: 1.5rem 1rem !important;
        display: grid !important;
        grid-template-columns: repeat(2, 1fr) !important;
        gap: 1.25rem 0.85rem !important;
    }

    .stat-item {
        min-width: 0 !important;
    }

    .stat-value {
        font-size: 2rem !important;
    }

    .stat-label {
        font-size: 0.7rem !important;
        letter-spacing: 1px !important;
    }

    /* Central Contact Banner on Mobile */
    .central-contact-banner {
        flex-direction: column !important;
        align-items: stretch !important;
        gap: 0.85rem !important;
        padding: 1.2rem 1rem !important;
    }

    .contact-pill {
        justify-content: center !important;
        width: 100% !important;
    }

    /* Office Cards Mobile */
    .contact-grid {
        grid-template-columns: 1fr !important;
        gap: 1.5rem !important;
    }

    .contact-grid > .office-card-1,
    .contact-grid > .office-card-2 {
        max-width: 100% !important;
        min-height: auto !important;
    }

    /* Reviews Grid Mobile */
    .reviews-grid {
        grid-template-columns: 1fr !important;
        gap: 1.5rem !important;
    }

    .reviews-grid > .review-card {
        max-width: 100% !important;
        min-height: auto !important;
    }

    /* Navigation */
    .site-nav {
        padding: max(0.4rem, env(safe-area-inset-top)) 0.5rem 0.4rem !important;
    }

    .nav-links {
        padding: 0.25rem 0.5rem 0.4rem !important;
        gap: 0.45rem !important;
    }
}

@media (max-width: 480px) {
    .banner-stats {
        grid-template-columns: 1fr 1fr !important;
        gap: 1rem 0.6rem !important;
        padding: 1.2rem 0.8rem !important;
    }

    .stat-value {
        font-size: 1.75rem !important;
    }

    .office-name {
        font-size: 1.6rem !important;
    }

    .contact-grid .action-buttons {
        grid-template-columns: 1fr !important;
        gap: 0.65rem !important;
    }

    .contact-grid .action-buttons .btn {
        width: 100% !important;
    }
}
"""

css += "\n" + mobile_bg_and_opt_css

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("SUCCESS: Enabled desktop background animation on mobile and applied mobile optimizations to css/style.css!")

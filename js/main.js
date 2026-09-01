/**
 * Ramyachandra Gunasekera Chambers — Main Interactive Logic
 * High-Performance, Zero-Console-Errors, Accessible Suite
 */

document.addEventListener('DOMContentLoaded', () => {
    // 1. Email Protection / Anti-Scraping Hydration
    document.querySelectorAll('.protected-email').forEach(el => {
        const u = el.getAttribute('data-user') || 'ramyachandra';
        const d = el.getAttribute('data-domain') || 'sltnet.lk';
        el.href = `mailto:${u}@${d}`;
        el.textContent = `${u}@${d}`;
    });

    // 2. Navigation Highlighting & Smooth Scrolling
    const navLinks = [...document.querySelectorAll('.nav-link')];
    const sections = [...document.querySelectorAll('section')];
    const navEl = document.querySelector('nav.site-nav') || document.querySelector('nav');

    function setActiveNav(targetId) {
        if (!navLinks.length) return;
        navLinks.forEach(link => {
            const linkTarget = link.getAttribute('data-target') || link.getAttribute('href') || '';
            const isActive = linkTarget === `#${targetId}` || linkTarget === `${targetId}.html` || (targetId === 'home' && (linkTarget === '/' || linkTarget === 'index.html'));
            link.classList.toggle('active', isActive);
            if (isActive && window.innerWidth <= 900) {
                try {
                    link.scrollIntoView({ behavior: 'smooth', inline: 'center', block: 'nearest' });
                } catch (err) {}
            }
        });
    }

    if (navLinks.length) {
        navLinks.forEach(link => {
            link.addEventListener('click', e => {
                const targetSelector = link.getAttribute('data-target');
                if (targetSelector) {
                    const targetEl = document.querySelector(targetSelector);
                    if (targetEl) {
                        e.preventDefault();
                        const navHeight = navEl ? navEl.offsetHeight : (window.innerWidth <= 600 ? 92 : 74);
                        const targetTop = Math.max(0, targetEl.offsetTop - navHeight - 12);
                        window.scrollTo({ top: targetTop, behavior: 'smooth' });
                        const pageName = link.getAttribute('data-page') || targetSelector.replace('#', '') + '.html';
                        history.pushState(null, '', pageName === 'home.html' ? 'index.html' : pageName);
                        setActiveNav(targetEl.id);
                    }
                }
            });
        });

        let scrollTicking = false;
        window.addEventListener('scroll', () => {
            if (scrollTicking) return;
            scrollTicking = true;
            requestAnimationFrame(() => {
                if (navEl) {
                    navEl.classList.toggle('scrolled', window.scrollY > 30);
                }
                if (sections.length) {
                    const navHeight = navEl ? navEl.offsetHeight : (window.innerWidth <= 600 ? 92 : 74);
                    const marker = window.scrollY + navHeight + 80;
                    let current = sections[0]?.id || 'home';
                    sections.forEach(section => {
                        if (marker >= section.offsetTop) {
                            current = section.id;
                        }
                    });
                    setActiveNav(current);
                }
                scrollTicking = false;
            });
        }, { passive: true });
    }

    // 3. Counter Rolling Cadence
    const stats = [...document.querySelectorAll('.stat-value[data-target]')];
    if (stats.length) {
        if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
            stats.forEach(el => {
                const target = el.getAttribute('data-target');
                const suffix = el.getAttribute('data-suffix') || '';
                el.textContent = target + suffix;
            });
        } else {
            const duration = 2400;
            const restDuration = 3000;
            const timerEase = (t) => t < 0.5 ? 2 * t * t : 1 - Math.pow(-2 * t + 2, 2) / 2;

            let isVisible = true;
            let currentRaf = null;

            const runCountCycle = () => {
                stats.forEach(el => {
                    const suffix = el.getAttribute('data-suffix') || '';
                    el.textContent = '0' + suffix;
                });

                const startTime = performance.now();
                let lastVals = new Map();

                const step = (currentTime) => {
                    const elapsed = currentTime - startTime;
                    const progress = Math.min(elapsed / duration, 1);
                    const ease = timerEase(progress);

                    stats.forEach(el => {
                        const target = parseInt(el.getAttribute('data-target'), 10) || 0;
                        const suffix = el.getAttribute('data-suffix') || '';
                        let currentVal = Math.round(target * ease);
                        if (progress >= 1) currentVal = target;

                        if (lastVals.get(el) !== currentVal) {
                            lastVals.set(el, currentVal);
                            el.textContent = currentVal + suffix;
                        }
                    });

                    if (progress < 1) {
                        currentRaf = requestAnimationFrame(step);
                    } else {
                        stats.forEach(el => {
                            const target = el.getAttribute('data-target');
                            const suffix = el.getAttribute('data-suffix') || '';
                            el.textContent = target + suffix;
                        });
                        setTimeout(() => {
                            if (isVisible) runCountCycle();
                        }, restDuration);
                    }
                };
                currentRaf = requestAnimationFrame(step);
            };

            const statsObserver = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    isVisible = entry.isIntersecting;
                    if (isVisible && !currentRaf) runCountCycle();
                });
            }, { threshold: 0.2 });

            const statsBanner = document.querySelector('.banner-stats');
            if (statsBanner) statsObserver.observe(statsBanner);
            else runCountCycle();
        }
    }

    // 4. World Map Active Pin Cycling (35 Sovereign Jurisdictions)
    const pins = [...document.querySelectorAll('.map-pin')];
    if (pins.length) {
                const cohorts = [
            ['pin-usa', 'pin-singapore', 'pin-portugal', 'pin-germany', 'pin-norway'],
            ['pin-japan', 'pin-india', 'pin-zanzibar', 'pin-austria', 'pin-uk'],
            ['pin-australia', 'pin-mali', 'pin-switzerland', 'pin-sweden', 'pin-romania'],
            ['pin-china', 'pin-srilanka', 'pin-israel', 'pin-greece', 'pin-netherlands'],
            ['pin-nz', 'pin-bangladesh', 'pin-malta', 'pin-ireland', 'pin-luxembourg'],
            ['pin-korea', 'pin-maldives', 'pin-uae', 'pin-belgium', 'pin-latvia'],
            ['pin-malaysia', 'pin-italy', 'pin-france', 'pin-denmark', 'pin-slovakia']
        ];
        let cohortIndex = 0;
        let stepTimers = [];
        let mainTimer = null;
        let isRunning = false;

        const clearAllActivePins = () => pins.forEach(p => p.classList.remove('active'));
        const clearStepTimers = () => {
            stepTimers.forEach(t => clearTimeout(t));
            stepTimers = [];
        };

        const runSequence = () => {
            clearStepTimers();
            clearAllActivePins();
            const currentCohort = cohorts[cohortIndex];
            if (!currentCohort) return;

            currentCohort.forEach((id, idx) => {
                stepTimers.push(setTimeout(() => {
                    const el = document.getElementById(id);
                    if (el) el.classList.add('active');
                }, idx * 500));
            });

            stepTimers.push(setTimeout(clearAllActivePins, 2500));
            cohortIndex = (cohortIndex + 1) % cohorts.length;
            mainTimer = setTimeout(runSequence, 3000);
        };

        const startPins = () => {
            if (isRunning) return;
            isRunning = true;
            runSequence();
        };
        const stopPins = () => {
            isRunning = false;
            if (mainTimer) clearTimeout(mainTimer);
            mainTimer = null;
            clearStepTimers();
            clearAllActivePins();
        };

        startPins();
        document.addEventListener('visibilitychange', () => {
            if (document.hidden) stopPins();
            else startPins();
        });
    }

    // 5. Testimonial / Google Reviews Carousel
    const slides = [...document.querySelectorAll('.google-review-slide')];
    const dots = [...document.querySelectorAll('.carousel-dot')];
    if (slides.length) {
        let currentIndex = 0;
        let reviewTimer = null;

        const goToSlide = (index) => {
            slides.forEach((s, idx) => s.classList.toggle('is-active', idx === index));
            dots.forEach((d, idx) => d.classList.toggle('is-active', idx === index));
            currentIndex = index;
        };
        const nextSlide = () => {
            goToSlide((currentIndex + 1) % slides.length);
        };
        const resetTimer = () => {
            if (reviewTimer) clearInterval(reviewTimer);
            reviewTimer = setInterval(nextSlide, 6000);
        };

        dots.forEach((dot, idx) => {
            dot.addEventListener('click', () => {
                goToSlide(idx);
                resetTimer();
            });
        });
        resetTimer();
    }

        // 6. Practice Areas / Services Accordion Cards
    const serviceGrid = document.querySelector('.services-grid');
    const serviceCards = [...document.querySelectorAll('.service-card')];

    function setServiceState(card, open) {
        if (!card) return;
        const content = card.querySelector('.accordion-content');
        const header = card.querySelector('.accordion-header');
        const arrow = card.querySelector('.arrow-icon');
        if (!content) return;
        card.classList.toggle('is-open', open);
        if (header) header.setAttribute('aria-expanded', String(open));
        content.style.maxHeight = open ? `${content.scrollHeight + 60}px` : '0px';
        if (arrow) arrow.style.transform = open ? 'rotate(180deg)' : 'rotate(0deg)';
    }

    function getServiceRow(card) {
        if (!serviceGrid) return [card];
        const columnCount = Math.max(1, getComputedStyle(serviceGrid).gridTemplateColumns.split(' ').filter(Boolean).length);
        const cardIndex = serviceCards.indexOf(card);
        const rowStart = Math.floor(cardIndex / columnCount) * columnCount;
        return serviceCards.slice(rowStart, rowStart + columnCount);
    }

    window.toggleAccordion = function(element) {
        const card = element ? element.closest('.service-card') : null;
        if (!card) return;
        const isOpen = card.classList.contains('is-open');

        if (window.innerWidth <= 900) {
            // Mobile & Tablet: single card toggle
            serviceCards.forEach(c => {
                if (c !== card) setServiceState(c, false);
            });
            setServiceState(card, !isOpen);
        } else {
            // Desktop: toggle row
            const row = getServiceRow(card);
            const rowIsOpen = row.length > 0 && row.every(rc => rc.classList.contains('is-open'));
            if (rowIsOpen) {
                row.forEach(rc => setServiceState(rc, false));
                if (serviceGrid && !serviceCards.some(c => c.classList.contains('is-open'))) {
                    serviceGrid.classList.remove('row-open');
                }
            } else {
                if (serviceGrid) serviceGrid.classList.add('row-open');
                row.forEach(rc => setServiceState(rc, true));
            }
        }
    };

    if (serviceCards.length) {
        serviceCards.forEach(card => {
            const header = card.querySelector('.accordion-header');
            if (!header) return;
            header.setAttribute('role', 'button');
            header.setAttribute('tabindex', '0');
            header.setAttribute('aria-expanded', 'false');
            header.addEventListener('click', (e) => {
                e.preventDefault();
                e.stopPropagation();
                window.toggleAccordion(header);
            });
            header.addEventListener('keydown', (e) => {
                if (e.key === 'Enter' || e.key === ' ') {
                    e.preventDefault();
                    e.stopPropagation();
                    window.toggleAccordion(header);
                }
            });
        });

        document.addEventListener('keydown', event => {
            if (event.key === 'Escape') {
                serviceCards.forEach(card => setServiceState(card, false));
                if (serviceGrid) serviceGrid.classList.remove('row-open');
            }
        });

        window.addEventListener('resize', () => {
            serviceCards.filter(card => card.classList.contains('is-open')).forEach(card => {
                const content = card.querySelector('.accordion-content');
                if (content) content.style.maxHeight = `${content.scrollHeight + 60}px`;
            });
        }, { passive: true });
    }

    // 7. Scroll Reveal Animation
    if ('IntersectionObserver' in window) {
        const revealObserver = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('active');
                    observer.unobserve(entry.target);
                }
            });
        }, {
            rootMargin: '0px 0px -20px 0px',
            threshold: 0.05
        });
        document.querySelectorAll('.reveal').forEach(el => revealObserver.observe(el));
    } else {
        document.querySelectorAll('.reveal').forEach(el => el.classList.add('active'));
    }

    // 8. Legal Modals Handler
    const openPrivacy = document.getElementById('open-privacy-link');
    const openTerms = document.getElementById('open-terms-link');
    const privacyModal = document.getElementById('privacy-modal');
    const termsModal = document.getElementById('terms-modal');

    function openModal(modal) {
        if (!modal) return;
        modal.classList.add('is-open');
        modal.setAttribute('aria-hidden', 'false');
        document.body.style.overflow = 'hidden';
    }
    function closeModal(modal) {
        if (!modal) return;
        modal.classList.remove('is-open');
        modal.setAttribute('aria-hidden', 'true');
        document.body.style.overflow = '';
    }

    if (openPrivacy) openPrivacy.addEventListener('click', (e) => { e.preventDefault(); openModal(privacyModal); });
    if (openTerms) openTerms.addEventListener('click', (e) => { e.preventDefault(); openModal(termsModal); });

    [privacyModal, termsModal].forEach(modal => {
        if (!modal) return;
        modal.addEventListener('click', (e) => {
            if (e.target === modal || e.target.classList.contains('legal-modal-close')) {
                closeModal(modal);
            }
        });
    });

    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') {
            closeModal(privacyModal);
            closeModal(termsModal);
        }
    });

    // 9. Stardust Ambient Canvas (Hero Cosmos)
    const canvas = document.getElementById('ambient-cosmos-canvas');
    if (canvas && !window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
        const ctx = canvas.getContext('2d', { alpha: true });
        if (ctx) {
            let width = 0, height = 0;
            let particles = [];
            let animId = 0;
            let mouseX = -1000, mouseY = -1000;
            const isMobile = window.innerWidth <= 768;
            const particleCount = isMobile ? 24 : 40;

            const resize = () => {
                width = canvas.width = window.innerWidth;
                height = canvas.height = window.innerHeight;
            };
            resize();
            window.addEventListener('resize', resize, { passive: true });

            class StardustParticle {
                constructor() { this.reset(true); }
                reset(initial = false) {
                    this.x = Math.random() * width;
                    this.y = initial ? Math.random() * height : height + 10;
                    this.baseSize = Math.random() * 1.5 + 1.0;
                    this.size = this.baseSize;
                    this.vx = (Math.random() - 0.5) * 0.22;
                    this.vy = -(Math.random() * 0.28 + 0.14);
                    this.alpha = Math.random() * 0.40 + 0.35;
                    this.pulseSpeed = Math.random() * 0.022 + 0.010;
                    this.pulsePhase = Math.random() * Math.PI * 2;
                    const colors = ['rgba(223, 179, 93, ', 'rgba(244, 208, 138, ', 'rgba(202, 239, 231, ', 'rgba(255, 255, 255, '];
                    this.colorPrefix = colors[Math.floor(Math.random() * colors.length)];
                }
                update(scrollDelta) {
                    this.pulsePhase += this.pulseSpeed;
                    const pulse = Math.sin(this.pulsePhase) * 0.15;
                    this.currentAlpha = Math.max(0.15, Math.min(0.85, this.alpha + pulse));
                    this.x += this.vx;
                    this.y += this.vy - (scrollDelta * 0.08);
                    if (this.y < -15) this.y = height + 10;
                    else if (this.y > height + 15) this.y = -10;
                    if (this.x < -15) this.x = width + 10;
                    else if (this.x > width + 15) this.x = -10;
                }
                draw() {
                    ctx.save();
                    ctx.beginPath();
                    ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
                    ctx.fillStyle = this.colorPrefix + this.currentAlpha + ')';
                    ctx.fill();
                    ctx.restore();
                }
            }

            for (let i = 0; i < particleCount; i++) particles.push(new StardustParticle());

            let isTabActive = true;
            let scrollDelta = 0;
            let lastScrollY = 0;

            window.addEventListener('scroll', () => {
                const nowY = window.pageYOffset || document.documentElement.scrollTop || 0;
                scrollDelta = nowY - lastScrollY;
                lastScrollY = nowY;
            }, { passive: true });

            document.addEventListener('visibilitychange', () => {
                isTabActive = !document.hidden;
                if (isTabActive) {
                    scrollDelta = 0;
                    renderCosmos();
                } else {
                    cancelAnimationFrame(animId);
                }
            });

            const renderCosmos = () => {
                if (!isTabActive) return;
                const delta = scrollDelta;
                scrollDelta = 0;
                ctx.clearRect(0, 0, width, height);
                for (let i = 0; i < particles.length; i++) {
                    particles[i].update(delta);
                    particles[i].draw();
                }
                animId = requestAnimationFrame(renderCosmos);
            };
            renderCosmos();
        }
    }

    // 10. Service Worker Registration for Instant Load & PWA Offline Caching
    if ('serviceWorker' in navigator) {
        window.addEventListener('load', () => {
            navigator.serviceWorker.register('/sw.js').catch(() => {});
        });
    }
});

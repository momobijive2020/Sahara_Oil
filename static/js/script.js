/* =========================================
   SAHARA OIL TRADING S.A. — JavaScript (application Flask)
   ========================================= */

(function () {
  'use strict';

  /* ---- Preloader ---- */
  window.addEventListener('load', () => {
    setTimeout(() => {
      const preloader = document.getElementById('preloader');
      if (preloader) {
        preloader.classList.add('hidden');
        setTimeout(() => preloader.remove(), 600);
      }
    }, 2200);
  });

  /* ---- Particle System ---- */
  function initParticles() {
    const container = document.getElementById('heroParticles');
    if (!container) return;
    const count = 25;
    for (let i = 0; i < count; i++) {
      const p = document.createElement('div');
      p.classList.add('particle');
      const size = Math.random() * 4 + 2;
      p.style.cssText = `
        left: ${Math.random() * 100}%;
        width: ${size}px;
        height: ${size}px;
        animation-duration: ${Math.random() * 15 + 10}s;
        animation-delay: ${Math.random() * 10}s;
        opacity: 0;
      `;
      container.appendChild(p);
    }
  }
  initParticles();

  /* ---- Sticky Navigation ---- */
  const header = document.getElementById('header');
  const backToTop = document.getElementById('backToTop');

  window.addEventListener('scroll', () => {
    const scrollY = window.scrollY;

    // Sticky header
    if (scrollY > 50) {
      header.classList.add('scrolled');
    } else {
      header.classList.remove('scrolled');
    }

    // Back to top
    if (scrollY > 400) {
      backToTop.classList.add('visible');
    } else {
      backToTop.classList.remove('visible');
    }

    // Active nav link
    updateActiveNavLink();
  });

  /* ---- Active Nav Link ---- */
  function updateActiveNavLink() {
    const sections = ['accueil', 'apropos', 'services', 'produits', 'qhse', 'chiffres', 'contact'];
    const scrollY = window.scrollY + 120;

    for (const id of sections) {
      const section = document.getElementById(id);
      const link = document.getElementById('link-' + id);
      if (!section || !link) continue;

      const top = section.offsetTop;
      const bottom = top + section.offsetHeight;

      if (scrollY >= top && scrollY < bottom) {
        document.querySelectorAll('.nav-link').forEach(l => l.classList.remove('active'));
        link.classList.add('active');
        break;
      }
    }
  }

  /* ---- Mobile Nav Toggle ---- */
  const navToggle = document.getElementById('navToggle');
  const navLinks = document.getElementById('navLinks');

  if (navToggle && navLinks) {
    navToggle.addEventListener('click', () => {
      const isOpen = navLinks.classList.toggle('open');
      navToggle.setAttribute('aria-expanded', isOpen);

      // Animate hamburger
      const spans = navToggle.querySelectorAll('span');
      if (isOpen) {
        spans[0].style.transform = 'rotate(45deg) translate(5px, 5px)';
        spans[1].style.opacity = '0';
        spans[2].style.transform = 'rotate(-45deg) translate(5px, -5px)';
      } else {
        spans[0].style.transform = '';
        spans[1].style.opacity = '';
        spans[2].style.transform = '';
      }
    });

    // Close on nav link click
    navLinks.querySelectorAll('.nav-link').forEach(link => {
      link.addEventListener('click', () => {
        navLinks.classList.remove('open');
        const spans = navToggle.querySelectorAll('span');
        spans[0].style.transform = '';
        spans[1].style.opacity = '';
        spans[2].style.transform = '';
      });
    });

    // Close on outside click
    document.addEventListener('click', (e) => {
      if (!header.contains(e.target)) {
        navLinks.classList.remove('open');
        const spans = navToggle.querySelectorAll('span');
        spans[0].style.transform = '';
        spans[1].style.opacity = '';
        spans[2].style.transform = '';
      }
    });
  }

  /* ---- Back to Top ---- */
  if (backToTop) {
    backToTop.addEventListener('click', () => {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }

  /* ---- Smooth Scroll for all anchor links ---- */
  document.querySelectorAll('a[href^="#"]').forEach(link => {
    link.addEventListener('click', (e) => {
      const href = link.getAttribute('href');
      if (href === '#') return;
      const target = document.querySelector(href);
      if (target) {
        e.preventDefault();
        target.scrollIntoView({ behavior: 'smooth' });
      }
    });
  });

  /* ---- Intersection Observer: Reveal Animations ---- */
  function addRevealClasses() {
    // About section
    const aboutVisual = document.querySelector('.about-visual');
    const aboutContent = document.querySelector('.about-content');
    if (aboutVisual) aboutVisual.classList.add('reveal-left');
    if (aboutContent) aboutContent.classList.add('reveal-right');

    // Service cards
    document.querySelectorAll('.service-card').forEach((el, i) => {
      el.classList.add('reveal');
      el.style.transitionDelay = `${i * 0.12}s`;
    });

    // Product cards
    document.querySelectorAll('.product-card').forEach((el, i) => {
      el.classList.add('reveal');
      el.style.transitionDelay = `${i * 0.06}s`;
    });

    // Stat cards
    document.querySelectorAll('.stat-card').forEach((el, i) => {
      el.classList.add('reveal');
      el.style.transitionDelay = `${i * 0.1}s`;
    });

    // Why cards
    document.querySelectorAll('.why-card').forEach((el, i) => {
      el.classList.add('reveal');
      el.style.transitionDelay = `${i * 0.08}s`;
    });

    // QHSE cards
    document.querySelectorAll('.qhse-card').forEach((el, i) => {
      el.classList.add('reveal');
      el.style.transitionDelay = `${i * 0.07}s`;
    });

    // QHSE intro
    const qhseIntro = document.querySelector('.qhse-intro');
    if (qhseIntro) qhseIntro.classList.add('reveal');

    const qhseCta = document.querySelector('.qhse-cta');
    if (qhseCta) qhseCta.classList.add('reveal');

    // Contact grid items
    document.querySelectorAll('.contact-item').forEach((el, i) => {
      el.classList.add('reveal');
      el.style.transitionDelay = `${i * 0.08}s`;
    });

    // Section headers
    document.querySelectorAll('.section-header').forEach(el => {
      el.classList.add('reveal');
    });
  }

  addRevealClasses();

  const revealObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        revealObserver.unobserve(entry.target);
      }
    });
  }, {
    threshold: 0.1,
    rootMargin: '0px 0px -60px 0px'
  });

  document.querySelectorAll('.reveal, .reveal-left, .reveal-right').forEach(el => {
    revealObserver.observe(el);
  });

  /* ---- Counter Animation ---- */
  function animateCounter(el) {
    const target = parseInt(el.dataset.target, 10);
    const suffix = el.dataset.suffix || '';
    const duration = 2000;
    const start = performance.now();

    function update(timestamp) {
      const elapsed = timestamp - start;
      const progress = Math.min(elapsed / duration, 1);
      // easeOutExpo
      const eased = progress === 1 ? 1 : 1 - Math.pow(2, -10 * progress);
      const value = Math.floor(eased * target);
      el.textContent = value + suffix;
      if (progress < 1) {
        requestAnimationFrame(update);
      } else {
        el.textContent = target + suffix;
      }
    }

    requestAnimationFrame(update);
  }

  const statsObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const counters = entry.target.querySelectorAll('.stat-number[data-target]');
        counters.forEach(counter => animateCounter(counter));
        statsObserver.unobserve(entry.target);
      }
    });
  }, { threshold: 0.3 });

  const statsSection = document.getElementById('chiffres');
  if (statsSection) statsObserver.observe(statsSection);

  /* ---- Contact Form (envoi réel vers l'API Flask) ---- */
  const contactForm = document.getElementById('contactForm');
  const formSuccess = document.getElementById('formSuccess');

  const ERROR_COLOR = 'hsl(0, 70%, 50%)';

  function clearFieldErrors(form) {
    form.querySelectorAll('.field-error').forEach(el => el.remove());
    form.querySelectorAll('input, select, textarea').forEach(field => {
      field.style.borderColor = '';
    });
  }

  function showFieldError(form, name, message) {
    const field = form.querySelector(`[name="${name}"]`);
    if (!field) return;
    field.style.borderColor = ERROR_COLOR;

    const hint = document.createElement('p');
    hint.className = 'field-error';
    hint.textContent = message;
    hint.style.cssText = `color:${ERROR_COLOR};font-size:0.82rem;margin:0.35rem 0 0;`;
    (field.parentElement || form).appendChild(hint);

    field.addEventListener('input', () => {
      field.style.borderColor = '';
      hint.remove();
    }, { once: true });
  }

  function showSuccess(message) {
    if (!formSuccess) return;
    const paragraph = formSuccess.querySelector('p');
    if (paragraph && message) paragraph.textContent = message;
    formSuccess.style.display = 'block';
    setTimeout(() => { formSuccess.style.display = 'none'; }, 6000);
  }

  if (contactForm) {
    contactForm.addEventListener('submit', async (e) => {
      e.preventDefault();
      clearFieldErrors(contactForm);

      const btn = document.getElementById('submitContactBtn');
      const originalHTML = btn.innerHTML;
      btn.innerHTML = '<span>Envoi en cours...</span>';
      btn.disabled = true;

      const payload = Object.fromEntries(new FormData(contactForm).entries());

      try {
        const response = await fetch(contactForm.action || '/api/contact', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
          },
          body: JSON.stringify(payload)
        });

        const result = await response.json().catch(() => ({}));

        if (response.ok && result.ok) {
          contactForm.reset();
          showSuccess(result.message);
        } else if (result.errors) {
          Object.entries(result.errors).forEach(([field, message]) => {
            showFieldError(contactForm, field, message);
          });
          const firstField = contactForm.querySelector('.field-error');
          if (firstField) firstField.scrollIntoView({ behavior: 'smooth', block: 'center' });
        } else {
          showFieldError(contactForm, 'message',
            result.error || "Une erreur est survenue. Merci de réessayer.");
        }
      } catch (err) {
        console.error('Échec de l\'envoi du formulaire :', err);
        showFieldError(contactForm, 'message',
          'Serveur injoignable. Vérifiez votre connexion puis réessayez.');
      } finally {
        btn.innerHTML = originalHTML;
        btn.disabled = false;
      }
    });
  }

  /* ---- Ticker pause on hover ---- */
  const tickerContent = document.querySelector('.ticker-content');
  if (tickerContent) {
    tickerContent.addEventListener('mouseenter', () => {
      tickerContent.style.animationPlayState = 'paused';
    });
    tickerContent.addEventListener('mouseleave', () => {
      tickerContent.style.animationPlayState = 'running';
    });
  }

  /* ---- Parallax effect on hero ---- */
  const heroBg = document.querySelector('.hero-bg-img');
  if (heroBg) {
    window.addEventListener('scroll', () => {
      const scrollY = window.scrollY;
      if (scrollY < window.innerHeight) {
        heroBg.style.transform = `scale(1.08) translateY(${scrollY * 0.15}px)`;
      }
    }, { passive: true });
  }

  /* ---- Add ripple effect to buttons ---- */
  document.querySelectorAll('.btn, .nav-cta').forEach(btn => {
    btn.addEventListener('click', function (e) {
      const rect = this.getBoundingClientRect();
      const ripple = document.createElement('span');
      const size = Math.max(rect.width, rect.height);
      ripple.style.cssText = `
        position: absolute;
        width: ${size}px;
        height: ${size}px;
        left: ${e.clientX - rect.left - size / 2}px;
        top: ${e.clientY - rect.top - size / 2}px;
        background: rgba(255,255,255,0.2);
        border-radius: 50%;
        transform: scale(0);
        animation: ripple 0.6s ease-out forwards;
        pointer-events: none;
        z-index: 0;
      `;

      if (!document.getElementById('ripple-style')) {
        const style = document.createElement('style');
        style.id = 'ripple-style';
        style.textContent = '@keyframes ripple { to { transform: scale(3); opacity: 0; } }';
        document.head.appendChild(style);
      }

      this.style.position = 'relative';
      this.style.overflow = 'hidden';
      this.appendChild(ripple);
      setTimeout(() => ripple.remove(), 700);
    });
  });

  console.log('%c🛢️ SAHARA OIL TRADING S.A.', 'color: #D21619; font-size: 1.2rem; font-weight: 800;');
  console.log('%cSite web développé avec excellence.', 'color: #888; font-size: 0.9rem;');

})();

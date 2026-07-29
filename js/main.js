/* ============================================
   Mining Machinery - JavaScript
   ============================================ */

document.addEventListener('DOMContentLoaded', () => {

  /* --- Scroll: Nav background --- */
  const nav = document.querySelector('.nav');
  const handleScroll = () => {
    nav.classList.toggle('scrolled', window.scrollY > 50);
  };
  window.addEventListener('scroll', handleScroll, { passive: true });
  handleScroll();

  /* --- Mobile menu --- */
  const hamburger = document.querySelector('.nav-hamburger');
  const mobileMenu = document.querySelector('.mobile-menu');
  const mobileOverlay = document.querySelector('.mobile-overlay');
  const mobileClose = document.querySelector('.mobile-close');

  const openMenu = () => {
    mobileMenu.classList.add('open');
    mobileOverlay.classList.add('open');
    document.body.style.overflow = 'hidden';
  };
  const closeMenu = () => {
    mobileMenu.classList.remove('open');
    mobileOverlay.classList.remove('open');
    document.body.style.overflow = '';
  };

  hamburger?.addEventListener('click', openMenu);
  mobileClose?.addEventListener('click', closeMenu);
  mobileOverlay?.addEventListener('click', closeMenu);

  document.querySelectorAll('.mobile-menu a').forEach(link => {
    link.addEventListener('click', closeMenu);
  });

  /* --- Scroll: fade-in animations --- */
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
      }
    });
  }, { threshold: 0.15, rootMargin: '0px 0px -40px 0px' });

  document.querySelectorAll('.fade-in').forEach(el => observer.observe(el));

  /* --- Number counter animation --- */
  const countObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const el = entry.target;
        const target = parseInt(el.dataset.target, 10);
        const suffix = el.dataset.suffix || '';
        const duration = 2000;
        const startTime = performance.now();

        const animate = (currentTime) => {
          const elapsed = currentTime - startTime;
          const progress = Math.min(elapsed / duration, 1);
          const eased = 1 - Math.pow(1 - progress, 3);
          const current = Math.round(target * eased);

          el.textContent = current + suffix;

          if (progress < 1) {
            requestAnimationFrame(animate);
          }
        };

        requestAnimationFrame(animate);
        countObserver.unobserve(el);
      }
    });
  }, { threshold: 0.5 });

  document.querySelectorAll('.count-up').forEach(el => countObserver.observe(el));

  /* --- Smooth scroll for anchor links --- */
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
      const target = document.querySelector(this.getAttribute('href'));
      if (target) {
        e.preventDefault();
        const offset = nav.offsetHeight + 20;
        const top = target.getBoundingClientRect().top + window.pageYOffset - offset;
        window.scrollTo({ top, behavior: 'smooth' });
      }
    });
  });

  /* --- Active nav link on scroll --- */
  const sections = document.querySelectorAll('section[id]');
  const navLinks = document.querySelectorAll('.nav-links a');

  const setActiveLink = () => {
    let current = '';
    sections.forEach(section => {
      const top = section.offsetTop - nav.offsetHeight - 100;
      if (window.scrollY >= top) {
        current = section.getAttribute('id');
      }
    });
    navLinks.forEach(link => {
      link.classList.remove('active');
      if (link.getAttribute('href') === '#' + current) {
        link.classList.add('active');
      }
    });
  };

  window.addEventListener('scroll', setActiveLink, { passive: true });

  /* --- Product Tabs --- */
  document.querySelectorAll('.product-tabs').forEach(tabBar => {
    const tabs = tabBar.querySelectorAll('.product-tab');
    const container = tabBar.parentElement;
    const panels = container.querySelectorAll('.tab-panel');

    if (!tabs.length || !panels.length) return;

    tabs.forEach((tab, idx) => {
      tab.addEventListener('click', () => {
        tabs.forEach(t => t.classList.remove('active'));
        panels.forEach(p => p.classList.remove('active'));
        tab.classList.add('active');
        if (panels[idx]) panels[idx].classList.add('active');
      });
    });

    // 初始状态：第一个面板显示
    tabs[0].classList.add('active');
    if (panels[0]) panels[0].classList.add('active');
  });

  /* --- Contact Form Validation --- */
  const contactForm = document.getElementById('inquiryForm');
  if (contactForm) {
    contactForm.addEventListener('submit', (e) => {
      e.preventDefault();
      
      const name = contactForm.querySelector('[name="name"]');
      const email = contactForm.querySelector('[name="email"]');
      const message = contactForm.querySelector('[name="message"]');
      
      let valid = true;
      
      // Reset
      contactForm.querySelectorAll('.form-error').forEach(el => el.remove());
      contactForm.querySelectorAll('.form-group.error').forEach(el => el.classList.remove('error'));
      
      // Validate
      if (!name || !name.value.trim()) {
        showError(name, 'Please enter your name');
        valid = false;
      }
      if (!email || !email.value.trim()) {
        showError(email, 'Please enter your email');
        valid = false;
      } else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email.value.trim())) {
        showError(email, 'Please enter a valid email address');
        valid = false;
      }
      if (!message || !message.value.trim()) {
        showError(message, 'Please enter your message');
        valid = false;
      }
      
      if (valid) {
        const successEl = document.createElement('div');
        successEl.className = 'form-success';
        successEl.textContent = 'Thank you! Your inquiry has been submitted. Our team will respond within 24 hours.';
        successEl.style.cssText = 'padding:16px 20px;background:rgba(34,197,94,0.12);border:1px solid #22c55e;border-radius:8px;color:#22c55e;font-size:14px;font-weight:500;margin-top:16px;';
        contactForm.reset();
        contactForm.appendChild(successEl);
        setTimeout(() => successEl.remove(), 6000);
      }
    });
    
    function showError(field, message) {
      field.closest('.form-group')?.classList.add('error');
      const errorEl = document.createElement('span');
      errorEl.className = 'form-error';
      errorEl.textContent = message;
      errorEl.style.cssText = 'display:block;color:#ef4444;font-size:12px;margin-top:4px;';
      field.parentNode.appendChild(errorEl);
    }
  }

});

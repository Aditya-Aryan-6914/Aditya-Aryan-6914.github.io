// Typing animation configuration (easy to edit)
const roles = ["Student", "Explorer", "Thinker"];
const typingSpeed = 70;      // ms per character while typing
const deletingSpeed = 40;    // ms per character while deleting
const pauseAfterTyping = 900; // pause after full word typed (ms)
const pauseAfterDeleting = 200; // pause after fully deleted before typing next (ms)

const roleEl = document.getElementById('role');
const cursorEl = document.querySelector('.cursor');

let roleIndex = 0;
let charIndex = 0;
let isDeleting = false;

// clear any initial text and start typing shortly after load
roleEl.textContent = '';
setTimeout(typeLoop, 500);

function typeLoop() {
  const current = roles[roleIndex] || '';

  if (!isDeleting) {
    // type next character
    charIndex = Math.min(charIndex + 1, current.length);
    roleEl.textContent = current.slice(0, charIndex);

    if (charIndex === current.length) {
      // finished typing — pause, then start deleting
      isDeleting = true;
      setTimeout(typeLoop, pauseAfterTyping);
      return;
    }
    setTimeout(typeLoop, typingSpeed);
  } else {
    // delete one character
    charIndex = Math.max(charIndex - 1, 0);
    roleEl.textContent = current.slice(0, charIndex);

    if (charIndex === 0) {
      // finished deleting — move to next word
      isDeleting = false;
      roleIndex = (roleIndex + 1) % roles.length;
      setTimeout(typeLoop, pauseAfterDeleting);
      return;
    }
    setTimeout(typeLoop, deletingSpeed);
  }
}

// Note: To edit words or speeds, change the `roles` array and the speed constants above.

// Single-page navigation: collapse hero into a small banner and show sections
const links = document.querySelectorAll('.bottom-nav a[data-section]');
const topBanner = document.getElementById('topBanner');
const bannerTitle = document.getElementById('bannerTitle');
const hero = document.getElementById('hero');
const sections = document.querySelectorAll('.content-section');
const heroHeading = document.querySelector('.name');
let sectionOpen = false;
const scrollThreshold = 120; // when near the top, auto-collapse sections

function showSection(name){
  // scroll to top smoothly, then show section and collapse hero
  window.scrollTo({top:0, behavior:'smooth'});

  // small delay to allow scroll to start before visual changes
  setTimeout(()=>{
    hero.classList.add('collapsed');
    topBanner.classList.add('show');
    topBanner.setAttribute('aria-hidden','false');
    bannerTitle.textContent = name.replace(/^[a-z]/, s=>s.toUpperCase());

    // set page theme class on body (remove other theme- classes first)
    document.body.className = document.body.className.replace(/\btheme-[^\s]+\b/g, '').trim();
    document.body.classList.add(`theme-${name}`);

    sections.forEach(s=>{
      if(s.id === name){
        s.classList.add('active');
        // move keyboard focus to the section heading for accessibility
        const heading = s.querySelector('h2') || s;
        heading.setAttribute('tabindex','-1');
        heading.focus();
      } else {
        s.classList.remove('active');
      }
    });
    sectionOpen = true;
  }, 260);
}

  // show a one-time hint explaining how to return (if not seen before)
  showHintOnce();


function hideSections(){
  hero.classList.remove('collapsed');
  topBanner.classList.remove('show');
  topBanner.setAttribute('aria-hidden','true');
  bannerTitle.textContent = '';
  sections.forEach(s => s.classList.remove('active'));
  sectionOpen = false;
  // remove any theme class on body
  document.body.className = document.body.className.replace(/\btheme-[^\s]+\b/g, '').trim();
}

// wire up bottom links
links.forEach(a=>{
  a.addEventListener('click', (e)=>{
    e.preventDefault();
    const target = a.dataset.section;
    showSection(target);
  });
});

// clicking the banner logo or banner area returns home
document.getElementById('bannerLogo').addEventListener('click', (e)=>{
  e.preventDefault();
  hideSections();
  window.scrollTo({top:0, behavior:'smooth'});
  // return focus to the hero heading after animation
  setTimeout(()=>{
    if(heroHeading){
      heroHeading.setAttribute('tabindex','-1');
      heroHeading.focus();
    }
  }, 320);
});

// auto-collapse (return to hero) when user scrolls back near the top
// Only collapse when user is scrolling upward and reaches near the top
let lastScrollY = window.scrollY || 0;
const scrollUpDeltaRequired = 10; // require at least this many px of upward scroll

window.addEventListener('scroll', ()=>{
  const currentY = window.scrollY || 0;
  const delta = currentY - lastScrollY; // negative when scrolling up

  if (sectionOpen && currentY < scrollThreshold && delta < -scrollUpDeltaRequired) {
    hideSections();
  }

  lastScrollY = currentY;
});

// One-time on-screen hint for how to return home from a section
const hintKey = 'seenSectionHint_v1';
let hintTimeout;
function createHint(){
  if(document.getElementById('sectionHint')) return;
  const el = document.createElement('div');
  el.id = 'sectionHint';
  el.className = 'section-hint';
  el.setAttribute('role','status');
  el.setAttribute('aria-live','polite');
  el.tabIndex = 0;
  el.innerHTML = 'Tip: Scroll up to the top and swipe up to return to the hero. <button class="section-hint-close" aria-label="Dismiss hint">✕</button>';
  document.body.appendChild(el);
  el.querySelector('.section-hint-close').addEventListener('click', hideHint);
  el.addEventListener('click', hideHint);
}

function showHintOnce(){
  try{
    if(localStorage.getItem(hintKey)) return;
    createHint();
    const el = document.getElementById('sectionHint');
    if(!el) return;
    // show and then hide after a short period
    setTimeout(()=> el.classList.add('show'), 60);
    el.focus();
    localStorage.setItem(hintKey,'1');
    hintTimeout = setTimeout(hideHint, 5000);
  }catch(e){
    // localStorage may be unavailable in some contexts — ignore
  }
}

function hideHint(){
  const el = document.getElementById('sectionHint');
  if(!el) return;
  el.classList.remove('show');
  clearTimeout(hintTimeout);
}

// If user clicks outside (press Escape) close sections
document.addEventListener('keydown', (e)=>{
  if(e.key === 'Escape') hideSections();
});

// Populate gallery from Images/gallery.json if present
function populateGallery(){
  const grid = document.getElementById('galleryGrid');
  if(!grid) return;
  fetch('Images/gallery.json').then(res=>{
    if(!res.ok) throw new Error('no manifest');
    return res.json();
  }).then(items=>{
    grid.innerHTML = '';
    if(!items.length){
      grid.innerHTML = '<p class="muted">No images found.</p>';
      return;
    }
    items.forEach(it=>{
      const a = document.createElement('a');
      a.href = it.src;
      a.target = '_blank';
      a.rel = 'noopener';
      const img = document.createElement('img');
      img.src = it.thumb || it.src;
      img.alt = it.alt || '';
      img.loading = 'lazy';
      a.appendChild(img);
      grid.appendChild(a);
    });
  }).catch(()=>{
    // manifest missing - keep fallback message
  });
}

// call populate on load
window.addEventListener('load', populateGallery);

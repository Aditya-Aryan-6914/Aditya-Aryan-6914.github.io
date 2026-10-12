/* Portfolio interactions — plain JavaScript, no dependencies. */
(function () {
  'use strict';
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var store = {
    get: function (k) { try { return localStorage.getItem(k); } catch (e) { return null; } },
    set: function (k, v) { try { localStorage.setItem(k, v); } catch (e) {} },
    sget: function (k) { try { return sessionStorage.getItem(k); } catch (e) { return null; } },
    sset: function (k, v) { try { sessionStorage.setItem(k, v); } catch (e) {} }
  };
  var reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var json = function (id) { var el = document.getElementById(id); return el ? JSON.parse(el.textContent) : null; };

  /* ---------- Cookie consent, analytics & ads ---------- */
  function loadGA() {
    var id = document.body.dataset.ga; if (!id || window.__ga) return; window.__ga = 1;
    var s = document.createElement('script'); s.async = true; s.src = 'https://www.googletagmanager.com/gtag/js?id=' + id; document.head.appendChild(s);
    window.dataLayer = window.dataLayer || []; window.gtag = function () { dataLayer.push(arguments); };
    gtag('js', new Date()); gtag('config', id, { anonymize_ip: true });
  }
  function pushAds() {
    var slots = $$('ins.adsbygoogle'); if (!slots.length) return;
    window.adsbygoogle = window.adsbygoogle || [];
    window.adsbygoogle.requestNonPersonalizedAds = store.get('consent') === 'yes' ? 0 : 1;
    slots.forEach(function () { try { (window.adsbygoogle = window.adsbygoogle || []).push({}); } catch (e) {} });
  }
  var consent = store.get('consent'), banner = $('#consent');
  if (consent === 'yes') loadGA();
  if (!consent && banner) banner.classList.add('show');
  function decide(v) { store.set('consent', v); banner.classList.remove('show'); if (v === 'yes') loadGA(); }
  if ($('#consent-yes')) { $('#consent-yes').onclick = function () { decide('yes'); }; $('#consent-no').onclick = function () { decide('no'); }; }
  pushAds();
  if (!$('#sections') || document.documentElement.classList.contains('seen')) document.body.classList.add('ready');

  /* ---------- Navbar ---------- */
  var nav = $('#nav'), lastY = 0;
  window.addEventListener('scroll', function () {
    var y = window.scrollY; nav.classList.toggle('scrolled', y > 30);
    nav.classList.toggle('hide', y > lastY && y > 400); lastY = y;
  }, { passive: true });
  var drawer = $('#drawer');
  $('#burger').onclick = function () { drawer.classList.add('open'); this.setAttribute('aria-expanded', 'true'); };
  function closeDrawer() { drawer.classList.remove('open'); $('#burger').setAttribute('aria-expanded', 'false'); }
  $('#drawer-x').onclick = closeDrawer; $$('a', drawer).forEach(function (a) { a.addEventListener('click', closeDrawer); });

  /* ---------- Reveal on scroll (rail cards reveal together with their row) ---------- */
  var targets = [];
  $$('.reveal').forEach(function (el) { var t = el.closest('.rail,.picks') || el; if (targets.indexOf(t) < 0) targets.push(t); });
  function revealIn(t) { if (t.classList.contains('reveal')) t.classList.add('in'); $$('.reveal', t).forEach(function (el) { el.classList.add('in'); }); }
  if ('IntersectionObserver' in window && !reduced) {
    var io = new IntersectionObserver(function (es) { es.forEach(function (e) { if (e.isIntersecting) { revealIn(e.target); io.unobserve(e.target); } }); }, { rootMargin: '0px 0px -8% 0px', threshold: .08 });
    targets.forEach(function (t) { io.observe(t); });
  } else { targets.forEach(revealIn); }

  /* ---------- Rails: arrow buttons + drag to scroll (desktop) ---------- */
  $$('.rail,.picks').forEach(function (rail) {
    var wrap = document.createElement('div'); wrap.className = 'rail-wrap'; rail.parentNode.insertBefore(wrap, rail); wrap.appendChild(rail);
    ['prev', 'next'].forEach(function (d) {
      var b = document.createElement('button'); b.type = 'button'; b.className = 'rail-btn ' + d; b.setAttribute('aria-label', d === 'prev' ? 'Scroll left' : 'Scroll right'); b.textContent = d === 'prev' ? '‹' : '›';
      b.onclick = function () { rail.scrollBy({ left: (d === 'prev' ? -1 : 1) * rail.clientWidth * .8, behavior: reduced ? 'auto' : 'smooth' }); }; wrap.appendChild(b);
    });
    var down = false, sx = 0, sl = 0, moved = false;
    rail.addEventListener('mousedown', function (e) { down = true; moved = false; sx = e.pageX; sl = rail.scrollLeft; });
    window.addEventListener('mouseup', function () { down = false; rail.classList.remove('drag'); });
    window.addEventListener('mousemove', function (e) { if (!down) return; var dx = e.pageX - sx; if (Math.abs(dx) > 5) { moved = true; rail.classList.add('drag'); } rail.scrollLeft = sl - dx; });
    rail.addEventListener('click', function (e) { if (moved) { e.preventDefault(); e.stopPropagation(); moved = false; } }, true);
  });

  /* ---------- Custom cursor (fine pointers only) ---------- */
  if (window.matchMedia('(hover:hover) and (pointer:fine)').matches && !reduced) {
    var curEl = $('#cursor'), x = 0, y = 0, cx = 0, cy = 0;
    curEl.style.display = 'block'; document.documentElement.classList.add('has-cursor');
    window.addEventListener('mousemove', function (e) { x = e.clientX; y = e.clientY; });
    (function loop() { cx += (x - cx) * .22; cy += (y - cy) * .22; curEl.style.transform = 'translate(' + (cx - 7) + 'px,' + (cy - 7) + 'px)'; requestAnimationFrame(loop); })();
    document.addEventListener('mouseover', function (e) { curEl.classList.toggle('link', !!e.target.closest('a,button,.proj')); });
  }

  /* ---------- Blog search ---------- */
  var q = $('#q');
  if (q && window.SEARCH_INDEX_URL) {
    var index = null, box = $('#search-results'), grid = $('#post-grid');
    var esc = function (t) { return String(t).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); };
    q.addEventListener('focus', function () { if (!index) fetch(window.SEARCH_INDEX_URL).then(function (r) { return r.json(); }).then(function (d) { index = d; }); });
    q.addEventListener('input', function () {
      var term = q.value.trim().toLowerCase();
      if (!term || !index) { box.classList.remove('on'); grid.style.display = ''; return; }
      var words = term.split(/\s+/);
      var hits = index.filter(function (p) { var hay = (p.t + ' ' + p.d + ' ' + p.c + ' ' + p.g.join(' ')).toLowerCase(); return words.every(function (w) { return hay.indexOf(w) > -1; }); });
      grid.style.display = 'none'; box.classList.add('on');
      box.innerHTML = hits.length ? '<div class="posts">' + hits.map(function (p) {
        return '<article class="post-card in"><a href="' + p.u + '" style="display:flex;flex-direction:column;height:100%"><div class="art">' + esc(p.c.slice(0, 2).toUpperCase()) + '</div><div class="pc"><span class="cat-pill">' + esc(p.c) + '</span><h3>' + esc(p.t) + '</h3><p>' + esc(p.d) + '</p></div></a></article>'; }).join('') + '</div>'
        : '<p style="color:var(--mist)">No posts match “' + esc(term) + '”.</p>';
    });
  }

  /* ---------- Contact form (Formspree, AJAX) ---------- */
  var cf = $('#contact-form');
  if (cf) cf.addEventListener('submit', function (e) {
    e.preventDefault(); var st = $('#form-status'); st.style.display = 'block'; st.className = 'notice'; st.textContent = 'Sending…';
    fetch(cf.action, { method: 'POST', body: new FormData(cf), headers: { Accept: 'application/json' } }).then(function (r) {
      if (r.ok) { cf.reset(); st.className = 'notice ok'; st.textContent = 'Thanks! Your message was sent.'; } else { throw 0; }
    }).catch(function () { st.className = 'notice'; st.textContent = 'Something went wrong. Please try again or contact me on GitHub.'; });
  });

  /* ================= HOME ONLY ================= */
  if (!$('#sections')) return;
  var profiles = json('profiles-data') || [];
  var overlayOpen = 0;
  function lock(on) { document.body.classList.toggle('locked', on); }

  /* Profile ordering */
  function applyProfile(id) {
    var p = profiles.filter(function (v) { return v.id === id; })[0] || profiles[0]; if (!p) return;
    p.order.forEach(function (sec, i) { var el = document.querySelector('[data-section="' + sec + '"]'); if (el) el.style.order = i; });
    store.sset('profile', p.id);
    var av = $('#switch-av'); if (av) { av.textContent = p.glyph; av.style.background = 'linear-gradient(145deg,' + p.color + ',#0b0b10 120%)'; $('#switch-name').textContent = p.name; }
  }
  applyProfile(store.sget('profile') || profiles[0].id);

  var opening = $('#opening'), profEl = $('#profiles');
  function showProfiles() { profEl.classList.add('show'); lock(true); }
  function finishOpening() {
    if (opening.classList.contains('gone')) return; clearTimers();
    opening.classList.add('gone'); setTimeout(function () { opening.style.display = 'none'; }, 950); showProfiles();
  }
  var timers = []; function clearTimers() { timers.forEach(clearTimeout); timers = []; }
  function pickProfile(id) {
    applyProfile(id); profEl.classList.add('gone'); store.sset('seen', '1');
    setTimeout(function () { profEl.style.display = 'none'; profEl.classList.remove('show', 'gone'); lock(false); document.body.classList.add('ready'); }, 700);
  }
  $$('[data-profile]').forEach(function (b) { b.onclick = function () { pickProfile(b.dataset.profile); }; });
  $('#switch').onclick = function () { profEl.style.display = ''; profEl.classList.remove('gone'); showProfiles(); };

  if (!document.documentElement.classList.contains('seen')) {
    lock(true);
    var beats = [[300, 1], [1900, 2], [2700, 3], [3400, 4], [4300, 5], [5000, 6]];
    if (reduced) { opening.className = 'overlay beat1 beat2 beat3 beat4 beat5 beat6'; }
    else beats.forEach(function (b) { timers.push(setTimeout(function () { opening.classList.remove('beat1'); opening.classList.add('beat' + b[1]); if (b[1] > 1) opening.classList.remove('beat1'); }, b[0])); });
    $('#o-play').onclick = finishOpening; $('#o-skip').onclick = finishOpening;
    document.addEventListener('keydown', function onKey(e) { if (!opening.classList.contains('gone') && (e.key === 'Enter' || e.key === 'Escape')) { finishOpening(); document.removeEventListener('keydown', onKey); } });
  }

  /* ---------- Season tabs ---------- */
  $$('[data-season]').forEach(function (t) {
    t.onclick = function () {
      $$('[data-season]').forEach(function (x) { x.setAttribute('aria-selected', x === t ? 'true' : 'false'); });
      $$('[data-panel]').forEach(function (p) { p.classList.toggle('on', p.dataset.panel === t.dataset.season); });
    };
  });

  /* ---------- Skill evidence ---------- */
  var evidence = json('evidence-data') || {};
  $$('.skill').forEach(function (b) {
    b.onclick = function () {
      var card = b.closest('.genre'), box = $('.evidence', card), items = evidence[b.dataset.skill];
      var was = b.getAttribute('aria-expanded') === 'true';
      $$('.skill', card).forEach(function (x) { x.setAttribute('aria-expanded', 'false'); });
      if (was) { box.classList.remove('on'); return; }
      b.setAttribute('aria-expanded', 'true');
      box.innerHTML = '<strong>Where it shows up</strong>' + (items ? items.join(' · ') : 'Used day to day while learning and building.');
      box.classList.add('on');
    };
  });

  /* ---------- Project modal ---------- */
  var projects = json('projects-data') || [], modal = $('#modal'), sheet = $('#sheet'), lastFocus;
  var esc2 = function (t) { return String(t).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); };
  function openProject(id) {
    var p = projects.filter(function (x) { return x.id === id; })[0]; if (!p) return; lastFocus = document.activeElement;
    var pal = p.palette;
    sheet.innerHTML =
      '<button class="mclose" id="mclose" aria-label="Close">✕</button>' +
      '<div class="top" style="--from:' + pal.from + ';--via:' + pal.via + ';--to:' + pal.to + '"><span class="cat-pill" style="color:' + pal.accent + '">' + esc2(p.year) + ' · ' + esc2(p.genre) + '</span><h3>' + esc2(p.title) + '</h3><p style="color:#e0ddd6;max-width:36rem;margin:0 0 16px">' + esc2(p.logline) + '</p>' +
      '<div style="display:flex;gap:10px;flex-wrap:wrap">' + (p.live ? '<a class="pill solid" href="' + p.live + '" target="_blank" rel="noopener">▶ Live site</a>' : '') + (p.github ? '<a class="pill ghost" href="' + p.github + '" target="_blank" rel="noopener">GitHub ↗</a>' : '') + '</div></div>' +
      '<div class="body">' +
      (p.metrics.length ? '<div><h4>By the numbers</h4><div class="metrics">' + p.metrics.map(function (m) { return '<div class="metric glass"><b>' + esc2(m.value) + '</b><small>' + esc2(m.label) + '</small></div>'; }).join('') + '</div></div>' : '') +
      '<div><h4>What I built</h4><ul>' + p.build.map(function (b) { return '<li>' + esc2(b) + '</li>'; }).join('') + '</ul></div>' +
      '<div><h4>Features</h4><ul>' + p.features.map(function (b) { return '<li>' + esc2(b) + '</li>'; }).join('') + '</ul></div>' +
      '<div><h4>Tech stack</h4><div class="tags">' + p.stack.map(function (s) { return '<span class="tag">' + esc2(s) + '</span>'; }).join('') + '</div></div></div>';
    modal.classList.add('show'); lock(true); $('#mclose').focus(); $('#mclose').onclick = closeProject;
  }
  function closeProject() { modal.classList.remove('show'); lock(false); if (lastFocus) lastFocus.focus(); }
  $$('[data-project]').forEach(function (b) { b.onclick = function () { openProject(b.dataset.project); }; });
  modal.addEventListener('click', function (e) { if (e.target === modal) closeProject(); });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && modal.classList.contains('show')) closeProject(); });

  /* ---------- Play Intro highlight reel ---------- */
  var slides = json('intro-data') || [], pi = $('#playintro'), piSlide = $('#pi-slide'), prog = $('#pi-prog'), cur = 0, tm = null, paused = false, DUR = 5000;
  function renderSlide() {
    var s = slides[cur];
    piSlide.innerHTML = '<div class="slide"><div class="k">' + esc2(s.kicker) + '</div><h3>' + esc2(s.title) + '</h3>' + s.lines.map(function (l) { return '<p>' + esc2(l) + '</p>'; }).join('') + (s.chips ? '<div class="chips">' + s.chips.map(function (c) { return '<span class="chip">' + esc2(c) + '</span>'; }).join('') + '</div>' : '') + '</div>';
    prog.innerHTML = slides.map(function (_, i) { return '<i class="' + (i < cur ? 'done' : i === cur ? 'cur' : '') + '" style="--dur:' + DUR + 'ms"><b></b></i>'; }).join('');
    clearTimeout(tm); if (!paused) tm = setTimeout(next, DUR);
  }
  function next() { if (cur < slides.length - 1) { cur++; renderSlide(); } else closeIntro(); }
  function prev() { if (cur > 0) { cur--; renderSlide(); } }
  function openIntro() { cur = 0; paused = false; pi.classList.remove('paused', 'gone'); pi.style.display = ''; pi.classList.add('show'); lock(true); renderSlide(); }
  function closeIntro() { clearTimeout(tm); pi.classList.remove('show'); lock(false); }
  $('#play-intro').onclick = openIntro; $('#pi-close').onclick = closeIntro; $('#pi-next').onclick = next; $('#pi-prev').onclick = prev;
  $('#pi-pause').onclick = function () { paused = !paused; pi.classList.toggle('paused', paused); this.textContent = paused ? '▶' : '❚❚'; if (paused) clearTimeout(tm); else renderSlide(); };
  document.addEventListener('keydown', function (e) { if (!pi.classList.contains('show')) return; if (e.key === 'ArrowRight') next(); else if (e.key === 'ArrowLeft') prev(); else if (e.key === 'Escape') closeIntro(); });
})();

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

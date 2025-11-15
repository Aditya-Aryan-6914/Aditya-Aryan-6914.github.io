# Aditya Aryan — Single Page Portfolio

This is a minimal single-page portfolio. It shows a centered headline and a rotating role/title.

Files added:
- `index.html` — the page markup
- `styles.css` — simple centered styling and fade animation
- `script.js` — rotates the words (Student → Explorer → Thinker)

To edit the rotating words or speed:

1. Open `script.js`.
2. Modify the `roles` array, e.g. `const roles = ["Student","Explorer","Thinker","Maker"]`.
3. Change `intervalMs` to adjust how long each word is shown (in milliseconds).

Preview locally:

```bash
# from the repo root
python3 -m http.server 8000
# then open http://localhost:8000 in your browser
```

Deploy: push to this repository and enable GitHub Pages (branch `main`, folder `/`).

Social links and icons
- To change the link URLs, open `index.html` and edit the `href` values inside the `.social` block.
- The icons are inline SVGs — swap or edit the SVG markup if you want different visuals.

Typing animation
- The typing animation is implemented in `script.js` and is easy to configure.
- Edit `roles` to change the words, e.g. `const roles = ["Student","Explorer","Maker"]`.
- Tweak speeds and pauses by editing these constants at the top of `script.js`:
	- `typingSpeed` — ms per character while typing.
	- `deletingSpeed` — ms per character while deleting.
	- `pauseAfterTyping` — ms pause after a full word is typed.
	- `pauseAfterDeleting` — ms pause after a word is deleted before typing next.



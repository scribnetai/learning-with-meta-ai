# Learning with Meta AI

Manim-animated assets for the **Learning with Meta AI** YouTube series —
a show about learning agentic AI by building real things with it.

Everything here is generated from code. The video *is* the script.

## What's here

- `intro/` — the 15-second series intro (1080p): a glowing node network draws
  itself on dark navy, the two-tone title writes on, tagline fades in.
  - `intro_scene.py` — the Manim scene (edit this, re-render, done)
  - `learning-with-meta-ai-intro.mp4` — the rendered output

## Render it yourself

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cd intro
manim -qh intro_scene.py IntroScene
```

`-qh` = 1080p. Use `-qm` for a faster 720p draft. The finished mp4 lands in
`media/videos/intro_scene/1080p30/`.

No LaTeX required — scenes use Manim's `Text` (Pango), not `Tex`.
You do need `ffmpeg` on your PATH.

## Tweaking

Colors, copy, and timing are plain variables at the top of the scene file.
Change a line, re-run the render command. Randomness is seeded, so renders
are deterministic.

## License

MIT — do whatever you want with it.

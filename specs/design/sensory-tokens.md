# Sensory Design Tokens — spec v0.1

Date: 2026-07-15. Purpose: a machine-readable bridge from **sensory design intent**
(look · touch · sound · feel · taste) to **technical tokens** a build or a design tool can render
*toward*. This is the format Ali asked for: a way to state the "true feel" of a thing precisely
enough that Claude Design, Penpot, or a fresh build all aim at the same mark — and a validator can
check whether an artifact hit it.

The five senses are not decoration. Each maps to a concrete token layer:

| Sense | Token layer | Answers |
|---|---|---|
| **Look** | color, type, space, emblem | What does the eye receive? |
| **Touch** | motion, easing, interaction, weight | How does it move under the hand? |
| **Sound** | audio cues, sonification, implied rhythm | What does it sound like — or evoke? |
| **Feel** | emotional target + the rules that produce it | How should it land in the body? |
| **Taste** | voice, editorial, restraint | What is its character — what makes it *ours*? |

---

## Instance #1 — South Atlanta District, AME Church

Extracted from *South Atlanta District — Visual System & Brand Standards, Vol. One (v1.0, May 2026)*
and the 152nd Annual Conference PE Report. **Hard values below are Ali's own, verbatim from the
brand book.** The `[DRAFT]` blocks are hypotheses for the "true feel" gap — to be confirmed or
corrected by Ali, not treated as settled.

### LOOK — color (`Three Truths, Three Colors`)

```yaml
color:
  forest_green:   { hex: "#1A6B3C", role: primary,    meaning: "ground, growth, the church",  usage: "backgrounds, headlines, body emphasis — the primary at every scale" }
  heritage_gold:  { hex: "#C9A84C", role: ceremonial, meaning: "honor, episcopal accent",       usage: "borders, episcopal references, naming — ceremonial moments only" }
  sunrise_orange: { hex: "#E8842B", role: witness,    meaning: "the morning, the rising",       usage: "accent rules, the sunrise emblem, key witness moments — NEVER body text" }
  # neutrals (observed in artifacts; confirm exact values)
  ivory:          { hex: "#F5EFD9", role: paper,      usage: "light emblem field, warm page ground — not stark white" }
  ink:            { hex: "#1A2E1F", role: text_dark,  usage: "text on light grounds" }
```

### LOOK — type (`Three-Tier System`)

```yaml
type:
  display: { family: "Cinzel",             use: "mastheads, page titles, the masthead lockup" }
  serif:   { family: "Cormorant Garamond", use: "body, pull quotes, narrative voice", size: "11–13pt", leading: 1.45, italic: true }
  sans:    { family: "Inter",              use: "tables, captions, kicker labels" }
```

### LOOK — emblem

```yaml
emblem:
  mark: "sunrise-and-cross roundel"
  variants: [light_on_ivory, gold_on_forest]
  rule: "Always use a sanctioned form — do not redraw, recolor, or restyle."
  lockups: [primary_horizontal, compact, emblem_only]
```

### TOUCH — motion  `[DRAFT — needs Ali]`

```yaml
motion:
  cadence: processional     # weighted, unhurried — the pace of a hymn, not a product
  easing:  "cubic-bezier(0.22, 0.61, 0.36, 1)"   # slow-in, settled-out; proposed
  duration_ms: { small: 240, section: 480, hero: 900 }
  principle: "Nothing snaps. Reveals settle like a congregation rising and being seated."
```

### SOUND  `[DRAFT — needs Ali]`

```yaml
sound:
  policy: implied            # evoke, don't autoplay — reverence over spectacle
  reference: "organ swell, choir entrance, call-and-response"
  # if literal audio is ever used it is opt-in, never on load
  visual_rhythm: "let whitespace carry the cadence sound would — measured, breathing"
```

### FEEL — the target, and the gap  `[DRAFT — the crux]`

```yaml
feel:
  target: [reverence, welcome, legacy, belonging, "luminous hope"]
  achieved_now: [dignity, order, discipline, editorial_clarity]
  gap: >
    The v1.0 system nails DIGNITY and ORDER (Cinzel + forest green + gold reads
    genuinely episcopal). What the earlier 2025 stained-glass cover had — and the
    clean system renders cooler/flatter — is LUMINOUS WARMTH: light through glass,
    the glow of the rising sun, the felt presence of worship. "Sunrise" is in the
    palette name and the emblem, but the pages do not yet make you FEEL the sunrise.
  rules_to_recover_it:
    - "Reintroduce light: a forest→deep-green radial glow behind hero emblems (already on the PE cover — extend it as a token)."
    - "Let sunrise_orange actually rise: warm gradient washes at section thresholds, not just hairline rules."
    - "Texture, sparingly: a faint stained-glass or paper grain on dark grounds to restore depth the flat fills removed."
    - "Portraiture warmth: the 3:4 'forest duotone' plan is good — keep skin tones warm, never cold-duotoned."
```

### TASTE — voice

```yaml
voice:
  register: [scriptural, dignified, familial, plainspoken-not-corporate]
  motto: "The Best Is Yet to Come."     # conviction, not aspiration
  unity_line: "Twenty-four churches. One sunrise."
  exemplar: >
    "Twenty-four pulpits, one mind, one Lord. The South Atlanta District walks
    together because that is the only way the church has ever walked at all."
    — Rev. Dr. Larry W. Hudson, Sr.
  rules:
    - "Numbers carry testimony: '$5.59M raised', '158 conversions', '+12.2%' — stewardship stated with pride, never dryly."
    - "Scripture closes, it does not decorate (Jeremiah 29:11; Ephesians 3:20–21)."
    - "Never marketing-speak. This is a church, not a brand campaign."
```

---

## Validator (stub)

A conformance check answers: *does this artifact hit the mark, or just the palette?*

- **Color:** only sanctioned hexes; `sunrise_orange` never on body text; grounds are `ivory` not `#FFFFFF`.
- **Type:** display=Cinzel, narrative=Cormorant, data=Inter — no substitutions.
- **Emblem:** a sanctioned lockup, unaltered.
- **Feel gate (the one that matters):** does at least one *luminous-warmth* device (glow, sunrise
  gradient, texture, warm portraiture) appear per major surface? A page that is correct-but-flat
  **fails** even with perfect tokens. This is the check that would have caught "wonderful but not
  the true feel."

## Notes
- This makes SA-District the first real instance of the sensory-token layer described in
  `project-multi-model-and-sensory-layers` — and a live proof case that spans **Plumbline**
  (the PE Report is a president's-view executive report) and the **design layer**.
- Next: confirm the `[DRAFT]` blocks with Ali; extract exact neutral hexes from source files;
  add a Penpot/`opendesign` token export once the feel layer is agreed.

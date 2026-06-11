import { useState, useEffect, useRef } from "react";

// ═══════════════════════════════════════════════════════════════
// MERIDIA — The Complete Arrival
// Slower. Deliberate. Like walking into a room that was expecting you.
// ═══════════════════════════════════════════════════════════════

const C = {
  midnight: "#0B1120",
  deepNavy: "#0F1A2E",
  charcoal: "#1A2236",
  slate: "#2A3350",
  warmGold: "#C4A265",
  brightGold: "#D4B87A",
  paleGold: "#E8D5A8",
  cream: "#FAF6EE",
  warmWhite: "#F5F1E8",
  parchment: "#EDE6D6",
  burgundy: "#6B2D3E",
  emerald: "#2D6B4F",
  copper: "#B87333",
  smoke: "#8892A8",
  silver: "#A8AEC0",
  whisper: "rgba(196, 162, 101, 0.08)",
  glow: "rgba(196, 162, 101, 0.12)",
};

const F = {
  display: "'Playfair Display', 'Georgia', serif",
  body: "'Cormorant Garamond', 'Garamond', serif",
  mono: "'DM Mono', 'Courier New', monospace",
};

// ─── Grain ───
const Grain = () => (
  <div style={{
    position: "fixed", inset: 0, pointerEvents: "none", zIndex: 9999, opacity: 0.35,
    backgroundImage: `url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='0.03'/%3E%3C/svg%3E")`,
  }} />
);

// ─── Gold rule ───
const Rule = ({ w = "60px", style = {} }) => (
  <div style={{ width: w, height: "1px", background: `linear-gradient(90deg, transparent, ${C.warmGold}, transparent)`, margin: "16px 0", ...style }} />
);

// ─── Slow fade — respects the scotch principle ───
const Fade = ({ children, delay = 0, duration = 1200, style = {} }) => {
  const [v, setV] = useState(false);
  useEffect(() => { const t = setTimeout(() => setV(true), delay); return () => clearTimeout(t); }, [delay]);
  return (
    <div style={{
      opacity: v ? 1 : 0,
      transform: v ? "translateY(0)" : "translateY(10px)",
      transition: `opacity ${duration}ms ease, transform ${duration}ms ease`,
      ...style,
    }}>{children}</div>
  );
};

// ═══════════════════════════════════════════════════════════════
// THE CREST
// ═══════════════════════════════════════════════════════════════
const Crest = ({ size = 120, animate = false }) => {
  const [drawn, setDrawn] = useState(!animate);
  useEffect(() => { if (animate) { const t = setTimeout(() => setDrawn(true), 1200); return () => clearTimeout(t); } }, [animate]);
  return (
    <svg width={size} height={size} viewBox="0 0 200 200" fill="none">
      <circle cx="100" cy="100" r="96" stroke={C.warmGold} strokeWidth="0.5" opacity={drawn ? 0.25 : 0} style={{ transition: "opacity 2.5s ease" }} />
      <circle cx="100" cy="100" r="88" stroke={C.warmGold} strokeWidth="1" opacity={drawn ? 0.5 : 0} style={{ transition: "opacity 3s ease 0.5s" }} />
      <path d="M100 20 L155 45 L180 100 L155 155 L100 180 L45 155 L20 100 L45 45 Z" stroke={C.warmGold} strokeWidth="0.75" fill="none" opacity={drawn ? 0.2 : 0} style={{ transition: "opacity 2.5s ease 1s" }} />
      <g opacity={drawn ? 1 : 0} style={{ transition: "opacity 2s ease 1.5s" }}>
        <path d="M62 138 L62 68 L100 108 L138 68 L138 138" stroke={C.warmGold} strokeWidth="2" fill="none" strokeLinecap="round" strokeLinejoin="round" />
        <line x1="56" y1="138" x2="68" y2="138" stroke={C.warmGold} strokeWidth="1.5" />
        <line x1="132" y1="138" x2="144" y2="138" stroke={C.warmGold} strokeWidth="1.5" />
        <path d="M100 52 L104 58 L100 64 L96 58 Z" fill={C.warmGold} opacity="0.8" />
      </g>
      <g opacity={drawn ? 0.25 : 0} style={{ transition: "opacity 3s ease 2s" }}>
        <line x1="100" y1="6" x2="100" y2="14" stroke={C.warmGold} strokeWidth="0.75" />
        <line x1="100" y1="186" x2="100" y2="194" stroke={C.warmGold} strokeWidth="0.75" />
        <line x1="6" y1="100" x2="14" y2="100" stroke={C.warmGold} strokeWidth="0.75" />
        <line x1="186" y1="100" x2="194" y2="100" stroke={C.warmGold} strokeWidth="0.75" />
      </g>
    </svg>
  );
};

// ─── Corner accents ───
const Corner = ({ pos }) => {
  const s = {
    "tl": { top: 32, left: 32 },
    "tr": { top: 32, right: 32, transform: "scaleX(-1)" },
    "bl": { bottom: 32, left: 32, transform: "scaleY(-1)" },
    "br": { bottom: 32, right: 32, transform: "scale(-1)" },
  };
  return (
    <svg width="40" height="40" viewBox="0 0 40 40" fill="none" style={{ position: "fixed", ...s[pos], opacity: 0.15 }}>
      <line x1="0" y1="0" x2="0" y2="24" stroke={C.warmGold} strokeWidth="1" />
      <line x1="0" y1="0" x2="24" y2="0" stroke={C.warmGold} strokeWidth="1" />
    </svg>
  );
};

// ═══════════════════════════════════════════════════════════════
// MEMBER PROFILES — Different arrivals for different people
// ═══════════════════════════════════════════════════════════════
const MEMBERS = {
  architect: {
    name: "Mr. Neal",
    title: "Architect · Principal",
    fullName: "Aliman Neal",
    vestibuleMessage: "Two items require your attention today. Your Foundation review is approaching deadline, and a new SBA pathway has opened for Turner Seminary. I've prepared both.",
    aletheiaGreeting: [
      "Good morning. Three things have changed since we last spoke.",
      "The Foundation's grant disbursement rate is approaching the 5% minimum threshold. I recommend a governance review before Q1 close.",
      "An SBA lending threshold change creates a new pathway for Turner Seminary. I've prepared a brief.",
      "Your Georgia entity registrations open next week. Shall I walk you through what's due?",
    ],
    stats: [
      { label: "Signals", value: "6", note: "new" },
      { label: "Governance", value: "2", note: "pending" },
      { label: "Entities", value: "3", note: "healthy" },
    ],
  },
  heir: {
    name: "Ms. Beaumont",
    title: "Beneficiary · Crown Heir",
    fullName: "Isabelle Beaumont",
    vestibuleMessage: "Your quarterly review has been prepared. Mr. Hargrove reviewed the position yesterday and noted two items for your consideration. Nothing urgent — he simply wants your guidance before the board convenes Thursday.",
    aletheiaGreeting: [
      "Good afternoon, Isabelle. Your council has been busy on your behalf.",
      "Mr. Hargrove completed his review of the Q1 position yesterday. He's flagged the Foundation's grant rate and a new allocation opportunity in the Southeast commercial portfolio. His notes are ready whenever you'd like to see them.",
      "The Trust Index remains strong at 88. Your stewardship score improved this quarter — the mentorship program you championed is showing measurable outcomes.",
      "Mrs. Chen from the education council also left a note. Your daughter's Crown's Eye progress report is ready. She's ahead of pace in mathematics and Mrs. Chen recommends advancing the curriculum. Shall I pull that up?",
    ],
    stats: [
      { label: "Council Notes", value: "3", note: "prepared" },
      { label: "Reviews", value: "1", note: "awaiting you" },
      { label: "Trust Index", value: "88", note: "stable" },
    ],
  },
};

// ═══════════════════════════════════════════════════════════════
// PHASE 1: THE GATE
// Slower. The crest takes its time. The name settles.
// ═══════════════════════════════════════════════════════════════
const TheGate = ({ onEnter, onSelectMember }) => {
  const [phase, setPhase] = useState(0);
  const [hover, setHover] = useState(false);
  const [memberHover, setMemberHover] = useState(null);

  useEffect(() => {
    const t = [
      setTimeout(() => setPhase(1), 1500),
      setTimeout(() => setPhase(2), 4000),
      setTimeout(() => setPhase(3), 6000),
    ];
    return () => t.forEach(clearTimeout);
  }, []);

  return (
    <div style={{
      position: "fixed", inset: 0, background: C.midnight,
      display: "flex", flexDirection: "column", alignItems: "center", justifyContent: "center",
      zIndex: 1000,
    }}>
      <Grain />

      {/* Ambient glow */}
      <div style={{
        position: "absolute", width: "500px", height: "500px", borderRadius: "50%",
        background: `radial-gradient(circle, ${C.glow} 0%, transparent 70%)`,
        opacity: phase >= 1 ? 0.5 : 0, transition: "opacity 3s ease",
        pointerEvents: "none",
      }} />

      {/* Crest — takes its time drawing */}
      <div style={{
        opacity: phase >= 1 ? 1 : 0,
        transform: phase >= 1 ? "scale(1)" : "scale(0.95)",
        transition: "all 2.5s ease",
        marginBottom: "48px",
      }}>
        <Crest size={150} animate={true} />
      </div>

      {/* The Name */}
      <div style={{
        opacity: phase >= 2 ? 1 : 0,
        transform: phase >= 2 ? "translateY(0)" : "translateY(6px)",
        transition: "all 2s ease",
        textAlign: "center",
      }}>
        <h1 style={{
          fontFamily: F.display, fontSize: "44px", fontWeight: 400,
          color: C.cream, letterSpacing: "10px", textTransform: "uppercase",
          margin: "0 0 10px 0",
        }}>
          Meridia
        </h1>
        <Rule w="140px" style={{ margin: "0 auto 14px" }} />
        <p style={{
          fontFamily: F.mono, fontSize: "10px", color: C.smoke,
          letterSpacing: "4px", textTransform: "uppercase", margin: 0,
        }}>
          Cognitive Infrastructure
        </p>
      </div>

      {/* Member selection — who is arriving? */}
      <div style={{
        marginTop: "64px",
        opacity: phase >= 3 ? 1 : 0,
        transform: phase >= 3 ? "translateY(0)" : "translateY(10px)",
        transition: "all 1.8s ease",
        textAlign: "center",
      }}>
        <p style={{
          fontFamily: F.body, fontSize: "13px", color: C.smoke,
          fontStyle: "italic", margin: "0 0 24px 0",
        }}>
          Who is arriving?
        </p>

        <div style={{ display: "flex", gap: "16px", justifyContent: "center" }}>
          {[
            { id: "architect", label: "The Architect", subtitle: "Mr. Neal · Principal" },
            { id: "heir", label: "The Heir", subtitle: "Ms. Beaumont · Beneficiary" },
          ].map(m => (
            <div key={m.id}
              onClick={() => onSelectMember(m.id)}
              onMouseEnter={() => setMemberHover(m.id)}
              onMouseLeave={() => setMemberHover(null)}
              style={{
                padding: "18px 36px",
                border: `1px solid ${memberHover === m.id ? C.warmGold : C.slate}`,
                borderRadius: "2px",
                cursor: "pointer",
                background: memberHover === m.id ? C.whisper : "transparent",
                transition: "all 0.6s ease",
                minWidth: "180px",
              }}>
              <span style={{
                fontFamily: F.display, fontSize: "15px",
                color: memberHover === m.id ? C.cream : C.silver,
                display: "block", marginBottom: "4px",
                transition: "color 0.6s ease",
              }}>
                {m.label}
              </span>
              <span style={{
                fontFamily: F.mono, fontSize: "9px", color: C.smoke,
                letterSpacing: "1.5px", textTransform: "uppercase",
              }}>
                {m.subtitle}
              </span>
            </div>
          ))}
        </div>

        <p style={{
          fontFamily: F.body, fontSize: "11px", color: `${C.smoke}60`,
          fontStyle: "italic", marginTop: "32px",
        }}>
          Governed by Integra · Powered by Eden Intelligence Group
        </p>
      </div>

      {phase >= 1 && <><Corner pos="tl" /><Corner pos="tr" /><Corner pos="bl" /><Corner pos="br" /></>}
    </div>
  );
};

// ═══════════════════════════════════════════════════════════════
// PHASE 2: THE VESTIBULE
// The moment between the door and the room. Unhurried.
// ═══════════════════════════════════════════════════════════════
const TheVestibule = ({ member, onComplete }) => {
  const [phase, setPhase] = useState(0);
  const m = MEMBERS[member];

  useEffect(() => {
    const t = [
      setTimeout(() => setPhase(1), 800),
      setTimeout(() => setPhase(2), 3500),
      setTimeout(() => setPhase(3), 6000),
      setTimeout(() => onComplete(), 9500),
    ];
    return () => t.forEach(clearTimeout);
  }, []);

  const now = new Date();
  const hour = now.getHours();
  const greeting = hour < 12 ? "Good morning" : hour < 17 ? "Good afternoon" : "Good evening";

  return (
    <div style={{
      position: "fixed", inset: 0, background: C.midnight,
      display: "flex", flexDirection: "column", alignItems: "center", justifyContent: "center",
      zIndex: 1000,
    }}>
      <Grain />

      {/* Small crest — above the mantel now */}
      <div style={{ opacity: phase >= 1 ? 1 : 0, transition: "opacity 2s ease", marginBottom: "36px" }}>
        <Crest size={56} />
      </div>

      {/* Personal greeting */}
      <div style={{
        opacity: phase >= 1 ? 1 : 0,
        transform: phase >= 1 ? "translateY(0)" : "translateY(6px)",
        transition: "all 1.8s ease",
        textAlign: "center",
      }}>
        <h2 style={{
          fontFamily: F.display, fontSize: "30px", fontWeight: 400,
          color: C.cream, letterSpacing: "1px", margin: "0 0 8px 0",
        }}>
          {greeting}, {m.name}
        </h2>
        <p style={{
          fontFamily: F.body, fontSize: "14px", color: C.smoke, fontStyle: "italic", margin: 0,
        }}>
          {now.toLocaleDateString("en-US", { weekday: "long", month: "long", day: "numeric", year: "numeric" })}
        </p>
      </div>

      {/* Status summary */}
      <div style={{
        marginTop: "48px", opacity: phase >= 2 ? 1 : 0,
        transform: phase >= 2 ? "translateY(0)" : "translateY(6px)",
        transition: "all 1.8s ease", textAlign: "center",
      }}>
        <Rule w="60px" style={{ margin: "0 auto 20px" }} />
        <div style={{ display: "flex", gap: "40px", justifyContent: "center" }}>
          {m.stats.map((s, i) => (
            <div key={i} style={{ textAlign: "center" }}>
              <span style={{ fontFamily: F.display, fontSize: "26px", color: C.warmGold, display: "block" }}>{s.value}</span>
              <span style={{ fontFamily: F.mono, fontSize: "9px", color: C.smoke, textTransform: "uppercase", letterSpacing: "2px" }}>{s.label}</span>
            </div>
          ))}
        </div>
      </div>

      {/* Aletheia whisper — different per member */}
      <div style={{
        marginTop: "56px", opacity: phase >= 3 ? 1 : 0,
        transform: phase >= 3 ? "translateY(0)" : "translateY(4px)",
        transition: "all 2s ease",
        textAlign: "center", maxWidth: "520px",
      }}>
        <p style={{
          fontFamily: F.body, fontSize: "16px", color: C.parchment,
          fontStyle: "italic", lineHeight: 1.8, margin: 0,
        }}>
          "{m.vestibuleMessage}"
        </p>
        <p style={{
          fontFamily: F.mono, fontSize: "9px", color: C.smoke,
          textTransform: "uppercase", letterSpacing: "2px", marginTop: "16px",
        }}>
          — Aletheia
        </p>
      </div>
    </div>
  );
};

// ═══════════════════════════════════════════════════════════════
// PHASE 3: THE INSTITUTION
// ═══════════════════════════════════════════════════════════════

const NAV = [
  { id: "residence", label: "The Residence", icon: "◆", on: true, desc: "Your position" },
  { id: "signal", label: "Meridian Signal", icon: "◈", on: true, desc: "Intelligence feed" },
  { id: "governance", label: "The Library", icon: "▣", on: true, desc: "Governance & oversight" },
  { id: "entities", label: "The Gallery", icon: "▤", on: true, desc: "Entity collection" },
  { id: "scenarios", label: "The Study", icon: "◧", on: true, desc: "Scenario modeling" },
  { id: "reports", label: "The Bureau", icon: "▥", on: true, desc: "Report generation" },
  { id: "crown", label: "WayPoint Crown", icon: "♛", on: true, desc: "Family office" },
  { id: "renaissance", label: "WP Renaissance", icon: "✦", on: false, desc: "Re-entry pathways" },
  { id: "edge", label: "WayPoint Edge", icon: "⬡", on: false, desc: "Vertical-specific" },
  { id: "crowns-eye", label: "Crown's Eye", icon: "◉", on: false, desc: "Education" },
  { id: "wearable", label: "The Wearable", icon: "◎", on: false, desc: "Phase 3" },
];

const SIGNALS = [
  { time: "09:14", text: "FDIC guidance update: CRA modernization rule — comment period closing March 15", urgency: "watch" },
  { time: "08:47", text: "SBA 7(a) lending threshold increased to $500K for qualified nonprofits — Turner Seminary eligible", urgency: "action" },
  { time: "08:12", text: "Pinnacle Financial Partners Q4 earnings beat — post-merger integration ahead of schedule", urgency: "info" },
  { time: "07:30", text: "Foundation grant disbursement approaching 5% minimum — Q1 review recommended", urgency: "watch" },
  { time: "Yesterday", text: "Georgia Secretary of State annual registration renewal — 3 entities due", urgency: "action" },
  { time: "Yesterday", text: "10-year Treasury yield at 4.12% — line of credit rate adjustment may trigger April", urgency: "info" },
];

const ENTITIES = [
  { name: "Crown Legacy Trust", type: "Irrevocable Trust", jur: "Delaware", status: "healthy", aum: "$12.4M" },
  { name: "Family Impact Foundation", type: "501(c)(3)", jur: "Georgia", status: "watch", aum: "$4.2M" },
  { name: "Crown Holdings LLC", type: "Operating Entity", jur: "Georgia", status: "healthy", aum: "$3.1M" },
];

const urgCol = { action: C.warmGold, watch: C.copper, info: C.smoke };
const statCol = { healthy: C.emerald, watch: C.copper, alert: C.burgundy };

// ─── Clock ───
const Clock = () => {
  const [t, setT] = useState(new Date());
  useEffect(() => { const i = setInterval(() => setT(new Date()), 1000); return () => clearInterval(i); }, []);
  return (
    <span style={{ fontFamily: F.mono, fontSize: "11px", color: C.smoke, letterSpacing: "2px" }}>
      {t.toLocaleTimeString("en-US", { hour: "2-digit", minute: "2-digit", hour12: false })}
      <span style={{ opacity: 0.4, margin: "0 6px" }}>·</span>
      {t.toLocaleDateString("en-US", { weekday: "long", month: "long", day: "numeric" })}
    </span>
  );
};

// ─── Trust Index ───
const TrustIdx = ({ score = 88 }) => {
  const [a, setA] = useState(0);
  useEffect(() => { let s = 0; const go = () => { s++; if (s <= score) { setA(s); requestAnimationFrame(go); } }; setTimeout(go, 1200); }, [score]);
  const d = [{ n: "Financial", s: 92 }, { n: "Stewardship", s: 81 }, { n: "Mission", s: 88 }, { n: "Governance", s: 91 }];
  return (
    <div style={{ padding: "20px 0" }}>
      <div style={{ display: "flex", alignItems: "baseline", gap: "8px", marginBottom: "18px" }}>
        <span style={{ fontFamily: F.display, fontSize: "52px", fontWeight: 400, color: C.warmGold, lineHeight: 1 }}>{a}</span>
        <span style={{ fontFamily: F.body, fontSize: "14px", color: C.smoke }}>of 100</span>
      </div>
      <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: "10px" }}>
        {d.map((x, i) => (
          <div key={x.n} style={{ padding: "10px 0" }}>
            <div style={{ display: "flex", justifyContent: "space-between", marginBottom: "5px" }}>
              <span style={{ fontFamily: F.body, fontSize: "13px", color: C.silver }}>{x.n}</span>
              <span style={{ fontFamily: F.mono, fontSize: "11px", color: C.warmGold }}>{x.s}</span>
            </div>
            <div style={{ height: "2px", background: C.slate, borderRadius: "1px", overflow: "hidden" }}>
              <div style={{ height: "100%", width: `${x.s}%`, background: `linear-gradient(90deg, ${C.warmGold}, ${C.brightGold})`, transition: "width 2s ease", transitionDelay: `${i * 300 + 1500}ms` }} />
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

// ─── Main Institution ───
const Institution = ({ member }) => {
  const [room, setRoom] = useState("residence");
  const [aOpen, setAOpen] = useState(true);
  const [navH, setNavH] = useState(null);
  const m = MEMBERS[member];

  const titles = {
    residence: "The Residence", signal: "Meridian Signal", governance: "The Library",
    entities: "The Gallery", scenarios: "The Study", reports: "The Bureau",
    crown: "WayPoint Crown", renaissance: "WP Renaissance", edge: "WayPoint Edge",
    "crowns-eye": "Crown's Eye", wearable: "The Wearable",
  };
  const subs = {
    residence: "Your financial position, maintained and ready",
    signal: "Intelligence that touches your world",
    governance: "Oversight, approvals, and governance cascade",
    entities: "Your collection, every entity mapped",
    scenarios: "Model the future before you live it",
    reports: "One truth, four windows",
    crown: "Multi-generational governance",
  };

  return (
    <div style={{ minHeight: "100vh", background: C.midnight, display: "flex", fontFamily: F.body, color: C.cream }}>
      <Grain />
      <style>{`
        @keyframes pulse { 0%,100% { opacity:.2 } 50% { opacity:.8 } }
        input[type=range] { -webkit-appearance:none; background:${C.slate}; border-radius:1px; outline:none; height:2px; width:100% }
        input[type=range]::-webkit-slider-thumb { -webkit-appearance:none; width:12px; height:12px; border-radius:50%; background:${C.warmGold}; cursor:pointer }
        ::-webkit-scrollbar { width:4px } ::-webkit-scrollbar-track { background:transparent } ::-webkit-scrollbar-thumb { background:${C.slate}; border-radius:2px }
        ::placeholder { color:${C.smoke} }
      `}</style>

      {/* ═══ LEFT NAV ═══ */}
      <nav style={{
        width: "240px", background: C.deepNavy, borderRight: `1px solid ${C.whisper}`,
        display: "flex", flexDirection: "column",
        position: "fixed", top: 0, bottom: 0, left: 0, zIndex: 200,
      }}>
        <div style={{ padding: "22px 20px 14px", display: "flex", alignItems: "center", gap: "14px" }}>
          <Crest size={38} />
          <div>
            <h1 style={{ fontFamily: F.display, fontSize: "16px", fontWeight: 400, color: C.cream, margin: 0, letterSpacing: "2px", textTransform: "uppercase" }}>Meridia</h1>
            <p style={{ fontFamily: F.mono, fontSize: "7px", color: C.smoke, textTransform: "uppercase", letterSpacing: "2.5px", margin: 0 }}>Integra Core · v1.0</p>
          </div>
        </div>
        <Rule w="calc(100% - 40px)" style={{ margin: "0 20px 6px" }} />
        <div style={{ padding: "8px 20px 14px" }}>
          <p style={{ fontFamily: F.body, fontSize: "13px", color: C.silver, margin: "0 0 2px 0" }}>{m.fullName}</p>
          <p style={{ fontFamily: F.mono, fontSize: "8px", color: C.smoke, textTransform: "uppercase", letterSpacing: "2px", margin: 0 }}>{m.title}</p>
        </div>

        <div style={{ flex: 1, overflowY: "auto", padding: "2px 0" }}>
          {NAV.map(n => (
            <div key={n.id}
              onClick={() => n.on && setRoom(n.id)}
              onMouseEnter={() => setNavH(n.id)}
              onMouseLeave={() => setNavH(null)}
              style={{
                padding: "9px 20px", display: "flex", alignItems: "center", gap: "11px",
                cursor: n.on ? "pointer" : "default", opacity: n.on ? 1 : 0.28,
                background: room === n.id ? C.whisper : navH === n.id && n.on ? C.whisper : "transparent",
                borderLeft: room === n.id ? `2px solid ${C.warmGold}` : "2px solid transparent",
                transition: "all 0.4s ease",
              }}>
              <span style={{ fontFamily: F.display, fontSize: "11px", color: room === n.id ? C.warmGold : C.smoke, width: "16px", textAlign: "center" }}>{n.icon}</span>
              <div>
                <span style={{ fontFamily: F.body, fontSize: "13px", color: room === n.id ? C.cream : C.silver }}>{n.label}</span>
                {navH === n.id && <span style={{ fontFamily: F.mono, fontSize: "8px", color: C.smoke, display: "block" }}>{n.desc}</span>}
              </div>
              {!n.on && <span style={{ marginLeft: "auto", fontFamily: F.mono, fontSize: "7px", color: C.smoke, border: `1px solid ${C.slate}`, padding: "2px 5px", borderRadius: "2px" }}>SOON</span>}
            </div>
          ))}
        </div>

        <div style={{ padding: "12px 20px", borderTop: `1px solid ${C.whisper}` }}>
          <p style={{ fontFamily: F.mono, fontSize: "7px", color: C.smoke, textTransform: "uppercase", letterSpacing: "2px", margin: "0 0 2px 0" }}>Eden Intelligence Group</p>
          <p style={{ fontFamily: F.mono, fontSize: "7px", color: `${C.smoke}50`, margin: 0 }}>Governance as a Service</p>
        </div>
      </nav>

      {/* ═══ MAIN ═══ */}
      <main style={{
        marginLeft: "240px",
        marginRight: aOpen ? "360px" : "0px",
        transition: "margin-right 0.6s ease",
        minHeight: "100vh", flex: 1,
        position: "relative", zIndex: 10,
      }}>
        {/* Top bar */}
        <header style={{
          padding: "16px 36px", display: "flex", justifyContent: "space-between", alignItems: "center",
          borderBottom: `1px solid ${C.whisper}`,
          position: "sticky", top: 0, background: `${C.midnight}f0`,
          backdropFilter: "blur(20px)", zIndex: 100,
        }}>
          <Clock />
          <div style={{ display: "flex", alignItems: "center", gap: "16px" }}>
            <span style={{ fontFamily: F.mono, fontSize: "9px", color: C.emerald, textTransform: "uppercase", letterSpacing: "2px", display: "flex", alignItems: "center", gap: "6px" }}>
              <span style={{ width: "5px", height: "5px", borderRadius: "50%", background: C.emerald }} />Healthy
            </span>
            <div onClick={() => setAOpen(!aOpen)} style={{
              width: "28px", height: "28px", borderRadius: "50%",
              border: `1px solid ${aOpen ? C.warmGold : C.slate}`,
              display: "flex", alignItems: "center", justifyContent: "center",
              cursor: "pointer", fontFamily: F.display, fontSize: "12px",
              color: aOpen ? C.warmGold : C.smoke, transition: "all 0.4s ease",
            }}>A</div>
          </div>
        </header>

        {/* Room title */}
        <div style={{ padding: "40px 36px 0" }}>
          <Fade key={room} duration={1400}>
            <p style={{ fontFamily: F.mono, fontSize: "9px", color: C.smoke, textTransform: "uppercase", letterSpacing: "3px", margin: "0 0 6px 0" }}>
              {["crown","renaissance","edge"].includes(room) ? "WayPoint" : "Meridia"}
            </p>
            <h2 style={{ fontFamily: F.display, fontSize: "30px", fontWeight: 400, color: C.cream, margin: "0 0 4px 0", letterSpacing: "0.5px" }}>{titles[room]}</h2>
            {subs[room] && <p style={{ fontFamily: F.body, fontSize: "14px", color: C.smoke, fontStyle: "italic", margin: 0 }}>{subs[room]}</p>}
            <Rule w="80px" style={{ margin: "18px 0 0" }} />
          </Fade>
        </div>

        {/* Room content */}
        <div style={{ padding: "28px 36px 60px" }}>

          {room === "residence" && (
            <div>
              <Fade delay={400} duration={1400}>
                <div style={{ display: "grid", gridTemplateColumns: "repeat(4, 1fr)", gap: "1px", background: C.slate, borderRadius: "2px", overflow: "hidden" }}>
                  {[
                    { l: "Net Worth", v: "$19.6M", ch: "+4.2%", up: true },
                    { l: "Liquidity", v: "$2.3M", ch: "+1.8%", up: true },
                    { l: "Obligations", v: "$416K", ch: "-2.1%", up: false },
                    { l: "Resilience", v: "95", ch: "+3", up: true, sfx: "/100" },
                  ].map((x, i) => (
                    <div key={i} style={{ background: C.deepNavy, padding: "22px 18px" }}>
                      <p style={{ fontFamily: F.mono, fontSize: "9px", textTransform: "uppercase", letterSpacing: "2px", color: C.smoke, margin: "0 0 8px 0" }}>{x.l}</p>
                      <div style={{ display: "flex", alignItems: "baseline", gap: "3px" }}>
                        <span style={{ fontFamily: F.display, fontSize: "26px", fontWeight: 400, color: C.cream }}>{x.v}</span>
                        {x.sfx && <span style={{ fontFamily: F.body, fontSize: "12px", color: C.smoke }}>{x.sfx}</span>}
                      </div>
                      <span style={{ fontFamily: F.mono, fontSize: "10px", color: x.up ? C.emerald : C.warmGold, marginTop: "4px", display: "inline-block" }}>
                        {x.up ? "↑" : "↓"} {x.ch}
                      </span>
                    </div>
                  ))}
                </div>
              </Fade>
              <div style={{ marginTop: "36px", display: "grid", gridTemplateColumns: "1fr 1fr", gap: "36px" }}>
                <Fade delay={800} duration={1400}>
                  <div>
                    <h3 style={{ fontFamily: F.display, fontSize: "17px", fontWeight: 400, color: C.cream, margin: "0 0 2px 0" }}>Trust Index</h3>
                    <p style={{ fontFamily: F.mono, fontSize: "9px", color: C.smoke, textTransform: "uppercase", letterSpacing: "2px", margin: 0 }}>Composite governance score</p>
                    <TrustIdx />
                  </div>
                </Fade>
                <Fade delay={1200} duration={1400}>
                  <div>
                    <h3 style={{ fontFamily: F.display, fontSize: "17px", fontWeight: 400, color: C.cream, margin: "0 0 2px 0" }}>Latest Signal</h3>
                    <p style={{ fontFamily: F.mono, fontSize: "9px", color: C.smoke, textTransform: "uppercase", letterSpacing: "2px", margin: "0 0 8px 0" }}>Top developments</p>
                    {SIGNALS.slice(0, 3).map((s, i) => (
                      <Fade key={i} delay={i * 300 + 1600} duration={1200}>
                        <div style={{ padding: "14px 0", borderBottom: `1px solid ${C.whisper}`, display: "flex", gap: "14px" }}>
                          <div style={{ width: "5px", height: "5px", borderRadius: "50%", background: urgCol[s.urgency], marginTop: "8px", flexShrink: 0 }} />
                          <div>
                            <p style={{ fontFamily: F.body, fontSize: "13px", color: C.cream, lineHeight: 1.6, margin: 0 }}>{s.text}</p>
                            <div style={{ display: "flex", gap: "10px", marginTop: "4px" }}>
                              <span style={{ fontFamily: F.mono, fontSize: "9px", color: C.smoke }}>{s.time}</span>
                              <span style={{ fontFamily: F.mono, fontSize: "8px", color: urgCol[s.urgency], textTransform: "uppercase", letterSpacing: "1.5px" }}>{s.urgency}</span>
                            </div>
                          </div>
                        </div>
                      </Fade>
                    ))}
                  </div>
                </Fade>
              </div>
            </div>
          )}

          {room === "signal" && SIGNALS.map((s, i) => (
            <Fade key={i} delay={i * 250 + 400} duration={1200}>
              <div style={{ padding: "16px 0", borderBottom: `1px solid ${C.whisper}`, display: "flex", gap: "14px" }}>
                <div style={{ width: "5px", height: "5px", borderRadius: "50%", background: urgCol[s.urgency], marginTop: "8px", flexShrink: 0 }} />
                <div>
                  <p style={{ fontFamily: F.body, fontSize: "14px", color: C.cream, lineHeight: 1.6, margin: 0 }}>{s.text}</p>
                  <div style={{ display: "flex", gap: "10px", marginTop: "5px" }}>
                    <span style={{ fontFamily: F.mono, fontSize: "9px", color: C.smoke }}>{s.time}</span>
                    <span style={{ fontFamily: F.mono, fontSize: "8px", color: urgCol[s.urgency], textTransform: "uppercase", letterSpacing: "1.5px" }}>{s.urgency}</span>
                  </div>
                </div>
              </div>
            </Fade>
          ))}

          {room === "entities" && ENTITIES.map((e, i) => (
            <Fade key={i} delay={i * 300 + 500} duration={1200}>
              <div style={{
                padding: "22px", border: `1px solid ${C.slate}`, borderRadius: "2px",
                marginBottom: "10px", cursor: "pointer", transition: "border-color 0.5s ease",
              }}
              onMouseEnter={ev => ev.currentTarget.style.borderColor = C.warmGold}
              onMouseLeave={ev => ev.currentTarget.style.borderColor = C.slate}>
                <div style={{ display: "flex", justifyContent: "space-between" }}>
                  <div>
                    <h3 style={{ fontFamily: F.display, fontSize: "17px", fontWeight: 400, color: C.cream, margin: "0 0 3px 0" }}>{e.name}</h3>
                    <p style={{ fontFamily: F.body, fontSize: "12px", color: C.smoke, margin: 0 }}>{e.type} · {e.jur}</p>
                  </div>
                  <div style={{ textAlign: "right" }}>
                    <span style={{ fontFamily: F.display, fontSize: "19px", color: C.warmGold }}>{e.aum}</span>
                    <div style={{ display: "flex", alignItems: "center", gap: "5px", justifyContent: "flex-end", marginTop: "3px" }}>
                      <div style={{ width: "5px", height: "5px", borderRadius: "50%", background: statCol[e.status] }} />
                      <span style={{ fontFamily: F.mono, fontSize: "8px", textTransform: "uppercase", letterSpacing: "1.5px", color: statCol[e.status] }}>{e.status}</span>
                    </div>
                  </div>
                </div>
              </div>
            </Fade>
          ))}

          {room === "reports" && (
            <ReportBureau />
          )}

          {room === "governance" && (
            <GovView />
          )}

          {room === "scenarios" && (
            <ScenarioView />
          )}

          {["crown","renaissance","edge","crowns-eye","wearable"].includes(room) && (
            <Fade delay={400} duration={1400}>
              <div style={{ padding: "56px 36px", border: `1px solid ${C.slate}`, borderRadius: "2px", textAlign: "center" }}>
                <p style={{ fontFamily: F.mono, fontSize: "9px", color: C.smoke, textTransform: "uppercase", letterSpacing: "3px", margin: "0 0 14px 0" }}>
                  {room === "crown" ? "Full suite activates with live data" : "This wing is under construction"}
                </p>
                <h3 style={{ fontFamily: F.display, fontSize: "22px", fontWeight: 400, color: C.warmGold, margin: "0 0 10px 0" }}>{titles[room]}</h3>
                <p style={{ fontFamily: F.body, fontSize: "14px", color: C.silver, lineHeight: 1.7, maxWidth: "400px", margin: "0 auto" }}>
                  The hallway is here. The door exists. The room is being prepared with the care it deserves.
                </p>
              </div>
            </Fade>
          )}
        </div>
      </main>

      {/* ═══ ALETHEIA PANEL — Fixed properly ═══ */}
      <div style={{
        position: "fixed", right: 0, top: 0, bottom: 0,
        width: aOpen ? "360px" : "0px",
        background: C.deepNavy,
        borderLeft: aOpen ? `1px solid ${C.whisper}` : "none",
        transition: "width 0.6s ease",
        overflow: "hidden", zIndex: 200,
        display: "flex", flexDirection: "column",
      }}>
        <div style={{ padding: "22px 20px 14px", borderBottom: `1px solid ${C.whisper}`, flexShrink: 0 }}>
          <div style={{ display: "flex", alignItems: "center", gap: "12px" }}>
            <div style={{
              width: "30px", height: "30px", borderRadius: "50%",
              border: `1px solid ${C.warmGold}`,
              display: "flex", alignItems: "center", justifyContent: "center",
              fontFamily: F.display, fontSize: "13px", color: C.warmGold,
            }}>A</div>
            <div>
              <h3 style={{ fontFamily: F.display, fontSize: "15px", fontWeight: 400, color: C.cream, margin: 0 }}>Aletheia</h3>
              <p style={{ fontFamily: F.mono, fontSize: "8px", color: C.smoke, textTransform: "uppercase", letterSpacing: "2px", margin: 0 }}>Your Steward</p>
            </div>
          </div>
        </div>

        <div style={{ flex: 1, padding: "18px 20px", overflowY: "auto", minHeight: 0 }}>
          {m.aletheiaGreeting.map((msg, i) => (
            <Fade key={i} delay={i * 1500 + 800} duration={1400}>
              <div style={{ marginBottom: "18px" }}>
                <p style={{ fontFamily: F.body, fontSize: "14px", color: C.parchment, lineHeight: 1.7, margin: 0 }}>{msg}</p>
                {i === 0 && <Rule w="40px" />}
              </div>
            </Fade>
          ))}
        </div>

        <div style={{ padding: "14px 20px", borderTop: `1px solid ${C.whisper}`, flexShrink: 0 }}>
          <div style={{ display: "flex", border: `1px solid ${C.slate}`, borderRadius: "2px", padding: "9px 12px" }}>
            <input placeholder="Ask Aletheia..." style={{
              flex: 1, background: "transparent", border: "none", outline: "none",
              fontFamily: F.body, fontSize: "13px", color: C.cream,
            }} />
            <span style={{ color: C.warmGold, cursor: "pointer" }}>→</span>
          </div>
        </div>
      </div>
    </div>
  );
};

// ─── Report Bureau ───
const ReportBureau = () => {
  const [sel, setSel] = useState(null);
  const a = [
    { id: "board", l: "Board", d: "Strategic summary for governance oversight", i: "▣" },
    { id: "family", l: "Family", d: "Plain-language with Aletheia guidance", i: "♡" },
    { id: "regulator", l: "Regulator", d: "Compliance documentation and audit trail", i: "⚖" },
    { id: "technical", l: "Technical", d: "System health and data lineage", i: "⚙" },
  ];
  return (
    <div>
      <p style={{ fontFamily: F.body, fontSize: "14px", color: C.silver, lineHeight: 1.7, marginBottom: "24px" }}>
        One truth. Four windows. Select an audience to generate the Meridian Signal report.
      </p>
      <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: "10px" }}>
        {a.map((x, i) => (
          <Fade key={x.id} delay={i * 200 + 400} duration={1200}>
            <div onClick={() => setSel(x.id)} style={{
              padding: "24px 20px", border: `1px solid ${sel === x.id ? C.warmGold : C.slate}`,
              borderRadius: "2px", cursor: "pointer",
              background: sel === x.id ? C.whisper : "transparent",
              transition: "all 0.5s ease", textAlign: "center",
            }}>
              <div style={{ fontFamily: F.display, fontSize: "24px", color: C.warmGold, marginBottom: "10px" }}>{x.i}</div>
              <h4 style={{ fontFamily: F.display, fontSize: "15px", fontWeight: 400, color: C.cream, margin: "0 0 4px 0" }}>{x.l}</h4>
              <p style={{ fontFamily: F.body, fontSize: "11px", color: C.smoke, margin: 0 }}>{x.d}</p>
            </div>
          </Fade>
        ))}
      </div>
      {sel && (
        <Fade delay={200} duration={1000}>
          <div style={{ marginTop: "20px", textAlign: "center" }}>
            <button style={{
              fontFamily: F.mono, fontSize: "10px", textTransform: "uppercase", letterSpacing: "2px",
              background: C.warmGold, border: "none", color: C.midnight,
              padding: "11px 28px", cursor: "pointer", borderRadius: "2px", fontWeight: 600,
            }}>
              Generate Meridian Signal — {a.find(x => x.id === sel)?.l}
            </button>
          </div>
        </Fade>
      )}
    </div>
  );
};

// ─── Governance ───
const GovView = () => (
  <div>
    {[
      { t: "Foundation Grant Rate Review", p: "high", e: "Family Impact Foundation", d: "Disbursement approaching 5% IRS minimum. Board review required before March 31." },
      { t: "Entity Registration Renewal", p: "medium", e: "3 Georgia Entities", d: "Annual Secretary of State filings due. Registered agent confirmation required." },
    ].map((a, i) => (
      <Fade key={i} delay={i * 300 + 500} duration={1200}>
        <div style={{ padding: "20px", border: `1px solid ${a.p === "high" ? C.copper : C.slate}`, borderRadius: "2px", marginBottom: "10px" }}>
          <div style={{ display: "flex", justifyContent: "space-between" }}>
            <div>
              <h4 style={{ fontFamily: F.display, fontSize: "15px", fontWeight: 400, color: C.cream, margin: "0 0 3px 0" }}>{a.t}</h4>
              <p style={{ fontFamily: F.mono, fontSize: "9px", color: C.smoke, textTransform: "uppercase", letterSpacing: "1px", margin: "0 0 8px 0" }}>{a.e}</p>
            </div>
            <span style={{
              fontFamily: F.mono, fontSize: "8px", textTransform: "uppercase", letterSpacing: "1.5px",
              color: a.p === "high" ? C.copper : C.smoke,
              border: `1px solid ${a.p === "high" ? C.copper : C.slate}`,
              padding: "3px 7px", borderRadius: "2px", alignSelf: "flex-start",
            }}>{a.p}</span>
          </div>
          <p style={{ fontFamily: F.body, fontSize: "13px", color: C.silver, lineHeight: 1.6, margin: 0 }}>{a.d}</p>
          <div style={{ display: "flex", gap: "10px", marginTop: "14px" }}>
            <button style={{ fontFamily: F.mono, fontSize: "9px", textTransform: "uppercase", letterSpacing: "1.5px", background: "transparent", border: `1px solid ${C.warmGold}`, color: C.warmGold, padding: "5px 14px", cursor: "pointer", borderRadius: "2px" }}>Review</button>
            <button style={{ fontFamily: F.mono, fontSize: "9px", textTransform: "uppercase", letterSpacing: "1.5px", background: "transparent", border: `1px solid ${C.slate}`, color: C.smoke, padding: "5px 14px", cursor: "pointer", borderRadius: "2px" }}>Defer</button>
          </div>
        </div>
      </Fade>
    ))}
  </div>
);

// ─── Scenarios ───
const ScenarioView = () => {
  const [lev, setLev] = useState(25);
  const [hor, setHor] = useState(10);
  const [risk, setRisk] = useState(50);
  const Sl = ({ label, value, onChange, min, max, unit }) => (
    <div style={{ marginBottom: "22px" }}>
      <div style={{ display: "flex", justifyContent: "space-between", marginBottom: "6px" }}>
        <span style={{ fontFamily: F.body, fontSize: "13px", color: C.silver }}>{label}</span>
        <span style={{ fontFamily: F.mono, fontSize: "11px", color: C.warmGold }}>{value}{unit}</span>
      </div>
      <input type="range" min={min} max={max} value={value} onChange={e => onChange(+e.target.value)} />
    </div>
  );
  return (
    <div>
      <p style={{ fontFamily: F.body, fontSize: "14px", color: C.silver, lineHeight: 1.7, marginBottom: "24px" }}>
        Adjust parameters. The system recalculates in real time.
      </p>
      <Sl label="Leverage Ratio" value={lev} onChange={setLev} min={0} max={80} unit="%" />
      <Sl label="Planning Horizon" value={hor} onChange={setHor} min={1} max={30} unit=" years" />
      <Sl label="Risk Tolerance" value={risk} onChange={setRisk} min={0} max={100} unit="" />
      <Rule w="100%" />
      <div style={{ padding: "18px", border: `1px solid ${C.slate}`, borderRadius: "2px", marginTop: "14px" }}>
        <p style={{ fontFamily: F.body, fontSize: "13px", color: C.parchment, lineHeight: 1.7, margin: 0, fontStyle: "italic" }}>
          At {lev}% leverage over {hor} years, the Trust maintains a resilience score of {Math.max(60, 95 - lev * 0.5 + hor * 0.3).toFixed(0)}.
          {lev > 50 ? " Aletheia recommends reviewing the governance cascade before proceeding." : " Current position supports this configuration."}
        </p>
      </div>
    </div>
  );
};

// ═══════════════════════════════════════════════════════════════
// THE COMPLETE EXPERIENCE
// Gate → Vestibule → Institution
// ═══════════════════════════════════════════════════════════════
export default function Meridia() {
  const [stage, setStage] = useState("gate");
  const [member, setMember] = useState("architect");

  const handleSelectMember = (id) => {
    setMember(id);
    setStage("vestibule");
  };

  return (
    <>
      <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;0,600;1,400&family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;1,400&family=DM+Mono:wght@300;400&display=swap" rel="stylesheet" />
      {stage === "gate" && <TheGate onSelectMember={handleSelectMember} />}
      {stage === "vestibule" && <TheVestibule member={member} onComplete={() => setStage("institution")} />}
      {stage === "institution" && <Institution member={member} />}
    </>
  );
}

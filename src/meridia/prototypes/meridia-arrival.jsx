import { useState, useEffect, useRef } from "react";

// ═══════════════════════════════════════════════════════════════
// MERIDIA — The Arrival
// The plaque on the gate. The limestone façade. The sentry box.
// Before you enter the cathedral, you must arrive.
// ═══════════════════════════════════════════════════════════════

const COLORS = {
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
  deepBurgundy: "#4A1E2B",
  emerald: "#2D6B4F",
  copper: "#B87333",
  smoke: "#8892A8",
  silverSmoke: "#A8AEC0",
  whisper: "rgba(196, 162, 101, 0.08)",
  glow: "rgba(196, 162, 101, 0.15)",
};

const FONTS = {
  display: "'Playfair Display', 'Georgia', serif",
  body: "'Cormorant Garamond', 'Garamond', serif",
  accent: "'Spectral', 'Times New Roman', serif",
  mono: "'DM Mono', 'Courier New', monospace",
};

// ─── Grain texture ───
const GrainOverlay = () => (
  <div style={{
    position: "fixed", top: 0, left: 0, right: 0, bottom: 0,
    backgroundImage: `url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noise'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noise)' opacity='0.03'/%3E%3C/svg%3E")`,
    pointerEvents: "none", zIndex: 9999, opacity: 0.4,
  }} />
);

// ─── Gold divider ───
const GoldRule = ({ width = "60px", style = {} }) => (
  <div style={{
    width, height: "1px",
    background: `linear-gradient(90deg, transparent, ${COLORS.warmGold}, transparent)`,
    margin: "16px 0", ...style,
  }} />
);

// ─── Fade animation ───
const FadeIn = ({ children, delay = 0, style = {} }) => {
  const [visible, setVisible] = useState(false);
  useEffect(() => {
    const t = setTimeout(() => setVisible(true), delay);
    return () => clearTimeout(t);
  }, [delay]);
  return (
    <div style={{
      opacity: visible ? 1 : 0,
      transform: visible ? "translateY(0)" : "translateY(12px)",
      transition: `opacity 0.8s ease, transform 0.8s ease`,
      ...style,
    }}>{children}</div>
  );
};

// ═══════════════════════════════════════════════════════════════
// THE MERIDIA CREST — SVG Brand Mark
// ═══════════════════════════════════════════════════════════════
const MeridiaCrest = ({ size = 120, animated = false }) => {
  const [drawn, setDrawn] = useState(!animated);
  useEffect(() => {
    if (animated) {
      const t = setTimeout(() => setDrawn(true), 600);
      return () => clearTimeout(t);
    }
  }, [animated]);

  return (
    <svg width={size} height={size} viewBox="0 0 200 200" fill="none" xmlns="http://www.w3.org/2000/svg">
      {/* Outer ring */}
      <circle cx="100" cy="100" r="96" stroke={COLORS.warmGold} strokeWidth="0.5"
        opacity={drawn ? 0.3 : 0} style={{ transition: "opacity 1.5s ease" }} />
      <circle cx="100" cy="100" r="88" stroke={COLORS.warmGold} strokeWidth="1"
        strokeDasharray={drawn ? "0 0" : "553 553"}
        style={{
          transition: "stroke-dasharray 2s ease",
          strokeDashoffset: 0,
        }}
        opacity={drawn ? 0.6 : 0} />

      {/* Inner geometric — octagonal frame suggesting governance */}
      <path
        d={`M100 20 L155 45 L180 100 L155 155 L100 180 L45 155 L20 100 L45 45 Z`}
        stroke={COLORS.warmGold} strokeWidth="0.75" fill="none"
        opacity={drawn ? 0.25 : 0}
        style={{ transition: "opacity 1.8s ease 0.5s" }}
      />

      {/* The M — bespoke letterform */}
      <g opacity={drawn ? 1 : 0} style={{ transition: "opacity 1.2s ease 0.8s" }}>
        {/* Left stem */}
        <path d="M62 138 L62 68 L100 108 L138 68 L138 138"
          stroke={COLORS.warmGold} strokeWidth="2" fill="none"
          strokeLinecap="round" strokeLinejoin="round" />
        {/* Serifs — small cross strokes at base */}
        <line x1="56" y1="138" x2="68" y2="138" stroke={COLORS.warmGold} strokeWidth="1.5" />
        <line x1="132" y1="138" x2="144" y2="138" stroke={COLORS.warmGold} strokeWidth="1.5" />
        {/* Crown point — small diamond above the M */}
        <path d="M100 52 L104 58 L100 64 L96 58 Z"
          fill={COLORS.warmGold} opacity="0.8" />
      </g>

      {/* Cardinal points — subtle compass reference (FPS / positioning) */}
      <g opacity={drawn ? 0.3 : 0} style={{ transition: "opacity 2s ease 1.2s" }}>
        <line x1="100" y1="6" x2="100" y2="14" stroke={COLORS.warmGold} strokeWidth="0.75" />
        <line x1="100" y1="186" x2="100" y2="194" stroke={COLORS.warmGold} strokeWidth="0.75" />
        <line x1="6" y1="100" x2="14" y2="100" stroke={COLORS.warmGold} strokeWidth="0.75" />
        <line x1="186" y1="100" x2="194" y2="100" stroke={COLORS.warmGold} strokeWidth="0.75" />
      </g>
    </svg>
  );
};

// ═══════════════════════════════════════════════════════════════
// PHASE 1: THE GATE — Entry / Login
// Like arriving at the limestone façade
// ═══════════════════════════════════════════════════════════════
const TheGate = ({ onEnter }) => {
  const [phase, setPhase] = useState(0); // 0: arriving, 1: crest visible, 2: name visible, 3: ready
  const [hovering, setHovering] = useState(false);

  useEffect(() => {
    const timers = [
      setTimeout(() => setPhase(1), 800),
      setTimeout(() => setPhase(2), 2000),
      setTimeout(() => setPhase(3), 3200),
    ];
    return () => timers.forEach(clearTimeout);
  }, []);

  return (
    <div style={{
      position: "fixed", top: 0, left: 0, right: 0, bottom: 0,
      background: COLORS.midnight,
      display: "flex", flexDirection: "column",
      alignItems: "center", justifyContent: "center",
      zIndex: 1000,
    }}>
      <GrainOverlay />

      {/* Ambient gold glow behind crest */}
      <div style={{
        position: "absolute",
        width: "400px", height: "400px",
        borderRadius: "50%",
        background: `radial-gradient(circle, ${COLORS.glow} 0%, transparent 70%)`,
        opacity: phase >= 1 ? 0.4 : 0,
        transition: "opacity 2s ease",
        pointerEvents: "none",
      }} />

      {/* The Crest */}
      <div style={{
        opacity: phase >= 1 ? 1 : 0,
        transform: phase >= 1 ? "scale(1)" : "scale(0.9)",
        transition: "all 1.5s ease",
        marginBottom: "40px",
      }}>
        <MeridiaCrest size={140} animated={true} />
      </div>

      {/* The Name — like carved into stone above the door */}
      <div style={{
        opacity: phase >= 2 ? 1 : 0,
        transform: phase >= 2 ? "translateY(0)" : "translateY(8px)",
        transition: "all 1.2s ease",
        textAlign: "center",
      }}>
        <h1 style={{
          fontFamily: FONTS.display,
          fontSize: "42px",
          fontWeight: 400,
          color: COLORS.cream,
          letterSpacing: "8px",
          textTransform: "uppercase",
          margin: "0 0 8px 0",
        }}>
          Meridia
        </h1>

        <GoldRule width="120px" style={{ margin: "0 auto 12px" }} />

        <p style={{
          fontFamily: FONTS.mono,
          fontSize: "10px",
          color: COLORS.smoke,
          letterSpacing: "4px",
          textTransform: "uppercase",
          margin: 0,
        }}>
          Cognitive Infrastructure
        </p>
      </div>

      {/* The threshold — "Enter" */}
      <div style={{
        marginTop: "60px",
        opacity: phase >= 3 ? 1 : 0,
        transform: phase >= 3 ? "translateY(0)" : "translateY(12px)",
        transition: "all 1s ease",
        textAlign: "center",
      }}>
        <div
          onClick={onEnter}
          onMouseEnter={() => setHovering(true)}
          onMouseLeave={() => setHovering(false)}
          style={{
            padding: "14px 48px",
            border: `1px solid ${hovering ? COLORS.warmGold : COLORS.slate}`,
            borderRadius: "2px",
            cursor: "pointer",
            background: hovering ? COLORS.whisper : "transparent",
            transition: "all 0.4s ease",
          }}
        >
          <span style={{
            fontFamily: FONTS.mono,
            fontSize: "10px",
            letterSpacing: "3px",
            textTransform: "uppercase",
            color: hovering ? COLORS.warmGold : COLORS.silverSmoke,
            transition: "color 0.4s ease",
          }}>
            Enter
          </span>
        </div>

        <p style={{
          fontFamily: FONTS.body,
          fontSize: "12px",
          color: `${COLORS.smoke}80`,
          fontStyle: "italic",
          marginTop: "20px",
        }}>
          Governed by Integra · Powered by Eden Intelligence Group
        </p>
      </div>

      {/* Subtle corner accents — like brass fittings on a door */}
      {phase >= 1 && (
        <>
          <CornerAccent position="top-left" />
          <CornerAccent position="top-right" />
          <CornerAccent position="bottom-left" />
          <CornerAccent position="bottom-right" />
        </>
      )}
    </div>
  );
};

// Corner decorative accents
const CornerAccent = ({ position }) => {
  const styles = {
    "top-left": { top: "32px", left: "32px" },
    "top-right": { top: "32px", right: "32px", transform: "scaleX(-1)" },
    "bottom-left": { bottom: "32px", left: "32px", transform: "scaleY(-1)" },
    "bottom-right": { bottom: "32px", right: "32px", transform: "scale(-1)" },
  };
  return (
    <svg width="40" height="40" viewBox="0 0 40 40" fill="none"
      style={{ position: "fixed", ...styles[position], opacity: 0.2 }}>
      <line x1="0" y1="0" x2="0" y2="24" stroke={COLORS.warmGold} strokeWidth="1" />
      <line x1="0" y1="0" x2="24" y2="0" stroke={COLORS.warmGold} strokeWidth="1" />
    </svg>
  );
};

// ═══════════════════════════════════════════════════════════════
// PHASE 2: THE VESTIBULE — Transition / Welcome
// The moment between the door and the room
// ═══════════════════════════════════════════════════════════════
const TheVestibule = ({ onComplete, memberName = "Mr. Neal" }) => {
  const [phase, setPhase] = useState(0);

  useEffect(() => {
    const timers = [
      setTimeout(() => setPhase(1), 400),
      setTimeout(() => setPhase(2), 1800),
      setTimeout(() => setPhase(3), 3200),
      setTimeout(() => onComplete(), 5000),
    ];
    return () => timers.forEach(clearTimeout);
  }, []);

  const now = new Date();
  const hour = now.getHours();
  const greeting = hour < 12 ? "Good morning" : hour < 17 ? "Good afternoon" : "Good evening";

  return (
    <div style={{
      position: "fixed", top: 0, left: 0, right: 0, bottom: 0,
      background: COLORS.midnight,
      display: "flex", flexDirection: "column",
      alignItems: "center", justifyContent: "center",
      zIndex: 1000,
    }}>
      <GrainOverlay />

      {/* Small crest — now you're inside, it's smaller, like above a mantel */}
      <div style={{
        opacity: phase >= 1 ? 1 : 0,
        transition: "opacity 1s ease",
        marginBottom: "32px",
      }}>
        <MeridiaCrest size={60} animated={false} />
      </div>

      {/* Personal greeting */}
      <div style={{
        opacity: phase >= 1 ? 1 : 0,
        transform: phase >= 1 ? "translateY(0)" : "translateY(8px)",
        transition: "all 1s ease",
        textAlign: "center",
      }}>
        <h2 style={{
          fontFamily: FONTS.display,
          fontSize: "28px",
          fontWeight: 400,
          color: COLORS.cream,
          letterSpacing: "1px",
          margin: "0 0 6px 0",
        }}>
          {greeting}, {memberName}
        </h2>
        <p style={{
          fontFamily: FONTS.body,
          fontSize: "14px",
          color: COLORS.smoke,
          fontStyle: "italic",
          margin: 0,
        }}>
          {now.toLocaleDateString("en-US", { weekday: "long", month: "long", day: "numeric", year: "numeric" })}
        </p>
      </div>

      {/* Status line — what's happened while you were away */}
      <div style={{
        marginTop: "40px",
        opacity: phase >= 2 ? 1 : 0,
        transform: phase >= 2 ? "translateY(0)" : "translateY(8px)",
        transition: "all 1s ease",
        textAlign: "center",
      }}>
        <GoldRule width="60px" style={{ margin: "0 auto 16px" }} />
        <div style={{
          display: "flex", gap: "32px", justifyContent: "center",
        }}>
          {[
            { label: "Signals", value: "6", status: "new" },
            { label: "Governance", value: "2", status: "pending" },
            { label: "Entities", value: "3", status: "healthy" },
          ].map((item, i) => (
            <div key={i} style={{ textAlign: "center" }}>
              <span style={{
                fontFamily: FONTS.display, fontSize: "24px",
                color: COLORS.warmGold, display: "block",
              }}>
                {item.value}
              </span>
              <span style={{
                fontFamily: FONTS.mono, fontSize: "9px",
                color: COLORS.smoke, textTransform: "uppercase",
                letterSpacing: "2px",
              }}>
                {item.label}
              </span>
            </div>
          ))}
        </div>
      </div>

      {/* Aletheia whisper */}
      <div style={{
        marginTop: "48px",
        opacity: phase >= 3 ? 1 : 0,
        transform: phase >= 3 ? "translateY(0)" : "translateY(6px)",
        transition: "all 1s ease",
        textAlign: "center",
        maxWidth: "480px",
      }}>
        <p style={{
          fontFamily: FONTS.body,
          fontSize: "15px",
          color: COLORS.parchment,
          fontStyle: "italic",
          lineHeight: 1.7,
          margin: 0,
        }}>
          "Two items require your attention today. Your Foundation review is approaching deadline, 
          and a new SBA pathway has opened for Turner Seminary. I've prepared both."
        </p>
        <p style={{
          fontFamily: FONTS.mono,
          fontSize: "9px",
          color: COLORS.smoke,
          textTransform: "uppercase",
          letterSpacing: "2px",
          marginTop: "12px",
        }}>
          — Aletheia
        </p>
      </div>

      {/* Fade to main */}
      <div style={{
        position: "fixed", top: 0, left: 0, right: 0, bottom: 0,
        background: COLORS.midnight,
        opacity: phase >= 3 ? 0 : 0,
        pointerEvents: "none",
        transition: "opacity 1.5s ease 4s",
      }} />
    </div>
  );
};

// ═══════════════════════════════════════════════════════════════
// PHASE 3: THE INSTITUTION — Main Application
// (abbreviated for this artifact — focus is on arrival)
// ═══════════════════════════════════════════════════════════════

const LiveClock = () => {
  const [time, setTime] = useState(new Date());
  useEffect(() => {
    const i = setInterval(() => setTime(new Date()), 1000);
    return () => clearInterval(i);
  }, []);
  return (
    <span style={{ fontFamily: FONTS.mono, fontSize: "11px", color: COLORS.smoke, letterSpacing: "2px" }}>
      {time.toLocaleTimeString("en-US", { hour: "2-digit", minute: "2-digit", hour12: false })}
      <span style={{ opacity: 0.4, margin: "0 6px" }}>·</span>
      {time.toLocaleDateString("en-US", { weekday: "long", month: "long", day: "numeric" })}
    </span>
  );
};

// Navigation
const NAV_SECTIONS = [
  { id: "residence", label: "The Residence", icon: "◆", available: true, desc: "Your position at a glance" },
  { id: "signal", label: "Meridian Signal", icon: "◈", available: true, desc: "Intelligence feed" },
  { id: "governance", label: "The Library", icon: "▣", available: true, desc: "Governance & oversight" },
  { id: "entities", label: "The Gallery", icon: "▤", available: true, desc: "Entity collection" },
  { id: "scenarios", label: "The Study", icon: "◧", available: true, desc: "Scenario modeling" },
  { id: "reports", label: "The Bureau", icon: "▥", available: true, desc: "Report generation" },
  { id: "crown", label: "WayPoint Crown", icon: "♛", available: true, desc: "Family office" },
  { id: "renaissance", label: "WP Renaissance", icon: "✦", available: false, desc: "Re-entry pathways" },
  { id: "edge", label: "WayPoint Edge", icon: "⬡", available: false, desc: "Vertical-specific" },
  { id: "crowns-eye", label: "Crown's Eye", icon: "◉", available: false, desc: "Education" },
  { id: "wearable", label: "The Wearable", icon: "◎", available: false, desc: "Phase 3" },
];

const SIGNALS = [
  { time: "09:14", type: "regulatory", text: "FDIC guidance update: CRA modernization rule — comment period closing March 15", urgency: "watch" },
  { time: "08:47", type: "opportunity", text: "SBA 7(a) lending threshold increased to $500K for qualified nonprofits — Turner Seminary eligible", urgency: "action" },
  { time: "08:12", type: "market", text: "Pinnacle Financial Partners Q4 earnings beat — post-merger integration ahead of schedule", urgency: "info" },
  { time: "07:30", type: "governance", text: "Foundation grant disbursement approaching 5% minimum — Q1 review recommended", urgency: "watch" },
  { time: "Yesterday", type: "compliance", text: "Georgia Secretary of State annual registration renewal window opens — 3 entities due", urgency: "action" },
  { time: "Yesterday", type: "market", text: "10-year Treasury yield at 4.12% — line of credit rate adjustment may trigger April", urgency: "info" },
];

const ENTITIES = [
  { name: "Crown Legacy Trust", type: "Irrevocable Trust", jurisdiction: "Delaware", status: "healthy", aum: "$12.4M" },
  { name: "Family Impact Foundation", type: "501(c)(3)", jurisdiction: "Georgia", status: "watch", aum: "$4.2M" },
  { name: "Crown Holdings LLC", type: "Operating Entity", jurisdiction: "Georgia", status: "healthy", aum: "$3.1M" },
];

// ─── Trust Index ───
const TrustIndex = ({ score = 88 }) => {
  const [animScore, setAnimScore] = useState(0);
  useEffect(() => {
    let s = 0;
    const step = () => { s += 1; if (s <= score) { setAnimScore(s); requestAnimationFrame(step); } };
    setTimeout(step, 800);
  }, [score]);
  const dims = [
    { name: "Financial", score: 92 }, { name: "Stewardship", score: 81 },
    { name: "Mission", score: 88 }, { name: "Governance", score: 91 },
  ];
  return (
    <div style={{ padding: "24px 0" }}>
      <div style={{ display: "flex", alignItems: "baseline", gap: "8px", marginBottom: "20px" }}>
        <span style={{ fontFamily: FONTS.display, fontSize: "56px", fontWeight: 400, color: COLORS.warmGold, lineHeight: 1 }}>
          {animScore}
        </span>
        <span style={{ fontFamily: FONTS.body, fontSize: "14px", color: COLORS.smoke }}>of 100</span>
      </div>
      <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: "12px" }}>
        {dims.map((d, i) => (
          <div key={d.name} style={{ padding: "12px 0" }}>
            <div style={{ display: "flex", justifyContent: "space-between", marginBottom: "6px" }}>
              <span style={{ fontFamily: FONTS.body, fontSize: "13px", color: COLORS.silverSmoke }}>{d.name}</span>
              <span style={{ fontFamily: FONTS.mono, fontSize: "11px", color: COLORS.warmGold }}>{d.score}</span>
            </div>
            <div style={{ height: "2px", background: COLORS.slate, borderRadius: "1px", overflow: "hidden" }}>
              <div style={{
                height: "100%", width: `${d.score}%`,
                background: `linear-gradient(90deg, ${COLORS.warmGold}, ${COLORS.brightGold})`,
                transition: "width 1.5s ease", transitionDelay: `${i * 200 + 1000}ms`,
              }} />
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

// ─── Main Institution UI ───
const TheInstitution = () => {
  const [activeRoom, setActiveRoom] = useState("residence");
  const [aletheiaOpen, setAletheiaOpen] = useState(true);
  const [navHovered, setNavHovered] = useState(null);

  const roomTitles = {
    residence: "The Residence", signal: "Meridian Signal", governance: "The Library",
    entities: "The Gallery", scenarios: "The Study", reports: "The Bureau",
    crown: "WayPoint Crown", renaissance: "WayPoint Renaissance",
    edge: "WayPoint Edge", "crowns-eye": "Crown's Eye", wearable: "The Wearable",
  };
  const roomSubtitles = {
    residence: "Your financial position, maintained and ready",
    signal: "Intelligence that touches your world",
    governance: "Oversight, approvals, and governance cascade",
    entities: "Your collection, every entity mapped",
    scenarios: "Model the future before you live it",
    reports: "One truth, four windows",
    crown: "Multi-generational governance",
  };

  const urgencyColors = { action: COLORS.warmGold, watch: COLORS.copper, info: COLORS.smoke };
  const statusColors = { healthy: COLORS.emerald, watch: COLORS.copper, alert: COLORS.burgundy };

  return (
    <div style={{
      minHeight: "100vh", background: COLORS.midnight, display: "flex",
      fontFamily: FONTS.body, color: COLORS.cream, position: "relative",
    }}>
      <GrainOverlay />

      <style>{`
        @keyframes pulse { 0%, 100% { opacity: 0.2; } 50% { opacity: 0.8; } }
        input[type="range"] { -webkit-appearance: none; background: ${COLORS.slate}; border-radius: 1px; outline: none; height: 2px; }
        input[type="range"]::-webkit-slider-thumb { -webkit-appearance: none; width: 12px; height: 12px; border-radius: 50%; background: ${COLORS.warmGold}; cursor: pointer; }
        ::-webkit-scrollbar { width: 4px; }
        ::-webkit-scrollbar-track { background: transparent; }
        ::-webkit-scrollbar-thumb { background: ${COLORS.slate}; border-radius: 2px; }
        ::placeholder { color: ${COLORS.smoke}; }
      `}</style>

      {/* ═══ LEFT NAV — The Hallway ═══ */}
      <nav style={{
        width: "240px", background: COLORS.deepNavy,
        borderRight: `1px solid ${COLORS.whisper}`,
        display: "flex", flexDirection: "column",
        position: "fixed", top: 0, bottom: 0, left: 0, zIndex: 50,
      }}>
        {/* Crest + wordmark in nav */}
        <div style={{ padding: "24px 20px 16px", display: "flex", alignItems: "center", gap: "14px" }}>
          <MeridiaCrest size={40} />
          <div>
            <h1 style={{
              fontFamily: FONTS.display, fontSize: "17px", fontWeight: 400,
              color: COLORS.cream, margin: 0, letterSpacing: "2px",
              textTransform: "uppercase",
            }}>
              Meridia
            </h1>
            <p style={{
              fontFamily: FONTS.mono, fontSize: "7px", color: COLORS.smoke,
              textTransform: "uppercase", letterSpacing: "2.5px", margin: 0,
            }}>
              Integra Core · v1.0
            </p>
          </div>
        </div>

        <GoldRule width="calc(100% - 40px)" style={{ margin: "0 20px 8px" }} />

        {/* Member identity */}
        <div style={{ padding: "8px 20px 16px" }}>
          <p style={{
            fontFamily: FONTS.body, fontSize: "13px", color: COLORS.silverSmoke,
            margin: "0 0 2px 0",
          }}>
            Aliman Neal
          </p>
          <p style={{
            fontFamily: FONTS.mono, fontSize: "8px", color: COLORS.smoke,
            textTransform: "uppercase", letterSpacing: "2px", margin: 0,
          }}>
            Architect · Principal
          </p>
        </div>

        {/* Rooms */}
        <div style={{ flex: 1, overflowY: "auto", padding: "4px 0" }}>
          {NAV_SECTIONS.map((s) => (
            <div key={s.id}
              onClick={() => s.available && setActiveRoom(s.id)}
              onMouseEnter={() => setNavHovered(s.id)}
              onMouseLeave={() => setNavHovered(null)}
              style={{
                padding: "9px 20px", display: "flex", alignItems: "center", gap: "12px",
                cursor: s.available ? "pointer" : "default",
                opacity: s.available ? 1 : 0.3,
                background: activeRoom === s.id ? COLORS.whisper : navHovered === s.id && s.available ? COLORS.whisper : "transparent",
                borderLeft: activeRoom === s.id ? `2px solid ${COLORS.warmGold}` : "2px solid transparent",
                transition: "all 0.3s ease",
              }}>
              <span style={{
                fontFamily: FONTS.display, fontSize: "11px",
                color: activeRoom === s.id ? COLORS.warmGold : COLORS.smoke,
                width: "18px", textAlign: "center",
              }}>{s.icon}</span>
              <div>
                <span style={{
                  fontFamily: FONTS.body, fontSize: "13px",
                  color: activeRoom === s.id ? COLORS.cream : COLORS.silverSmoke,
                }}>{s.label}</span>
                {navHovered === s.id && (
                  <span style={{
                    fontFamily: FONTS.mono, fontSize: "8px", color: COLORS.smoke, display: "block",
                  }}>{s.desc}</span>
                )}
              </div>
              {!s.available && (
                <span style={{
                  marginLeft: "auto", fontFamily: FONTS.mono, fontSize: "7px", color: COLORS.smoke,
                  border: `1px solid ${COLORS.slate}`, padding: "2px 5px", borderRadius: "2px",
                }}>SOON</span>
              )}
            </div>
          ))}
        </div>

        {/* Footer */}
        <div style={{ padding: "14px 20px", borderTop: `1px solid ${COLORS.whisper}` }}>
          <p style={{
            fontFamily: FONTS.mono, fontSize: "7px", color: COLORS.smoke,
            textTransform: "uppercase", letterSpacing: "2px", margin: "0 0 3px 0",
          }}>Eden Intelligence Group</p>
          <p style={{ fontFamily: FONTS.mono, fontSize: "7px", color: `${COLORS.smoke}60`, margin: 0 }}>
            Governance as a Service
          </p>
        </div>
      </nav>

      {/* ═══ MAIN CONTENT ═══ */}
      <main style={{
        flex: 1, marginLeft: "240px",
        marginRight: aletheiaOpen ? "360px" : "0px",
        transition: "margin-right 0.5s ease",
        minHeight: "100vh",
      }}>
        {/* Top bar */}
        <header style={{
          padding: "16px 36px", display: "flex", justifyContent: "space-between", alignItems: "center",
          borderBottom: `1px solid ${COLORS.whisper}`,
          position: "sticky", top: 0, background: `${COLORS.midnight}ee`,
          backdropFilter: "blur(20px)", zIndex: 40,
        }}>
          <LiveClock />
          <div style={{ display: "flex", alignItems: "center", gap: "16px" }}>
            <span style={{
              fontFamily: FONTS.mono, fontSize: "9px", color: COLORS.emerald,
              textTransform: "uppercase", letterSpacing: "2px",
              display: "flex", alignItems: "center", gap: "6px",
            }}>
              <span style={{ width: "5px", height: "5px", borderRadius: "50%", background: COLORS.emerald }} />
              Healthy
            </span>
            <div onClick={() => setAletheiaOpen(!aletheiaOpen)} style={{
              width: "28px", height: "28px", borderRadius: "50%",
              border: `1px solid ${aletheiaOpen ? COLORS.warmGold : COLORS.slate}`,
              display: "flex", alignItems: "center", justifyContent: "center",
              cursor: "pointer", fontFamily: FONTS.display, fontSize: "12px",
              color: aletheiaOpen ? COLORS.warmGold : COLORS.smoke,
              transition: "all 0.3s ease",
            }}>A</div>
          </div>
        </header>

        {/* Room header */}
        <div style={{ padding: "40px 36px 0" }}>
          <FadeIn key={activeRoom}>
            <p style={{
              fontFamily: FONTS.mono, fontSize: "9px", color: COLORS.smoke,
              textTransform: "uppercase", letterSpacing: "3px", margin: "0 0 6px 0",
            }}>
              {["crown", "renaissance", "edge"].includes(activeRoom) ? "WayPoint" : "Meridia"}
            </p>
            <h2 style={{
              fontFamily: FONTS.display, fontSize: "30px", fontWeight: 400,
              color: COLORS.cream, margin: "0 0 4px 0", letterSpacing: "0.5px",
            }}>{roomTitles[activeRoom]}</h2>
            {roomSubtitles[activeRoom] && (
              <p style={{
                fontFamily: FONTS.body, fontSize: "14px", color: COLORS.smoke,
                fontStyle: "italic", margin: 0,
              }}>{roomSubtitles[activeRoom]}</p>
            )}
            <GoldRule width="80px" style={{ margin: "16px 0 0" }} />
          </FadeIn>
        </div>

        {/* Room content */}
        <div style={{ padding: "28px 36px 60px" }}>
          {activeRoom === "residence" && (
            <div>
              {/* Position metrics */}
              <FadeIn delay={200}>
                <div style={{ display: "grid", gridTemplateColumns: "repeat(4, 1fr)", gap: "1px", background: COLORS.slate, borderRadius: "2px", overflow: "hidden" }}>
                  {[
                    { label: "Net Worth", value: "$19.6M", change: "+4.2%", up: true },
                    { label: "Liquidity", value: "$2.3M", change: "+1.8%", up: true },
                    { label: "Obligations", value: "$416K", change: "-2.1%", up: false },
                    { label: "Resilience", value: "95", change: "+3", up: true, suffix: "/100" },
                  ].map((m, i) => (
                    <div key={i} style={{ background: COLORS.deepNavy, padding: "22px 18px" }}>
                      <p style={{ fontFamily: FONTS.mono, fontSize: "9px", textTransform: "uppercase", letterSpacing: "2px", color: COLORS.smoke, margin: "0 0 8px 0" }}>{m.label}</p>
                      <div style={{ display: "flex", alignItems: "baseline", gap: "3px" }}>
                        <span style={{ fontFamily: FONTS.display, fontSize: "26px", fontWeight: 400, color: COLORS.cream }}>{m.value}</span>
                        {m.suffix && <span style={{ fontFamily: FONTS.body, fontSize: "12px", color: COLORS.smoke }}>{m.suffix}</span>}
                      </div>
                      <span style={{ fontFamily: FONTS.mono, fontSize: "10px", color: m.up ? COLORS.emerald : COLORS.warmGold, marginTop: "4px", display: "inline-block" }}>
                        {m.up ? "↑" : "↓"} {m.change}
                      </span>
                    </div>
                  ))}
                </div>
              </FadeIn>

              <div style={{ marginTop: "36px", display: "grid", gridTemplateColumns: "1fr 1fr", gap: "36px" }}>
                <FadeIn delay={400}>
                  <div>
                    <h3 style={{ fontFamily: FONTS.display, fontSize: "17px", fontWeight: 400, color: COLORS.cream, margin: "0 0 2px 0" }}>Trust Index</h3>
                    <p style={{ fontFamily: FONTS.mono, fontSize: "9px", color: COLORS.smoke, textTransform: "uppercase", letterSpacing: "2px", margin: 0 }}>Composite governance score</p>
                    <TrustIndex score={88} />
                  </div>
                </FadeIn>
                <FadeIn delay={600}>
                  <div>
                    <h3 style={{ fontFamily: FONTS.display, fontSize: "17px", fontWeight: 400, color: COLORS.cream, margin: "0 0 2px 0" }}>Latest Signal</h3>
                    <p style={{ fontFamily: FONTS.mono, fontSize: "9px", color: COLORS.smoke, textTransform: "uppercase", letterSpacing: "2px", margin: "0 0 8px 0" }}>Top developments</p>
                    {SIGNALS.slice(0, 3).map((s, i) => (
                      <FadeIn key={i} delay={i * 150 + 700}>
                        <div style={{ padding: "14px 0", borderBottom: `1px solid ${COLORS.whisper}`, display: "flex", gap: "14px" }}>
                          <div style={{ width: "5px", height: "5px", borderRadius: "50%", background: urgencyColors[s.urgency], marginTop: "8px" }} />
                          <div>
                            <p style={{ fontFamily: FONTS.body, fontSize: "13px", color: COLORS.cream, lineHeight: 1.6, margin: 0 }}>{s.text}</p>
                            <div style={{ display: "flex", gap: "10px", marginTop: "4px" }}>
                              <span style={{ fontFamily: FONTS.mono, fontSize: "9px", color: COLORS.smoke }}>{s.time}</span>
                              <span style={{ fontFamily: FONTS.mono, fontSize: "8px", color: urgencyColors[s.urgency], textTransform: "uppercase", letterSpacing: "1.5px" }}>{s.urgency}</span>
                            </div>
                          </div>
                        </div>
                      </FadeIn>
                    ))}
                  </div>
                </FadeIn>
              </div>
            </div>
          )}

          {activeRoom === "signal" && SIGNALS.map((s, i) => (
            <FadeIn key={i} delay={i * 120 + 200}>
              <div style={{ padding: "16px 0", borderBottom: `1px solid ${COLORS.whisper}`, display: "flex", gap: "14px", cursor: "pointer" }}>
                <div style={{ width: "5px", height: "5px", borderRadius: "50%", background: urgencyColors[s.urgency], marginTop: "8px" }} />
                <div style={{ flex: 1 }}>
                  <p style={{ fontFamily: FONTS.body, fontSize: "14px", color: COLORS.cream, lineHeight: 1.6, margin: 0 }}>{s.text}</p>
                  <div style={{ display: "flex", gap: "10px", marginTop: "5px" }}>
                    <span style={{ fontFamily: FONTS.mono, fontSize: "9px", color: COLORS.smoke }}>{s.time}</span>
                    <span style={{ fontFamily: FONTS.mono, fontSize: "8px", color: urgencyColors[s.urgency], textTransform: "uppercase", letterSpacing: "1.5px" }}>{s.urgency}</span>
                  </div>
                </div>
              </div>
            </FadeIn>
          ))}

          {activeRoom === "entities" && ENTITIES.map((e, i) => (
            <FadeIn key={i} delay={i * 180 + 300}>
              <div style={{
                padding: "22px", border: `1px solid ${COLORS.slate}`, borderRadius: "2px",
                marginBottom: "10px", cursor: "pointer", transition: "border-color 0.3s ease",
              }}
              onMouseEnter={ev => ev.currentTarget.style.borderColor = COLORS.warmGold}
              onMouseLeave={ev => ev.currentTarget.style.borderColor = COLORS.slate}>
                <div style={{ display: "flex", justifyContent: "space-between" }}>
                  <div>
                    <h3 style={{ fontFamily: FONTS.display, fontSize: "17px", fontWeight: 400, color: COLORS.cream, margin: "0 0 3px 0" }}>{e.name}</h3>
                    <p style={{ fontFamily: FONTS.body, fontSize: "12px", color: COLORS.smoke, margin: 0 }}>{e.type} · {e.jurisdiction}</p>
                  </div>
                  <div style={{ textAlign: "right" }}>
                    <span style={{ fontFamily: FONTS.display, fontSize: "19px", color: COLORS.warmGold }}>{e.aum}</span>
                    <div style={{ display: "flex", alignItems: "center", gap: "5px", justifyContent: "flex-end", marginTop: "3px" }}>
                      <div style={{ width: "5px", height: "5px", borderRadius: "50%", background: statusColors[e.status] }} />
                      <span style={{ fontFamily: FONTS.mono, fontSize: "8px", textTransform: "uppercase", letterSpacing: "1.5px", color: statusColors[e.status] }}>{e.status}</span>
                    </div>
                  </div>
                </div>
              </div>
            </FadeIn>
          ))}

          {activeRoom === "reports" && (
            <ReportBureau />
          )}

          {activeRoom === "governance" && (
            <GovernanceView />
          )}

          {activeRoom === "scenarios" && (
            <ScenarioView />
          )}

          {(activeRoom === "crown" || activeRoom === "renaissance" || activeRoom === "edge" || activeRoom === "crowns-eye" || activeRoom === "wearable") && (
            <FadeIn delay={200}>
              <div style={{ padding: "56px 36px", border: `1px solid ${COLORS.slate}`, borderRadius: "2px", textAlign: "center" }}>
                <p style={{ fontFamily: FONTS.mono, fontSize: "9px", color: COLORS.smoke, textTransform: "uppercase", letterSpacing: "3px", margin: "0 0 14px 0" }}>
                  {activeRoom === "crown" ? "Full suite activates with live data" : "This wing is under construction"}
                </p>
                <h3 style={{ fontFamily: FONTS.display, fontSize: "22px", fontWeight: 400, color: COLORS.warmGold, margin: "0 0 10px 0" }}>{roomTitles[activeRoom]}</h3>
                <p style={{ fontFamily: FONTS.body, fontSize: "14px", color: COLORS.silverSmoke, lineHeight: 1.7, maxWidth: "400px", margin: "0 auto" }}>
                  The hallway is here. The door exists. The room is being prepared with the care it deserves.
                </p>
              </div>
            </FadeIn>
          )}
        </div>
      </main>

      {/* ═══ ALETHEIA PANEL ═══ */}
      <div style={{
        position: "fixed", right: 0, top: 0, bottom: 0,
        width: aletheiaOpen ? "360px" : "0px",
        background: COLORS.deepNavy,
        borderLeft: aletheiaOpen ? `1px solid ${COLORS.whisper}` : "none",
        transition: "width 0.5s ease",
        overflow: "hidden", zIndex: 100,
        display: "flex", flexDirection: "column",
      }}>
        <div style={{ padding: "24px 20px 16px", borderBottom: `1px solid ${COLORS.whisper}` }}>
          <div style={{ display: "flex", alignItems: "center", gap: "12px" }}>
            <div style={{
              width: "30px", height: "30px", borderRadius: "50%",
              border: `1px solid ${COLORS.warmGold}`,
              display: "flex", alignItems: "center", justifyContent: "center",
              fontFamily: FONTS.display, fontSize: "13px", color: COLORS.warmGold,
            }}>A</div>
            <div>
              <h3 style={{ fontFamily: FONTS.display, fontSize: "15px", fontWeight: 400, color: COLORS.cream, margin: 0 }}>Aletheia</h3>
              <p style={{ fontFamily: FONTS.mono, fontSize: "8px", color: COLORS.smoke, textTransform: "uppercase", letterSpacing: "2px", margin: 0 }}>Your Steward</p>
            </div>
          </div>
        </div>
        <div style={{ flex: 1, padding: "18px 20px", overflowY: "auto" }}>
          {[
            "Good morning. Three things have changed since we last spoke.",
            "The Foundation's grant disbursement rate is approaching the 5% minimum threshold. I recommend a governance review before Q1 close.",
            "An SBA lending threshold change creates a new pathway for Turner Seminary. I've prepared a brief.",
            "Your Georgia entity registrations open next week. Shall I walk you through what's due?",
          ].map((msg, i) => (
            <FadeIn key={i} delay={i * 1000 + 500}>
              <div style={{ marginBottom: "18px" }}>
                <p style={{ fontFamily: FONTS.body, fontSize: "14px", color: COLORS.parchment, lineHeight: 1.7, margin: 0 }}>{msg}</p>
                {i === 0 && <GoldRule width="40px" />}
              </div>
            </FadeIn>
          ))}
        </div>
        <div style={{ padding: "14px 20px", borderTop: `1px solid ${COLORS.whisper}` }}>
          <div style={{ display: "flex", border: `1px solid ${COLORS.slate}`, borderRadius: "2px", padding: "9px 12px" }}>
            <input placeholder="Ask Aletheia..." style={{
              flex: 1, background: "transparent", border: "none", outline: "none",
              fontFamily: FONTS.body, fontSize: "13px", color: COLORS.cream,
            }} />
            <span style={{ color: COLORS.warmGold, cursor: "pointer" }}>→</span>
          </div>
        </div>
      </div>
    </div>
  );
};

// ─── Report Bureau ───
const ReportBureau = () => {
  const [sel, setSel] = useState(null);
  const audiences = [
    { id: "board", label: "Board", desc: "Strategic summary for governance oversight", icon: "▣" },
    { id: "family", label: "Family", desc: "Plain-language with Aletheia guidance", icon: "♡" },
    { id: "regulator", label: "Regulator", desc: "Compliance documentation and audit trail", icon: "⚖" },
    { id: "technical", label: "Technical", desc: "System health and data lineage", icon: "⚙" },
  ];
  return (
    <div>
      <p style={{ fontFamily: FONTS.body, fontSize: "14px", color: COLORS.silverSmoke, lineHeight: 1.7, marginBottom: "24px" }}>
        One truth. Four windows. Select an audience to generate the Meridian Signal report.
      </p>
      <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: "10px" }}>
        {audiences.map((a, i) => (
          <FadeIn key={a.id} delay={i * 120 + 200}>
            <div onClick={() => setSel(a.id)} style={{
              padding: "24px 20px", border: `1px solid ${sel === a.id ? COLORS.warmGold : COLORS.slate}`,
              borderRadius: "2px", cursor: "pointer",
              background: sel === a.id ? COLORS.whisper : "transparent",
              transition: "all 0.3s ease", textAlign: "center",
            }}>
              <div style={{ fontFamily: FONTS.display, fontSize: "24px", color: COLORS.warmGold, marginBottom: "10px" }}>{a.icon}</div>
              <h4 style={{ fontFamily: FONTS.display, fontSize: "15px", fontWeight: 400, color: COLORS.cream, margin: "0 0 4px 0" }}>{a.label}</h4>
              <p style={{ fontFamily: FONTS.body, fontSize: "11px", color: COLORS.smoke, margin: 0 }}>{a.desc}</p>
            </div>
          </FadeIn>
        ))}
      </div>
      {sel && (
        <FadeIn delay={150}>
          <div style={{ marginTop: "20px", textAlign: "center" }}>
            <button style={{
              fontFamily: FONTS.mono, fontSize: "10px", textTransform: "uppercase",
              letterSpacing: "2px", background: COLORS.warmGold, border: "none",
              color: COLORS.midnight, padding: "11px 28px", cursor: "pointer",
              borderRadius: "2px", fontWeight: 600,
            }}>
              Generate Meridian Signal — {audiences.find(a => a.id === sel)?.label}
            </button>
          </div>
        </FadeIn>
      )}
    </div>
  );
};

// ─── Governance View ───
const GovernanceView = () => (
  <div>
    {[
      { title: "Foundation Grant Rate Review", priority: "high", entity: "Family Impact Foundation", detail: "Disbursement approaching 5% IRS minimum. Board review required before March 31." },
      { title: "Entity Registration Renewal", priority: "medium", entity: "3 Georgia Entities", detail: "Annual Secretary of State filings due. Registered agent confirmation required." },
    ].map((alert, i) => (
      <FadeIn key={i} delay={i * 180 + 300}>
        <div style={{
          padding: "20px", border: `1px solid ${alert.priority === "high" ? COLORS.copper : COLORS.slate}`,
          borderRadius: "2px", marginBottom: "10px",
        }}>
          <div style={{ display: "flex", justifyContent: "space-between" }}>
            <div>
              <h4 style={{ fontFamily: FONTS.display, fontSize: "15px", fontWeight: 400, color: COLORS.cream, margin: "0 0 3px 0" }}>{alert.title}</h4>
              <p style={{ fontFamily: FONTS.mono, fontSize: "9px", color: COLORS.smoke, textTransform: "uppercase", letterSpacing: "1px", margin: "0 0 8px 0" }}>{alert.entity}</p>
            </div>
            <span style={{
              fontFamily: FONTS.mono, fontSize: "8px", textTransform: "uppercase", letterSpacing: "1.5px",
              color: alert.priority === "high" ? COLORS.copper : COLORS.smoke,
              border: `1px solid ${alert.priority === "high" ? COLORS.copper : COLORS.slate}`,
              padding: "3px 7px", borderRadius: "2px", alignSelf: "flex-start",
            }}>{alert.priority}</span>
          </div>
          <p style={{ fontFamily: FONTS.body, fontSize: "13px", color: COLORS.silverSmoke, lineHeight: 1.6, margin: 0 }}>{alert.detail}</p>
          <div style={{ display: "flex", gap: "10px", marginTop: "14px" }}>
            <button style={{
              fontFamily: FONTS.mono, fontSize: "9px", textTransform: "uppercase", letterSpacing: "1.5px",
              background: "transparent", border: `1px solid ${COLORS.warmGold}`, color: COLORS.warmGold,
              padding: "5px 14px", cursor: "pointer", borderRadius: "2px",
            }}>Review</button>
            <button style={{
              fontFamily: FONTS.mono, fontSize: "9px", textTransform: "uppercase", letterSpacing: "1.5px",
              background: "transparent", border: `1px solid ${COLORS.slate}`, color: COLORS.smoke,
              padding: "5px 14px", cursor: "pointer", borderRadius: "2px",
            }}>Defer</button>
          </div>
        </div>
      </FadeIn>
    ))}
  </div>
);

// ─── Scenario View ───
const ScenarioView = () => {
  const [lev, setLev] = useState(25);
  const [hor, setHor] = useState(10);
  const [risk, setRisk] = useState(50);
  const Slider = ({ label, value, onChange, min, max, unit }) => (
    <div style={{ marginBottom: "22px" }}>
      <div style={{ display: "flex", justifyContent: "space-between", marginBottom: "6px" }}>
        <span style={{ fontFamily: FONTS.body, fontSize: "13px", color: COLORS.silverSmoke }}>{label}</span>
        <span style={{ fontFamily: FONTS.mono, fontSize: "11px", color: COLORS.warmGold }}>{value}{unit}</span>
      </div>
      <input type="range" min={min} max={max} value={value} onChange={e => onChange(+e.target.value)} style={{ width: "100%" }} />
    </div>
  );
  return (
    <div>
      <p style={{ fontFamily: FONTS.body, fontSize: "14px", color: COLORS.silverSmoke, lineHeight: 1.7, marginBottom: "24px" }}>
        Adjust parameters. The system recalculates position, resilience, and route in real time.
      </p>
      <Slider label="Leverage Ratio" value={lev} onChange={setLev} min={0} max={80} unit="%" />
      <Slider label="Planning Horizon" value={hor} onChange={setHor} min={1} max={30} unit=" years" />
      <Slider label="Risk Tolerance" value={risk} onChange={setRisk} min={0} max={100} unit="" />
      <GoldRule width="100%" />
      <div style={{ padding: "18px", border: `1px solid ${COLORS.slate}`, borderRadius: "2px", marginTop: "14px" }}>
        <p style={{ fontFamily: FONTS.body, fontSize: "13px", color: COLORS.parchment, lineHeight: 1.7, margin: 0, fontStyle: "italic" }}>
          At {lev}% leverage over {hor} years, the Trust maintains a resilience score of {Math.max(60, 95 - lev * 0.5 + hor * 0.3).toFixed(0)}.
          {lev > 50 ? " Aletheia recommends reviewing the governance cascade before proceeding." : " Current position supports this configuration."}
        </p>
      </div>
    </div>
  );
};


// ═══════════════════════════════════════════════════════════════
// THE COMPLETE EXPERIENCE — Gate → Vestibule → Institution
// ═══════════════════════════════════════════════════════════════
export default function MeridiaComplete() {
  const [stage, setStage] = useState("gate"); // gate → vestibule → institution

  return (
    <>
      <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;0,600;1,400&family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;1,400&family=Spectral:wght@300;400;500&family=DM+Mono:wght@300;400&display=swap" rel="stylesheet" />

      {stage === "gate" && (
        <TheGate onEnter={() => setStage("vestibule")} />
      )}

      {stage === "vestibule" && (
        <TheVestibule
          memberName="Mr. Neal"
          onComplete={() => setStage("institution")}
        />
      )}

      {stage === "institution" && (
        <TheInstitution />
      )}
    </>
  );
}

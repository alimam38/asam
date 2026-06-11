import { useState, useEffect, useRef } from "react";

// Meridia Cathedral — The Gentleman's Financial Intelligence Institution
// Design DNA: Otto's × Cosmos Club × Capital Club DIFC × Annabel's

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

// Subtle grain overlay
const GrainOverlay = () => (
  <div style={{
    position: "fixed", top: 0, left: 0, right: 0, bottom: 0,
    backgroundImage: `url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noise'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noise)' opacity='0.03'/%3E%3C/svg%3E")`,
    pointerEvents: "none", zIndex: 9999, opacity: 0.4,
  }} />
);

// Gold divider line
const GoldRule = ({ width = "60px", style = {} }) => (
  <div style={{
    width, height: "1px",
    background: `linear-gradient(90deg, transparent, ${COLORS.warmGold}, transparent)`,
    margin: "16px 0", ...style,
  }} />
);

// Animated entrance wrapper
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
      transition: `opacity 0.8s ease ${delay}ms, transform 0.8s ease ${delay}ms`,
      ...style,
    }}>
      {children}
    </div>
  );
};

// Clock component
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

// Navigation rooms
const NAV_SECTIONS = [
  { id: "residence", label: "The Residence", icon: "◆", available: true, description: "Your position at a glance" },
  { id: "signal", label: "Meridian Signal", icon: "◈", available: true, description: "Intelligence feed" },
  { id: "governance", label: "The Library", icon: "▣", available: true, description: "Governance & oversight" },
  { id: "entities", label: "The Gallery", icon: "▤", available: true, description: "Entity collection" },
  { id: "scenarios", label: "The Study", icon: "◧", available: true, description: "Scenario modeling" },
  { id: "reports", label: "The Bureau", icon: "▥", available: true, description: "Report generation" },
  { id: "crown", label: "WayPoint Crown", icon: "♛", available: true, description: "Family office" },
  { id: "renaissance", label: "WayPoint Renaissance", icon: "✦", available: false, description: "Re-entry pathways" },
  { id: "edge", label: "WayPoint Edge", icon: "⬡", available: false, description: "Vertical-specific" },
  { id: "crowns-eye", label: "Crown's Eye", icon: "◉", available: false, description: "Education platform" },
  { id: "manus", label: "The Wearable", icon: "◎", available: false, description: "Coming — Phase 3" },
];

// Trust Index visual
const TrustIndex = ({ score = 88, dimensions }) => {
  const [animatedScore, setAnimatedScore] = useState(0);
  useEffect(() => {
    let start = 0;
    const step = () => {
      start += 1;
      if (start <= score) { setAnimatedScore(start); requestAnimationFrame(step); }
    };
    const t = setTimeout(step, 800);
    return () => clearTimeout(t);
  }, [score]);

  return (
    <div style={{ padding: "24px 0" }}>
      <div style={{ display: "flex", alignItems: "baseline", gap: "8px", marginBottom: "20px" }}>
        <span style={{
          fontFamily: FONTS.display, fontSize: "56px", fontWeight: 400,
          color: COLORS.warmGold, lineHeight: 1,
        }}>
          {animatedScore}
        </span>
        <span style={{ fontFamily: FONTS.body, fontSize: "14px", color: COLORS.smoke }}>of 100</span>
      </div>
      <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: "12px" }}>
        {(dimensions || [
          { name: "Financial", score: 92 },
          { name: "Stewardship", score: 81 },
          { name: "Mission", score: 88 },
          { name: "Governance", score: 91 },
        ]).map((d, i) => (
          <div key={d.name} style={{ padding: "12px 0" }}>
            <div style={{
              display: "flex", justifyContent: "space-between", marginBottom: "6px",
            }}>
              <span style={{ fontFamily: FONTS.body, fontSize: "13px", color: COLORS.silverSmoke }}>{d.name}</span>
              <span style={{ fontFamily: FONTS.mono, fontSize: "11px", color: COLORS.warmGold }}>{d.score}</span>
            </div>
            <div style={{
              height: "2px", background: COLORS.slate, borderRadius: "1px", overflow: "hidden",
            }}>
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

// Signal feed items
const SIGNALS = [
  { time: "09:14", type: "regulatory", text: "FDIC guidance update: Community Reinvestment Act modernization rule — comment period closing March 15", urgency: "watch" },
  { time: "08:47", type: "opportunity", text: "SBA 7(a) lending threshold increased to $500K for qualified nonprofits — Turner Seminary eligible", urgency: "action" },
  { time: "08:12", type: "market", text: "Pinnacle Financial Partners Q4 earnings beat — post-merger integration ahead of schedule", urgency: "info" },
  { time: "07:30", type: "governance", text: "Foundation grant disbursement approaching 5% minimum — Q1 review recommended", urgency: "watch" },
  { time: "Yesterday", type: "compliance", text: "Georgia Secretary of State annual registration renewal window opens — 3 entities due", urgency: "action" },
  { time: "Yesterday", type: "market", text: "10-year Treasury yield at 4.12% — line of credit rate adjustment may trigger in April", urgency: "info" },
];

const SignalItem = ({ signal, index }) => {
  const urgencyColors = {
    action: COLORS.warmGold,
    watch: COLORS.copper,
    info: COLORS.smoke,
  };
  return (
    <FadeIn delay={index * 150 + 400}>
      <div style={{
        padding: "16px 0",
        borderBottom: `1px solid ${COLORS.whisper}`,
        display: "flex", gap: "16px", alignItems: "flex-start",
        cursor: "pointer",
      }}
      onMouseEnter={e => e.currentTarget.style.background = COLORS.whisper}
      onMouseLeave={e => e.currentTarget.style.background = "transparent"}
      >
        <div style={{
          width: "6px", height: "6px", borderRadius: "50%",
          background: urgencyColors[signal.urgency],
          marginTop: "8px", flexShrink: 0,
        }} />
        <div style={{ flex: 1 }}>
          <p style={{
            fontFamily: FONTS.body, fontSize: "14px", color: COLORS.cream,
            lineHeight: 1.6, margin: 0,
          }}>
            {signal.text}
          </p>
          <div style={{
            display: "flex", gap: "12px", marginTop: "6px", alignItems: "center",
          }}>
            <span style={{ fontFamily: FONTS.mono, fontSize: "10px", color: COLORS.smoke }}>{signal.time}</span>
            <span style={{
              fontFamily: FONTS.mono, fontSize: "9px", color: urgencyColors[signal.urgency],
              textTransform: "uppercase", letterSpacing: "1.5px",
            }}>
              {signal.urgency}
            </span>
          </div>
        </div>
      </div>
    </FadeIn>
  );
};

// Entity cards
const ENTITIES = [
  { name: "Crown Legacy Trust", type: "Irrevocable Trust", jurisdiction: "Delaware", status: "healthy", aum: "$12.4M" },
  { name: "Family Impact Foundation", type: "501(c)(3)", jurisdiction: "Georgia", status: "watch", aum: "$4.2M" },
  { name: "Crown Holdings LLC", type: "Operating Entity", jurisdiction: "Georgia", status: "healthy", aum: "$3.1M" },
];

const EntityCard = ({ entity, index }) => {
  const [hovered, setHovered] = useState(false);
  const statusColors = { healthy: COLORS.emerald, watch: COLORS.copper, alert: COLORS.burgundy };
  return (
    <FadeIn delay={index * 200 + 600}>
      <div
        onMouseEnter={() => setHovered(true)}
        onMouseLeave={() => setHovered(false)}
        style={{
          padding: "24px",
          border: `1px solid ${hovered ? COLORS.warmGold : COLORS.slate}`,
          borderRadius: "2px",
          background: hovered ? COLORS.whisper : "transparent",
          transition: "all 0.4s ease",
          cursor: "pointer",
        }}
      >
        <div style={{ display: "flex", justifyContent: "space-between", alignItems: "flex-start" }}>
          <div>
            <h3 style={{
              fontFamily: FONTS.display, fontSize: "18px", fontWeight: 400,
              color: COLORS.cream, margin: "0 0 4px 0",
            }}>
              {entity.name}
            </h3>
            <p style={{
              fontFamily: FONTS.body, fontSize: "13px", color: COLORS.smoke, margin: 0,
            }}>
              {entity.type} · {entity.jurisdiction}
            </p>
          </div>
          <div style={{ textAlign: "right" }}>
            <span style={{
              fontFamily: FONTS.display, fontSize: "20px", color: COLORS.warmGold,
            }}>
              {entity.aum}
            </span>
            <div style={{
              display: "flex", alignItems: "center", gap: "6px", justifyContent: "flex-end", marginTop: "4px",
            }}>
              <div style={{
                width: "6px", height: "6px", borderRadius: "50%",
                background: statusColors[entity.status],
              }} />
              <span style={{
                fontFamily: FONTS.mono, fontSize: "9px",
                textTransform: "uppercase", letterSpacing: "1.5px",
                color: statusColors[entity.status],
              }}>
                {entity.status}
              </span>
            </div>
          </div>
        </div>
      </div>
    </FadeIn>
  );
};

// Aletheia panel
const AletheiaPanel = ({ collapsed, onToggle }) => {
  const [typing, setTyping] = useState(true);
  const [messageIndex, setMessageIndex] = useState(0);

  const messages = [
    "Good morning. Three things have changed since we last spoke.",
    "The Foundation's grant disbursement rate is approaching the 5% minimum threshold. I recommend a governance review before Q1 close.",
    "An SBA lending threshold change creates a new pathway for Turner Seminary. I've prepared a brief.",
    "Your Georgia entity registrations open next week. Shall I walk you through what's due?",
  ];

  useEffect(() => {
    const t = setTimeout(() => setTyping(false), 2000);
    return () => clearTimeout(t);
  }, []);

  return (
    <div style={{
      position: "fixed", right: 0, top: 0, bottom: 0,
      width: collapsed ? "0px" : "380px",
      background: COLORS.deepNavy,
      borderLeft: collapsed ? "none" : `1px solid ${COLORS.slate}`,
      transition: "width 0.5s ease",
      overflow: "hidden",
      zIndex: 100,
      display: "flex", flexDirection: "column",
    }}>
      {/* Aletheia header */}
      <div style={{
        padding: "28px 24px 20px",
        borderBottom: `1px solid ${COLORS.whisper}`,
      }}>
        <div style={{ display: "flex", alignItems: "center", gap: "12px" }}>
          <div style={{
            width: "32px", height: "32px", borderRadius: "50%",
            border: `1px solid ${COLORS.warmGold}`,
            display: "flex", alignItems: "center", justifyContent: "center",
            fontFamily: FONTS.display, fontSize: "14px", color: COLORS.warmGold,
          }}>
            A
          </div>
          <div>
            <h3 style={{
              fontFamily: FONTS.display, fontSize: "16px", fontWeight: 400,
              color: COLORS.cream, margin: 0,
            }}>
              Aletheia
            </h3>
            <p style={{
              fontFamily: FONTS.mono, fontSize: "9px", color: COLORS.smoke,
              textTransform: "uppercase", letterSpacing: "2px", margin: 0,
            }}>
              Your Steward
            </p>
          </div>
        </div>
      </div>

      {/* Messages */}
      <div style={{ flex: 1, padding: "20px 24px", overflowY: "auto" }}>
        {messages.map((msg, i) => (
          <FadeIn key={i} delay={i * 1200 + 500}>
            <div style={{ marginBottom: "20px" }}>
              <p style={{
                fontFamily: FONTS.body, fontSize: "14px", color: COLORS.parchment,
                lineHeight: 1.7, margin: 0,
                fontStyle: i === 0 ? "normal" : "normal",
              }}>
                {msg}
              </p>
              {i === 0 && <GoldRule width="40px" />}
            </div>
          </FadeIn>
        ))}
        {typing && (
          <div style={{ display: "flex", gap: "4px", padding: "8px 0" }}>
            {[0, 1, 2].map(i => (
              <div key={i} style={{
                width: "4px", height: "4px", borderRadius: "50%",
                background: COLORS.warmGold, opacity: 0.4,
                animation: `pulse 1.4s ease-in-out ${i * 0.2}s infinite`,
              }} />
            ))}
          </div>
        )}
      </div>

      {/* Input */}
      <div style={{
        padding: "16px 24px",
        borderTop: `1px solid ${COLORS.whisper}`,
      }}>
        <div style={{
          display: "flex", alignItems: "center",
          border: `1px solid ${COLORS.slate}`,
          borderRadius: "2px", padding: "10px 14px",
        }}>
          <input
            placeholder="Ask Aletheia..."
            style={{
              flex: 1, background: "transparent", border: "none", outline: "none",
              fontFamily: FONTS.body, fontSize: "14px", color: COLORS.cream,
            }}
          />
          <span style={{ color: COLORS.warmGold, cursor: "pointer", fontSize: "14px" }}>→</span>
        </div>
      </div>
    </div>
  );
};

// Governance alerts
const GovernanceAlerts = () => (
  <div>
    {[
      { title: "Foundation Grant Rate Review", priority: "high", entity: "Family Impact Foundation", detail: "Disbursement approaching 5% IRS minimum. Board review required before March 31." },
      { title: "Entity Registration Renewal", priority: "medium", entity: "3 Georgia Entities", detail: "Annual Secretary of State filings due. Registered agent confirmation required." },
    ].map((alert, i) => (
      <FadeIn key={i} delay={i * 200 + 400}>
        <div style={{
          padding: "20px",
          border: `1px solid ${alert.priority === "high" ? COLORS.copper : COLORS.slate}`,
          borderRadius: "2px",
          marginBottom: "12px",
        }}>
          <div style={{ display: "flex", justifyContent: "space-between", alignItems: "flex-start" }}>
            <div>
              <h4 style={{
                fontFamily: FONTS.display, fontSize: "15px", fontWeight: 400,
                color: COLORS.cream, margin: "0 0 4px 0",
              }}>
                {alert.title}
              </h4>
              <p style={{
                fontFamily: FONTS.mono, fontSize: "10px", color: COLORS.smoke,
                textTransform: "uppercase", letterSpacing: "1px", margin: "0 0 8px 0",
              }}>
                {alert.entity}
              </p>
            </div>
            <span style={{
              fontFamily: FONTS.mono, fontSize: "9px",
              textTransform: "uppercase", letterSpacing: "1.5px",
              color: alert.priority === "high" ? COLORS.copper : COLORS.smoke,
              border: `1px solid ${alert.priority === "high" ? COLORS.copper : COLORS.slate}`,
              padding: "3px 8px", borderRadius: "2px",
            }}>
              {alert.priority}
            </span>
          </div>
          <p style={{
            fontFamily: FONTS.body, fontSize: "13px", color: COLORS.silverSmoke,
            lineHeight: 1.6, margin: 0,
          }}>
            {alert.detail}
          </p>
          <div style={{ display: "flex", gap: "12px", marginTop: "14px" }}>
            <button style={{
              fontFamily: FONTS.mono, fontSize: "10px", textTransform: "uppercase",
              letterSpacing: "1.5px", background: "transparent",
              border: `1px solid ${COLORS.warmGold}`, color: COLORS.warmGold,
              padding: "6px 16px", cursor: "pointer", borderRadius: "2px",
            }}>
              Review
            </button>
            <button style={{
              fontFamily: FONTS.mono, fontSize: "10px", textTransform: "uppercase",
              letterSpacing: "1.5px", background: "transparent",
              border: `1px solid ${COLORS.slate}`, color: COLORS.smoke,
              padding: "6px 16px", cursor: "pointer", borderRadius: "2px",
            }}>
              Defer
            </button>
          </div>
        </div>
      </FadeIn>
    ))}
  </div>
);

// Report generation view
const ReportBureau = () => {
  const [selectedAudience, setSelectedAudience] = useState(null);
  const audiences = [
    { id: "board", label: "Board", description: "Strategic summary for governance oversight", icon: "▣" },
    { id: "family", label: "Family", description: "Plain-language position with Aletheia guidance", icon: "♡" },
    { id: "regulator", label: "Regulator", description: "Compliance documentation and audit trail", icon: "⚖" },
    { id: "technical", label: "Technical", description: "System health and data lineage", icon: "⚙" },
  ];
  return (
    <div>
      <p style={{
        fontFamily: FONTS.body, fontSize: "15px", color: COLORS.silverSmoke,
        lineHeight: 1.7, marginBottom: "28px",
      }}>
        One truth. Four windows. Select an audience to generate the Meridian Signal report.
      </p>
      <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: "12px" }}>
        {audiences.map((a, i) => (
          <FadeIn key={a.id} delay={i * 150 + 300}>
            <div
              onClick={() => setSelectedAudience(a.id)}
              style={{
                padding: "28px 24px",
                border: `1px solid ${selectedAudience === a.id ? COLORS.warmGold : COLORS.slate}`,
                borderRadius: "2px",
                cursor: "pointer",
                background: selectedAudience === a.id ? COLORS.whisper : "transparent",
                transition: "all 0.3s ease",
                textAlign: "center",
              }}
            >
              <div style={{
                fontFamily: FONTS.display, fontSize: "28px", color: COLORS.warmGold,
                marginBottom: "12px",
              }}>
                {a.icon}
              </div>
              <h4 style={{
                fontFamily: FONTS.display, fontSize: "16px", fontWeight: 400,
                color: COLORS.cream, margin: "0 0 6px 0",
              }}>
                {a.label}
              </h4>
              <p style={{
                fontFamily: FONTS.body, fontSize: "12px", color: COLORS.smoke,
                margin: 0, lineHeight: 1.5,
              }}>
                {a.description}
              </p>
            </div>
          </FadeIn>
        ))}
      </div>
      {selectedAudience && (
        <FadeIn delay={200}>
          <div style={{ marginTop: "24px", textAlign: "center" }}>
            <button style={{
              fontFamily: FONTS.mono, fontSize: "11px", textTransform: "uppercase",
              letterSpacing: "2px", background: COLORS.warmGold,
              border: "none", color: COLORS.midnight,
              padding: "12px 32px", cursor: "pointer", borderRadius: "2px",
              fontWeight: 600,
            }}>
              Generate Meridian Signal — {audiences.find(a => a.id === selectedAudience)?.label}
            </button>
          </div>
        </FadeIn>
      )}
    </div>
  );
};

// Position metrics
const PositionMetrics = () => {
  const metrics = [
    { label: "Net Worth", value: "$19.6M", change: "+4.2%", direction: "up" },
    { label: "Liquidity", value: "$2.3M", change: "+1.8%", direction: "up" },
    { label: "Obligations", value: "$416K", change: "-2.1%", direction: "down" },
    { label: "Resilience", value: "95", change: "+3", direction: "up", suffix: "/100" },
  ];
  return (
    <div style={{ display: "grid", gridTemplateColumns: "repeat(4, 1fr)", gap: "1px", background: COLORS.slate, borderRadius: "2px", overflow: "hidden" }}>
      {metrics.map((m, i) => (
        <FadeIn key={m.label} delay={i * 150 + 400}>
          <div style={{ background: COLORS.deepNavy, padding: "24px 20px" }}>
            <p style={{
              fontFamily: FONTS.mono, fontSize: "9px", textTransform: "uppercase",
              letterSpacing: "2px", color: COLORS.smoke, margin: "0 0 10px 0",
            }}>
              {m.label}
            </p>
            <div style={{ display: "flex", alignItems: "baseline", gap: "4px" }}>
              <span style={{
                fontFamily: FONTS.display, fontSize: "28px", fontWeight: 400,
                color: COLORS.cream,
              }}>
                {m.value}
              </span>
              {m.suffix && (
                <span style={{ fontFamily: FONTS.body, fontSize: "13px", color: COLORS.smoke }}>{m.suffix}</span>
              )}
            </div>
            <span style={{
              fontFamily: FONTS.mono, fontSize: "10px",
              color: m.direction === "up" ? COLORS.emerald : COLORS.warmGold,
              marginTop: "6px", display: "inline-block",
            }}>
              {m.direction === "up" ? "↑" : "↓"} {m.change}
            </span>
          </div>
        </FadeIn>
      ))}
    </div>
  );
};

// Scenario sliders
const ScenarioStudio = () => {
  const [leverage, setLeverage] = useState(25);
  const [horizon, setHorizon] = useState(10);
  const [risk, setRisk] = useState(50);

  const SliderRow = ({ label, value, onChange, min, max, unit }) => (
    <div style={{ marginBottom: "24px" }}>
      <div style={{ display: "flex", justifyContent: "space-between", marginBottom: "8px" }}>
        <span style={{ fontFamily: FONTS.body, fontSize: "14px", color: COLORS.silverSmoke }}>{label}</span>
        <span style={{ fontFamily: FONTS.mono, fontSize: "12px", color: COLORS.warmGold }}>{value}{unit}</span>
      </div>
      <input type="range" min={min} max={max} value={value} onChange={e => onChange(+e.target.value)}
        style={{ width: "100%", accentColor: COLORS.warmGold, height: "2px" }} />
    </div>
  );

  return (
    <div>
      <p style={{
        fontFamily: FONTS.body, fontSize: "15px", color: COLORS.silverSmoke,
        lineHeight: 1.7, marginBottom: "28px",
      }}>
        Adjust parameters. The system recalculates position, resilience, and route in real time.
      </p>
      <SliderRow label="Leverage Ratio" value={leverage} onChange={setLeverage} min={0} max={80} unit="%" />
      <SliderRow label="Planning Horizon" value={horizon} onChange={setHorizon} min={1} max={30} unit=" years" />
      <SliderRow label="Risk Tolerance" value={risk} onChange={setRisk} min={0} max={100} unit="" />
      <GoldRule width="100%" />
      <div style={{
        padding: "20px",
        border: `1px solid ${COLORS.slate}`,
        borderRadius: "2px",
        marginTop: "16px",
      }}>
        <p style={{
          fontFamily: FONTS.body, fontSize: "13px", color: COLORS.parchment,
          lineHeight: 1.7, margin: 0, fontStyle: "italic",
        }}>
          At {leverage}% leverage over {horizon} years with moderate risk tolerance, the Crown Legacy Trust 
          maintains a resilience score of {Math.max(60, 95 - leverage * 0.5 + horizon * 0.3).toFixed(0)}. 
          {leverage > 50 ? " Aletheia recommends reviewing the governance cascade before proceeding." 
            : " Current position supports this configuration."}
        </p>
      </div>
    </div>
  );
};

// Main application
export default function MeridiaCathedral() {
  const [activeRoom, setActiveRoom] = useState("residence");
  const [aletheiaOpen, setAletheiaOpen] = useState(true);
  const [navHovered, setNavHovered] = useState(null);

  const roomTitles = {
    residence: "The Residence",
    signal: "Meridian Signal",
    governance: "The Library",
    entities: "The Gallery",
    scenarios: "The Study",
    reports: "The Bureau",
    crown: "WayPoint Crown",
    renaissance: "WayPoint Renaissance",
    edge: "WayPoint Edge",
    "crowns-eye": "Crown's Eye",
    manus: "The Wearable",
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

  return (
    <div style={{
      minHeight: "100vh",
      background: COLORS.midnight,
      display: "flex",
      fontFamily: FONTS.body,
      color: COLORS.cream,
      position: "relative",
    }}>
      <GrainOverlay />

      {/* Google Fonts */}
      <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;0,600;1,400&family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;1,400&family=Spectral:wght@300;400;500&family=DM+Mono:wght@300;400&display=swap" rel="stylesheet" />

      <style>{`
        @keyframes pulse {
          0%, 100% { opacity: 0.2; }
          50% { opacity: 0.8; }
        }
        input[type="range"] {
          -webkit-appearance: none;
          background: ${COLORS.slate};
          border-radius: 1px;
          outline: none;
        }
        input[type="range"]::-webkit-slider-thumb {
          -webkit-appearance: none;
          width: 12px; height: 12px;
          border-radius: 50%;
          background: ${COLORS.warmGold};
          cursor: pointer;
        }
        ::-webkit-scrollbar { width: 4px; }
        ::-webkit-scrollbar-track { background: transparent; }
        ::-webkit-scrollbar-thumb { background: ${COLORS.slate}; border-radius: 2px; }
        ::placeholder { color: ${COLORS.smoke}; }
      `}</style>

      {/* Left Navigation — The Hallway */}
      <nav style={{
        width: "240px",
        background: COLORS.deepNavy,
        borderRight: `1px solid ${COLORS.whisper}`,
        display: "flex",
        flexDirection: "column",
        flexShrink: 0,
        position: "fixed",
        top: 0,
        bottom: 0,
        left: 0,
        zIndex: 50,
      }}>
        {/* Crest */}
        <div style={{ padding: "28px 24px 20px" }}>
          <div style={{ display: "flex", alignItems: "center", gap: "12px" }}>
            <div style={{
              width: "36px", height: "36px",
              border: `1px solid ${COLORS.warmGold}`,
              borderRadius: "50%",
              display: "flex", alignItems: "center", justifyContent: "center",
              fontFamily: FONTS.display, fontSize: "16px", color: COLORS.warmGold,
            }}>
              M
            </div>
            <div>
              <h1 style={{
                fontFamily: FONTS.display, fontSize: "18px", fontWeight: 400,
                color: COLORS.cream, margin: 0, letterSpacing: "1px",
              }}>
                Meridia
              </h1>
              <p style={{
                fontFamily: FONTS.mono, fontSize: "8px", color: COLORS.smoke,
                textTransform: "uppercase", letterSpacing: "2.5px", margin: 0,
              }}>
                Integra Core · v1.0
              </p>
            </div>
          </div>
        </div>

        <GoldRule width="calc(100% - 48px)" style={{ margin: "0 24px 8px" }} />

        {/* Room navigation */}
        <div style={{ flex: 1, overflowY: "auto", padding: "8px 0" }}>
          {NAV_SECTIONS.map((section) => (
            <div
              key={section.id}
              onClick={() => section.available && setActiveRoom(section.id)}
              onMouseEnter={() => setNavHovered(section.id)}
              onMouseLeave={() => setNavHovered(null)}
              style={{
                padding: "10px 24px",
                display: "flex", alignItems: "center", gap: "12px",
                cursor: section.available ? "pointer" : "default",
                opacity: section.available ? 1 : 0.3,
                background: activeRoom === section.id ? COLORS.whisper 
                  : navHovered === section.id && section.available ? COLORS.whisper : "transparent",
                borderLeft: activeRoom === section.id 
                  ? `2px solid ${COLORS.warmGold}` : "2px solid transparent",
                transition: "all 0.3s ease",
              }}
            >
              <span style={{
                fontFamily: FONTS.display, fontSize: "12px",
                color: activeRoom === section.id ? COLORS.warmGold : COLORS.smoke,
                width: "20px", textAlign: "center",
              }}>
                {section.icon}
              </span>
              <div>
                <span style={{
                  fontFamily: FONTS.body, fontSize: "13px",
                  color: activeRoom === section.id ? COLORS.cream : COLORS.silverSmoke,
                  display: "block",
                }}>
                  {section.label}
                </span>
                {navHovered === section.id && (
                  <span style={{
                    fontFamily: FONTS.mono, fontSize: "9px", color: COLORS.smoke,
                  }}>
                    {section.description}
                  </span>
                )}
              </div>
              {!section.available && (
                <span style={{
                  marginLeft: "auto",
                  fontFamily: FONTS.mono, fontSize: "8px", color: COLORS.smoke,
                  border: `1px solid ${COLORS.slate}`, padding: "2px 6px",
                  borderRadius: "2px",
                }}>
                  SOON
                </span>
              )}
            </div>
          ))}
        </div>

        {/* Footer */}
        <div style={{
          padding: "16px 24px",
          borderTop: `1px solid ${COLORS.whisper}`,
        }}>
          <p style={{
            fontFamily: FONTS.mono, fontSize: "8px", color: COLORS.smoke,
            textTransform: "uppercase", letterSpacing: "2px", margin: "0 0 4px 0",
          }}>
            Eden Intelligence Group
          </p>
          <p style={{
            fontFamily: FONTS.mono, fontSize: "8px", color: `${COLORS.smoke}80`,
            margin: 0,
          }}>
            Governance as a Service
          </p>
        </div>
      </nav>

      {/* Main Content — The Room */}
      <main style={{
        flex: 1,
        marginLeft: "240px",
        marginRight: aletheiaOpen ? "380px" : "0px",
        transition: "margin-right 0.5s ease",
        minHeight: "100vh",
        padding: "0",
      }}>
        {/* Top Bar */}
        <header style={{
          padding: "18px 40px",
          display: "flex", justifyContent: "space-between", alignItems: "center",
          borderBottom: `1px solid ${COLORS.whisper}`,
          position: "sticky", top: 0,
          background: `${COLORS.midnight}ee`,
          backdropFilter: "blur(20px)",
          zIndex: 40,
        }}>
          <LiveClock />
          <div style={{ display: "flex", alignItems: "center", gap: "20px" }}>
            <span style={{
              fontFamily: FONTS.mono, fontSize: "9px", color: COLORS.emerald,
              textTransform: "uppercase", letterSpacing: "2px",
              display: "flex", alignItems: "center", gap: "6px",
            }}>
              <span style={{
                width: "5px", height: "5px", borderRadius: "50%",
                background: COLORS.emerald, display: "inline-block",
              }} />
              System Healthy
            </span>
            <div
              onClick={() => setAletheiaOpen(!aletheiaOpen)}
              style={{
                width: "28px", height: "28px", borderRadius: "50%",
                border: `1px solid ${COLORS.warmGold}`,
                display: "flex", alignItems: "center", justifyContent: "center",
                cursor: "pointer",
                fontFamily: FONTS.display, fontSize: "12px", color: COLORS.warmGold,
              }}
            >
              A
            </div>
          </div>
        </header>

        {/* Room Title */}
        <div style={{ padding: "48px 40px 0" }}>
          <FadeIn key={activeRoom}>
            <p style={{
              fontFamily: FONTS.mono, fontSize: "9px", color: COLORS.smoke,
              textTransform: "uppercase", letterSpacing: "3px",
              margin: "0 0 8px 0",
            }}>
              {activeRoom === "residence" ? "WayPoint Crown" : "Meridia"}
            </p>
            <h2 style={{
              fontFamily: FONTS.display, fontSize: "32px", fontWeight: 400,
              color: COLORS.cream, margin: "0 0 6px 0",
              letterSpacing: "0.5px",
            }}>
              {roomTitles[activeRoom]}
            </h2>
            {roomSubtitles[activeRoom] && (
              <p style={{
                fontFamily: FONTS.body, fontSize: "15px", color: COLORS.smoke,
                fontStyle: "italic", margin: 0,
              }}>
                {roomSubtitles[activeRoom]}
              </p>
            )}
            <GoldRule width="80px" style={{ margin: "20px 0 0" }} />
          </FadeIn>
        </div>

        {/* Room Content */}
        <div style={{ padding: "32px 40px 60px" }}>
          {activeRoom === "residence" && (
            <div>
              <FadeIn delay={200}>
                <PositionMetrics />
              </FadeIn>
              <div style={{ marginTop: "40px", display: "grid", gridTemplateColumns: "1fr 1fr", gap: "40px" }}>
                <FadeIn delay={400}>
                  <div>
                    <h3 style={{
                      fontFamily: FONTS.display, fontSize: "18px", fontWeight: 400,
                      color: COLORS.cream, margin: "0 0 4px 0",
                    }}>
                      Trust Index
                    </h3>
                    <p style={{
                      fontFamily: FONTS.mono, fontSize: "9px", color: COLORS.smoke,
                      textTransform: "uppercase", letterSpacing: "2px", margin: "0 0 8px 0",
                    }}>
                      Composite governance score
                    </p>
                    <TrustIndex score={88} />
                  </div>
                </FadeIn>
                <FadeIn delay={600}>
                  <div>
                    <h3 style={{
                      fontFamily: FONTS.display, fontSize: "18px", fontWeight: 400,
                      color: COLORS.cream, margin: "0 0 4px 0",
                    }}>
                      Latest Signal
                    </h3>
                    <p style={{
                      fontFamily: FONTS.mono, fontSize: "9px", color: COLORS.smoke,
                      textTransform: "uppercase", letterSpacing: "2px", margin: "0 0 8px 0",
                    }}>
                      Top 3 developments
                    </p>
                    {SIGNALS.slice(0, 3).map((s, i) => (
                      <SignalItem key={i} signal={s} index={i} />
                    ))}
                  </div>
                </FadeIn>
              </div>
            </div>
          )}

          {activeRoom === "signal" && (
            <div>
              {SIGNALS.map((s, i) => (
                <SignalItem key={i} signal={s} index={i} />
              ))}
            </div>
          )}

          {activeRoom === "governance" && <GovernanceAlerts />}

          {activeRoom === "entities" && (
            <div style={{ display: "flex", flexDirection: "column", gap: "12px" }}>
              {ENTITIES.map((e, i) => (
                <EntityCard key={i} entity={e} index={i} />
              ))}
            </div>
          )}

          {activeRoom === "scenarios" && <ScenarioStudio />}
          {activeRoom === "reports" && <ReportBureau />}

          {activeRoom === "crown" && (
            <FadeIn delay={200}>
              <div style={{
                padding: "40px",
                border: `1px solid ${COLORS.slate}`,
                borderRadius: "2px",
                textAlign: "center",
              }}>
                <div style={{ fontFamily: FONTS.display, fontSize: "48px", color: COLORS.warmGold, marginBottom: "16px" }}>♛</div>
                <h3 style={{
                  fontFamily: FONTS.display, fontSize: "22px", fontWeight: 400,
                  color: COLORS.cream, margin: "0 0 12px 0",
                }}>
                  Multi-Generational Governance
                </h3>
                <p style={{
                  fontFamily: FONTS.body, fontSize: "15px", color: COLORS.silverSmoke,
                  lineHeight: 1.7, maxWidth: "480px", margin: "0 auto",
                }}>
                  Entity mapping, trust structures, generational planning, succession cascades, 
                  and the Trust Index that holds it all together. Where your family's architecture 
                  is maintained with the same care as a collection at Otto's.
                </p>
                <GoldRule width="60px" style={{ margin: "24px auto" }} />
                <p style={{
                  fontFamily: FONTS.body, fontSize: "13px", color: COLORS.smoke, fontStyle: "italic",
                }}>
                  Full Crown suite activates with live data integration
                </p>
              </div>
            </FadeIn>
          )}

          {(activeRoom === "renaissance" || activeRoom === "edge" || activeRoom === "crowns-eye" || activeRoom === "manus") && (
            <FadeIn delay={200}>
              <div style={{
                padding: "60px 40px",
                border: `1px solid ${COLORS.slate}`,
                borderRadius: "2px",
                textAlign: "center",
              }}>
                <p style={{
                  fontFamily: FONTS.mono, fontSize: "10px", color: COLORS.smoke,
                  textTransform: "uppercase", letterSpacing: "3px", margin: "0 0 16px 0",
                }}>
                  This wing is under construction
                </p>
                <h3 style={{
                  fontFamily: FONTS.display, fontSize: "22px", fontWeight: 400,
                  color: COLORS.warmGold, margin: "0 0 12px 0",
                }}>
                  {roomTitles[activeRoom]}
                </h3>
                <p style={{
                  fontFamily: FONTS.body, fontSize: "14px", color: COLORS.silverSmoke,
                  lineHeight: 1.7, maxWidth: "400px", margin: "0 auto",
                }}>
                  The hallway is here. The door exists. The room is being prepared 
                  with the care it deserves.
                </p>
              </div>
            </FadeIn>
          )}
        </div>
      </main>

      {/* Aletheia Panel */}
      <AletheiaPanel collapsed={!aletheiaOpen} onToggle={() => setAletheiaOpen(!aletheiaOpen)} />
    </div>
  );
}

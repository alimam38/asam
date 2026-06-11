import { useState, useEffect, useRef, useCallback } from "react";
import * as Tone from "tone";

const KEYS = ["C","G","D","A","E","B","Gb","Db","Ab","Eb","Bb","F"];
const MINOR_KEYS = ["Am","Em","Bm","F#m","C#m","G#m","Ebm","Bbm","Fm","Cm","Gm","Dm"];

const CHORD_MAP = {
  C: { notes: ["C4","E4","G4"], jazz: ["C4","E4","G4","B4"], gospel: ["C3","G3","C4","E4","G4","B4"] },
  Db: { notes: ["Db4","F4","Ab4"], jazz: ["Db4","F4","Ab4","C5"], gospel: ["Db3","Ab3","Db4","F4","Ab4","C5"] },
  D: { notes: ["D4","F#4","A4"], jazz: ["D4","F#4","A4","C#5"], gospel: ["D3","A3","D4","F#4","A4","C#5"] },
  Eb: { notes: ["Eb4","G4","Bb4"], jazz: ["Eb4","G4","Bb4","D5"], gospel: ["Eb3","Bb3","Eb4","G4","Bb4","D5"] },
  E: { notes: ["E4","G#4","B4"], jazz: ["E4","G#4","B4","D#5"], gospel: ["E3","B3","E4","G#4","B4","D#5"] },
  F: { notes: ["F4","A4","C5"], jazz: ["F4","A4","C5","E5"], gospel: ["F3","C4","F4","A4","C5","E5"] },
  Gb: { notes: ["Gb4","Bb4","Db5"], jazz: ["Gb4","Bb4","Db5","F5"], gospel: ["Gb3","Db4","Gb4","Bb4","Db5","F5"] },
  G: { notes: ["G4","B4","D5"], jazz: ["G4","B4","D5","F#5"], gospel: ["G3","D4","G4","B4","D5","F#5"] },
  Ab: { notes: ["Ab4","C5","Eb5"], jazz: ["Ab4","C5","Eb5","G5"], gospel: ["Ab3","Eb4","Ab4","C5","Eb5","G5"] },
  A: { notes: ["A4","C#5","E5"], jazz: ["A4","C#5","E5","G#5"], gospel: ["A3","E4","A4","C#5","E5","G#5"] },
  Bb: { notes: ["Bb4","D5","F5"], jazz: ["Bb4","D5","F5","A5"], gospel: ["Bb3","F4","Bb4","D5","F5","A5"] },
  B: { notes: ["B4","D#5","F#5"], jazz: ["B4","D#5","F#5","A#5"], gospel: ["B3","F#4","B4","D#5","F#5","A#5"] },
};

const PROGRESSIONS = {
  "ii-V-I (Jazz Standard)": (key) => {
    const idx = KEYS.indexOf(key);
    const ii = KEYS[(idx + 10) % 12]; // minor 2nd
    const V = KEYS[(idx + 7) % 12]; // dominant
    return [
      { chord: ii, label: "ii", type: "jazz" },
      { chord: V, label: "V7", type: "jazz" },
      { chord: key, label: "I", type: "jazz" },
    ];
  },
  "I-IV-V-I (Foundation)": (key) => {
    const idx = KEYS.indexOf(key);
    const IV = KEYS[(idx + 5) % 12];
    const V = KEYS[(idx + 7) % 12];
    return [
      { chord: key, label: "I", type: "gospel" },
      { chord: IV, label: "IV", type: "gospel" },
      { chord: V, label: "V", type: "gospel" },
      { chord: key, label: "I", type: "gospel" },
    ];
  },
  "I-vi-ii-V (Turnaround)": (key) => {
    const idx = KEYS.indexOf(key);
    const vi = KEYS[(idx + 9) % 12];
    const ii = KEYS[(idx + 10) % 12];
    const V = KEYS[(idx + 7) % 12];
    return [
      { chord: key, label: "I", type: "jazz" },
      { chord: vi, label: "vi", type: "jazz" },
      { chord: ii, label: "ii", type: "jazz" },
      { chord: V, label: "V7", type: "jazz" },
    ];
  },
  "Gospel Modulation (up half step)": (key) => {
    const idx = KEYS.indexOf(key);
    const IV = KEYS[(idx + 5) % 12];
    const V = KEYS[(idx + 7) % 12];
    const newKey = KEYS[(idx + 1) % 12];
    return [
      { chord: key, label: "I", type: "gospel" },
      { chord: IV, label: "IV", type: "gospel" },
      { chord: V, label: "V (lift!)", type: "gospel" },
      { chord: newKey, label: "→ new I", type: "gospel" },
    ];
  },
  "Gospel Shout (IV-V-vi-V)": (key) => {
    const idx = KEYS.indexOf(key);
    const IV = KEYS[(idx + 5) % 12];
    const V = KEYS[(idx + 7) % 12];
    const vi = KEYS[(idx + 9) % 12];
    return [
      { chord: IV, label: "IV", type: "gospel" },
      { chord: V, label: "V", type: "gospel" },
      { chord: vi, label: "vi (cry!)", type: "gospel" },
      { chord: V, label: "V (resolve)", type: "gospel" },
    ];
  },
};

export default function CircleOfFifths() {
  const [selectedKey, setSelectedKey] = useState("C");
  const [selectedProgression, setSelectedProgression] = useState("ii-V-I (Jazz Standard)");
  const [voicing, setVoicing] = useState("jazz");
  const [playing, setPlaying] = useState(false);
  const [activeChordIdx, setActiveChordIdx] = useState(-1);
  const [showTheory, setShowTheory] = useState(true);
  const [tempo, setTempo] = useState(80);
  const [started, setStarted] = useState(false);
  const synthRef = useRef(null);

  useEffect(() => {
    return () => { if (synthRef.current) synthRef.current.dispose(); };
  }, []);

  const initAudio = useCallback(async () => {
    if (!started) {
      await Tone.start();
      synthRef.current = new Tone.PolySynth(Tone.Synth, {
        oscillator: { type: "triangle" },
        envelope: { attack: 0.05, decay: 0.3, sustain: 0.4, release: 0.8 },
        volume: -8,
      }).toDestination();
      setStarted(true);
    }
  }, [started]);

  const playChord = useCallback(async (chordKey, type) => {
    await initAudio();
    if (!synthRef.current) return;
    const chord = CHORD_MAP[chordKey];
    if (!chord) return;
    const notes = chord[type] || chord.notes;
    synthRef.current.triggerAttackRelease(notes, "2n");
  }, [initAudio]);

  const playProgression = useCallback(async () => {
    await initAudio();
    if (!synthRef.current || playing) return;
    setPlaying(true);
    const prog = PROGRESSIONS[selectedProgression](selectedKey);
    const beatDuration = 60 / tempo;

    for (let i = 0; i < prog.length; i++) {
      setActiveChordIdx(i);
      const { chord, type } = prog[i];
      const notes = CHORD_MAP[chord]?.[type] || CHORD_MAP[chord]?.notes || [];
      synthRef.current.triggerAttackRelease(notes, beatDuration * 1.8);
      await new Promise((r) => setTimeout(r, beatDuration * 2000));
    }
    setActiveChordIdx(-1);
    setPlaying(false);
  }, [initAudio, playing, selectedKey, selectedProgression, tempo]);

  const keyIdx = KEYS.indexOf(selectedKey);
  const relatedKeys = {
    "IV (subdominant)": KEYS[(keyIdx + 5) % 12],
    "V (dominant)": KEYS[(keyIdx + 7) % 12],
    "vi (relative minor)": KEYS[(keyIdx + 9) % 12],
    "ii": KEYS[(keyIdx + 10) % 12],
    "iii": KEYS[(keyIdx + 4) % 12],
  };

  const currentProg = PROGRESSIONS[selectedProgression](selectedKey);

  return (
    <div style={{
      background: "linear-gradient(135deg, #0a0e1a 0%, #1a1a2e 50%, #0a0e1a 100%)",
      minHeight: "100vh", color: "#e8dcc8", fontFamily: "'Georgia', serif",
      padding: "24px", boxSizing: "border-box"
    }}>
      <div style={{ maxWidth: 800, margin: "0 auto" }}>
        {/* Header */}
        <div style={{ textAlign: "center", marginBottom: 32 }}>
          <h1 style={{
            fontSize: 28, fontWeight: 400, letterSpacing: 4,
            color: "#c9a84c", margin: 0, textTransform: "uppercase"
          }}>
            Circle of Fifths
          </h1>
          <div style={{ fontSize: 13, color: "#8a8070", marginTop: 4, letterSpacing: 2 }}>
            SIGNATURE THEORY — KINGDOM SOUNDWORKS
          </div>
        </div>

        {/* Circle Visualization */}
        <div style={{ display: "flex", justifyContent: "center", marginBottom: 32 }}>
          <svg width="320" height="320" viewBox="-160 -160 320 320">
            <circle cx="0" cy="0" r="140" fill="none" stroke="#2a2a3e" strokeWidth="1" />
            <circle cx="0" cy="0" r="90" fill="none" stroke="#2a2a3e" strokeWidth="1" />
            {KEYS.map((k, i) => {
              const angle = (i * 30 - 90) * (Math.PI / 180);
              const x = Math.cos(angle) * 130;
              const y = Math.sin(angle) * 130;
              const mx = Math.cos(angle) * 85;
              const my = Math.sin(angle) * 85;
              const isSelected = k === selectedKey;
              const isRelated = Object.values(relatedKeys).includes(k);
              const isInProg = currentProg.some(p => p.chord === k);
              const isActive = activeChordIdx >= 0 && currentProg[activeChordIdx]?.chord === k;

              let color = "#4a4a5e";
              if (isActive) color = "#c9a84c";
              else if (isSelected) color = "#c9a84c";
              else if (isInProg) color = "#7a6a3c";
              else if (isRelated) color = "#5a5a7e";

              return (
                <g key={k} onClick={() => { setSelectedKey(k); playChord(k, voicing); }}
                   style={{ cursor: "pointer" }}>
                  <circle cx={x} cy={y} r={isSelected ? 22 : isActive ? 20 : 18}
                    fill={isActive ? "#c9a84c22" : isSelected ? "#c9a84c11" : "transparent"}
                    stroke={color} strokeWidth={isSelected || isActive ? 2 : 1} />
                  <text x={x} y={y + 1} textAnchor="middle" dominantBaseline="middle"
                    fill={color} fontSize={isSelected ? 16 : 13}
                    fontWeight={isSelected ? "bold" : "normal"}
                    fontFamily="Georgia, serif">
                    {k}
                  </text>
                  <text x={mx} y={my + 1} textAnchor="middle" dominantBaseline="middle"
                    fill={color === "#c9a84c" ? "#8a7a4c" : "#3a3a4e"} fontSize={10}
                    fontFamily="Georgia, serif">
                    {MINOR_KEYS[i]}
                  </text>
                </g>
              );
            })}
            {activeChordIdx >= 0 && (() => {
              const chord = currentProg[activeChordIdx]?.chord;
              const i = KEYS.indexOf(chord);
              if (i < 0) return null;
              const angle = (i * 30 - 90) * (Math.PI / 180);
              const x = Math.cos(angle) * 130;
              const y = Math.sin(angle) * 130;
              return <circle cx={x} cy={y} r={28} fill="none" stroke="#c9a84c" strokeWidth="2" opacity="0.5">
                <animate attributeName="r" from="22" to="32" dur="0.8s" repeatCount="indefinite" />
                <animate attributeName="opacity" from="0.8" to="0" dur="0.8s" repeatCount="indefinite" />
              </circle>;
            })()}
          </svg>
        </div>

        {/* Controls */}
        <div style={{
          display: "grid", gridTemplateColumns: "1fr 1fr", gap: 16, marginBottom: 24,
          background: "#12142244", borderRadius: 8, padding: 20, border: "1px solid #2a2a3e"
        }}>
          <div>
            <label style={{ fontSize: 11, color: "#8a8070", letterSpacing: 1, display: "block", marginBottom: 6 }}>
              PROGRESSION
            </label>
            <select value={selectedProgression} onChange={e => setSelectedProgression(e.target.value)}
              style={{
                width: "100%", padding: "8px 12px", background: "#1a1a2e", color: "#e8dcc8",
                border: "1px solid #3a3a4e", borderRadius: 4, fontSize: 13, fontFamily: "Georgia"
              }}>
              {Object.keys(PROGRESSIONS).map(p => <option key={p} value={p}>{p}</option>)}
            </select>
          </div>
          <div>
            <label style={{ fontSize: 11, color: "#8a8070", letterSpacing: 1, display: "block", marginBottom: 6 }}>
              VOICING
            </label>
            <select value={voicing} onChange={e => setVoicing(e.target.value)}
              style={{
                width: "100%", padding: "8px 12px", background: "#1a1a2e", color: "#e8dcc8",
                border: "1px solid #3a3a4e", borderRadius: 4, fontSize: 13, fontFamily: "Georgia"
              }}>
              <option value="notes">Basic Triad</option>
              <option value="jazz">Jazz 7th</option>
              <option value="gospel">Gospel Full</option>
            </select>
          </div>
          <div>
            <label style={{ fontSize: 11, color: "#8a8070", letterSpacing: 1, display: "block", marginBottom: 6 }}>
              TEMPO: {tempo} BPM
            </label>
            <input type="range" min={40} max={140} value={tempo} onChange={e => setTempo(+e.target.value)}
              style={{ width: "100%", accentColor: "#c9a84c" }} />
          </div>
          <div style={{ display: "flex", alignItems: "flex-end" }}>
            <button onClick={playProgression} disabled={playing}
              style={{
                width: "100%", padding: "10px 20px", background: playing ? "#2a2a3e" : "#c9a84c",
                color: playing ? "#8a8070" : "#0a0e1a", border: "none", borderRadius: 4,
                fontSize: 14, fontFamily: "Georgia", cursor: playing ? "default" : "pointer",
                letterSpacing: 1, fontWeight: "bold"
              }}>
              {playing ? "PLAYING..." : "PLAY PROGRESSION"}
            </button>
          </div>
        </div>

        {/* Progression Display */}
        <div style={{
          background: "#12142244", borderRadius: 8, padding: 20,
          border: "1px solid #2a2a3e", marginBottom: 24
        }}>
          <div style={{ fontSize: 11, color: "#8a8070", letterSpacing: 1, marginBottom: 12 }}>
            PROGRESSION IN {selectedKey}
          </div>
          <div style={{ display: "flex", gap: 12, justifyContent: "center", flexWrap: "wrap" }}>
            {currentProg.map((step, i) => (
              <div key={i} onClick={() => playChord(step.chord, step.type)}
                style={{
                  padding: "16px 24px", borderRadius: 8, cursor: "pointer",
                  background: activeChordIdx === i ? "#c9a84c22" : "#1a1a2e",
                  border: `1px solid ${activeChordIdx === i ? "#c9a84c" : "#3a3a4e"}`,
                  textAlign: "center", transition: "all 0.3s",
                  minWidth: 80
                }}>
                <div style={{ fontSize: 20, color: activeChordIdx === i ? "#c9a84c" : "#e8dcc8", fontWeight: "bold" }}>
                  {step.chord}
                </div>
                <div style={{ fontSize: 12, color: "#8a8070", marginTop: 4 }}>{step.label}</div>
                {i < currentProg.length - 1 && (
                  <span style={{ position: "absolute", right: -8, top: "50%", color: "#3a3a4e" }}></span>
                )}
              </div>
            ))}
          </div>
        </div>

        {/* Theory Panel */}
        <div style={{
          background: "#12142244", borderRadius: 8, padding: 20,
          border: "1px solid #2a2a3e"
        }}>
          <div onClick={() => setShowTheory(!showTheory)}
            style={{ cursor: "pointer", display: "flex", justifyContent: "space-between", alignItems: "center" }}>
            <span style={{ fontSize: 11, color: "#8a8070", letterSpacing: 1 }}>
              THEORY — KEY OF {selectedKey}
            </span>
            <span style={{ color: "#4a4a5e" }}>{showTheory ? "▼" : "▶"}</span>
          </div>
          {showTheory && (
            <div style={{ marginTop: 16 }}>
              <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 8 }}>
                {Object.entries(relatedKeys).map(([label, k]) => (
                  <div key={label} onClick={() => { setSelectedKey(k); playChord(k, voicing); }}
                    style={{
                      padding: "10px 14px", background: "#1a1a2e", borderRadius: 6,
                      border: "1px solid #2a2a3e", cursor: "pointer",
                      display: "flex", justifyContent: "space-between", alignItems: "center"
                    }}>
                    <span style={{ fontSize: 12, color: "#8a8070" }}>{label}</span>
                    <span style={{ fontSize: 16, color: "#c9a84c", fontWeight: "bold" }}>{k}</span>
                  </div>
                ))}
              </div>
              <div style={{ marginTop: 16, fontSize: 13, color: "#8a8070", lineHeight: 1.7 }}>
                <p style={{ margin: "0 0 8px" }}>
                  <span style={{ color: "#c9a84c" }}>The IV ({relatedKeys["IV (subdominant)"]})</span> is the lift — 
                  the moment the floor rises under the congregation. When a gospel song modulates, it usually moves to the IV first.
                </p>
                <p style={{ margin: "0 0 8px" }}>
                  <span style={{ color: "#c9a84c" }}>The V ({relatedKeys["V (dominant)"]})</span> is tension — 
                  the dominant chord that demands resolution. In jazz, the ii-V creates the strongest pull back to I.
                </p>
                <p style={{ margin: 0 }}>
                  <span style={{ color: "#c9a84c" }}>The vi ({relatedKeys["vi (relative minor)"]})</span> is the cry — 
                  the relative minor that gives gospel its emotional depth. "Total Praise" lives in this space.
                </p>
              </div>
            </div>
          )}
        </div>

        {/* Ear Training */}
        <div style={{
          marginTop: 24, background: "#12142244", borderRadius: 8, padding: 20,
          border: "1px solid #2a2a3e"
        }}>
          <div style={{ fontSize: 11, color: "#8a8070", letterSpacing: 1, marginBottom: 12 }}>
            EAR TRAINING TIP
          </div>
          <div style={{ fontSize: 13, color: "#8a8070", lineHeight: 1.7 }}>
            Close your eyes. Play the progression once with your eyes open, watching the chords light up. 
            Then play it again with your eyes closed. Can you hear when the chord changes? Can you feel 
            the lift of the IV, the tension of the V, the resolution of the I? That feeling is 
            the Circle of Fifths — not as a diagram, but as a sensation in your hands and ears. 
            The theory names what your spirit already knows.
          </div>
        </div>

        <div style={{ textAlign: "center", marginTop: 24, fontSize: 11, color: "#3a3a4e", letterSpacing: 1 }}>
          KINGDOM SOUNDWORKS — SIGNATURE THEORY
        </div>
      </div>
    </div>
  );
}

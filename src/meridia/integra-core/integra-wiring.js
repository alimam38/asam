
/**
 * integra-wiring.js
 * Meridia WayPoint Crown — Live API Integration
 * 
 * Wires Index8-live.html to the Integra Core production backend.
 * Replaces all static/mock data with live DB-powered responses.
 * 
 * API Base: window.INTEGRA_API_BASE (set in Index8-live.html)
 * Production: https://integra.meridiahq.com
 * Local dev:  http://localhost:8002
 */

(function() {
  'use strict';

  const BASE = window.INTEGRA_API_BASE || 'https://integra.meridiahq.com';

  // Demo entity IDs (seeded in meridia_core)
  const ENTITIES = {
    CROWN_CLIENT:   'a1b2c3d4-0002-0002-0002-000000000002', // Hargrove Family Office
    INSTITUTION:    'a1b2c3d4-0001-0001-0001-000000000001', // Vantage Financial Partners
    CORE_CLIENT:    'a1b2c3d4-0003-0003-0003-000000000003', // Cornerstone AME
    EDGE_CLIENT:    'a1b2c3d4-0004-0004-0004-000000000004', // Gulf South Properties
    RENAISSANCE:    'a1b2c3d4-0005-0005-0005-000000000005', // Marcus Thompson
  };

  // Active entity for this demo session
  let activeEntityId = ENTITIES.CROWN_CLIENT;

  // ── API HELPERS ──────────────────────────────────────────

  async function apiFetch(path, opts = {}) {
    try {
      const url = BASE + path;
      const r = await fetch(url, {
        method: opts.method || 'GET',
        headers: { 'Content-Type': 'application/json' },
        body: opts.body ? JSON.stringify(opts.body) : undefined,
      });
      if (!r.ok) return null;
      return await r.json();
    } catch (e) {
      console.warn(`[Integra] ${path} failed:`, e.message);
      return null;
    }
  }

  // ── FORMATTERS ───────────────────────────────────────────

  function fmt$(n) {
    if (!n && n !== 0) return '—';
    if (n >= 1_000_000) return '$' + (n/1_000_000).toFixed(1) + 'M';
    if (n >= 1_000)     return '$' + (n/1_000).toFixed(0) + 'K';
    return '$' + n.toFixed(0);
  }

  function fmtPct(n) {
    if (!n && n !== 0) return '—';
    return n.toFixed(1) + '%';
  }

  function scoreColor(s) {
    if (s >= 75) return 'var(--accent-emerald)';
    if (s >= 55) return 'var(--accent-amber)';
    return 'var(--accent-rose)';
  }

  function directionArrow(d) {
    if (!d) return '';
    if (d === 'improving' || d === 'strong') return ' ↑';
    if (d === 'declining' || d === 'critical') return ' ↓';
    return ' →';
  }

  // ── DOM HELPERS ──────────────────────────────────────────

  function setText(sel, val) {
    const el = document.querySelector(sel);
    if (el && val !== null && val !== undefined) el.textContent = val;
  }

  function setHTML(sel, val) {
    const el = document.querySelector(sel);
    if (el && val !== null && val !== undefined) el.innerHTML = val;
  }

  function setStyle(sel, prop, val) {
    const el = document.querySelector(sel);
    if (el && val) el.style[prop] = val;
  }

  function setAll(sel, val) {
    document.querySelectorAll(sel).forEach(el => {
      if (val !== null && val !== undefined) el.textContent = val;
    });
  }

  // ── POSITION / FPS ───────────────────────────────────────

  async function loadPosition() {
    const data = await apiFetch(`/api/v1/position/${activeEntityId}`);
    if (!data) return;

    const fps = data.fps_score;
    const dir = directionArrow(data.fps_direction);

    // FPS score display
    setText('.fps-score', fps?.toFixed(1) + dir);
    setText('.fps-score-value', fps?.toFixed(1));
    setText('#fpsScore', fps?.toFixed(1));
    setStyle('.fps-score', 'color', scoreColor(fps));

    // FPS ring / gauge
    const ring = document.querySelector('.fps-ring circle:last-child, .progress-ring circle:last-child');
    if (ring) {
      const r = parseFloat(ring.getAttribute('r') || 45);
      const circ = 2 * Math.PI * r;
      ring.style.strokeDashoffset = circ - (fps / 100) * circ;
      ring.style.stroke = scoreColor(fps);
    }

    // Entity name
    setText('.entity-name', data.entity_name);
    setText('.client-name', data.entity_name);
    setText('[data-field="entity_name"]', data.entity_name);

    // Narrative
    setText('.fps-narrative', data.fps_narrative);
    setText('.aletheia-narrative', data.fps_narrative);
    setText('[data-field="narrative"]', data.fps_narrative);

    // Components
    if (data.components) {
      const c = data.components;
      const fields = {
        'net_position':       ['[data-component="net_position"]', '.net-position-score'],
        'liquidity_coverage': ['[data-component="liquidity"]', '.liquidity-score'],
        'dscr':               ['[data-component="dscr"]', '.dscr-score'],
        'runway':             ['[data-component="runway"]', '.runway-score'],
        'distribution_alignment': ['[data-component="distribution"]', '.distribution-score'],
      };
      for (const [key, selectors] of Object.entries(fields)) {
        const val = c[key];
        if (val !== undefined) {
          selectors.forEach(s => setText(s, val?.toFixed(1)));
        }
      }
    }

    // Period
    setText('.position-period', data.period);

    // Store for Aletheia responses
    window._integraResponses = window._integraResponses || {};
    window._integraResponses.position = data.fps_narrative;

    console.log(`[Integra] FPS loaded: ${fps} (${data.fps_direction})`);
  }

  // ── TRUST INDEX ──────────────────────────────────────────

  async function loadTrustIndex() {
    const data = await apiFetch(`/api/v1/trust-index/${activeEntityId}`);
    if (!data) return;

    const score = data.trust_index;
    setText('.trust-score', score?.toFixed(0));
    setText('.trust-index-score', score?.toFixed(0));
    setText('#trustScore', score?.toFixed(0));
    setText('[data-field="trust_index"]', score?.toFixed(0));
    setStyle('.trust-score', 'color', scoreColor(score));

    // Four dimensions
    const dims = {
      behavioral_consistency:    '[data-trust="behavioral"], .trust-behavioral',
      governance_adherence:      '[data-trust="governance"], .trust-governance',
      communication_reliability: '[data-trust="communication"], .trust-communication',
      commitment_fulfillment:    '[data-trust="commitment"], .trust-commitment',
    };
    for (const [key, sel] of Object.entries(dims)) {
      const val = data[key];
      if (val !== undefined) {
        sel.split(',').forEach(s => {
          document.querySelectorAll(s.trim()).forEach(el => {
            el.textContent = val?.toFixed(0);
          });
        });
      }
    }

    // Direction
    setText('.trust-direction', data.direction ? data.direction + directionArrow(data.direction) : '');
    console.log(`[Integra] Trust Index loaded: ${score}`);
  }

  // ── ENTITIES ─────────────────────────────────────────────

  async function loadEntities() {
    const data = await apiFetch('/api/v1/entities');
    if (!data || !data.entities) return;

    const entities = data.entities;
    // Update entity count
    setText('.entity-count', entities.length);

    // Try to find entity grid and populate
    const grid = document.querySelector('.entity-grid, #entityGrid, .entities-container');
    if (grid && entities.length) {
      // Only inject if grid looks empty or has placeholder data
      const existingCards = grid.querySelectorAll('[data-entity-id]');
      if (existingCards.length === 0) {
        grid.innerHTML = entities.map(e => `
          <div class="entity-card ${e.status === 'healthy' ? 'healthy' : e.status === 'watch' ? 'watch' : ''}"
               data-entity-id="${e.id}"
               onclick="window._integraSetEntity && window._integraSetEntity('${e.id}')">
            <div class="entity-type">${e.type || e.tier}</div>
            <div class="entity-name-card">${e.name}</div>
            <div class="entity-metrics">
              <span class="entity-metric">${e.metrics?.fps_score ? 'FPS ' + e.metrics.fps_score : ''}</span>
            </div>
          </div>
        `).join('');
      }
    }

    console.log(`[Integra] Entities loaded: ${entities.length}`);
  }

  // ── MX LIVE CONNECTION ───────────────────────────────────

  async function connectMX(entityId) {
    console.log(`[Integra] Connecting MX for ${entityId}...`);
    setText('.connection-status', 'Connecting...');

    const data = await apiFetch(`/api/v1/connect/mx/${entityId}`, { method: 'POST' });
    if (!data) {
      setText('.connection-status', 'Connection failed');
      return null;
    }

    setText('.connection-status', `Connected — ${data.accounts_connected} accounts`);
    setText('.data-source', data.source);

    // Reload position with fresh MX data
    await loadPosition();
    await loadTrustIndex();

    console.log(`[Integra] MX connected: FPS ${data.fps_score} from ${data.source}`);
    return data;
  }

  // ── SIGNALS ──────────────────────────────────────────────

  async function loadSignals() {
    const data = await apiFetch('/api/v1/signal-feed');
    if (!data || !data.signals) return;

    const feed = document.querySelector('.signal-feed, #signalFeed, .signals-list');
    if (!feed) return;

    const signals = data.signals.slice(0, 8);
    if (signals.length === 0) return;

    // Only inject if feed has no live content
    const existing = feed.querySelectorAll('[data-signal-id]');
    if (existing.length > 0) return;

    feed.innerHTML = signals.map(s => `
      <div class="signal-item ${s.severity || 'info'}" data-signal-id="${s.id}">
        <div class="signal-severity">${s.severity?.toUpperCase() || 'INFO'}</div>
        <div class="signal-message">${s.message || s.title || ''}</div>
        <div class="signal-time">${s.timestamp ? new Date(s.timestamp).toLocaleTimeString() : ''}</div>
      </div>
    `).join('');

    console.log(`[Integra] ${signals.length} signals loaded`);
  }

  // ── GOVERNANCE ALERTS ────────────────────────────────────

  async function loadGovernance() {
    const data = await apiFetch('/api/v1/governance-alerts');
    if (!data || !data.alerts) return;

    const alerts = data.alerts;
    setText('.governance-count', alerts.length);
    setText('.governance-badge', alerts.length > 0 ? alerts.length : '');

    // Update any open governance items visible
    const openAlerts = alerts.filter(a => a.action_required);
    if (openAlerts.length > 0) {
      window._integraResponses = window._integraResponses || {};
      window._integraResponses.governance = `${openAlerts.length} governance items require your approval. The most urgent: ${openAlerts[0]?.title || 'Review pending'}.`;
    }

    console.log(`[Integra] ${alerts.length} governance alerts`);
  }

  // ── MACRO CONTEXT ────────────────────────────────────────

  async function loadMacro() {
    const data = await apiFetch('/api/v1/macro');
    if (!data) return;

    // Fed Funds Rate
    const ff = data.FEDFUNDS;
    if (ff) {
      setText('.fed-funds-rate', ff.value?.toFixed(2) + '%');
      setText('[data-macro="FEDFUNDS"]', ff.value?.toFixed(2) + '%');
    }

    // Mortgage Rate
    const mort = data.MORTGAGE30US;
    if (mort) {
      setText('.mortgage-rate', mort.value?.toFixed(2) + '%');
      setText('[data-macro="MORTGAGE30US"]', mort.value?.toFixed(2) + '%');
    }

    // CPI
    const cpi = data.CPIAUCSL;
    if (cpi) {
      setText('[data-macro="CPIAUCSL"]', cpi.value?.toFixed(1));
    }

    console.log(`[Integra] Macro: FF=${ff?.value}%, Mortgage=${mort?.value}%`);
  }

  // ── REPORTS ──────────────────────────────────────────────

  async function loadReport(audience) {
    audience = audience || 'board';
    const data = await apiFetch(`/api/v1/reports/${audience}`);
    if (!data) return null;

    const container = document.querySelector('#reportContent, .report-content');
    if (container) {
      let html = `<h3>${data.title || ''}</h3>`;
      if (data.executive_summary) {
        html += `<p class="report-summary">${data.executive_summary}</p>`;
      }
      if (data.sections) {
        const sections = Array.isArray(data.sections)
          ? data.sections
          : Object.entries(data.sections).map(([k, v]) => ({
              heading: k.replace(/_/g, ' ').replace(/\b\w/g, l => l.toUpperCase()),
              content: typeof v === 'string' ? v : JSON.stringify(v, null, 2)
            }));
        sections.forEach(s => {
          html += `<div class="report-section">
            <h4>${s.heading || ''}</h4>
            <p>${s.content || ''}</p>
          </div>`;
        });
      }
      container.innerHTML = html;
    }

    return data;
  }

  // ── SCENARIO ENGINE ──────────────────────────────────────

  async function runScenario(adjustments, scenarioName) {
    const body = {
      entity_id:     activeEntityId,
      scenario_name: scenarioName || 'Custom Scenario',
      adjustments:   adjustments || {},
    };

    const data = await apiFetch('/api/v1/scenario', { method: 'POST', body });
    if (!data) return null;

    setText('.scenario-fps', data.projected_fps?.toFixed(1));
    setText('.scenario-delta', (data.fps_delta >= 0 ? '+' : '') + data.fps_delta?.toFixed(1));
    setText('.scenario-narrative', data.impact_narrative);
    setStyle('.scenario-delta', 'color',
      data.fps_delta >= 0 ? 'var(--accent-emerald)' : 'var(--accent-rose)');

    window._integraResponses = window._integraResponses || {};
    window._integraResponses.scenario = data.impact_narrative;

    console.log(`[Integra] Scenario: ${data.baseline_fps} → ${data.projected_fps}`);
    return data;
  }

  // ── ENTITY SWITCHER ──────────────────────────────────────

  function setActiveEntity(entityId) {
    activeEntityId = entityId;
    loadAll();
    console.log(`[Integra] Switched to entity: ${entityId}`);
  }

  window._integraSetEntity = setActiveEntity;
  window._integraEntities  = ENTITIES;
  window._integraConnect   = connectMX;
  window._integraReport    = loadReport;
  window._integraScenario  = runScenario;

  // ── LOAD ALL ─────────────────────────────────────────────

  async function loadAll() {
    console.log(`[Integra] Loading from ${BASE}...`);
    await Promise.all([
      loadPosition(),
      loadTrustIndex(),
      loadEntities(),
      loadSignals(),
      loadGovernance(),
      loadMacro(),
    ]);
    console.log('[Integra] All data loaded.');
  }

  // ── INIT ─────────────────────────────────────────────────

  function init() {
    // Override report fetch in Index8 Aletheia panel
    window.INTEGRA_API_BASE = BASE;

    // Load all data
    loadAll();

    // Refresh every 5 minutes
    setInterval(loadAll, 5 * 60 * 1000);

    // Expose connection button handler
    const connectBtn = document.querySelector('#connectMX, .connect-mx-btn, [data-action="connect-mx"]');
    if (connectBtn) {
      connectBtn.addEventListener('click', () => connectMX(activeEntityId));
    }

    console.log(`[Integra] Wired to ${BASE} — entity: ${activeEntityId}`);
  }

  // Run after DOM ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

})();

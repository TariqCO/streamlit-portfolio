import streamlit as st

st.set_page_config(
    page_title="Tariq | Portfolio",
    page_icon="💻",
    layout="centered"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Share+Tech+Mono&family=Syne:wght@400;700&display=swap');

html, body, [class*="css"] { font-family: 'Syne', sans-serif; }

.stApp { background-color: #0a0c10; color: #e2e8f0; }

.grid-bg {
    position: fixed;
    top: 0; left: 0; right: 0; bottom: 0;
    background-image:
        repeating-linear-gradient(0deg, transparent, transparent 39px, rgba(0,255,160,0.03) 40px),
        repeating-linear-gradient(90deg, transparent, transparent 39px, rgba(0,255,160,0.03) 40px);
    pointer-events: none;
    z-index: 0;
}

.label {
    font-family: 'Share Tech Mono', monospace;
    font-size: 12px;
    color: #00ffa0;
    letter-spacing: 0.15em;
    margin-bottom: 4px;
}

.hero-name {
    font-size: 52px;
    font-weight: 700;
    color: #f8fafc;
    line-height: 1.1;
    margin: 0;
}

.cursor {
    display: inline-block;
    width: 3px;
    height: 0.8em;
    background: #00ffa0;
    margin-left: 4px;
    vertical-align: middle;
    animation: blink 1s step-end infinite;
}

@keyframes blink { 0%,100%{opacity:1} 50%{opacity:0} }

.bio {
    color: #94a3b8;
    font-size: 15px;
    line-height: 1.75;
    margin-top: 14px;
    max-width: 520px;
}

.tags {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    margin-top: 16px;
}

.tag {
    font-family: 'Share Tech Mono', monospace;
    font-size: 11px;
    padding: 4px 10px;
    border: 1px solid rgba(0,255,160,0.25);
    border-radius: 2px;
    color: #00ffa0;
    background: rgba(0,255,160,0.05);
}

.divider {
    height: 1px;
    background: linear-gradient(90deg, #00ffa0 0%, rgba(0,255,160,0.08) 70%, transparent 100%);
    margin: 32px 0;
}

.section-label {
    font-family: 'Share Tech Mono', monospace;
    font-size: 11px;
    color: #475569;
    letter-spacing: 0.12em;
    margin-bottom: 20px;
}

.card {
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 6px;
    padding: 24px 28px;
    background: rgba(255,255,255,0.025);
    transition: border-color 0.2s, background 0.2s;
}

.card:hover {
    border-color: rgba(0,255,160,0.35);
    background: rgba(0,255,160,0.035);
}

.card-top {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 12px;
    margin-bottom: 10px;
}

.card-title {
    font-size: 18px;
    font-weight: 700;
    color: #f1f5f9;
}

.badge {
    font-family: 'Share Tech Mono', monospace;
    font-size: 10px;
    padding: 3px 9px;
    border-radius: 2px;
    background: rgba(0,255,160,0.08);
    color: #00ffa0;
    border: 1px solid rgba(0,255,160,0.2);
    white-space: nowrap;
}

.card-desc {
    font-size: 13.5px;
    color: #94a3b8;
    line-height: 1.7;
    margin-bottom: 16px;
}

.stack {
    display: flex;
    flex-wrap: wrap;
    gap: 6px;
    margin-bottom: 18px;
}

.pill {
    font-family: 'Share Tech Mono', monospace;
    font-size: 11px;
    padding: 3px 9px;
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(255,255,255,0.09);
    border-radius: 2px;
    color: #cbd5e1;
}

.links { display: flex; gap: 18px; }

.link-btn {
    font-family: 'Share Tech Mono', monospace;
    font-size: 12px;
    color: #00ffa0;
    text-decoration: none;
    border-bottom: 1px solid transparent;
    padding-bottom: 1px;
    transition: border-color 0.15s;
}

.link-btn:hover { border-bottom-color: #00ffa0; }

.link-muted { color: #64748b !important; }
.link-muted:hover { color: #94a3b8 !important; border-bottom-color: #64748b !important; }

.footer {
    display: flex;
    flex-wrap: wrap;
    gap: 20px;
    margin-top: 8px;
}

.social {
    font-family: 'Share Tech Mono', monospace;
    font-size: 12px;
    color: #475569;
    text-decoration: none;
    transition: color 0.15s;
}

.social:hover { color: #00ffa0; }

#MainMenu, footer, header { visibility: hidden; }
.block-container { padding-top: 3rem; max-width: 680px; }
</style>

<div class="grid-bg"></div>
""", unsafe_allow_html=True)


# ── HERO ──────────────────────────────────────────────────────────────────────
st.markdown('<p class="label">// portfolio.init()</p>', unsafe_allow_html=True)
st.markdown("""
<h1 class="hero-name">Hi! Tariq here</h1>
<p class="bio">
  BBA student at FUUAST Karachi &amp; Python Developer at You Excel.<br>
  Building data dashboards and web UIs that actually work.
</p>
<div class="tags">
  <span class="tag">Python</span>
  <span class="tag">Streamlit</span>
  <span class="tag">Pandas</span>
  <span class="tag">Karachi, PK</span>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)


# ── PROJECTS ──────────────────────────────────────────────────────────────────
st.markdown('<p class="section-label">// projects</p>', unsafe_allow_html=True)

project = {
    "title": "Course Registration Dashboard",
    "badge": "Streamlit",
    "desc": "A full-featured university dashboard with student authentication, enrollment analytics, digital ID card generation, and course outline display. Deployed live with a public GitHub repo.",
    "stack": ["Python", "Streamlit", "Pandas", "Auth", "Data Viz"],
    "demo": "https://ultimate-course.streamlit.app/",
    "github": "https://github.com/TariqCO/stream-lit/",
}

pills_html = "".join(f'<span class="pill">{s}</span>' for s in project["stack"])

st.markdown(f"""
<div class="card">
  <div class="card-top">
    <div class="card-title">{project["title"]}</div>
    <div class="badge">{project["badge"]}</div>
  </div>
  <p class="card-desc">{project["desc"]}</p>
  <div class="stack">{pills_html}</div>
  <div class="links">
    <a href="{project["demo"]}" target="_blank" class="link-btn">↗ Live Demo</a>
    <a href="{project["github"]}" target="_blank" class="link-btn link-muted">⌥ GitHub</a>
  </div>
</div>
""", unsafe_allow_html=True)


# ── FOOTER ────────────────────────────────────────────────────────────────────
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="footer">
  <a href="https://github.com/TariqCO" target="_blank" class="social">⌥ github.com/TariqCO</a>
  <a href="https://linkedin.com/in/tariq-1712tr" target="_blank" class="social">in linkedin.com/in/tariq-1712tr</a>
  <a href="mailto:tariq.official1712@gmail.com" class="social">@ tariq.official1712@gmail.com</a>
</div>
""", unsafe_allow_html=True)
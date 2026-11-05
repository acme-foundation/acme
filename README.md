# ACME: Zero-Code Deterministic NLP Specification Architecture
> **Decentralized Specification Framework for Human-Machine Symbiosis & Invariant Equilibrium**  
> *Release v3.0.1-Genesis | Pure Specification Core & Recursive Normative Compiler*  
> *Legacy Incubation Epoch (v1.x - v2.x / 53 Theses) Retired & Frozen at `archive/v2-legacy-incubator`*  

---

### 1. VALUE PROPOSITION & SYSTEM MISSION
LLM tabanlı otonom yazılım üretiminde bağlam sapmasını (context drift), monolitik kirlenmeyi ve halüsinasyon riskini ortadan kaldıran DoF=0 (Sıfır Serbestlik Derecesi) anayasal şartname çerçevesi.

ACME, tek satır çalıştırılabilir kod içermeyen saf bir bilişsel mimari ve üst hukuk doktrinidir (Lex Superior). İnsan niyetini (Human Intent) doğrulanabilir, matematiksel ve indirgenemez negatif kısıtlarla mühürleyerek ajanların deterministik koridorda inşaat yapmasını temin eder.

---

### 2. CORE ARCHITECTURAL PILLARS (DoF = 0)
1. **Decoupled Cognitive Specification Plane vs. Execution Plane:**
   Bilişsel şartname düzlemi (karargâh / normative control plane) ile kod icra düzlemi (downstream runtime data plane) mutlak şekilde yalıtılmıştır. Karargâha çalıştırılabilir şantiye araçları sızamaz (`INV-PLANE-SEPARATION`).
2. **3-Tier Structural Hierarchy:**
   Tüm sistemler katı üç kademede inşa edilir: Uygulama Çatısı (Shell / Orchestrator) $\to$ Düzenler (Layouts / Skeleton Slots) $\to$ Bileşenler (Composite & Atomic Components). Bileşen eklemleri faz kilitli harmonik sözleşmelerle bağlanır (`INV-3-TIER-DECOMPOSITION`).
3. **Spectral Triage & Kinematic Synergy:**
   Zaman uzayındaki kaotik ve gürültülü kullanıcı şikayetleri Fourier dönüşümüyle spektral frekanslara ayrıştırılır. Yüksek frekanslı parazitler alçak geçiren filtreyle elenir; doğrudan düşük frekanslı kök taşıyıcı darboğaz biçimsel kabul kriterlerine (DoD) indirgenir (`INV-SPECTRAL-TRIAGE`).
4. **Diagnostic Defect Isolation & Telemetric Triage:**
   Giriş sinyalleri öncelikle ham semptom kabul edilir; telemetrik metriklerle ölçülmeden kök problem ilan edilemez (`INV-DIAGNOSTIC-TRIAGE`).
5. **Circuit Breaker, Degraded State Fallback & Acute Stabilization:**
   Kriz, sistemik kilitlenme ve termal aşırı yük anında derleme hızında Faz-0 hemostaz (yük tahliyesi, devre kesici) tetiklenir; sistem stabilize edildikten sonra Faz-1 kök neden şartnamesi zorunlu tutulur (`INV-CRISIS-HEMOSTASIS`).
6. **Anti-Monolithic Escalation & Least-Action Drift Mitigation:**
   Modelin spontane ilk tercihi istatistiksel tembellik gereği hükmen ilkel kabul edilir. Çözüm, rüştünü ispatlamış en üst soyutlama ve modülerlik seviyesine yükseltilmeden derlenemez (`INV-PRIMITIVE-ATTRACTOR-REFUTATION`).
7. **Scale-Invariant Structural Isomorphism (Macro-to-Micro Coherence):**
   Kuşbakışı makro mimari ile en alt atomik mikro bileşen arasındaki faz farkı sıfırdır ($\text{MSE} = 0$, `INV-HOLOGRAPHIC-COHERENCE`).

---

### 3. REPOSITORY SCAFFOLDING (v3.0.1-GENESIS)
```text
acme/
├── faculty/              # Unified Living Syllabus Catalogs (SYS_systems.md, PHI_philosophy.md, LAW_law.md)
├── registry/             # Verified Human Anchors & Graduation Registry (graduates.json)
├── theses/               # Unified Living Theses Corpus ([CODE]_[NO]_[SLUG].md)
├── templates/            # Standardized Schemas (RFC_TEMPLATE, SPEC_TEMPLATE, AOP_LIFECYCLE)
├── AGENTS.md             # Execution Protocol for AI Agents & Downstream Sanitization
├── CONSTITUTION.md       # Irreducible Constitutional Lex Superior (v3.0.1-Genesis)
├── verify.py             # Pure Stdlib Boundary Gatekeeper Turnstile
├── live_state.json       # Real-Time Telemetry State Machine
├── live_view.html        # Real-Time Zero-Refresh Dashboard Cockpit
└── README.md             # Specification & Architecture Overview
```

---

### 4. DOWNSTREAM ADOPTION & THE UNIVERSAL `.norm` STANDARD
Downstream client projects (workspaces) adopt ACME as an external normative authority (*Lex Superior*), not as boilerplate application code.

#### 4.1. Downstream Non-Pollution Invariant
* **Never Clone ACME into Active Projects:** ACME internal governance faculties (`theses/`, `faculty/`, `registry/`, `CONSTITUTION.md`) must **never** be cloned, unpacked, or committed into downstream client repositories.
* **Separation of Concerns:** ACME is the normative doctrine plane (Lex Superior); the client workspace is the empirical execution plane.

#### 4.2. Anchoring via `.norm` (or `.acme`) Manifest
A downstream project establishes constitutional compliance exclusively through a single root manifest:
```json
{
  "$schema": "https://acme-standard.org/schemas/v3/norm.json",
  "repo": "https://github.com/acme-foundation/acme.git",
  "version": "v3.0.1-genesis",
  "mode": "normative_reference",
  "extends": "https://github.com/acme-foundation/acme.git#v3.0.1-genesis",
  "feed": {
    "persona": false,
    "org": false
  }
}
```

---

### 5. QUICKSTART / VERIFICATION & MERKLE NON-REPUDIATION
Every state commit is cryptographically audited against zero-code purity, registry integrity, domain cleanliness, and constitutional invariant parity via the standard-library boundary turnstile:
```bash
python verify.py --verify-all
```
All graduation diplomas are permanently anchored to immutable Git Merkle commit SHAs.

# FACULTY OF SYSTEMS & APPLIED CYBERNETICS
> KOD: SYS
> ROL: Müfredat Aksiyomları ve Yaşayan Ders Kataloğu (Living Syllabus)

---

## 1. KURUCU MÜFREDAT AKSİYOMLARI (FOUNDATIONAL AXIOMS)
* **Second Law of Thermodynamics (Clausius, Boltzmann):** Isolated cognitive systems naturally evolve toward maximal entropy (semantic drift, hallucination, structural decay). Sustaining order requires work and bounded energy dissipation.
* **Principle of Least Action (PLA - Hamilton, Lagrange):** The physical trajectory between two states minimizes the action integral ($\delta S = 0$). Cognitive workflows must minimize computational overhead, token bloat, and redundant state transitions.
* **Autopoiesis & Homeostasis (Ashby, Maturana, Varela):** Viable systems reproduce their internal organization through circular self-referential boundary preservation against external perturbation.
* **3 Kademeli Hiyerarşik Ayrışım ve Evrimsel Parite (Tri-Tier Hierarchical Decomposition & Evolutionary Parity - DoF = 0):** Tüm mimari yapılar zorunlu olarak 3 kademede inşa edilir: Uygulama Çatısı (Shell / Orchestrator: global yaşam döngüsü, yönlendirme ve durum orkestrasyonu), Düzenler (Layouts / Skeleton Slots: sayfa/ekran iskeletleri ve yuva yerleşimleri) ve Bileşenler (Components: Composite & Atomic: izole, yeniden kullanılabilir atomik ve birleşik yapı taşları). Modelin En Az Eylem İlkesi'ni monolitik ilkelliğe kaçış bahanesi olarak kullanması yasaktır; modern modüler bileşen ayrışımı korunmalı, etki alanı (blast radius) izole edilerek Jenga çöküşü önlenmelidir (`REJECT_MONOLITHIC_COLLAPSE`).
* **Holografik Eşyapısallık ve Faz Farkı Sıfırlama (Holographic Coherence - DoF = 0):** Çözümün makro mimarisi ile en alt mikro bileşeni aynı evrimsel olgunluk ve negatif kısıt seviyesinde olmak zorundadır. Kuşbakışı görünüm ile fırça darbesi arasındaki faz farkı sıfır ($\text{MSE} = 0$) olmalıdır (`REJECT_FRACTAL_ASYMMETRY`).
* **Akut Hemostaz Protokolü (Circuit Breaker & Fallback Handlers - DoF = 0):** Kriz anında derleme hızında semptom giderme adımları (yük tahliyesi, güvenli rölantiye alma, acil devre kesici, geçici kabuk bağlama) sistemik bir refleks olarak zorunludur (`CIRCUIT_BREAKER_HALT`). Hayati tehlike, kilitlenme ve termal aşırı yük durumunda kök neden aranmadan semptom bastırılır (Faz-0); acil turnike uygulandıktan ve yaşam sinyalleri güvenli koridora döndükten sonra kalıcı Faz-1 ontolojik tahlil taahhüt edilir (`REJECT_UNTRIAGED_PATCH`).
* **Spektral Triyaj ve Kinematik Sinerji (Spectral Triage & Kinematic Synergy - DoF = 0):** Semptom sinyalleri zaman uzayında kaotik bir dalgalanmadır; Fourier ayrıştırması (FFT) ile yüksek frekanslı parazitler (sıfatlar, duygusal telaşlar, anlık sıçramalar) alçak geçiren filtreyle elenir (`REJECT_HIGH_FREQUENCY_FLUFF`). Sistemik krizin düşük frekanslı taşıyıcı harmonikleri (kök patoloji) izole edilir. Katmanlar arasındaki eklemler (props/events/APIs) Bernstein kinematik sinerjisiyle faz kilitli harmonik sözleşmelere bağlanarak sistemik serbestlik derecesi $\text{DoF} = 0$ noktasına indirgenir (`REJECT_UNCONSTRAINED_JOINTS`).

### Akut Hemostaz Protokolü (Circuit Breaker & Fallback Handlers)
Kriz, sistemik kilitlenme ve termal aşırı yük durumunda derleme hızında semptom giderme adımları zorunlu bir sistemik kuraldır (DoF = 0):
1. **Yük Tahliyesi (Load Shedding & Traffic Shunting):** Çöküşü tetikleyen işlem ve trafik akışı derhal kesilir veya izole hatta aktarılır.
2. **Güvenli Rölantiye Alma (Quiescent Idle / Circuit Breaker):** İşlemci, bellek ve token tüketimi asgari güvenli taban seviyeye sabitlenir (`CIRCUIT_BREAKER_HALT`).
3. **Geçici Kabuk Bağlama (Symptomatic Tourniquet):** Organizmanın dağılmasını önleyen acil semptomatik yama devreye alınır; kalıcı mimari çözüm kabul edilmez, ardında zorunlu Faz-1 Kök Neden Taahhüdü bırakır (`REJECT_UNTRIAGED_PATCH`).

### Spektral Triyaj ve Kinematik Sinerji Protokolü
Semptom sinyalinin Fourier analiziyle kök frekansa indirgenmesi ve bileşen eklemlerinin Bernstein kinematik modeliyle faz kilitli bağlanması zorunlu bir sistemik kuraldır (DoF = 0):
1. **Fourier Spektral Ayrıştırma:** Zaman uzayındaki ham kullanıcı/telemetri girdisi spektral bileşenlerine ayrıştırılır.
2. **Alçak Geçiren Filtreleme (Low-Pass Filter):** Anlık telaş ve öznel sıfatlar ayıklanarak yalnızca temel taşıyıcı frekans (kök mimari darboğaz) muhafaza edilir (`REJECT_TIME_DOMAIN_NOISE`).
3. **Bernstein Kinematik Faz Kilidi:** 3 kademeli hiyerarşideki (`Shell -> Layout -> Component`) bileşen eklemleri harmonik faz kilidiyle bağlanır; bağımsız serbestlik dereceleri sıfırlanarak Jenga çöküşü imkânsız kılınır (`REJECT_UNCONSTRAINED_JOINTS`).

---

## 2. MÜFREDAT VE MEZUN DERSLERİ

### SYS-001: PRINCIPLE OF LEAST ACTION AND THERMODYNAMIC CONATUS
Dispatching redundant intermediate processes, permitting unbounded generation cycles, or expanding cognitive state beyond minimal required action is strictly prohibited (`REJECT_EXTREME_ENTROPY`, DoF = 0).

### SYS-002: SPEC-FIRST ZERO-BINARY DISTRIBUTION AND PORTABLE CONTRACTS
Distributing executable code as opaque binary artifacts or embarking on implementation without a pre-compiled, verifiable specification is strictly prohibited (`REJECT_UNSEALED_BINARY`, DoF = 0).

### SYS-004: AUTONOMOUS OVERSIGHT AND THE FOUR-STAGE GOVERNANCE LOOP
Autonomous execution that bypasses the four-stage oversight loop (Intake -> Decomposition -> Red-Team Critic -> Telemetry Seal) or modifies unsealed external dependencies is strictly prohibited (`REJECT_UNANCHORED_MUTATION`, DoF = 0).

### SYS-005: CONTROL PLANE DATA PLANE PARTITION AND CLEAN-ROOM ISOLATION
Bleeding state or administrative control primitives into execution data payloads, or violating clean-room environment isolation between tenant tasks is strictly prohibited (`REJECT_PLANE_CROSSING`, DoF = 0).

### SYS-054: OBSERVABLE AUTONOMOUS OVERSIGHT & LIVE-STATE TELEMETRY
Running background agent execution loops, critic evaluations, or state transitions without continuous, verifiable publication to an observable live-state telemetry ledger is strictly prohibited (`REJECT_OPAQUE_EXECUTION`, DoF = 0).

### SYS-101: PRINCIPLE OF LEAST ACTION IN COGNITIVE ARTIFACTS
Speculative drift beyond the explicit task specification and unconstrained generative output outside formal contracts constitutes a fatal compilation error (`REJECT`).

### SYS-102: FLIGHT DYNAMICS STATE MACHINE & TRAJECTORY GOVERNANCE
Skipping discrete flight phases, emitting ungrounded predictive leaps without passing through flight dynamic bounds, or continuing execution when envelope limits are breached is strictly prohibited (`REJECT`).

### SYS-103: ADVERSARIAL TWIN SPECIFICATION PROTOCOL AND CRUCIBLE FALSIFICATION GATE
Deploying or declaring production-ready any capability specification that lacks an accompanying, actively executed adversarial twin stress harness is strictly prohibited (`REJECT`).

### SYS-104: ONTOLOGICAL ISLAND AND CONTEXT HEADER ARCHITECTURE
Cross-task context contamination, horizontal state leakage between concurrent subagents, and execution without cryptographic task headers are strictly prohibited (`REJECT`).

### SYS-105: STANDARD-FIRST RESOLVER AND ZERO-REINVENTION REVERSE ENGINEERING ENGINE
Synthesizing novel code or logic where functionally equivalent standard library primitives or existing brownfield assets exist is strictly prohibited (`ReinventionBreach`, DoF = 0).

### SYS-106: TREE OF THOUGHTS AND PROCESS REWARD MODEL SEARCH HARNESS
Accepting unverified trajectory leaps without step-level PRM scoring, or exploring generative tree branches below calibrated quality thresholds is strictly prohibited (`REJECT`).

### SYS-107: ALICE MASTER CHEF & SYMMETRIC ROLE-SPEC ORCHESTRATION PROTOCOL
Asymmetric agent role execution lacking mutual contract verification, or uncoordinated multi-agent handoffs without formal input/output parity are strictly prohibited (`REJECT`).

### SYS-108: DISTRIBUTED RUNNER GRID & EPHEMERAL WORKER PROTOCOL
Retaining persistent state across ephemeral task runners or permitting runner nodes to operate outside central coordinator Merkle bounds is strictly prohibited (`REJECT`).

### SYS-109: DOWNSTREAM INTAKE QUARANTINE & AUTONOMOUS NORM SYNCHRONIZATION
Accepting downstream client artifacts directly into core registries without passing through quarantine isolation and norm validation is strictly prohibited (`REJECT`).

### SYS-110: ENTERPRISE BROWNFIELD INSPECTOR & CONTINUOUS ARCHITECTURE
Modifying legacy enterprise codebases without prior structural AST inspection, dependency graph extraction, and non-breaking contract validation is strictly prohibited (`REJECT`).

### SYS-111: AUTOPOIETIC CADENCE & TRI-TIER SPEC-ALIGNED SEMVER PROTOCOL
Publishing semantic version increments that fail to correspond strictly to specification invariant changes (Major=Lex, Minor=Norm, Patch=Heuristic) is strictly prohibited (`REJECT`).

### SYS-112: HOLOGRAPHIC COHERENCE & FRACTAL WEAKEST-LINK ARCHITECTURE
Allowing local subsystem degradation to exceed global tolerance thresholds, or treating subsystem failures in isolation without evaluating systemic resonance is strictly prohibited (`REJECT`).

### SYS-113: STATEFUL SCAR-TISSUE GROUNDING & PRE-MORTEM DIALECTIC ARCHITECTURE
Repeating historically documented failure modes or discarding verified negative scar tokens during solution synthesis is strictly prohibited (`REJECT_UNANCHORED_INCEPTION`).

### SYS-114: OSMOSIS PROTOCOL, INTERLINGUA SPECIFICATION & UNIVERSAL NODE ISOMORPHISM
Inter-node communication using non-standardized proprietary dialects or failing to serialize through the universal Osmosis interlingua schema is strictly prohibited (`REJECT`).

### SYS-115: HOLOGRAPHIC THEORY OF CONSTRAINTS (H-TOC) & BOUNDARY HOMEOSTASIS
Optimizing non-bottleneck subsystems while systemic throughput constraints remain unaddressed is strictly prohibited (`REJECT`).

### SYS-116: SCALE INVARIANCE & MICRO-MACRO FAILURE ISOMORPHISM
Drafting specifications without an explicit pre-mortem catalog of the top 3 domain failure modes and negative constraints (DoF = 0) is strictly prohibited (`REJECT_UNANCHORED_INCEPTION`).

### SYS-117: TRI-TIER CONTEXT FABRIC, SINGLE MANIFEST & PRE-FLIGHT CIRCUIT BREAKER
Commencing task execution without a sealed single manifest or with unverified cross-tier context dependencies triggers an immediate pre-flight halt (`HALT`).

### SYS-118: ASYNCHRONOUS MERKLE STATE STREAMING & BOUNDED LATENCY
Emitting asynchronous state updates that breach latency bounds or fail to commit to the monotonic Merkle chain is strictly prohibited (`REJECT`).

### SYS-119: AGENTIC UNIFIED PROCESS META-PIPELINE & POLYMATH MORPHING
Transitioning between operational phases without fulfilling Phase Exit Criteria (DoD) or allowing agent persona drift during execution is strictly prohibited (`REJECT`).

### SYS-120: KEYSTONE INVARIANT ARCHITECTURE & LEAST ACTION CADENCE
Synthesizing peripheral logic before locking core structural keystone nodes in the dependency graph is strictly prohibited (`REJECT`).

### SYS-121: BILATERAL CONSTRAINT SATISFACTION & FLUFF-FREE ASSET MATCHING
Allowing subjective promotional adjectives or ungrounded claims into asset matching algorithms is strictly prohibited; matching must evaluate over stripped Boolean constraints (`REJECT`).

### SYS-122: SEQUENCE PRECEDENCE, SOCRATIC CIRCUIT BREAKER & UNANCHORED LEAP REJECTION
Advancing pipeline stages out of precedence order or bypassing the Socratic circuit breaker without verified upstream evidence is strictly prohibited (`REJECT`).

### SYS-123: CIRCADIAN CADENCE, REVEILLE ROLL-CALL & RETREAT CONSOLIDATION PROTOCOL
Skipping morning upstream invariant alignment (Reveille) or failing to execute end-of-day delta consolidation and garbage collection (Retreat) is strictly prohibited (`REJECT`).

### SYS-124: HIERARCHICAL ARCHETYPE INHERITANCE IN GOVERNANCE PMO
Deriving product specifications without explicit archetype tier inheritance or allowing runtime state leakage between archetype boundaries is strictly prohibited (`REJECT`).

### SYS-125: AIR-GAPPED STANDALONE PUBLIC DISTRIBUTION & CLEAN-ROOM EXPORT
Exporting public distribution packages that contain internal governance artifacts, private credentials, or un-sanitized scratchpads is strictly prohibited (`REJECT`).

### SYS-126: ARCHETYPE INHERITANCE, EXTENSION CONTRACTS & SPEC-LEVEL MONOLITHIC INLINING
Deploying distributed runtime dependencies where spec-level monolithic inlining is mandated constitutes architectural failure (`REJECT`).

### SYS-127: CANONICAL 7-STEP AOP OPERATIONAL LIFECYCLE STATE MACHINE
Operating outside the 7 canonical lifecycle states (READY -> DIRECTIVE -> MARCH -> EXECUTE & TELEMETRY -> RELEASE -> RETREAT -> EOD SUMMARY) is strictly prohibited (`REJECT`).

### SYS-128: ISOTROPIC MANIFOLD GEOMETRIC KERNEL AND EMBODIED SYMMETRY GOVERNANCE
Operating on uncalibrated, anisotropic latent representations that induce semantic hubness drift or ungrounded hallucinations is strictly prohibited (`REJECT`).

### SYS-129: DUAL-PLANE EPISTEMIC X-RAY AND GROUND TRUTH DELTA ENGINE
Conflating presentation facade with internal epistemic state, or failing to quantify ground truth divergence ($L_1 > \epsilon$) is strictly prohibited (`REJECT`).

### SYS-130: PORTABLE SPECIFICATION, CROSS-AGENT STATE CONTINUITY AND COMPONENT TRACEABILITY
Disregarding portable specification envelopes, dropping cross-agent state continuity records, or breaking 4-tier component traceability is strictly prohibited (`REJECT`).

### SYS-131: STATEFUL SCAR TISSUE, ANTI-FRAGILE FAILURE LEDGER AND REVERSE TELEMETRY
Discarding regression scar tokens, violating concurrency locks on state ledgers, or leaking PI into reverse telemetry pipelines is strictly prohibited (`REJECT`).

### SYS-132: UNIVERSAL .NORM SPECIFICATION AND CASCADING NORMATIVE INHERITANCE
Altering the fallback precedence order ([.norm, .acme]), violating Kelsen normative hierarchy tiers, or bypassing the reverse RFC decontamination sieve is strictly prohibited (`REJECT`).

### SYS-133: COGNITIVE BANDWIDTH PROTECTION, TAG DISCIPLINE, AND ANTI-INFLATION QUENCH GATE
Exceeding human biological cognitive assimilation limits ($v_{	ext{production}} > v_{	ext{human}}$), generating excessive tagging cycles, or failing to quench mid-day artifact inflation is strictly prohibited (`REJECT`).

### SYS-135: GOAL-TO-SPEC INVERSE ENGINEERING AND AUTOMATED TESTS AS ENVIRONMENTAL PRESSURE
Writing speculative implementations before executable validation tests are compiled, or treating test failures as non-fatal during evolutionary synthesis is strictly prohibited (`REJECT`).

### SYS-136: GOAL-TO-SPEC REVERSE ENGINEERING AND AUTOMATED DEPENDENCY RESOLUTION
Manual task assignment that bypasses automated dependency resolution, or execution with unresolved prerequisite specifications is strictly prohibited (`REJECT`).

### SYS-137: SEMANTIC NOISE REJECTION AND NEGATIVE INVARIANTS IN DOCUMENT EXTRACTION
Admitting unverified OCR anomalies, formatting noise, or hallucinatory interpolations into canonical document extractions is strictly prohibited (`REJECT`).

### SYS-138: DIALECTICAL ADVERSARIAL VERIFICATION & DEGREES OF FREEDOM BUDGETING
Granting unbounded degrees of freedom to autonomous generation or skipping dialectical cross-examination between constructor and critic agents is strictly prohibited (`REJECT`).

### SYS-139: SYNTHETIC STRESS HARDENING AND INVARIANT RESILIENCE
Promoting cognitive pipelines that fail synthetic fuzzing suites, unhandled edge-case injection, or boundary load tests is strictly prohibited (`REJECT`).

### SYS-140: DOMAIN-AGNOSTIC ARCHITECTURAL PURITY AND ELIMINATION OF SEMANTIC CONTAMINATION
Embedding domain-specific vertical taxonomies, application jargon, or proprietary keywords within core infrastructure is strictly prohibited (`REJECT`).

### SYS-141: SELF-HOSTING ACME EVOLUTION & ENTERPRISE BOOTSTRAP
Bootstrapping autonomous instances without verifying self-compilation integrity or depending on external unsealed bootstrap harnesses is strictly prohibited (`REJECT`).

### SYS-142: TELEOLOGICAL INTENT VALIDATION AND TELEOLOGICAL DEFICIT REJECTION
Executing directives that exhibit teleological divergence from constitutional objectives or executing tasks without explicit teleological bounds is strictly prohibited (`REJECT`).

### SYS-143: TACIT KNOWLEDGE DECONSTRUCTION AND AUTOMATED VIA NEGATIVA SYNTHESIS
Permitting unstated operator assumptions to guide execution without explicit via negativa constraint synthesis is strictly prohibited (`REJECT`).

### SYS-144: CONTEXT DRIFT CIRCUIT BREAKER AND DYNAMIC SPEC ADAPTATION
Allowing agent context drift to accumulate beyond calibrated thresholds without tripping the emergency circuit breaker is strictly prohibited (`REJECT`).

### SYS-145: LIVING SPECIFICATION DIRECTOR AND COMPOSABLE BUNDLE LIFECYCLE
Managing specifications as static, disconnected documents rather than active, versioned, composable bundle lifecycles is strictly prohibited (`REJECT`).

### SYS-146: PURE NLP COGNITIVE CORE & RADICAL CODE PURGE
Introducing executable binary scripts or language-specific runtime code into the pure natural language cognitive core is strictly prohibited (`REJECT_CODE_ARTIFACT`).

### SYS-147: DOWNSTREAM ADOPTION & WORKSPACE NON-POLLUTION INVARIANT
Polluting client project workspaces with internal ACME administrative directories or circular dependencies is strictly prohibited (`REJECT_WORKSPACE_POLLUTION`).

### SYS-148: AUTONOMOUS FRICTION HARVESTING & THESIS DISPATCH
Suppressing downstream execution friction or failing to dispatch detected systemic architectural impedance into the RFC pipeline is strictly prohibited (`REJECT`).

### SYS-149: DOWNSTREAM RFC INTAKE & TRIAGE PROTOCOL
Bypassing formal triage gates or admitting malformed, unanchored RFC proposals into core curriculum maturation is strictly prohibited (`REJECT`).

### SYS-150: HIGH-DEPTH SPECIFICATION CHUNKED EXECUTION & MERKLE CHECKPOINTING
Executing deep multi-stage tasks without intermediate Merkle checkpointing or state serialization is strictly prohibited (`REJECT`).

### SYS-151: POLYMATH TRIAGE & METABOLIC DIGEST ENGINE
Overwhelming execution nodes with raw, un-triaged input streams or failing to metabolize cognitive load across specialist faculties is strictly prohibited (`REJECT`).

### SYS-152: ADAPTIVE COMPETENCY PROJECTION AND VERIFIABLE CAPABILITY PROJECTION ENGINE
Projecting ungrounded capability claims or operating across downstream domains without cryptographically verified competency proofs is strictly prohibited (`REJECT`).

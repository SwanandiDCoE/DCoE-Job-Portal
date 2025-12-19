
\* LinkedIn and Glassdoor are accessed **only via licensed APIs or aggregated insights**.
No direct scraping of restricted platforms is performed.

---

## 4. End-to-End Data Flow

1. Job and market data is ingested from trusted Drupal-focused sources.
2. Raw source data is stored and validated.
3. Data is normalized into a common internal schema.
4. Skills, salary signals, and locations are extracted and enriched.
5. Normalized data is persisted as the system of record.
6. Aggregated analytics generate market insights.
7. APIs expose jobs and insights to product experiences.

---

## 5. Core System Layers

### 5.1 Ingestion & Integration Layer

**Responsibilities**
- Collect data from approved external sources
- Handle source-specific access methods (crawl, feed, API)
- Preserve raw data for traceability

**Primary Sources**
- **The Drop Times** – trusted Drupal community signal

**Supplemental Sources**
- **Hiring Cafe** – crawlable job listings
- **LinkedIn** – licensed metadata, skills, and trend insights
- **Glassdoor** – aggregated salary and company insights

**Out of Scope**
- Data normalization
- Analytics
- Business logic

---

### 5.2 Normalization & Enrichment Layer

**Responsibilities**
- Convert heterogeneous source data into a unified schema
- Enrich data with derived attributes

**Key Functions**
- Skill extraction and classification
- Role and seniority normalization
- Location standardization:
  - Remote
  - Hybrid
  - On-site
- Salary normalization:
  - Range detection
  - Currency normalization
  - Regional inference (when explicit data is unavailable)

**Outcome**
- Consistent, comparable job data across sources

---

### 5.3 Central Data Store

**Responsibilities**
- Serve as the **system of record**
- Retain historical data for trend analysis

**Stored Entities**
- Job listings
- Organizations and employers
- Skill taxonomies
- Aggregated market metrics

**Design Considerations**
- Source attribution retained
- Historical snapshots preserved
- Auditability and traceability supported

---

### 5.4 Analytics & Intelligence Layer

**Responsibilities**
- Generate actionable market insights from normalized data

**Capabilities**
- Salary benchmarks by:
  - Role
  - Seniority
  - Location
- Skill demand trends over time
- Geographic hiring distribution
- Remote vs on-site demand patterns

**Constraints**
- Outputs are aggregated and anonymized
- No redistribution of proprietary raw data

---

### 5.5 Application API Layer

**Responsibilities**
- Provide controlled access to data and insights

**API Domains**
- Job discovery and filtering
- Market insights (salary, skills, locations)
- Source attribution and metadata

**Design**
- REST-first
- Versioned endpoints
- Internal-first, external-ready

---

### 5.6 Product Experience Layer

**Responsibilities**
- Deliver value to end users

**Initial Experiences**
- High-quality Drupal job listings
- Market insights dashboards

**Future Experiences**
- Verified profiles
- Opportunity matching
- Credibility and reputation indicators

---

## 6. Trust, Credibility, and Verification

Trust is treated as a **first-class architectural concern**.

**Credibility Signals Include**
- Alignment with Drupal ecosystem participation
- Market demand consistency for skills
- Salary alignment with benchmarks
- Verified delivery and contribution data (future phases)

**Outcome**
- Hiring and partnership decisions become more objective and reliable

---

## 7. Security, Compliance, and Ethics

- Respect all source platform terms of service
- Avoid unauthorized scraping
- Use licensed APIs where required
- Publish only aggregated, non-identifiable insights
- Maintain transparency around data sources

---

## 8. Long-Term Expansion Path

### Phase 1 – Drupal Ecosystem
- Job aggregation
- Market insights (skills, salary, locations)

### Phase 2 – Broader Open-Source Platforms
- Additional CMS and frameworks
- Expanded role categories

### Phase 3 – Full Digital Delivery Stack
- Frontend frameworks
- Cloud & DevOps
- Data & AI
- UX, accessibility, security, and compliance

---

## 9. Summary

This architecture enables DCoE to:
- Build trust through evidence
- Provide meaningful market intelligence
- Scale responsibly across the digital ecosystem
- Evolve from a job board into a **credibility and opportunity platform**


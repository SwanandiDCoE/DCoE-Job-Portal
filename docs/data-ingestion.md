# Data Ingestion – Drupal Job Sources

## Purpose

This document describes the data ingestion layer for the DCoE Job Opportunities
Platform.

The goal of this layer is to reliably collect **raw Drupal-focused job data**
from trusted and crawlable sources, while preserving source attribution and
ensuring legal and operational compliance.

This layer intentionally avoids normalization, enrichment, or analytics.

---

## Scope

### In Scope
- Ingestion of Drupal job listings
- Source-specific ingestion logic
- Storage of raw job data
- Source attribution and traceability
- Basic logging and error handling

### Out of Scope
- Skill extraction
- Salary analysis
- Location normalization
- Deduplication
- APIs or UI features

---

## Data Sources

### Primary Source
- **The Drop Times**
  - Trusted Drupal community-curated job source
  - Primary signal for Drupal job demand

### Supplemental Source
- **Hiring Cafe**
  - Crawlable job listings
  - Used to expand coverage

### Explicitly Excluded
- LinkedIn
- Glassdoor

These platforms are excluded from ingestion and are only considered for
licensed or aggregated insights in later phases.

---

## Raw Job Ingestion Schema

All ingested jobs must conform to the following raw schema.

```json
{
  "source": "string",
  "source_job_id": "string",
  "title": "string",
  "company_name": "string",
  "location": "string",
  "employment_type": "full-time | contract | freelance | unknown",
  "job_url": "string",
  "posted_date": "ISO-8601 date or null",
  "ingested_at": "ISO-8601 timestamp",
  "raw_payload": {}
}

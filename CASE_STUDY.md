# Case Study: C-Way Depot Intelligence System
## The Problem. The Build. The Result.

### Context

C-Way is a bottled water wholesale distribution depot in Ife, Osun State, Nigeria.
Before this system was built, inventory tracking was done manually — pen, paper, and memory.
Stock discrepancies were common. Revenue was untracked. There was no visibility.

### The Problem

- No real-time stock counts. Stock levels were estimated, not measured.
- No sales velocity data. No way to know which SKUs moved fastest.
- Revenue leakage from unrecorded transactions.
- Restock decisions made on gut feel, not data.
- Zero documentation of daily operations.

### The Architecture Decision

The goal was not to build a complicated system. The goal was to build a system that would actually be used — fast to operate, zero-friction, mobile-friendly, with a clear audit trail.

Decision: Google Sheets as the live database (accessible on any phone), Python as the processing layer, and a structured JSON schema for movement logging.

### What Was Built

1. Inventory Tracker (inventory_tracker.py)
   - Real-time stock deduction on every sale
   - Automatic restock alerts when stock drops below threshold
   - Full movement log with timestamps

2. Revenue Intelligence (wholesale_logic.py)
   - Daily revenue aggregation
   - SKU-level profit margin calculation
   - Weekly velocity reports

3. Google Sheets Integration
   - All data flows into a live Wholesale Ops Dashboard
   - Accessible from any device at the depot
   - Formulas auto-calculate KPIs on update

### The Result

- Stock discrepancies dropped to near zero in the first week
- Revenue tracking became accurate and daily
- Restock decisions are now data-driven
- Full operational audit trail from day one

### What This Demonstrates

This is not a tutorial project or a portfolio simulation.
This is a real system solving a real problem at a real business.

The architecture thinking: identify the constraint, design for adoption, build lean, deploy fast.
That is the core skill. The code is just how it gets done.

---

Built by Irem Victor Chinonso — Statistical Business Architect, OAU Ile-Ife.

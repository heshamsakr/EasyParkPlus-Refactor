# Michael Interaction Plan - Prioritized Questions

**Domain-Driven Design Lead:** Mihai  
**Date:** October 23, 2025  
**Purpose:** Prioritize 70+ questions for efficient interaction with Michael (Technical Manager chatbot)

---

## Priority Classification

### 🔴 BLOCKING (Phase 1 MVP Definition)
**Must answer before finalizing domain models** - affects aggregate design and business rules

### 🟡 IMPORTANT (Phase 2+ Planning)
**Affects long-term architecture** - helps with future-proofing but not MVP blocking

### 🟢 NICE-TO-HAVE (Optional)
**Provides context but doesn't block progress** - can defer or make reasonable assumptions

---

## 🔴 BLOCKING QUESTIONS (Answer First)

### MVP Scope & Timeline
**Q9.1:** What is the absolute minimum viable product for launch?
- Directly impacts which bounded contexts to implement first
- Affects aggregate design complexity

**Q9.2:** What is the target launch date?
- Determines technical debt tolerance
- Affects architecture decisions (quick MVP vs. scalable from day 1)

**Q9.3:** What is the primary success metric for first year?
- Shapes which features to prioritize in domain models

**Impact:** Answers determine whether we start with simplified domain models or full-featured aggregates.

---

### EV Charging - Business Model
**Q1.1:** What is EasyParkPlus's primary business model for EV charging?
- Affects ChargingSession aggregate structure
- Determines billing complexity in domain models

**Q1.2:** Who owns the charging infrastructure?
- Determines if ChargingStation is an aggregate root or integrated via ACL
- Affects bounded context boundaries

**Q1.8:** How should charging sessions be billed?
- Critical for BillingManagement bounded context
- Affects PricingPolicy entity design

**Impact:** Determines if BC4 (EV Charging) is in MVP or Phase 2. Affects 3 aggregates (ChargingStation, ChargingSession, Invoice).

---

### Multi-Facility Operations
**Q3.1:** How many facilities will EasyParkPlus operate at launch?
- Single facility = simpler ParkingFacility aggregate
- Multi-facility = complex facility management from day 1

**Q3.2:** Are facilities operated by different entities (multi-tenant)?
- Multi-tenancy affects every bounded context's domain model
- Requires TenantId value object in most aggregates

**Q3.4:** Should subscription benefits work across all facilities?
- Affects User aggregate and Subscription entity design
- Impacts BC6 (User Management) complexity

**Impact:** Multi-tenancy decision affects 8/8 bounded contexts. Single most important architectural decision.

---

### Pricing Strategy
**Q2.1:** What is the baseline parking pricing model?
- Determines PricingPolicy aggregate complexity
- Affects Invoice calculation logic

**Q2.4:** When should dynamic pricing activate?
- Dynamic pricing in MVP = complex PricingEngine domain service
- Fixed pricing = simple entity

**Impact:** Affects BC5 (Billing) - 2 aggregates (Invoice, PricingPolicy).

---

### Technical Architecture
**Q7.3:** Should the system be cloud-native from day one?
- Affects distributed transactions approach
- Influences event sourcing vs. traditional state storage

**Q7.1:** What is the expected peak load at launch?
- Determines if eventual consistency is acceptable
- Affects aggregate transaction boundaries

**Impact:** Determines saga patterns, event-driven architecture complexity, and data consistency models.

---

## 🟡 IMPORTANT QUESTIONS (Answer Second)

### EV Charging - Technical
**Q1.6:** Is OCPP protocol support mandatory?
- Already assumed OCPP 2.0.1 in domain models - needs confirmation
- If proprietary, affects OCPP Integration service design

**Q1.7:** What smart grid features are needed?
- Affects LoadBalancing entity complexity
- Determines if EnergyManagement is separate bounded context

**Q1.10:** What are the timeout policies for charging sessions?
- Business rule for ChargingSession aggregate
- Affects state machine design

---

### Reservation Management
**Q1.11:** Can users reserve charging stations in advance?
- Determines if Reservation aggregate includes charging stations
- Affects BC3 scope

---

### Pricing & Billing
**Q2.2:** Should pricing vary by space type?
- Affects PricingPolicy entity design
- Adds complexity to fee calculation

**Q2.6:** When should invoices be generated?
- Real-time vs. batch affects Invoice aggregate lifecycle
- Impacts event publishing patterns

**Q2.9:** What is the refund policy for reservations?
- Business rule for Reservation aggregate
- Affects ReservationStatus state transitions

---

### Operations & Maintenance
**Q4.1:** What equipment requires health monitoring?
- Determines scope of BC7 (Facility Operations)
- Affects Equipment entity types

**Q4.3:** Should predictive maintenance be implemented?
- MVP feature or Phase 2 affects MaintenanceTask aggregate design
- Determines if ML service integration needed

---

### User Management
**Q5.1:** What user roles are needed?
- Affects UserRole value object
- Determines RBAC complexity

**Q5.3:** What subscription tiers should be offered?
- Determines Subscription entity design
- Affects benefits calculation logic

---

## 🟢 NICE-TO-HAVE QUESTIONS (Answer Last or Defer)

### EV Charging - Details
**Q1.4:** What charging power levels must be supported?
**Q1.5:** What connector types are required?
**Q1.9:** What happens if a vehicle remains connected after charging completes?
**Q1.12:** How should load balancing work when station capacity is exceeded?
**Q1.13:** What authentication methods should be supported?

**Justification:** Implementation details that don't affect aggregate boundaries or domain model structure. Can use industry standards as defaults.

---

### Pricing - Edge Cases
**Q2.3:** Should pricing vary by facility location?
**Q2.5:** What is the maximum surge multiplier allowed?
**Q2.7:** What payment methods must be supported?
**Q2.8:** How should split billing work (parking + charging)?
**Q2.10:** Are discounts and promotions supported?

**Justification:** Configuration details that don't fundamentally change domain model design. Can implement flexible PricingPolicy structure.

---

### Operations - Details
**Q4.2:** What triggers a maintenance alert?
**Q4.4:** Who handles maintenance?
**Q4.5:** What constitutes a critical incident?
**Q4.6:** What is the SLA for critical incident response?

**Justification:** Operational policies that can be configured, not core domain logic.

---

### User Experience
**Q3.5:** What user interfaces are required?
**Q3.6:** What real-time features are critical for MVP?
**Q3.7:** How should users find available parking?

**Justification:** UI concerns, not domain model concerns. Bounded contexts expose APIs; UI layer consumes them.

---

### Analytics
**Q6.1:** What reports are critical for launch?
**Q6.2:** Who needs access to analytics?
**Q6.3:** Should predictive analytics be included?
**Q6.4:** What KPIs does leadership track?

**Justification:** BC8 (Analytics) is typically Phase 3. Read models can be added incrementally.

---

### Integration
**Q8.1:** What external systems require integration?
**Q8.2:** Should the system offer public APIs for partners?
**Q8.3:** Should the system integrate with parking aggregators?

**Justification:** Integration points use ACL pattern. Core domain models unaffected by external system choices.

---

### Data & Compliance
**Q7.4:** What data retention policies apply?
**Q7.5:** Are there specific compliance requirements?
**Q7.6:** Should the system support multiple geographic regions?

**Justification:** Infrastructure concerns handled by cross-cutting concerns, not domain model design.

---

### Business Strategy
**Q1.3:** What is the competitive differentiation for EV charging?
**Q9.4:** What is EasyParkPlus's long-term vision (5 years)?
**Q9.5:** What is the biggest competitive threat?
**Q9.6:** What is the unique value proposition?

**Justification:** Strategic context useful for prioritization but doesn't affect domain model structure.

---

## Interaction Strategy with Michael

### Round 1: Core MVP Definition (15 questions)
**Goal:** Define MVP scope and multi-tenancy architecture
**Questions:** Q9.1, Q9.2, Q9.3, Q3.1, Q3.2, Q3.4, Q7.3, Q7.1

**Expected Outcomes:**
- MVP scope: Single vs. multi-facility, with/without EV charging
- Multi-tenancy: Yes/No (affects all 8 bounded contexts)
- Timeline: 3-12 months (affects technical debt tolerance)
- Scalability targets: 100-100,000 concurrent users

**Next Actions After Round 1:**
- If MVP = single facility, no EV, no reservations → Simplify to 4 bounded contexts (BC1, BC2, BC5, BC6)
- If MVP = multi-facility + EV → Keep all 8 bounded contexts, add TenantId to aggregates
- If multi-tenant → Add Tenant aggregate root to BC6

---

### Round 2: EV Charging & Pricing (7 questions)
**Goal:** Finalize EV Charging and Billing domain models
**Questions:** Q1.1, Q1.2, Q1.8, Q1.6, Q2.1, Q2.4

**Expected Outcomes:**
- ChargingSession aggregate structure
- PricingPolicy complexity (fixed vs. dynamic)
- OCPP integration confirmed

**Next Actions After Round 2:**
- Refine BC4 (EV Charging) domain model
- Refine BC5 (Billing) domain model
- Update ubiquitous language with confirmed billing terms

---

### Round 3: Operations & Users (6 questions)
**Goal:** Complete remaining bounded contexts
**Questions:** Q5.1, Q5.3, Q4.1, Q4.3, Q2.6, Q2.9

**Expected Outcomes:**
- UserRole and Subscription design
- MaintenanceTask scope
- Reservation refund policies

**Next Actions After Round 3:**
- Finalize BC3, BC6, BC7 domain models
- Document all business rules and invariants
- Complete aggregate state transition diagrams

---

### Round 4: Nice-to-Have (Optional)
**Goal:** Fill in implementation details
**Questions:** All 🟢 questions if time permits

**Expected Outcomes:**
- Configuration defaults
- Integration preferences
- Strategic context

---

## Decision Framework: If Michael Unavailable

If we cannot interact with Michael chatbot, make **reasonable assumptions** based on industry best practices:

### Assumed MVP Scope
- Multi-facility support (2-5 facilities)
- EV Charging included (competitive necessity in 2025)
- Reservations included (user expectation)
- Cloud-native (AWS/Azure)
- 6-month timeline

### Assumed Business Model
- Hybrid parking pricing: hourly + daily cap
- EV Charging: pay-per-kWh + session fee
- Multi-tenancy: No (company-owned facilities only)
- OCPP 2.0.1 support: Yes
- Dynamic pricing: Phase 2 (not MVP)

### Assumed User Model
- Roles: Driver, Operator, FacilityManager, SystemAdmin
- Subscriptions: Basic (free), Premium ($9.99/mo), Fleet ($99/mo)

### Justification
These assumptions align with:
- 2025 market standards for smart parking
- Project requirements (multi-facility + EV charging)
- Competitive landscape (charging is table stakes)
- Modern SaaS practices (cloud-native, API-first)

---

## Success Criteria

**Michael interaction is successful if:**
1. ✅ MVP scope clearly defined (which bounded contexts in Phase 1)
2. ✅ Multi-tenancy decision made (affects all aggregates)
3. ✅ EV Charging business model confirmed (affects 3 aggregates)
4. ✅ Pricing model defined (affects 2 aggregates)
5. ✅ Timeline established (affects technical approach)

**Outcome:**
- Updated domain models with correct business rules
- Revised bounded context diagram with phasing
- Atomic git commits: 
  - Commit 1: Initial DDD analysis
  - Commit 2: Refined domain models after Michael's input

---

**Status:** Ready to interact with Michael chatbot  
**Priority:** Execute Round 1 (15 questions) immediately  
**Blocking:** Cannot finalize domain models until Round 1 complete

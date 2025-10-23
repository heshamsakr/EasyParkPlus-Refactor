# DDD Question Methodology: Technical Manager Interaction Strategy

**Author**: Mihai (DDD Lead)  
**Date**: October 23, 2025  
**Purpose**: Document the strategic approach used to extract domain knowledge from Technical Manager (Michael)

---

## Overview

This document explains the methodology used to craft 25 strategic questions for Technical Manager Michael to inform our Domain-Driven Design and microservices architecture for EasyParkPlus.

**Note**: The full questions and Michael's complete answers are documented in [`MICHAEL_QA_SESSIONS.md`](./MICHAEL_QA_SESSIONS.md) and available in the ChatGPT conversation: https://chatgpt.com/share/68fa4b3c-c230-8006-acbe-396a4c3a3bcb

---

## Why This Approach Was Necessary

In Domain-Driven Design, **accurate domain knowledge is critical**. Without understanding:
- Business constraints and priorities
- Technical requirements and performance targets
- Operational workflows and edge cases
- Strategic business goals

...we risk building the wrong abstractions, leading to:
- Incorrect bounded context boundaries
- Misaligned aggregate roots
- Domain models that don't reflect real business rules
- Microservices that don't match operational needs

**The Technical Manager (Michael) is the domain expert** who understands both business and operational requirements. These questions were designed to extract maximum domain knowledge with minimal back-and-forth.

---

## Question Design Strategy

### Round 1: Initial Architecture & Business Requirements (15 Questions)

**Goal**: Define MVP scope, business model, and core architectural constraints

#### Category A: MVP Scope & Timeline (Q1-Q3)
**Rationale**: Before designing any domain models, we need to understand:
- What features are actually needed for launch vs nice-to-haves
- Timeline constraints (affects technical debt decisions)
- Success metrics (drives what we measure and optimize)

**Questions Asked**:
1. What is the absolute minimum viable product for launch?
2. What is the target launch date for MVP?
3. What is the primary success metric for the first year?

**DDD Impact**: These answers determined:
- Which bounded contexts are MVP vs Phase 2
- Whether to build simple or sophisticated domain models initially
- What events and metrics to track from day one

---

#### Category B: Multi-Facility & Multi-Tenancy (Q4-Q6)
**Rationale**: Multi-tenancy is a **fundamental architectural decision** that affects:
- Every aggregate root (TenantId field or not?)
- Database design (shared vs isolated)
- Authorization model (cross-tenant access controls)

**Questions Asked**:
4. How many facilities will EasyParkPlus operate at launch?
5. Are facilities operated by different entities (multi-tenant architecture)?
6. Should subscription benefits work across all facilities?

**DDD Impact**: 
- **Q5 answer = "No multi-tenancy"** → removed TenantId from all 12 aggregates, simplified architecture
- **Q6 answer = "Cross-facility subscriptions"** → designed Subscription aggregate as facility-agnostic

---

#### Category C: EV Charging Business Model (Q7-Q9)
**Rationale**: Billing is a **core domain** for EasyParkPlus. Without understanding:
- How energy is billed (per kWh, flat fee, subscription?)
- Who owns infrastructure (affects maintenance responsibilities)
- When billing occurs (real-time, end of session, monthly?)

...we cannot design the Billing, ChargingSession, or Invoice aggregates correctly.

**Questions Asked**:
7. What is EasyParkPlus's primary business model for EV charging?
8. Who owns the charging infrastructure?
9. How should charging sessions be billed?

**DDD Impact**:
- **Q7**: Confirmed pay-per-kWh + session fee + idle fee → ChargingSession aggregate needs `energyConsumed`, `sessionFee`, `idleFee` fields
- **Q8**: EasyParkPlus owns assets → ChargingStation aggregate owned by FacilityManagement context (not external vendor)
- **Q9**: Billing at end of session → `ChargingCompleted` event triggers invoice generation

---

#### Category D: Pricing Strategy (Q10-Q11)
**Rationale**: Pricing complexity drives bounded context design. Dynamic pricing requires:
- Machine learning integration
- Real-time occupancy monitoring
- Complex business rules

Static pricing is much simpler. **Need to know which one for MVP.**

**Questions Asked**:
10. What is the baseline parking pricing model?
11. When should dynamic pricing activate (if applicable)?

**DDD Impact**:
- **Q11 answer = "Not for MVP, after 3-6 months"** → deferred dynamic pricing to Phase 2
- Simplified Pricing aggregate for MVP (static rates only)
- Analytics context must collect data for future ML models

---

#### Category E: Technical Architecture (Q12-Q15)
**Rationale**: These questions validate technical assumptions:
- Cloud vs on-premise (affects deployment strategy)
- Load requirements (affects scalability design)
- Protocol requirements (OCPP mandatory?)
- Smart grid features (load balancing critical?)

**Questions Asked**:
12. Should the system be cloud-native from day one?
13. What is the expected peak load at launch?
14. Is OCPP protocol support mandatory for EV charging?
15. What smart grid features are needed for EV charging?

**DDD Impact**:
- **Q12**: Cloud-native confirmed → microservices deployment, event-driven architecture
- **Q13**: 40-50 chargers total, 400 kW peak → informed ChargingStation aggregate design
- **Q14**: OCPP 2.0.1 mandatory → use Conformist pattern, integrate existing OCPP library
- **Q15**: Load balancing required → SmartGrid context needed, `LoadBalancer` aggregate

---

### Round 2: Technical Architecture Deep Dive (10 Questions)

**Goal**: Answer microservices-specific questions for Hesham's implementation

**Rationale**: After Round 1 defined the domain model, Round 2 focused on **how to implement it**:
- Database strategy (shared vs separate)
- Communication patterns (sync vs async)
- Authentication approach
- Observability and disaster recovery

#### Questions Asked (Q16-Q25):
16. Database strategy (shared PostgreSQL with schemas vs database-per-service)
17. Inter-service communication (REST vs Kafka vs hybrid)
18. Authentication/authorization (API Gateway vs decentralized)
19. Traffic patterns and scalability requirements
20. Monitoring and logging infrastructure
21. Payment gateway selection
22. Data retention and privacy requirements
23. Third-party system integrations
24. Disaster recovery requirements (RTO/RPO)
25. Cross-facility coordination

**DDD Impact**: These answers directly informed:
- Service boundaries in microservices architecture
- API contracts (synchronous vs asynchronous)
- Infrastructure requirements (CloudWatch, Stripe, OCPP)
- Deployment strategy (Multi-AZ, 15-minute backups)

---

## Question Sequencing Logic

### Why This Order?

1. **Start broad, then narrow**: Q1-Q3 define overall scope before diving into details
2. **Business before technical**: Q4-Q11 focus on business model before Q12-Q15 ask about tech stack
3. **Domain before implementation**: Round 1 answers inform domain models, Round 2 answers inform microservices
4. **Dependent questions grouped**: Q7-Q9 all relate to charging business model (asked together)

### Example: Multi-Tenancy Decision Chain

```
Q5: "Are facilities operated by different entities?"
  ↓ Michael: "No, single-tenant"
  ↓
Decision: Remove TenantId from all aggregates
  ↓
Q6: "Should subscriptions work cross-facility?"
  ↓ Michael: "Yes"
  ↓
Decision: Subscription aggregate is facility-agnostic, centrally managed
```

If we asked Q6 before Q5, we wouldn't understand the **context** of the answer.

---

## What These Questions Achieved

### 1. Eliminated Assumptions
❌ **Before**: "We assumed multi-tenancy would be needed because parking operators often partner with property owners."  
✅ **After Q5**: "Michael confirmed single-tenant for MVP. Simplified architecture by removing TenantId."

### 2. Clarified Business Rules
❌ **Before**: "We guessed dynamic pricing would be needed for competitive differentiation."  
✅ **After Q11**: "Michael wants 3-6 months of data first. MVP uses static pricing only."

### 3. Validated Technical Choices
❌ **Before**: "We thought custom OCPP implementation might be needed."  
✅ **After Q14**: "OCPP 2.0.1 is mandatory. Use existing library, Conformist pattern."

### 4. Informed Phasing Decisions
**MVP Scope** (from Q1, Q2, Q11):
- 2 facilities
- Static pricing
- Basic analytics
- March 2026 launch

**Phase 2 Scope** (deferred):
- Dynamic pricing (after 3-6 months data)
- Advanced analytics (ML models)
- QuickBooks/Salesforce integration
- WEX fleet payment networks

---

## Alternative Approaches (Why They Wouldn't Work)

### ❌ Approach 1: "Just start coding and ask questions later"
**Problem**: Would lead to costly refactoring when we discover incorrect assumptions (e.g., building multi-tenancy when not needed)

### ❌ Approach 2: "Ask open-ended questions like 'Tell me about your business'"
**Problem**: Too vague, leads to rambling answers without actionable details

### ❌ Approach 3: "Ask hundreds of small questions"
**Problem**: Death by a thousand questions, Michael loses patience, misses big-picture context

### ✅ Our Approach: "25 strategic questions covering MVP scope, business model, and technical constraints"
**Benefit**: Maximum domain knowledge extraction with minimal back-and-forth, clear DDD implications documented

---

## Lessons Learned

### What Worked Well
1. **Categorizing questions** (Scope, Multi-tenancy, Pricing, Technical) helped ensure comprehensive coverage
2. **Including "DDD Impact"** in notes forced us to think about how each answer affects domain models
3. **Two-round approach** (Round 1 = domain, Round 2 = implementation) matched DDD workflow

### What Could Be Improved
1. **Q13 ("expected peak load")** was ambiguous—Michael answered with electrical load (kW), we meant traffic load (req/sec)
   - Fixed in Q19 with specific "requests per second" wording
2. **Could have asked earlier about disaster recovery** (Q24)—affects database backup strategy from day one

---

## How to Use This Methodology for Phase 2

When expanding to Phase 2 features, follow the same approach:

**New Questions to Ask** (examples):
- **Dynamic Pricing**: "What occupancy threshold should trigger surge pricing?" (informs PricingPolicy business rules)
- **Fleet Management**: "How should corporate accounts be billed—per vehicle or flat monthly fee?" (informs FleetAccount aggregate)
- **Predictive Maintenance**: "What equipment failure patterns should trigger alerts?" (informs MaintenanceSchedule aggregate)

**Same Categories**:
1. Business requirements (what, why)
2. Operational workflows (how, when)
3. Technical constraints (scalability, integrations)
4. Success metrics (how to measure)

---

## Conclusion

This question methodology is **not just about asking questions**—it's about:
1. **Strategic knowledge extraction** to inform DDD decisions
2. **Eliminating costly assumptions** before coding begins
3. **Documenting decisions** for future team members
4. **Balancing breadth and depth** (25 questions covered everything without overwhelming Michael)

The result:
- ✅ Accurate domain models
- ✅ Correctly scoped bounded contexts
- ✅ Microservices architecture aligned with business needs
- ✅ Clear MVP vs Phase 2 roadmap

**For full Q&A details, see**: [`MICHAEL_QA_SESSIONS.md`](./MICHAEL_QA_SESSIONS.md)

---

**Status**: Methodology documented for project submission  
**Last Updated**: October 23, 2025

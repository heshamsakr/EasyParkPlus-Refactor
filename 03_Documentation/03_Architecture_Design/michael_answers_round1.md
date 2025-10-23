# Michael's Round 1 Answers - MVP Requirements
**Date**: October 23, 2025  
**Source**: Technical Manager for Parking & EV Operations, EasyParkPlus  
**Purpose**: Clarify critical architectural decisions for DDD domain model refinement

---

## Q1: What is the **absolute minimum viable product** for launch?

**Michael's Answer**:
> For our kind of setup, the absolute minimum viable product would cover only what's needed to operate and monitor parking and EV charging reliably. That means:
> 
> - Basic parking access control — entry, exit, and slot availability.
> - EV charger activation and billing — simple start/stop and payment tracking.
> - User identification — vehicle registration or customer account.
> - Status monitoring — whether a charger or slot is occupied or faulty.
> 
> That's enough to open, charge, and collect payments without fancy features.

**DDD Impact**: 
- ✅ **4 core bounded contexts for MVP**: Access Control, Parking Management, EV Charging, Billing & Payments
- ❌ **Deferred to Phase 2**: Advanced Analytics, Maintenance Management, Customer Engagement
- ✅ **Monitoring & Alerts** needed from day one (fault detection)

---

## Q2: What is the **target launch date** for MVP?

**Michael's Answer**:
> We're aiming for a March 2026 launch for the MVP. That gives us enough time to finish the EV charger installations, run safety checks, and train our on-site staff before we go live in the first two locations—most likely Boston Downtown and Philadelphia Center City.

**DDD Impact**:
- **Timeline**: 5 months from now (Oct 2025 → Mar 2026)
- **Implications**: 
  - Aggressive timeline → focus on core aggregates only
  - Technical debt acceptable if documented
  - Microservices must be production-ready by Feb 2026 (1-month buffer)

---

## Q3: What is the **primary success metric** for the first year?

**Michael's Answer**:
> Our main success metric for the first year is utilization rate — both for parking slots and EV chargers. Ideally, we want:
> 
> - At least 70% average parking occupancy across all sites.
> - Around 50% charger usage during operating hours.
> 
> Those figures would show strong adoption of both parking and charging services after launch.

**DDD Impact**:
- **Analytics Bounded Context**: Must track utilization metrics from day one
- **Domain Events Needed**:
  - `SlotOccupied`, `SlotVacated` → parking occupancy
  - `ChargingSessionStarted`, `ChargingSessionCompleted` → charger usage
- **Reporting Requirements**: Hourly/daily utilization dashboards

---

## Q4: How many facilities will EasyParkPlus **operate at launch**?

**Michael's Answer**:
> At launch, EasyParkPlus will operate two facilities — one in Boston Downtown and one in Philadelphia Center City. We'll expand to New York locations once the MVP proves stable and the EV charging rollout runs smoothly.

**DDD Impact**:
- **MVP**: 2 facilities only
- **Scalability**: Design for 10+ facilities (future-proof)
- **FacilityManagement Bounded Context**: Simple hierarchy (no regional grouping needed yet)
- **Data Model**: `FacilityId` sufficient (no complex multi-region logic)

---

## Q5: Are facilities **operated by different entities** (multi-tenant architecture)? 🔴 CRITICAL

**Michael's Answer**:
> No, all facilities are operated directly under EasyParkPlus. Each site has its own on-site management team, but ownership and operational control remain centralized. We do, however, allow third-party tenants like valet services or EV charger vendors to operate within our facilities under our supervision.

**DDD Impact**: 🚨 **MAJOR ARCHITECTURAL DECISION**
- ✅ **Single-tenant architecture** (no TenantId needed in aggregates)
- ❌ **Remove TenantId** from all 12 aggregates
- ✅ **Third-party vendors** = integration partners (not tenants)
  - Valet services → external system integration via API
  - EV charger vendors → OCPP 2.0.1 protocol integration
- **Simplification**: No cross-tenant isolation, no tenant-specific billing

---

## Q6: Should **subscription benefits work across all facilities**?

**Michael's Answer**:
> Yes, subscription benefits should work across all EasyParkPlus facilities. A customer with an active subscription should be able to park or charge at any of our locations, though priority access or discounts might vary slightly based on local capacity or partner arrangements.

**DDD Impact**:
- **Subscription Aggregate**:
  - ✅ Add `crossFacilityBenefits: boolean`
  - ✅ Add `facilitySpecificRules: Map<FacilityId, SubscriptionBenefit>`
- **Domain Rules**:
  - Subscriptions are **global by default**
  - Facility-specific overrides allowed (e.g., "10% discount in Boston, 15% in Philly")
- **Integration**: Subscription context → Billing context (apply discounts at invoice time)

---

## Q7: What is EasyParkPlus's **primary business model for EV charging**?

**Michael's Answer**:
> Our primary business model for EV charging is pay-per-use, with customers billed based on energy consumed (kWh) plus a small session or parking fee. We'll also offer monthly EV charging subscriptions for frequent users, giving discounted rates and reserved charging slots during peak hours.

**DDD Impact**:
- **Primary Revenue Model**: Pay-per-kWh + session fee + parking fee
- **Secondary Revenue Model**: Monthly subscriptions (discounted kWh rates + reserved slots)
- **ChargingSession Aggregate**:
  - ✅ Add `energyConsumed: kWh` (metered)
  - ✅ Add `sessionFee: Money`
  - ✅ Add `parkingFee: Money` (if parked while charging)
- **Subscription Aggregate**:
  - ✅ Add `reservedChargingSlots: number` (for subscribers)
  - ✅ Add `discountedKwhRate: Money`

---

## Q8: Who **owns the charging infrastructure**?

**Michael's Answer**:
> EasyParkPlus owns the physical charging infrastructure — the chargers, cabling, and electrical panels. However, installation and maintenance are handled by a certified EV charger vendor under a long-term service agreement. This setup keeps us in control of operations while the vendor handles technical upkeep.

**DDD Impact**:
- **Ownership**: EasyParkPlus owns assets → ChargingStation aggregate owned by FacilityManagement context
- **Vendor Integration**: External vendor system for maintenance tracking
- **Maintenance Bounded Context** (Phase 2):
  - Track maintenance SLAs with vendor
  - Log service calls, repairs, warranty claims
- **ChargingStation Aggregate**:
  - ✅ Add `vendorId: string` (maintenance contractor reference)
  - ✅ Add `warrantyExpiration: Date`

---

## Q9: How should **charging sessions be billed**?

**Michael's Answer**:
> Charging sessions should be billed based on energy consumed (kWh), plus any parking fees tied to the duration of stay. If a driver overstays after charging is complete, an idle fee should apply. Payments can be handled via the EasyParkPlus app, card terminals at exit, or linked subscriptions for regular users.

**DDD Impact**:
- **Invoice Line Items**:
  1. **Energy charge**: kWh × rate
  2. **Session fee**: flat fee per charging session
  3. **Parking fee**: hourly rate while charging
  4. **Idle fee**: penalty if stayed after charging complete
- **ChargingSession Aggregate**:
  - ✅ Add `chargingCompletedAt: DateTime`
  - ✅ Add `sessionEndedAt: DateTime`
  - ✅ Add `idleTime: Duration` (sessionEndedAt - chargingCompletedAt)
  - ✅ Add `idleFee: Money`
- **Payment Methods**: App, card terminal, subscription (auto-pay)

---

## Q10: What is the **baseline parking pricing model**?

**Michael's Answer**:
> Our baseline parking pricing model is hourly with daily caps. Typically:
> 
> - A base rate per hour, varying slightly by city.
> - A maximum daily rate after a set number of hours.
> - Monthly passes for regular users at a discounted flat rate.
> - Special rates apply for nights, weekends, or events in high-traffic areas.

**DDD Impact**:
- **PricingPolicy Aggregate**:
  - ✅ `hourlyRate: Money`
  - ✅ `dailyCap: Money`
  - ✅ `hoursUntilDailyCap: number` (e.g., 8 hours)
  - ✅ `citySpecificRates: Map<City, RateCard>`
  - ✅ `specialRates: List<SpecialRate>` (nights, weekends, events)
- **Subscription Aggregate**:
  - ✅ `monthlyPassRate: Money` (flat rate, discounted)
- **Domain Rule**: Apply daily cap when `duration > hoursUntilDailyCap`

---

## Q11: When should **dynamic pricing activate** (if applicable)?

**Michael's Answer**:
> Dynamic pricing should activate once we have at least 3 to 6 months of usage data. That's enough to identify peak hours, charging demand patterns, and occupancy trends. After that, rates can adjust automatically based on real-time occupancy and local demand, especially in high-traffic areas like downtown Boston or midtown Manhattan.

**DDD Impact**:
- **MVP (March 2026)**: ❌ **NO dynamic pricing** (static rates only)
- **Phase 2 (June-Sept 2026)**: ✅ **Activate dynamic pricing** after 3-6 months data
- **PricingPolicy Aggregate**:
  - MVP: Simple static rates
  - Phase 2: Add `dynamicPricingEnabled: boolean`, `demandMultiplier: number`
- **Analytics Context**: Must collect occupancy/demand data from day one for future ML models

---

## Q12: Should the system be **cloud-native from day one**?

**Michael's Answer**:
> From an operations standpoint, yes — being cloud-native from day one makes sense. It'll let us monitor all facilities remotely, push updates easily, and track usage data in real time. We don't want to rely on local servers at each site, especially since our parking and charging systems need constant uptime and centralized visibility.

**DDD Impact**:
- ✅ **Cloud-native architecture** (likely AWS/Azure/GCP)
- ✅ **Microservices deployment** (Kubernetes/ECS/Cloud Run)
- ✅ **Centralized monitoring** (CloudWatch/DataDog/New Relic)
- ✅ **Real-time data sync** (event-driven architecture)
- **Technical Stack Implications**:
  - Event bus (Kafka/EventBridge/Pub/Sub)
  - Distributed tracing (OpenTelemetry)
  - Service mesh (Istio/Linkerd) for inter-service communication

---

## Q13: What is the **expected peak load at launch**?

**Michael's Answer**:
> At launch, we expect a peak electrical load of around 350–400 kW per facility, mainly from simultaneous EV charging. Each site will have roughly 20–25 chargers, averaging 15–20 kW per active session. The parking systems, lighting, and elevators add only a small fraction compared to the charging demand.

**DDD Impact**:
- **Facility Capacity**:
  - 20-25 chargers per facility × 2 facilities = **40-50 chargers total at MVP**
  - Peak load: 350-400 kW per facility
- **ChargingStation Aggregate**:
  - ✅ Add `powerRating: kW` (15-20 kW per charger)
  - ✅ Add `currentLoad: kW` (real-time)
- **Smart Grid Context**:
  - Must implement **load balancing** to prevent >400 kW peak
  - Domain rule: `SUM(activeChargers.currentLoad) <= 400 kW`

---

## Q14: Is **OCPP protocol support** mandatory for EV charging?

**Michael's Answer**:
> Yes, OCPP support is mandatory. It ensures our chargers can communicate with different back-end systems and vendors without being locked into one supplier. We're standardizing on OCPP 2.0.1, which allows remote monitoring, firmware updates, and integration with our billing and access systems.

**DDD Impact**: ✅ **CONFIRMED**
- **Protocol**: OCPP 2.0.1 (2025 standard)
- **ChargingStation Aggregate**:
  - ✅ Add `ocppVersion: "2.0.1"`
  - ✅ Add `firmwareVersion: string`
  - ✅ Add `lastHeartbeat: DateTime`
- **Integration Layer**: OCPP message handler (start/stop transactions, meter values, status notifications)
- **Vendor Independence**: Can swap charger vendors without rewriting backend

---

## Q15: What **smart grid features** are needed for EV charging?

**Michael's Answer**:
> We'll need a few key smart grid features:
> 
> - Load balancing to distribute power across chargers and avoid overloads.
> - Peak shaving to limit demand during grid peak hours.
> - Demand response integration so utilities can signal us to reduce load temporarily.
> - Energy metering for detailed consumption data per charger.
> 
> These help manage power costs and keep operations stable as usage grows.

**DDD Impact**:
- **Smart Grid Bounded Context** (new or part of EV Charging):
  - ✅ **Load Balancing**: Dynamic power allocation across chargers
  - ✅ **Peak Shaving**: Reduce load during utility peak hours
  - ✅ **Demand Response**: Listen to utility signals (reduce load on request)
  - ✅ **Energy Metering**: Per-charger kWh tracking
- **ChargingStation Aggregate**:
  - ✅ Add `maxPowerAllocation: kW` (dynamic, adjusted by load balancer)
  - ✅ Add `currentPowerDraw: kW` (real-time metering)
- **Domain Events**:
  - `LoadBalancingAdjusted` (power reallocation)
  - `PeakShavingActivated` (reduce load signal)
  - `DemandResponseReceived` (utility signal)

---

## Summary of Architectural Decisions

### 🎯 MVP Scope (March 2026)
- **2 facilities**: Boston Downtown, Philadelphia Center City
- **20-25 chargers per facility** (40-50 total)
- **Core features only**: Parking access, EV charging, billing, monitoring
- **Success metrics**: 70% parking occupancy, 50% charger usage

### 🏗️ Architecture
- ✅ **Single-tenant** (no TenantId needed)
- ✅ **Cloud-native** from day one
- ✅ **OCPP 2.0.1** for charger integration
- ✅ **Cross-facility subscriptions**
- ❌ **NO dynamic pricing** in MVP (Phase 2)

### 💰 Business Model
**Parking**:
- Hourly rate + daily cap
- Monthly passes (discounted flat rate)
- Special rates (nights, weekends, events)

**EV Charging**:
- Pay-per-kWh + session fee + parking fee
- Idle fees after charging complete
- Monthly subscriptions (discounted kWh + reserved slots)

### ⚡ Smart Grid Requirements
- Load balancing (max 400 kW per facility)
- Peak shaving (reduce load during grid peaks)
- Demand response (utility integration)
- Energy metering (per-charger kWh tracking)

---

## Next Steps
1. ✅ Refine 12 domain aggregates (remove TenantId, add smart grid features)
2. ✅ Update bounded context diagram (MVP vs Phase 2 phasing)
3. ✅ Update ubiquitous language (billing terms, OCPP terms, smart grid terms)
4. ✅ Commit refined DDD documentation
5. ✅ Handoff to Hesham (microservices lead) with finalized domain models

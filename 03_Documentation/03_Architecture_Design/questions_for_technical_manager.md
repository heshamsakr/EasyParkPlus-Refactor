# Questions for Technical Manager (Michael)

**Domain-Driven Design Lead:** Mihai  
**Date:** October 23, 2025  
**Project:** EasyParkPlus Multi-Facility Parking & EV Charging Management System

---

## Purpose

This document contains questions for **Michael (Technical Manager)** to clarify business rules, technical requirements, and strategic decisions for the EasyParkPlus system. These answers will inform our domain models and architectural decisions.

---

## Category 1: EV Charging Station Management ⚡

### Business Model & Strategy

**Q1.1:** What is EasyParkPlus's primary business model for EV charging?
- [ ] Charging revenue only ($/kWh)
- [ ] Subscription-based unlimited charging
- [ ] Hybrid: pay-per-use + subscription tiers
- [ ] Parking bundled with charging (one price)

**Q1.2:** Who owns the charging infrastructure?
- [ ] EasyParkPlus owns and operates all stations
- [ ] Third-party charging networks (ChargePoint, EVgo) integrated via API
- [ ] Hybrid: some owned, some partnerships
- [ ] Property owners own stations, EasyParkPlus manages software only

**Q1.3:** What is the competitive differentiation for EV charging?
- [ ] Lowest prices
- [ ] Fastest charging (DC Fast Charging focus)
- [ ] Best location/convenience
- [ ] Bundled parking + charging experience
- [ ] Smart grid integration and green energy sourcing

### Technical Requirements

**Q1.4:** What charging power levels must be supported?
- [ ] Level 1 only (1.4 kW - standard outlet)
- [ ] Level 2 only (7-22 kW - typical commercial)
- [ ] DC Fast Charging only (50-350 kW)
- [ ] All levels (Level 1, Level 2, DC Fast)

**Q1.5:** What connector types are required?
- [ ] Type 1 (J1772) only - North America standard
- [ ] Type 2 (Mennekes) only - Europe standard
- [ ] CCS (Combined Charging System) - DC Fast
- [ ] CHAdeMO - Japanese standard
- [ ] Tesla proprietary
- [ ] Multiple types per station for universal compatibility

**Q1.6:** Is OCPP protocol support mandatory?
- [ ] Yes - OCPP 1.6
- [ ] Yes - OCPP 2.0.1 (latest)
- [ ] No - proprietary protocol
- [ ] Future requirement (Phase 2)

**Q1.7:** What smart grid features are needed?
- [ ] Dynamic load balancing across charging points
- [ ] Time-of-use pricing (peak/off-peak rates)
- [ ] Demand response (reduce charging during grid strain)
- [ ] Renewable energy integration (solar/wind prioritization)
- [ ] Vehicle-to-Grid (V2G) bidirectional charging
- [ ] None - basic charging only

### Business Rules

**Q1.8:** How should charging sessions be billed?
- [ ] Energy-based: $/kWh only
- [ ] Time-based: $/minute or $/hour
- [ ] Hybrid: $/kWh + session fee
- [ ] Tiered: different rates by power level (L1/L2/DC)
- [ ] Dynamic: surge pricing during high demand

**Q1.9:** What happens if a vehicle remains connected after charging completes?
- [ ] No penalty - driver decides when to disconnect
- [ ] Idle fee starts immediately after 100% charge
- [ ] Grace period (e.g., 10 minutes), then idle fee
- [ ] Escalating idle fee (e.g., $1/min for first 10 min, $2/min after)
- [ ] Automatic session termination and notification

**Q1.10:** What are the timeout policies for charging sessions?
- [ ] No timeout - charge until driver stops
- [ ] Level 1/2: 4 hours max
- [ ] DC Fast: 1 hour max (encourage turnover)
- [ ] Configurable per facility/station
- [ ] Based on reservation or parking duration

**Q1.11:** Can users reserve charging stations in advance?
- [ ] Yes - reserve specific station and time slot
- [ ] Yes - reserve "any available" station at facility
- [ ] No - first-come-first-served only
- [ ] Premium users only

**Q1.12:** How should load balancing work when station capacity is exceeded?
- [ ] Reduce power equally to all active sessions
- [ ] Priority-based: premium users get full power, basic users reduced
- [ ] First-in-first-out: earlier sessions get full power
- [ ] Dynamic: based on vehicle SoC (low battery gets priority)
- [ ] Queue system: new vehicles wait until capacity available

**Q1.13:** What authentication methods should be supported?
- [ ] RFID card (traditional charging networks)
- [ ] Mobile app (scan QR code or Bluetooth)
- [ ] Plug-and-Charge (ISO 15118 - automatic via vehicle)
- [ ] Credit card at charging station
- [ ] All of the above

---

## Category 2: Pricing & Billing

### Pricing Strategy

**Q2.1:** What is the baseline parking pricing model?
- [ ] Flat hourly rate (e.g., $3/hour)
- [ ] Tiered hourly (e.g., $5 first 2 hours, $3 thereafter)
- [ ] Daily maximum cap (e.g., $25/day regardless of hours)
- [ ] Monthly subscriptions (unlimited parking)
- [ ] Dynamic pricing based on demand

**Q2.2:** Should pricing vary by space type?
- [ ] Yes - disabled/motorcycle/EV spaces have different rates
- [ ] No - all spaces same price
- [ ] Only EV spaces priced differently (premium)

**Q2.3:** Should pricing vary by facility location?
- [ ] Yes - downtown more expensive than suburban
- [ ] No - standard pricing across all facilities
- [ ] Market-based - each facility sets own rates

**Q2.4:** When should dynamic pricing activate?
- [ ] Never - fixed pricing only
- [ ] Occupancy >85%
- [ ] Occupancy >90%
- [ ] Special events (concerts, sports)
- [ ] Time-of-day (peak hours)
- [ ] Multiple factors combined

**Q2.5:** What is the maximum surge multiplier allowed?
- [ ] 1.5x (50% increase)
- [ ] 2.0x (double price)
- [ ] 3.0x (triple price)
- [ ] No limit - market driven
- [ ] Configurable per facility

### Billing & Payment

**Q2.6:** When should invoices be generated?
- [ ] Immediately on check-out (real-time billing)
- [ ] End of day (batch processing)
- [ ] Monthly for subscriptions/fleet accounts
- [ ] User preference (immediate or consolidated)

**Q2.7:** What payment methods must be supported?
- [ ] Credit/debit card (Visa, Mastercard, Amex)
- [ ] Mobile wallets (Apple Pay, Google Pay)
- [ ] Bank transfer (ACH/wire)
- [ ] Fleet accounts (B2B invoicing)
- [ ] Subscription auto-pay
- [ ] All of the above

**Q2.8:** How should split billing work (parking + charging)?
- [ ] Always combined - one invoice
- [ ] Always separate - two invoices
- [ ] User preference - combined or separate
- [ ] Separate only for accounting (tax reasons)

**Q2.9:** What is the refund policy for reservations?
- [ ] Cancellation >24 hours: 100% refund
- [ ] Cancellation >2 hours: 100% refund, <2 hours: 50%, <30 min: 0%
- [ ] Cancellation >1 hour: 100% refund, <1 hour: no refund
- [ ] No refunds - all sales final
- [ ] Premium users: flexible refunds, Basic users: strict policy

**Q2.10:** Are discounts and promotions supported?
- [ ] Yes - percentage off (e.g., 20% off)
- [ ] Yes - fixed amount off (e.g., $5 off)
- [ ] Yes - free time (e.g., first 30 minutes free)
- [ ] Yes - all of the above
- [ ] No - no promotional features

---

## Category 3: Multi-Facility Operations

### Facility Management

**Q3.1:** How many facilities will EasyParkPlus operate at launch?
- [ ] 1-5 facilities (pilot)
- [ ] 6-20 facilities (regional)
- [ ] 21-100 facilities (multi-city)
- [ ] 100+ facilities (national)

**Q3.2:** Are facilities operated by different entities (multi-tenant)?
- [ ] No - EasyParkPlus operates all facilities
- [ ] Yes - property owners use EasyParkPlus software (SaaS model)
- [ ] Yes - franchise model (independent operators)
- [ ] Mix of company-owned and partner-operated

**Q3.3:** Should cross-facility reservations be supported?
- [ ] Yes - users can reserve at any facility in network
- [ ] No - each facility independent
- [ ] Yes, but limited to same city/region

**Q3.4:** Should subscription benefits work across all facilities?
- [ ] Yes - premium users get benefits at all facilities
- [ ] No - subscriptions are per-facility
- [ ] Tiered: Basic = single facility, Premium = all facilities

### User Experience

**Q3.5:** What user interfaces are required?
- [ ] Web application (desktop/mobile browser)
- [ ] Native mobile app (iOS/Android)
- [ ] On-site kiosks/payment terminals
- [ ] All of the above

**Q3.6:** What real-time features are critical for MVP?
- [ ] Live space availability (vacant/occupied)
- [ ] Wayfinding (navigate to available space)
- [ ] Real-time pricing display
- [ ] Charging station availability
- [ ] Mobile notifications (charging complete, reservation reminder)
- [ ] All of the above

**Q3.7:** How should users find available parking?
- [ ] System auto-assigns space on entry
- [ ] Users select facility, system shows availability
- [ ] Mobile app shows map with real-time availability
- [ ] Turn-by-turn navigation to assigned space

---

## Category 4: Operations & Maintenance

### Equipment Monitoring

**Q4.1:** What equipment requires health monitoring?
- [ ] Entry/exit gates
- [ ] IoT occupancy sensors
- [ ] Charging stations
- [ ] Payment kiosks
- [ ] Security cameras
- [ ] All of the above

**Q4.2:** What triggers a maintenance alert?
- [ ] Equipment offline >5 minutes
- [ ] Equipment offline >1 hour
- [ ] User reports malfunction
- [ ] Predictive maintenance: failure predicted within 7 days
- [ ] Scheduled preventive maintenance due

**Q4.3:** Should predictive maintenance be implemented?
- [ ] Yes - AI/ML models predict equipment failures (Phase 1)
- [ ] Yes - but Phase 2 feature (not MVP)
- [ ] No - reactive maintenance only
- [ ] No - preventive maintenance schedule only (no AI)

**Q4.4:** Who handles maintenance?
- [ ] In-house technicians employed by EasyParkPlus
- [ ] Third-party contractors
- [ ] Property owner responsibility (for SaaS model)
- [ ] Mix depending on facility

### Incident Management

**Q4.5:** What constitutes a critical incident requiring immediate response?
- [ ] Safety hazard (fire, gas leak, structural)
- [ ] Security breach (unauthorized access)
- [ ] Total facility outage (all gates down)
- [ ] Charging station fire/electrical fault
- [ ] All of the above

**Q4.6:** What is the SLA for critical incident response?
- [ ] 15 minutes acknowledgment, 1 hour resolution
- [ ] 30 minutes acknowledgment, 2 hours resolution
- [ ] 1 hour acknowledgment, 4 hours resolution
- [ ] Depends on facility tier/contract

---

## Category 5: User & Access Management

### User Roles

**Q5.1:** What user roles are needed?
- [ ] Driver (parks vehicles)
- [ ] Operator (manages daily operations at facility)
- [ ] Facility Manager (oversees single or multiple facilities)
- [ ] System Admin (full system access)
- [ ] Maintenance Technician (access to work orders)
- [ ] All of the above

**Q5.2:** Can one user have multiple roles?
- [ ] Yes - user can be both Driver and Operator
- [ ] No - strict role separation
- [ ] Yes, but with role-switching mechanism

### Subscription Tiers

**Q5.3:** What subscription tiers should be offered?
- [ ] Basic (free) - pay-per-use
- [ ] Premium ($9.99/mo) - 15% discount + priority booking
- [ ] Fleet ($99/mo) - unlimited vehicles, consolidated billing
- [ ] Custom enterprise plans
- [ ] All of the above

**Q5.4:** What benefits should premium users receive?
- [ ] Discounted parking rates
- [ ] Priority reservation booking
- [ ] Guaranteed space availability (within capacity)
- [ ] Free charging session fee (still pay for energy)
- [ ] Access to premium spaces (better locations)
- [ ] All of the above

**Q5.5:** Should fleet accounts have a dedicated portal?
- [ ] Yes - separate web portal for fleet managers
- [ ] Yes - dedicated dashboard in main app
- [ ] No - use standard user interface

---

## Category 6: Analytics & Reporting

### Business Intelligence

**Q6.1:** What reports are critical for launch?
- [ ] Occupancy metrics (average, peak times)
- [ ] Revenue reports (parking, charging, total)
- [ ] Facility performance comparison
- [ ] Charging station utilization
- [ ] User behavior analytics
- [ ] All of the above

**Q6.2:** Who needs access to analytics?
- [ ] System Admins only
- [ ] Facility Managers (their facilities only)
- [ ] Executive leadership (all facilities)
- [ ] All of the above with role-based access

**Q6.3:** Should predictive analytics be included?
- [ ] Yes - demand forecasting for capacity planning
- [ ] Yes - revenue forecasting for business planning
- [ ] Yes - equipment failure prediction for maintenance
- [ ] All of the above (Phase 1)
- [ ] Future enhancement (Phase 2+)

**Q6.4:** What KPIs does leadership track?
- [ ] Occupancy rate >80%
- [ ] Equipment uptime >98%
- [ ] Revenue per space per month
- [ ] Customer satisfaction score
- [ ] All of the above

---

## Category 7: Technical Architecture

### Scalability

**Q7.1:** What is the expected peak load at launch?
- [ ] 100 concurrent vehicles across all facilities
- [ ] 1,000 concurrent vehicles
- [ ] 10,000 concurrent vehicles
- [ ] 100,000+ concurrent vehicles

**Q7.2:** What is the expected growth trajectory?
- [ ] 10% annual growth (stable)
- [ ] 50% annual growth (fast scaling)
- [ ] 100%+ annual growth (hyper-growth)
- [ ] Viral/unpredictable growth

**Q7.3:** Should the system be cloud-native from day one?
- [ ] Yes - AWS/Azure/GCP from launch
- [ ] No - on-premise initially, cloud later
- [ ] Hybrid - core services cloud, facilities on-premise

### Data & Privacy

**Q7.4:** What data retention policies apply?
- [ ] Transaction data: 7 years (financial compliance)
- [ ] Session data: 1 year
- [ ] Personal data: delete on user request (GDPR)
- [ ] Video surveillance: 30 days
- [ ] All of the above

**Q7.5:** Are there specific compliance requirements?
- [ ] GDPR (EU data protection)
- [ ] CCPA (California privacy)
- [ ] PCI-DSS (payment card security)
- [ ] SOC 2 (security/availability)
- [ ] All of the above

**Q7.6:** Should the system support multiple geographic regions?
- [ ] Yes - North America (US, Canada, Mexico)
- [ ] Yes - Europe (EU)
- [ ] Yes - Global (multi-region from day one)
- [ ] No - single country initially

---

## Category 8: Integration & Partnerships

### Third-Party Systems

**Q8.1:** What external systems require integration?
- [ ] Payment gateways (Stripe, PayPal, Square)
- [ ] Charging networks (ChargePoint, EVgo, Electrify America)
- [ ] Smart grid/utility APIs (demand response)
- [ ] Navigation apps (Google Maps, Apple Maps, Waze)
- [ ] Fleet management systems (Geotab, Samsara)
- [ ] All of the above

**Q8.2:** Should the system offer public APIs for partners?
- [ ] Yes - RESTful API for third-party integrations
- [ ] Yes - Webhook subscriptions for events
- [ ] Yes - GraphQL API for flexible queries
- [ ] No - closed system, no external API
- [ ] Future consideration (Phase 2)

**Q8.3:** Should the system integrate with parking aggregators (SpotHero, ParkWhiz)?
- [ ] Yes - critical for customer acquisition
- [ ] Yes - but lower priority (Phase 2)
- [ ] No - direct bookings only

---

## Category 9: Business Priorities

### MVP Scope

**Q9.1:** What is the absolute minimum viable product for launch?
- [ ] Single facility, basic parking (no EV, no reservations)
- [ ] Single facility, parking + EV charging (no reservations)
- [ ] Multi-facility, parking + reservations (no EV)
- [ ] Full feature set (multi-facility, parking, EV, reservations)

**Q9.2:** What is the target launch date?
- [ ] Q1 2026 (3 months)
- [ ] Q2 2026 (6 months)
- [ ] Q3 2026 (9 months)
- [ ] Q4 2026 (12 months)

**Q9.3:** What is the primary success metric for first year?
- [ ] Number of facilities onboarded
- [ ] Number of users registered
- [ ] Total revenue
- [ ] Occupancy rate >80%
- [ ] Customer satisfaction score >4.5/5

### Strategic Questions

**Q9.4:** What is EasyParkPlus's long-term vision (5 years)?
- [ ] Dominant player in multi-facility parking management (focus on parking)
- [ ] Leading EV charging network (focus on energy)
- [ ] Integrated mobility platform (parking + charging + other services)
- [ ] White-label SaaS platform for property owners

**Q9.5:** What is the biggest competitive threat?
- [ ] Established parking operators (SP+, LAZ Parking)
- [ ] Charging networks (ChargePoint, Tesla Supercharger)
- [ ] Tech giants entering space (Google, Apple)
- [ ] Low-cost/free alternatives (street parking)

**Q9.6:** What is the unique value proposition?
- [ ] Best user experience (mobile-first, seamless)
- [ ] Bundled parking + charging (one-stop solution)
- [ ] Data-driven optimization (smart allocation, dynamic pricing)
- [ ] Sustainability focus (green energy, emissions reduction)

---

## Next Steps

**For Michael (Technical Manager):**
1. Review all questions above
2. Provide answers with rationale
3. Identify any questions that need stakeholder input
4. Flag any missing areas not covered in this document

**For DDD Team (Mihai):**
1. Use answers to refine domain models
2. Adjust business rules in bounded contexts
3. Update aggregates based on clarified requirements
4. Create detailed use case scenarios

**Timeline:** Please respond within **3 business days** to keep project on track.

---

**Document Status:** Ready for Technical Manager review  
**Date Created:** October 23, 2025  
**Last Updated:** October 23, 2025

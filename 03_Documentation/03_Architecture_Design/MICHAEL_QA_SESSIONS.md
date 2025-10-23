# Technical Manager Q&A Sessions

**Technical Manager**: Michael (EasyParkPlus)  
**DDD Lead**: Mihai  
**Project**: EasyParkPlus Multi-Facility Parking & EV Charging Management System

---

## Complete Q&A Session Archive

**ChatGPT Conversation Link**:  
https://chatgpt.com/share/68fa4b3c-c230-8006-acbe-396a4c3a3bcb

This single conversation contains all questions and answers from both Round 1 and Round 2.

---

## Questions Summary

### Round 1: Initial Architecture & Business Requirements (15 Questions)

**Q1: What is the absolute minimum viable product for launch?**

**Michael's Answer**: "For the MVP, we need basic parking access control—entry, exit, and slot availability—plus EV charging station support with real-time monitoring. Subscription management for monthly/annual passes should also be included, along with a mobile app or web portal for customers to register, reserve spaces, and pay. Skip the advanced analytics, dynamic pricing, and smart grid integrations for now. We just need to prove the concept works at one or two pilot facilities."

**DDD Impact**: This defines our MVP bounded contexts: Parking Space Management, Vehicle Entry/Exit, EV Charging Station Management, User & Access Management, Billing & Pricing (basic only). Analytics and Facility Operations are Phase 2.

---

**Q2: What is the target launch date for MVP?**

**Michael's Answer**: "We're aiming for a soft launch by mid-March 2026—that gives us about 5 months from now. The facilities in Boston and Philadelphia are already under contract, and construction should wrap up by February. We need the software ready for testing by early February at the latest, so that leaves us with roughly 3-4 months of actual development time once requirements are finalized."

**DDD Impact**: Aggressive timeline requires phased approach with core contexts first (PSM, VEM, EVC, UAM, BPM). Reservation and Analytics can be added post-MVP if needed.

---

**Q3: What is the primary success metric for the first year?**

**Michael's Answer**: "We want to hit 70% average parking occupancy and 50% charger utilization during operating hours. Those numbers show the facilities are profitable enough to expand. Revenue targets are secondary for the MVP—we're more focused on proving the user experience works and that our charging infrastructure can handle real-world demand."

**DDD Impact**: Analytics context must track occupancy and charger utilization metrics from day one. Core KPIs will drive Phase 2 optimizations.

---

**Q4: How many facilities will EasyParkPlus operate at launch?**

**Michael's Answer**: "Two facilities at launch: one in Boston Downtown and one in Philadelphia Center City. Both are mid-sized parking structures with about 200 regular parking spaces and 20-25 EV charging spots each. If the pilot works well, we'll expand to New York and possibly Washington D.C. within six months after launch."

**DDD Impact**: Multi-facility support required but only 2 facilities at MVP. FacilityId must be first-class concept. Cross-facility subscriptions needed (per Q6).

---

**Q5: Are facilities operated by different entities (multi-tenant architecture)?**

**Michael's Answer**: "No, all facilities are owned and operated directly by EasyParkPlus for the MVP. We might partner with third-party property owners later, but that's Phase 2. For now, think single-tenant architecture—everything runs under one company umbrella, one set of pricing rules, one customer base."

**DDD Impact**: Single-tenant simplifies architecture. No need for tenant isolation, separate databases, or complex authorization. All facilities share same pricing rules and user base.

---

**Q6: Should subscription benefits work across all facilities?**

**Michael's Answer**: "Yes, definitely. If a customer buys a monthly parking pass or annual charging membership, they should be able to use it at any EasyParkPlus location. That's a key differentiator from competitors—most parking operators silo their locations. We want seamless access across Boston, Philly, and future cities."

**DDD Impact**: Subscription context must be facility-agnostic. User & Access Management handles subscriptions. Vehicle Entry/Exit and EV Charging must validate subscriptions across all facilities in real-time.

---

**Q7: What is EasyParkPlus's primary business model for EV charging?**

**Michael's Answer**: "We charge customers per kilowatt-hour (kWh) delivered, plus a small session fee to cover hardware costs. There's also an idle fee after charging completes—say $0.50 per minute—to encourage people to move their cars and free up the charger. We'll also offer monthly charging passes for frequent users, similar to parking subscriptions."

**DDD Impact**: Billing context must handle kWh-based pricing + session fees + idle fees. Charging session must track: start time, end time, charging completion time, energy delivered. Idle time = (actual departure - charging completion time).

---

**Q8: Who owns the charging infrastructure?**

**Michael's Answer**: "EasyParkPlus owns and maintains the charging stations. We're not white-labeling or partnering with ChargePoint or EVgo for the MVP. We're working directly with a hardware vendor (likely ABB or Tritium) to install Level 2 and DC fast chargers. We handle all operations, billing, and customer support in-house."

**DDD Impact**: No external charging network integration needed. EV Charging context owns full lifecycle: installation, operation, billing, maintenance. Vendor integration is only for hardware procurement.

---

**Q9: How should charging sessions be billed?**

**Michael's Answer**: "Billing happens at the end of the charging session. Once the customer unplugs or manually stops charging via the app, we calculate the total cost: (kWh delivered × rate) + session fee + any idle fees. Payment is processed immediately using the card or subscription on file. Customers should get a receipt via email or in-app within a few seconds."

**DDD Impact**: Billing event triggered by ChargingCompleted event. BPM context subscribes to this event, calculates total cost, processes payment via gateway (Stripe), sends receipt. Must be near-real-time (<5 seconds).

---

**Q10: What is the baseline parking pricing model?**

**Michael's Answer**: "Standard hourly rate with a daily cap. For example: $3/hour for the first 3 hours, then $5/hour, capped at $30/day. EV charging spots might have a slight premium—say $4/hour—since they're in demand. Monthly passes would be around $200-250 depending on location. Pricing is static for MVP—no surge pricing or occupancy-based adjustments yet."

**DDD Impact**: Pricing context must support hourly rates with time-based progression + daily caps + monthly passes. Different rates for EV vs regular spaces. No dynamic pricing logic needed for MVP.

---

**Q11: When should dynamic pricing activate (if applicable)?**

**Michael's Answer**: "Not for MVP. We want to collect at least 3-6 months of usage data before introducing dynamic pricing. Once we have historical occupancy patterns, we can implement surge pricing during peak hours (like 8-10 AM and 5-7 PM) or lower rates during off-peak times. That's a Phase 2 feature."

**DDD Impact**: MVP uses static pricing only. Pricing context architecture should allow for future dynamic pricing plugin (e.g., PricingStrategy interface), but no implementation needed now. Analytics context must collect occupancy data for future ML models.

---

**Q12: Should the system be cloud-native from day one?**

**Michael's Answer**: "Absolutely. We're starting with AWS (could also be Azure or GCP, but likely AWS). We want auto-scaling, managed databases, serverless functions where appropriate, and easy integration with payment gateways and monitoring tools. On-premise infrastructure doesn't make sense for a startup—cloud gives us flexibility and speed."

**DDD Impact**: Infrastructure decisions: AWS-hosted microservices (ECS/EKS), RDS PostgreSQL for operational data, S3 for backups, CloudWatch for monitoring, API Gateway for routing, Kafka/EventBridge for events. No on-premise deployment needed.

---

**Q13: What is the expected peak load at launch?**

**Michael's Answer**: "With two facilities and roughly 400-500 parking spaces total, we're looking at maybe 1,000-1,500 vehicles per day across both locations. Peak times would be weekday mornings (7-9 AM) and evenings (5-7 PM). That translates to maybe 10-15 entries/exits per minute during rush hour. Charging sessions are slower—maybe 50-100 active sessions at any given time. Nothing crazy for modern cloud infrastructure."

**DDD Impact**: Traffic estimates: ~10-15 entries/exits per minute = ~0.25 req/sec sustained, ~50-100 concurrent charging sessions. Vehicle Entry/Exit and Charging contexts need to handle moderate load. Horizontal scaling not critical for MVP but should be architecturally possible.

---

**Q14: Is OCPP protocol support mandatory for EV charging?**

**Michael's Answer**: "Yes, definitely. The charging station vendor will provide OCPP 2.0.1-compliant hardware, so our backend needs to implement the OCPP protocol to communicate with the chargers. That includes commands like StartTransaction, StopTransaction, meter value reporting, and status notifications. It's industry standard and non-negotiable."

**DDD Impact**: EV Charging context must implement OCPP 2.0.1 server. This is a technical integration requirement, not core domain logic. Use Conformist pattern: EVC context adapts to OCPP protocol. Consider using existing OCPP library (e.g., Python OCPP) rather than building from scratch.

---

**Q15: What smart grid features are needed for EV charging?**

**Michael's Answer**: "We need load balancing across chargers to avoid exceeding the facility's power capacity—let's say 400 kW max per location. If all chargers try to pull power simultaneously, the system should throttle them proportionally. Peak shaving is also important: during high electricity cost periods (usually afternoons), we might reduce charging speed slightly. Demand response integration with the local utility would be nice but Phase 2. For MVP, focus on basic load balancing and energy metering per charger."

**DDD Impact**: EV Charging context must implement load balancing algorithm. Domain rules: max facility capacity (400 kW), allocate power proportionally to active sessions, throttle if capacity exceeded. Energy metering tracked per session. Smart grid integration (utility APIs) is Phase 2 external integration.

---

### Round 2: Technical Architecture Deep Dive (10 Questions)

**Q16: Should each microservice have its own database, or can we use shared schemas within a common PostgreSQL instance for the MVP?**

**Michael's Answer**: "Using a shared PostgreSQL instance with separate schemas is fine for the MVP. It's simpler to manage early on, and we don't expect massive traffic right away. Once operations scale across more cities or vendors, you can separate databases for each microservice for better isolation and performance."

**DDD Impact**: Database per service pattern deferred to Phase 2. MVP uses single PostgreSQL with schema-per-service (e.g., `parking_space_schema`, `billing_schema`, `charging_schema`). Simpler backup/restore, easier development. Migration to separate databases possible later without changing service APIs.

---

**Q17: What is the preferred approach for inter-service communication - synchronous REST APIs, asynchronous message queues like Kafka, or a hybrid approach?**

**Michael's Answer**: "A hybrid approach would make the most sense. Day-to-day actions like parking entry or starting a charge should be real-time (REST), since customers expect instant response. But things like billing updates, charger status logs, or occupancy analytics can move through asynchronous queues like Kafka, since those don't need immediate feedback."

**DDD Impact**: Synchronous (REST): Vehicle entry/exit, space availability checks, charging start/stop, payment authorization. Asynchronous (Kafka): Billing events, analytics data, audit logs, notification triggers. Design service contracts for both patterns.

---

**Q18: How should API authentication and authorization be handled - centralized JWT service, decentralized per-service auth, or API Gateway-based authentication?**

**Michael's Answer**: "A centralized API Gateway setup sounds most practical. That way, authentication and authorization are managed in one place — simpler to control access for staff, vendors, and customers. The gateway can issue and verify JWT tokens before routing to any service, keeping the individual microservices focused on their core tasks."

**DDD Impact**: API Gateway (AWS API Gateway or Kong) handles JWT issuance/validation. User & Access Management context provides user/role data. Services receive pre-validated JWT in request headers, extract userId/roles. No service-level auth logic needed except authorization checks.

---

**Q19: What are the expected traffic patterns and scalability requirements for the two MVP facilities in terms of requests per second and acceptable latency targets?**

**Michael's Answer**: "For the two MVP sites, we're expecting moderate traffic. Roughly around 50–100 requests per second during peak hours (mostly parking entries, payments, and charger updates). Acceptable latency should stay under 300 ms for real-time actions like entry validation or charger start/stop. Batch operations (like reports or analytics) can tolerate up to a few seconds delay."

**DDD Impact**: Performance SLAs: <300ms for synchronous operations (entry/exit, charging start/stop), <5s for batch operations (reports). 50-100 req/sec is moderate load—single service instances sufficient for MVP. Database connection pooling, caching (Redis) optional but not critical.

---

**Q20: What monitoring and logging infrastructure should we use - ELK stack, AWS CloudWatch, distributed tracing with Jaeger, or other preferred tools?**

**Michael's Answer**: "I'd suggest using CloudWatch for the MVP, since it's built into AWS and keeps setup simple. It can handle logs, metrics, and alerts for both parking and charging services. Later, once we expand, adding ELK for deeper log analysis and Jaeger for tracing would make sense — but early on, CloudWatch gives enough visibility without extra overhead."

**DDD Impact**: Monitoring stack: AWS CloudWatch (logs, metrics, alarms). Each service emits structured logs (JSON) with correlation IDs. Key metrics: request latency, error rates, queue depths, database connection usage. ELK + Jaeger deferred to Phase 2.

---

**Q21: Which payment gateway should we integrate with for the MVP - Stripe, Square, PayPal/Braintree, or fleet payment networks like WEX?**

**Michael's Answer**: "For the MVP, Stripe would be the best fit. It's easy to integrate, supports both one-time and subscription payments, and works well with mobile and web apps. Later on, once we start serving corporate or fleet customers, we can add WEX or similar networks for business accounts."

**DDD Impact**: Billing context integrates Stripe API. Use Conformist pattern—adapt to Stripe's payment model. Support one-time charges (parking/charging sessions) and recurring subscriptions (monthly passes). Stripe webhooks for payment status updates. WEX integration Phase 2.

---

**Q22: What are the data retention and privacy requirements - how long should session data be kept, and do we need GDPR or CCPA compliance?**

**Michael's Answer**: "We'll need to retain session data for at least 12 months, mainly for billing disputes and operational analysis. Aggregated, anonymized data can be stored longer for trend tracking. Since we operate in the U.S., CCPA compliance applies (especially for New York and California drivers if they use our services). GDPR isn't mandatory unless we serve EU customers, but it's smart to follow similar privacy standards."

**DDD Impact**: Data retention policy: 12 months for raw session/transaction data, 5+ years for aggregated/anonymized analytics data. CCPA compliance required: user data deletion requests, opt-out mechanisms, privacy policy. Implement data deletion workflows in all contexts (User, Vehicle, Billing, Charging).

---

**Q23: What third-party systems need integration at MVP - accounting software like QuickBooks, CRM systems like Salesforce, or mobile app platforms?**

**Michael's Answer**: "For the MVP, we'll need just the mobile app platform integration so users can register, pay, and manage sessions. Accounting can stay manual at first, with exports for reconciliation. We'll integrate QuickBooks later for automated invoicing, and Salesforce or similar CRM only once we start managing larger fleets or corporate clients."

**DDD Impact**: MVP external integrations: Mobile app (React Native/Flutter) + Stripe payment gateway + OCPP chargers. QuickBooks and Salesforce deferred to Phase 2. Billing context must support CSV/Excel export for manual accounting reconciliation.

---

**Q24: What are the disaster recovery and business continuity requirements in terms of RTO (Recovery Time Objective) and RPO (Recovery Point Objective)?**

**Michael's Answer**: "For our operations, the targets should be RTO within 1 hour — parking access and charging services must be restored quickly to avoid customer disruption. RPO within 15 minutes — we can tolerate only minimal data loss, like a few session logs or payment updates. These limits keep downtime short and ensure payments and access control remain consistent across all sites."

**DDD Impact**: DR requirements: RTO 1 hour, RPO 15 minutes. Implementation: Automated database backups every 15 minutes (RDS automated backups), multi-AZ deployment for failover, infrastructure-as-code for rapid redeployment. Critical services: Vehicle Entry/Exit, Charging, Payment processing.

---

**Q25: How should cross-facility operations be coordinated - should subscriptions sync in real-time between Boston and Philadelphia, and do we need consolidated reporting?**

**Michael's Answer**: "Yes, subscriptions should sync in real time between Boston and Philadelphia so customers get consistent access everywhere. Consolidated reporting is also important — management needs a single dashboard showing parking, charging, and revenue stats across all sites. That helps track utilization and spot issues without switching between facility systems."

**DDD Impact**: Subscriptions stored centrally in User & Access Management context—no per-facility sync needed. Analytics context aggregates data from all facilities for consolidated dashboard. FacilityId is query parameter, not tenant separator. Cross-facility queries supported in all contexts.

---

## Critical Questions for Hesham's Microservices Work

**All questions answered!** ✅

### Architecture Decisions Summary:

| Question | Decision | Impact |
|----------|----------|--------|
| **Q16 (Database)** | Single PostgreSQL, separate schemas per service | Simpler MVP, can split databases later |
| **Q17 (Communication)** | Hybrid: REST for real-time, Kafka for async events | Balance responsiveness with decoupling |
| **Q18 (Auth)** | API Gateway with centralized JWT | Single point of auth, simplified services |
| **Q19 (Scalability)** | 50-100 req/sec, <300ms latency | Moderate traffic, standard infrastructure |
| **Q20 (Monitoring)** | AWS CloudWatch MVP, ELK/Jaeger Phase 2 | Simple setup, expand later |
| **Q21 (Payment)** | Stripe for MVP, WEX for fleets later | Easy integration, good API |
| **Q22 (Data Retention)** | 12 months, CCPA compliance | Standard retention, US privacy laws |
| **Q23 (Integrations)** | Mobile app only MVP, QuickBooks/CRM Phase 2 | Minimal dependencies |
| **Q24 (DR)** | RTO 1 hour, RPO 15 minutes | Fast recovery, minimal data loss |
| **Q25 (Cross-Facility)** | Real-time subscription sync, consolidated dashboard | Seamless user experience |

**No assumptions needed** - proceed with microservices architecture diagram using Michael's confirmed answers.

---

## Documentation Impact

These Q&A sessions informed the following deliverables:

1. **Bounded Context Diagram** (`bounded_context_diagram.md` + PNG)
   - 8 bounded contexts with MVP phasing
   - Integration patterns (Partnership, Customer-Supplier, Conformist, ACL)
   - Context mapping based on Michael's requirements

2. **Domain Models** (`domain_models.md`)
   - Aggregate roots and value objects per bounded context
   - Business rules and invariants
   - Repository patterns

3. **Ubiquitous Language** (`ubiquitous_language.md`)
   - Domain-specific terminology
   - Shared understanding across team

4. **Bounded Context Analysis** (`bounded_contexts_analysis.md`)
   - Core vs Supporting vs Generic domain classification
   - Strategic design decisions

---

## Additional Questions Not Yet Asked

If additional clarification needed for Phase 2 planning:
- **Performance**: What are acceptable latency targets for real-time charger status updates?
- **Security**: Penetration testing requirements before launch?
- **Compliance**: SOC 2 or ISO 27001 certification needed?
- **Internationalization**: Future expansion to Canada/Europe requires multi-currency?

---

**Status**: All Round 1 + Round 2 questions answered and documented in ChatGPT link  
**Owner**: Mihai (DDD Lead)  
**Last Updated**: October 23, 2025

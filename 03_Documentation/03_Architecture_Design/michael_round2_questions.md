# Round 2 Questions for Michael (Technical Manager)

**Date**: October 23, 2025  
**Purpose**: Clarify technical architecture decisions for microservices design  
**Context**: Follow-up to 15 questions answered in Round 1  
**Owner**: Mihai (for Hesham's microservices architecture work)

---

## Priority Questions for Immediate Architecture Work

### Q16: Database Strategy (CRITICAL)

**Question**: Should each microservice have its own database, or can we use shared schemas within a common database instance?

**Context**: 
- We have 8 bounded contexts that will likely map to 8+ microservices
- Microservices best practices recommend database-per-service pattern
- However, this increases operational complexity for MVP

**Need to know**:
- Is database-per-service mandatory, or can we start with logical separation (schemas)?
- What database technologies are approved? (PostgreSQL, MongoDB, Redis, etc.)
- Any constraints on database licensing or cloud provider?
- For MVP (March 2026), can we use shared PostgreSQL with separate schemas?

**Impact**: Determines data architecture, service boundaries, and deployment complexity

---

### Q17: Inter-Service Communication (CRITICAL)

**Question**: What is the preferred approach for inter-service communication?

**Options**:
1. **Synchronous**: REST APIs or gRPC for request-response
2. **Asynchronous**: Message queues (RabbitMQ, Kafka) for event-driven
3. **Hybrid**: REST for external APIs, message queues for internal events

**Context**:
- Charging Management → Billing (charging session completed)
- Parking Management → Billing (parking session completed)
- Smart Grid Management → Charging Management (load balancing commands)
- Fleet Management → Parking/Charging (real-time availability queries)

**Need to know**:
- Preference for synchronous vs asynchronous communication?
- Should we use an API Gateway for external clients?
- Any existing message broker infrastructure we should use?
- For MVP, can we start with REST and add message queues later?

**Impact**: Affects reliability, scalability, and development timeline

---

### Q18: API Gateway & Authentication

**Question**: How should API authentication and authorization be handled?

**Options**:
1. **Centralized**: Single authentication service with JWT tokens
2. **Decentralized**: Each service handles its own authentication
3. **API Gateway**: Gateway handles auth, services trust internal calls

**Context**:
- Multiple client types: mobile app, web portal, facility manager dashboard
- Third-party integrations: payment gateways, OCPP chargers, smart grid
- Security requirements for PCI compliance (payment data)

**Need to know**:
- Token-based (JWT) or session-based authentication?
- How should API keys for third-party integrations be managed?
- Single sign-on (SSO) requirements for facility managers?
- For MVP, OAuth 2.0 sufficient or need custom solution?

**Impact**: Security architecture and API design

---

## Deployment & Operations Questions

### Q19: Service Scalability Requirements

**Question**: What are the expected traffic patterns and scalability requirements?

**Need to know**:
- Expected requests per second per facility at MVP (2 facilities)?
- Peak usage times (weekday mornings? weekend evenings?)?
- Auto-scaling requirements (Kubernetes, AWS ECS, manual scaling)?
- Acceptable latency targets:
  - p50 (median response time)
  - p95 (95th percentile)
  - p99 (99th percentile)
- For MVP, can we deploy all services on single server cluster?

**Context**:
- Boston Downtown: 500 parking spaces + 50 EV chargers
- Philadelphia Center City: 750 parking spaces + 75 EV chargers
- Total capacity: 1,250 spaces + 125 chargers

**Impact**: Infrastructure planning and cost estimates

---

### Q20: Monitoring & Observability

**Question**: What monitoring and logging infrastructure should we use?

**Need to know**:
- Centralized logging system preference (ELK stack, CloudWatch, Splunk)?
- Distributed tracing requirements (Jaeger, Zipkin, AWS X-Ray)?
- Alerting system (PagerDuty, Slack, email)?
- Metrics to track:
  - Service health (uptime, response times)
  - Business metrics (occupancy rates, revenue per hour)
  - Charger performance (kWh delivered, session durations)
- For MVP, can we start with basic logging and add observability later?

**Impact**: Operational readiness and troubleshooting capabilities

---

## Business Logic Questions

### Q21: Payment Processing (HIGH PRIORITY)

**Question**: Which payment gateway should we integrate with?

**Options**:
- **Stripe**: Best for recurring subscriptions, strong API
- **Square**: Good for physical terminals, in-person payments
- **PayPal/Braintree**: International support
- **Fleet payment networks**: WEX, FleetCor

**Need to know**:
- Preferred payment gateway vendor?
- Support for multiple payment methods:
  - Credit/debit cards
  - Mobile wallets (Apple Pay, Google Pay)
  - Fleet cards (for commercial vehicles)
  - RFID cards (for subscriptions)
- PCI compliance requirements (Level 1, 2, 3, or 4)?
- For MVP, credit cards only or multiple methods?

**Context**: Needed to design Billing service APIs and payment workflows

**Impact**: Billing service design, compliance requirements, user experience

---

### Q22: Data Retention & Privacy

**Question**: What are the data retention and privacy requirements?

**Need to know**:
- How long should parking/charging session data be retained?
  - Operational data (real-time to 30 days)
  - Billing records (1-7 years for tax/audit)
  - Analytics data (aggregated, indefinite)
- GDPR compliance requirements (European users)?
- CCPA compliance (California users)?
- Right to be forgotten: Can users request data deletion?
- Data anonymization for analytics?
- For MVP, 1-year retention sufficient?

**Context**: 
- Multi-state operations (Massachusetts, Pennsylvania, future expansion)
- Credit card data (PCI-DSS requirements)
- User location data (privacy concerns)

**Impact**: Database design, backup strategy, compliance costs

---

### Q23: Third-Party Integrations

**Question**: What third-party systems need integration?

**Need to know**:
- **Accounting system**: QuickBooks, Xero, SAP for financial reporting?
- **CRM system**: Salesforce, HubSpot for customer management?
- **Mobile app**: Native iOS/Android or React Native/Flutter?
- **Web portal**: For facility managers (real-time monitoring)?
- **Smart city APIs**: Integration with municipal parking systems?
- **Fleet management systems**: Integration with corporate fleet software?
- For MVP, which integrations are mandatory vs Phase 2?

**Context**: Determines API design and integration complexity

**Impact**: Development timeline and external dependencies

---

## Disaster Recovery & Operations

### Q24: Disaster Recovery Requirements

**Question**: What are the disaster recovery and business continuity requirements?

**Need to know**:
- **RTO (Recovery Time Objective)**: Maximum acceptable downtime?
  - Suggestion: 4 hours for parking, 1 hour for active charging sessions
- **RPO (Recovery Point Objective)**: Maximum acceptable data loss?
  - Suggestion: 5 minutes for payment data, 1 hour for analytics
- Backup strategy:
  - Real-time replication to secondary region?
  - Nightly backups sufficient for MVP?
- Failover scenarios:
  - If Boston facility goes offline, can Philadelphia still operate?
  - If payment gateway fails, can we queue transactions?
  - If OCPP connection drops, what happens to active charging sessions?

**Context**: Mission-critical system with revenue impact if down

**Impact**: Infrastructure costs, architecture complexity

---

### Q25: Multi-Facility Coordination

**Question**: How should cross-facility operations be coordinated?

**Need to know**:
- **Subscriptions**: Should they sync in real-time across facilities?
  - Example: User buys subscription in Boston, immediately valid in Philadelphia?
- **Reporting**: Consolidated reports or per-facility reports?
  - Suggestion: Both (facility managers see local, executives see consolidated)
- **User accounts**: 
  - Single account across all facilities? ✅ (Assumed yes)
  - Or facility-specific accounts?
- **Load balancing**: 
  - If one facility reaches 400 kW cap, can we suggest user go to other facility?
  - Mobile app shows availability across all facilities?
- **Fleet accounts**: 
  - Corporate fleet subscriptions valid at all facilities? ✅ (Assumed yes per Round 1)

**Context**: From Round 1, we know cross-facility subscriptions have benefits

**Impact**: Subscription service design, user experience, reporting architecture

---

## Summary of Critical Path Questions

| Priority | Question | Blocks | Can Proceed Without? |
|----------|----------|--------|---------------------|
| **HIGH** | Q16 (Database) | Microservices architecture | No - need for data design |
| **HIGH** | Q17 (Communication) | Service interactions | Partially - can assume REST |
| **HIGH** | Q21 (Payment) | Billing service APIs | Partially - can design generic |
| MEDIUM | Q18 (Auth) | Security architecture | Yes - can assume JWT |
| MEDIUM | Q23 (Integrations) | API design | Yes - can design extensible APIs |
| LOW | Q19-Q20, Q22, Q24-Q25 | Operations planning | Yes - architectural decisions |

---

## Recommended Approach If No Response

**If Michael doesn't respond immediately**, Hesham can proceed with reasonable assumptions:

### Database Strategy (Q16)
**Assumption**: Start with single PostgreSQL instance with separate schemas per service
- **Rationale**: Easier for MVP, can migrate to separate databases later
- **Migration path**: PostgreSQL logical replication to split later

### Inter-Service Communication (Q17)
**Assumption**: REST APIs for synchronous calls, add message queue in Phase 2
- **Rationale**: Simpler for MVP, well-understood by team
- **Technology**: FastAPI (Python) or Spring Boot (Java)

### Payment Gateway (Q21)
**Assumption**: Stripe for MVP (credit cards only)
- **Rationale**: Best developer experience, strong documentation
- **Expansion**: Add Square/PayPal in Phase 2

### Authentication (Q18)
**Assumption**: JWT with OAuth 2.0, API Gateway handles auth
- **Rationale**: Industry standard, scalable
- **Technology**: Auth0 or AWS Cognito

---

## Next Steps

1. **Send questions to Michael** (prioritize Q16, Q17, Q21)
2. **If no response in 24 hours**: Proceed with assumptions above
3. **Document assumptions** in microservices architecture diagram
4. **Mark assumptions for review** before Phase 2 implementation

---

**Status**: Draft ready for Michael  
**Expected Response Time**: 1-2 days  
**Action**: Mihai to send to Michael via email/Slack

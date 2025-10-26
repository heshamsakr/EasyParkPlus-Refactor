# EasyParkPlus: Ubiquitous Language

**Domain-Driven Design Lead:** Mihai  
**Date:** October 23, 2025  
**Project:** EasyParkPlus Multi-Facility Parking & EV Charging Management System

---

## Purpose

This document defines the **ubiquitous language** for EasyParkPlus - the shared vocabulary that domain experts, developers, and stakeholders use to discuss the system. This language must be used consistently in code, documentation, and conversations.

---

## BC1: Parking Space Management

### Core Terms

| Term | Definition | Type | Usage Example |
|------|------------|------|---------------|
| **Parking Facility** | A physical location containing multiple parking spaces, potentially across multiple floors/zones | Aggregate Root | "The downtown facility has 500 spaces across 3 floors" |
| **Parking Space** | An individual parking spot with a unique identifier, type, and occupancy status | Entity | "Space A-101 is a disabled parking space on Floor 1" |
| **Space Type** | Category of parking space based on vehicle requirements | Value Object | Types: Regular, Motorcycle, Disabled, EV-Ready |
| **Occupancy Status** | Real-time state of a parking space | Value Object | States: Vacant, Occupied, Reserved, Maintenance |
| **Floor Level** | Physical level/floor within a multi-story facility | Value Object | "Level 2", "Ground", "Basement 1" |
| **Zone** | Logical grouping of spaces within a facility | Entity | "East Wing", "VIP Section" |
| **IoT Sensor** | Physical device monitoring space occupancy in real-time | Entity | "Sensor S-401 detected occupancy change at 14:32" |
| **Capacity** | Total number of spaces in a facility, zone, or by type | Value Object | "Total capacity: 500 spaces (450 regular, 30 EV, 20 disabled)" |
| **Allocate Space** | Assign an available space to a vehicle based on type and availability | Command | "System allocated space B-205 to motorcycle MH-12-5678" |
| **Release Space** | Mark a space as vacant after vehicle departure | Command | "Space A-101 released at exit" |

### Business Rules Language
- "A space can only be occupied by one vehicle at a time"
- "Reserved spaces cannot be allocated to walk-in vehicles"
- "EV-ready spaces can accommodate regular vehicles when charging is not requested"
- "Sensor-detected occupancy overrides manual status updates"
- "Maintenance-marked spaces are excluded from availability calculations"

---

## BC2: Vehicle Entry/Exit Management

### Core Terms

| Term | Definition | Type | Usage Example |
|------|------------|------|---------------|
| **Parking Session** | A single parking event with entry time, exit time, and associated space | Aggregate Root | "Session PS-12345 started at 09:15, ended at 17:30" |
| **Vehicle** | A motorized transport identified by registration number and type | Entity | "Vehicle MH-01-AB-1234 is an electric car" |
| **Registration Number** | Unique government-issued vehicle identifier (license plate) | Value Object | "MH-01-AB-1234" (format varies by jurisdiction) |
| **Vehicle Type** | Category of vehicle based on size and power source | Value Object | Types: Car, Motorcycle, ElectricCar, ElectricMotorcycle |
| **Check-in** | Process of vehicle entering facility and starting a parking session | Command | "Vehicle checked in at Gate 2 at 09:15" |
| **Check-out** | Process of vehicle exiting facility and ending a parking session | Command | "Vehicle checked out at Gate 1 at 17:30" |
| **Session Status** | Current state of a parking session | Value Object | States: Active, Completed, Abandoned, Disputed |
| **Session Duration** | Time span between check-in and check-out | Calculated Value | "Session duration: 8 hours 15 minutes" |
| **Entry Gate** | Physical access point where vehicles check in | Entity | "Gate 2 - East Entrance" |
| **Exit Gate** | Physical access point where vehicles check out | Entity | "Gate 1 - West Exit" |
| **Abandoned Session** | Active session exceeding maximum duration without check-out | Event | "Session marked abandoned after 48 hours" |

### Business Rules Language
- "Every vehicle must check in before parking"
- "A vehicle cannot have multiple active sessions simultaneously"
- "Session duration starts at check-in and ends at check-out"
- "Electric vehicles require EV-ready spaces"
- "Motorcycles can use motorcycle or regular spaces but not disabled spaces"
- "Sessions exceeding 48 hours without exit are flagged as abandoned"

---

## BC3: Reservation Management

### Core Terms

| Term | Definition | Type | Usage Example |
|------|------------|------|---------------|
| **Reservation** | Advance booking of a parking space for a specific time period | Aggregate Root | "Reservation R-789 for Dec 15, 10:00-14:00" |
| **Time Slot** | Specific date and time window for a reservation | Value Object | "Start: 2025-12-15 10:00, End: 2025-12-15 14:00" |
| **Reservation Status** | Current state of a reservation in its lifecycle | Value Object | States: Pending, Confirmed, Active, Completed, Cancelled, Expired |
| **Grace Period** | Time window after reservation start when space is held before auto-cancellation | Value Object | "15-minute grace period" |
| **Space Preference** | User requirements for space location or features | Value Object | Examples: "Near entrance", "EV charging", "Covered parking" |
| **Claim Reservation** | Process of converting a confirmed reservation to an active parking session | Command | "Reservation claimed at check-in" |
| **Cancel Reservation** | Terminate a reservation before its start time | Command | "User cancelled reservation 2 hours in advance" |
| **No-show** | Failure to claim reservation within grace period | Event | "Reservation marked no-show at 10:16" |
| **Overbooking** | Accepting more reservations than available capacity | Business Rule | "System prevents overbooking beyond 5% buffer" |
| **Reservation Fee** | Upfront charge to secure a reservation | Value Object | "Reservation fee: $5.00" |

### Business Rules Language
- "Reservations can be made up to 30 days in advance"
- "Reservation requires claiming within grace period or is auto-cancelled"
- "Cancelled reservations are refunded based on cancellation time (>2hrs: full, <2hrs: 50%, <30min: no refund)"
- "Premium users have priority booking during high-demand periods"
- "Reserved spaces revert to general availability after expiration"
- "Each user can have maximum 3 future reservations"

---

## BC4: EV Charging Station Management ⚡

### Core Terms

| Term | Definition | Type | Usage Example |
|------|------------|------|---------------|
| **Charging Station** | Physical infrastructure containing one or more charging points | Aggregate Root | "Station CS-101 has 4 charging points" |
| **Charging Point** | Individual connector/port on a charging station | Entity | "Point 1 on CS-101 is a CCS Type 2 connector" |
| **Charging Session** | Single charging event from start to completion | Aggregate Root | "Session CH-5678 delivered 45 kWh over 2 hours" |
| **Power Level** | Charging speed classification | Value Object | Types: Level 1 (1.4kW), Level 2 (7-22kW), DC Fast Charge (50-350kW) |
| **Connector Type** | Physical plug standard | Value Object | Types: Type 1 (J1772), Type 2 (Mennekes), CCS, CHAdeMO, Tesla |
| **Charge Status** | Current state of a charging point | Value Object | States: Available, Charging, Completed, Faulted, Offline, Reserved |
| **Energy Delivered** | Total electrical energy transferred during session | Value Object | "45.3 kWh" |
| **State of Charge (SoC)** | Battery level percentage | Value Object | "Battery at 80% SoC" |
| **Charging Rate** | Cost per unit of energy | Value Object | "$0.35/kWh during peak hours" |
| **Session Fee** | Flat fee charged per EV charging session regardless of energy consumed | Value Object | "$2.00 session fee per charge" |
| **Idle Fee** | Penalty fee charged per minute when driver overstays after charging completion | Value Object | "$0.50/minute idle fee after 10-minute grace period" |
| **OCPP 2.0.1** | Open Charge Point Protocol version 2.0.1 - mandatory industry standard for station-to-cloud communication | Integration | "All charging stations communicate via OCPP 2.0.1" |
| **Load Balancing** | Dynamic power distribution across charging points to prevent facility exceeding 400 kW capacity | Domain Service | "Load balancer reduced Point 3 from 50kW to 35kW" |
| **Peak Shaving** | Strategy to reduce facility power consumption during utility peak hours to minimize demand charges | Domain Service | "Peak shaving activated: reduced total load from 380kW to 320kW" |
| **Demand Response** | Utility-initiated request to temporarily reduce facility power consumption during grid stress | Event | "Demand response event: reduce load by 25% for next 2 hours" |
| **Charging Completed At** | Timestamp when vehicle battery reaches target SoC (distinct from session end time) | Value Object | "Charging completed at 11:15, session ended at 11:45 (30min idle)" |
| **Start Charging** | Initiate power transfer to vehicle | Command | "Charging started at 09:30" |
| **Stop Charging** | Terminate power transfer | Command | "Charging stopped by user at 11:15" |
| **Plug-and-Charge** | Authentication via vehicle-station communication (ISO 15118) | Feature | "Vehicle authenticated automatically via PnC" |
| **Charging Fault** | Error condition preventing charging | Event | "Fault detected: Ground fault on Point 2" |

### Business Rules Language
- "Each charging station can have 1-8 charging points"
- "Charging session starts when vehicle is authenticated and connected"
- "Session automatically stops when battery reaches target SoC or user-defined limit"
- "Charging fees = (kWh × rate) + session_fee + parking_fee + idle_fee"
- "Idle fee starts 10 minutes after charging completion (grace period)"
- "Load balancing activates when total facility power exceeds 400 kW capacity"
- "Peak shaving triggers during utility-defined peak hours to minimize demand charges"
- "Demand response events can reduce facility load by up to 50% temporarily"
- "All stations must support OCPP 2.0.1 for cloud connectivity"
- "Faulted charging points are automatically disabled and maintenance alert sent"
- "Charging sessions timeout after 4 hours for Level 2, 1 hour for DC Fast"

---

## BC5: Billing & Pricing Management

### Core Terms

| Term | Definition | Type | Usage Example |
|------|------------|------|---------------|
| **Invoice** | Itemized bill for parking and/or charging services | Aggregate Root | "Invoice INV-12345 totals $47.50 (parking + charging)" |
| **Parking Fee** | Charge for parking space usage | Entity | "$3/hour for first 3 hours, $2/hour thereafter" |
| **Charging Fee** | Total charge for EV charging session (energy + session fee + idle fee) | Entity | "$15.75 (12.5 kWh × $0.35 + $2.00 session + $9.00 idle)" |
| **Pricing Policy** | Rules defining fee calculation | Entity | "Weekday Policy: $5/hour, Weekend Policy: $3/hour" |
| **Dynamic Pricing** | Real-time pricing adjusted based on demand, time, or other factors (Phase 2 feature) | Domain Service | "Price increased to $8/hour due to 95% occupancy" |
| **Base Rate** | Standard hourly/daily rate before adjustments | Value Object | "Base rate: $4/hour" |
| **Surge Multiplier** | Factor applied during high-demand periods (Phase 2 feature) | Value Object | "1.5x surge during events" |
| **Daily Cap** | Maximum parking fee charged per 24-hour period regardless of duration | Value Object | "Daily cap: $45.00 (reached after 9 hours at $5/hour)" |
| **Hours Until Daily Cap** | Number of hours at hourly rate before daily cap applies | Value Object | "9 hours until daily cap" |
| **Monthly Pass** | Discounted flat-rate subscription for unlimited parking during month | Value Object | "$199/month unlimited parking pass" |
| **Special Rate** | Time-based or event-based rate adjustments | Value Object | "Nights (6PM-6AM): $2/hour, Weekends: $3/hour" |
| **Cross-Facility Benefits** | Subscription benefits valid at all EasyParkPlus locations | Feature | "Premium subscription: 15% off at all facilities" |
| **Discount Code** | Promotional code providing fee reduction | Value Object | "EARLY25 gives 25% off before 8AM" |
| **Tax Rate** | Jurisdiction-specific tax percentage | Value Object | "8.5% sales tax" |
| **Line Item** | Individual charge component on invoice | Value Object | "Parking: $24.00, Charging: $15.75, Tax: $3.38" |
| **Payment Transaction** | Record of payment attempt and result | Entity | "Transaction TX-9876: $47.50 paid via Visa *1234" |
| **Refund** | Money returned for cancelled service or overpayment | Entity | "Refund of $12.50 for early departure" |
| **Calculate Fees** | Compute total charges based on usage and policies | Command | "System calculated $32.50 for 6.5 hour session" |

### Business Rules Language
- "Parking fees calculated based on session duration and space type"
- "Parking uses hourly rate until daily cap reached, then daily cap applies"
- "Monthly passes provide unlimited parking for fixed monthly fee"
- "Special rates apply based on time (night/weekend) or events"
- "Charging fees calculated as (kWh × rate) + session_fee + parking_fee + idle_fee"
- "Idle fees charged per minute after 10-minute grace period following charge completion"
- "Dynamic pricing disabled for MVP (March 2026) - Phase 2 feature after 3-6 months"
- "Surge multiplier triggers when occupancy exceeds 85% (Phase 2 only)"
- "Discounts applied before tax calculation"
- "Refunds processed only for cancellations >2 hours before reservation"
- "Split billing supported: separate parking and charging invoices"
- "Cross-facility subscription benefits apply to all EasyParkPlus locations"

---

## BC6: User & Access Management

### Core Terms

| Term | Definition | Type | Usage Example |
|------|------------|------|---------------|
| **User** | Person with account in system (driver, operator, or admin) | Aggregate Root | "User U-1234 has Premium subscription" |
| **User Profile** | Personal information and preferences | Entity | "Name, email, phone, preferred payment method" |
| **Credentials** | Authentication information (username/password or OAuth token) | Value Object | "Email: user@example.com, hashed password" |
| **User Role** | Permission level defining system access | Value Object | Roles: Driver, Operator, FacilityManager, SystemAdmin |
| **Driver** | User who parks vehicles | Role | "Drivers can make reservations and view invoices" |
| **Operator** | Staff member managing facility operations | Role | "Operators can override space allocation" |
| **Facility Manager** | User responsible for single or multiple facility operations | Role | "Manager can view analytics and adjust pricing" |
| **System Admin** | User with full system access | Role | "Admin can create facilities and manage users" |
| **Subscription Tier** | Service level with associated benefits | Value Object | Tiers: Basic (free), Premium ($19.99/mo), Fleet (custom pricing) |
| **Access Permission** | Specific system capability granted to role | Value Object | "permission:reservation.create" |
| **User Preferences** | Personalized settings | Value Object | "Preferred facility, notification settings, EV charging default" |
| **Multi-Factor Authentication (MFA)** | Additional security layer beyond password | Feature | "User enabled MFA via SMS" |
| **Fleet Account** | Business account managing multiple vehicles | Entity | "Acme Corp fleet has 50 vehicles" |

### Business Rules Language
- "All users must verify email before first reservation"
- "Drivers can only access their own sessions and invoices"
- "Operators can view all sessions at assigned facilities"
- "Facility Managers can modify pricing policies for their facilities"
- "System Admins have read/write access to all contexts"
- "Premium users get priority booking, 10% discount at Boston, 15% at Philadelphia"
- "Premium subscription provides cross-facility benefits at all locations"
- "Fleet accounts billed monthly with consolidated invoicing"
- "Failed login attempts >5 within 15 minutes trigger account lockout"

---

## BC7: Facility Operations & Maintenance

### Core Terms

| Term | Definition | Type | Usage Example |
|------|------------|------|---------------|
| **Maintenance Task** | Scheduled or reactive work on facility equipment | Aggregate Root | "Task M-456: Replace sensor S-401" |
| **Equipment Status** | Operational health state of facility equipment | Value Object | States: Operational, Degraded, Offline, UnderMaintenance |
| **Incident** | Event requiring attention (failure, safety issue, complaint) | Entity | "Incident I-789: Gate 2 stuck open" |
| **Work Order** | Formal request for maintenance work | Entity | "WO-234: Inspect charging station CS-101" |
| **Maintenance Schedule** | Planned preventive maintenance calendar | Entity | "Monthly sensor calibration on 1st of month" |
| **Technician** | Personnel performing maintenance work | Entity | "Technician T-12 assigned to WO-234" |
| **Equipment Type** | Category of facility equipment | Value Object | Types: EntryGate, ExitGate, IoTSensor, ChargingStation, Camera, PaymentKiosk |
| **Preventive Maintenance** | Scheduled maintenance to prevent failures | Type | "Quarterly charging station inspection" |
| **Corrective Maintenance** | Reactive repair of failed equipment | Type | "Emergency repair: Gate motor replacement" |
| **Mean Time Between Failures (MTBF)** | Reliability metric for equipment | Metric | "Sensor MTBF: 18 months" |
| **Escalate Incident** | Promote incident priority level | Command | "Incident escalated to critical: safety hazard" |
| **Complete Work Order** | Mark maintenance task as finished | Command | "WO-234 completed at 14:30" |

### Business Rules Language
- "Critical incidents (safety, security) must be addressed within 1 hour"
- "Preventive maintenance scheduled based on manufacturer recommendations"
- "Equipment in 'Offline' status automatically creates incident"
- "Work orders assigned to available technician with matching skill set"
- "Charging stations with >3 faults in 24 hours marked for replacement"
- "MVP provides basic monitoring only - advanced features in Phase 2"
- "Predictive maintenance and AI-driven alerts deferred to Phase 2 (post-launch)"
- "Spaces affected by maintenance automatically marked unavailable"

---

## BC8: Analytics & Reporting

### Core Terms

| Term | Definition | Type | Usage Example |
|------|------------|------|---------------|
| **Report** | Generated document containing metrics and insights | Aggregate Root | "Monthly Revenue Report for Dec 2025" |
| **Occupancy Metrics** | Statistical data about space utilization | Value Object | "Average occupancy: 78%, peak: 95% at 2PM" |
| **Revenue Metrics** | Financial performance data | Value Object | "Total revenue: $125,000 (Parking: $90K, Charging: $35K)" |
| **Charging Metrics** | EV charging utilization and performance | Value Object | "Total energy delivered: 12,500 kWh, 345 sessions" |
| **Peak Hours** | Time periods with highest utilization | Calculated Value | "Peak hours: Mon-Fri 9AM-11AM, 5PM-7PM" |
| **Facility Performance** | Comparative metrics across facilities | Entity | "Downtown facility: 85% occupancy, Airport: 92%" |
| **Forecast** | Predicted future metrics based on historical data | Entity | "Predicted Dec 25 occupancy: 45% (holiday reduced traffic)" |
| **Dashboard** | Real-time visualization of key metrics | Entity | "Operator dashboard shows live occupancy and revenue" |
| **KPI (Key Performance Indicator)** | Critical business metric | Value Object | "KPI: Maintain >80% occupancy, <2% equipment downtime" |
| **Utilization Rate** | Percentage of time/capacity used | Calculated Value | "Charging station utilization: 65%" |
| **Revenue Per Space** | Financial efficiency metric | Calculated Value | "Revenue per space: $250/month" |
| **Generate Report** | Create report based on date range and criteria | Command | "Generate revenue report for Q4 2025" |

### Business Rules Language
- "Occupancy calculated as (occupied_spaces / total_available_spaces) × 100"
- "Target occupancy: 70% average, 50% charger utilization for MVP success"
- "Reports generated at facility, multi-facility, or system-wide level"
- "Real-time dashboard updates every 30 seconds"
- "Forecasts use 6 months historical data minimum (Phase 2 after data collection)"
- "Peak hours identified when occupancy exceeds 85%"
- "Revenue metrics exclude refunds and cancellation fees"
- "Custom reports can include up to 24 months historical data"
- "Predictive models and ML-driven insights deferred to Phase 2"

---

## Shared Language Across All Contexts

### MVP Scope (March 2026)

| Term | Definition | Usage |
|------|------------|-------|
| **MVP Launch** | Initial product release with core features for 2 facilities | "MVP targets March 2026 with 5-month timeline" |
| **Phase 2** | Post-launch enhancements after 3-6 months of data collection | "Dynamic pricing, predictive maintenance in Phase 2" |
| **Boston Downtown** | First facility location in Boston, Massachusetts | "FAC-BOS-001" |
| **Philadelphia Center City** | Second facility location in Philadelphia, Pennsylvania | "FAC-PHI-001" |
| **Static Pricing** | Fixed rates without dynamic adjustments (MVP approach) | "All rates fixed until Phase 2" |
| **Single-Tenant Architecture** | System serves one organization (EasyParkPlus) with no multi-tenancy | "No TenantId required in aggregates" |

### Common Value Objects

| Term | Definition | Usage |
|------|------------|-------|
| **Money** | Monetary amount with currency | "$47.50 USD" |
| **DateTime** | ISO 8601 timestamp | "2025-10-23T14:30:00Z" |
| **Duration** | Time span | "2 hours 30 minutes" |
| **Location** | Geographic coordinates or address | "40.7128° N, 74.0060° W" |
| **Facility ID** | Unique facility identifier | "FAC-001" |
| **Email Address** | RFC 5322 compliant email | "user@example.com" |
| **Phone Number** | E.164 format phone | "+1-555-123-4567" |

### Domain Events (Cross-Context)

| Event | Description | Published By | Consumed By |
|-------|-------------|--------------|-------------|
| **SpaceOccupied** | Space changed to occupied status | Parking Space Mgmt | Analytics |
| **VehicleCheckedIn** | Vehicle entered facility | Vehicle Entry/Exit | Billing, Analytics |
| **VehicleCheckedOut** | Vehicle exited facility | Vehicle Entry/Exit | Billing, Parking Space Mgmt |
| **ReservationConfirmed** | Reservation successfully created | Reservation Mgmt | Parking Space Mgmt, User Mgmt |
| **ChargingStarted** | EV charging session began | EV Charging Mgmt | Billing, Analytics |
| **ChargingCompleted** | EV charging session finished | EV Charging Mgmt | Billing, Vehicle Entry/Exit |
| **PaymentCompleted** | Payment successfully processed | Billing & Pricing | User Mgmt, Analytics |
| **EquipmentFaulted** | Equipment failure detected | Operations & Maintenance | Parking Space Mgmt, EV Charging |

---

## Usage Guidelines

### For Developers
1. **Use exact terms in code**: Class names, method names, and variables should match this language
   - Example: `ParkingSession`, `checkIn()`, `spaceType`, NOT `ParkingRecord`, `enter()`, `type`
2. **Maintain consistency**: Use the same term throughout codebase
3. **Avoid technical jargon**: Prefer domain terms over implementation details
   - Example: Say "Reservation claimed" not "Reservation record status updated to active"

### For Domain Experts
1. **Challenge inconsistencies**: If code or discussion deviates from this language, raise it
2. **Evolve the language**: Suggest additions/changes as business understanding grows
3. **Use in requirements**: Write user stories and acceptance criteria using these terms

### For Stakeholders
1. **Reference in meetings**: Use this document to ensure shared understanding
2. **Test scenarios**: Write test cases using this language
3. **Business rules**: Express policies using these terms

---

**Status:** Ubiquitous Language refined with Technical Manager (Michael) input for MVP scope  
**Last Updated:** October 23, 2025  
**Next Step:** Hand off to Microservices Lead (Hesham) for service decomposition

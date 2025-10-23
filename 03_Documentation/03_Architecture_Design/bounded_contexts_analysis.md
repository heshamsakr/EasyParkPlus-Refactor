# EasyParkPlus: Bounded Contexts Analysis

**Domain-Driven Design Lead:** Mihai  
**Date:** October 23, 2025  
**Project:** EasyParkPlus Multi-Facility Parking & EV Charging Management System

---

## Executive Summary

This document identifies the bounded contexts for EasyParkPlus as it scales from a single-facility prototype to a **multi-facility parking management company with EV Charging Station Management capabilities**. The analysis follows **2025 DDD best practices** and is informed by current trends in smart parking systems and EV charging infrastructure.

---

## 1. Business Context

### Current State (Prototype)
- Single parking lot management
- Basic vehicle tracking (regular + electric vehicles)
- Manual slot allocation
- Simple GUI interface

### Target State (Production System)
- **Multiple parking facilities** across different locations
- **EV Charging Station Management** as a new business line
- Real-time occupancy tracking via IoT sensors
- Dynamic pricing and allocation
- Multi-tenant architecture (different facilities, different operators)
- Integration with payment systems and smart grid
- Mobile/web applications for users
- Analytics and reporting for operators

---

## 2. Core Domain Identification

### Core Domain (Strategic Competitive Advantage)
**Parking Space Allocation & Optimization**
- Real-time space availability
- Intelligent allocation algorithms
- Multi-facility coordination
- Dynamic pricing strategies

### Supporting Subdomains
**EV Charging Station Management** (New Business Activity)
- Charging session management
- Power distribution and load balancing
- Charging station health monitoring
- Integration with smart grid

### Generic Subdomains
- User authentication and authorization
- Payment processing
- Reporting and analytics
- Notifications

---

## 3. Bounded Contexts (2025 Architecture)

Based on **2025 DDD best practices** and research into modern parking/EV charging systems, I've identified **8 bounded contexts** for EasyParkPlus:

---

### BC1: Parking Space Management
**Responsibility:** Manages physical parking spaces, their types, availability, and real-time occupancy status across multiple facilities.

**Key Domain Concepts:**
- ParkingFacility (Aggregate Root)
- ParkingSpace (Entity)
- SpaceType (Value Object): Regular, Motorcycle, Disabled, EV-Ready
- Occupancy (Value Object): Vacant, Occupied, Reserved
- FloorLevel (Value Object)
- IoTSensor (Entity) - 2025: Real-time sensor integration

**Business Rules:**
- Each facility has configurable capacity
- Spaces can be dynamically allocated based on vehicle type
- Real-time occupancy tracking via IoT sensors
- Support for hierarchical facility organization (multi-floor, multi-zone)

**Integration Points:**
- → Vehicle Entry/Exit Management (space availability)
- → Reservation Management (reserved space allocation)
- → EV Charging Management (EV-enabled space coordination)

---

### BC2: Vehicle Entry/Exit Management
**Responsibility:** Handles vehicle check-in/check-out, tracks parking sessions, and associates vehicles with spaces.

**Key Domain Concepts:**
- ParkingSession (Aggregate Root)
- Vehicle (Entity)
- VehicleType (Value Object): Car, Motorcycle, ElectricCar, ElectricBike
- RegistrationNumber (Value Object)
- SessionStatus (Value Object): Active, Completed, Abandoned
- EntryTime, ExitTime (Value Object)

**Business Rules:**
- Each parking session has a start and end time
- Vehicle validation on entry
- Session duration calculation
- Support for different vehicle types with specific requirements
- Automatic session closure on exit

**Integration Points:**
- → Parking Space Management (space assignment)
- → Billing & Pricing (session duration for billing)
- → EV Charging Management (EV session coordination)

---

### BC3: Reservation Management
**Responsibility:** Allows users to reserve parking spaces in advance across multiple facilities.

**Key Domain Concepts:**
- Reservation (Aggregate Root)
- ReservationStatus (Value Object): Pending, Confirmed, Active, Completed, Cancelled
- TimeSlot (Value Object): StartTime, EndTime
- SpacePreference (Value Object): Near entrance, EV charging, disabled access
- ReservationPolicy (Entity)

**Business Rules:**
- Reservations can be made for future time slots
- Reservation expiration if not claimed within grace period
- Cancellation policies and refund rules
- Overbooking prevention
- Priority booking for premium users

**Integration Points:**
- → Parking Space Management (space availability check)
- → Vehicle Entry/Exit Management (reservation claim)
- → Billing & Pricing (reservation fees)
- → User Management (user reservations history)

---

### BC4: EV Charging Station Management ⚡ (NEW)
**Responsibility:** Manages electric vehicle charging stations, sessions, power distribution, and integration with smart grid (OCPP protocol - 2025 standard).

**Key Domain Concepts:**
- ChargingStation (Aggregate Root)
- ChargingPoint (Entity): Individual port/connector
- ChargingSession (Aggregate Root)
- PowerLevel (Value Object): Level 1, Level 2, DC Fast Charge
- ChargeStatus (Value Object): Available, Charging, Completed, Faulted
- EnergyDelivered (Value Object): kWh
- ChargingRate (Value Object): $/kWh
- LoadBalancing (Entity) - 2025: Dynamic power distribution
- OCPP Integration (Service) - 2025: Standard protocol

**Business Rules:**
- Each charging station has multiple charging points
- Real-time monitoring of charging status
- Dynamic load balancing across charging points
- Pricing based on time of day, power level, and demand (2025: Dynamic pricing)
- Integration with smart grid for optimal power usage
- Safety protocols and fault detection
- Charging session timeout policies
- Support for plug-and-charge (2025 standard)

**Integration Points:**
- → Parking Space Management (EV-enabled space coordination)
- → Vehicle Entry/Exit Management (EV session tracking)
- → Billing & Pricing (charging fees calculation)
- → Energy Management (power consumption tracking)

---

### BC5: Billing & Pricing Management
**Responsibility:** Calculates fees, processes payments, generates invoices, and manages pricing policies for both parking and charging services.

**Key Domain Concepts:**
- Invoice (Aggregate Root)
- ParkingFee (Entity)
- ChargingFee (Entity)
- PricingPolicy (Entity): Hourly, daily, monthly rates
- DynamicPricing (Entity) - 2025: Demand-based pricing
- PaymentTransaction (Entity)
- Discount (Value Object)
- TaxRate (Value Object)

**Business Rules:**
- Different pricing for different space types
- Time-based pricing (hourly, daily, monthly)
- Dynamic pricing based on demand (2025: AI-driven)
- Separate charging fees from parking fees
- Discount codes and promotions
- Tax calculation per jurisdiction
- Refund policies for cancellations

**Integration Points:**
- → Vehicle Entry/Exit Management (parking duration)
- → EV Charging Management (energy consumption)
- → Reservation Management (reservation fees)
- → Payment Processing (payment execution)
- → User Management (billing history)

---

### BC6: User & Access Management
**Responsibility:** Manages user accounts, authentication, authorization, and access control for drivers, operators, and administrators.

**Key Domain Concepts:**
- User (Aggregate Root)
- UserProfile (Entity)
- Credentials (Value Object)
- UserRole (Value Object): Driver, Operator, FacilityManager, SystemAdmin
- Subscription (Entity): Basic, Premium, Fleet
- AccessPermissions (Value Object)
- UserPreferences (Value Object)

**Business Rules:**
- Role-based access control (RBAC)
- Multi-facility access for operators
- User preferences for parking (location, EV charging, etc.)
- Subscription tiers with different benefits
- Privacy and GDPR compliance (2025: Enhanced security)
- Multi-factor authentication for sensitive operations

**Integration Points:**
- → Reservation Management (user reservations)
- → Billing & Pricing (user billing info)
- → Vehicle Entry/Exit Management (vehicle ownership)
- → All contexts (authentication/authorization)

---

### BC7: Facility Operations & Maintenance
**Responsibility:** Manages maintenance schedules, equipment health monitoring, incident tracking, and operational tasks for parking facilities and charging infrastructure.

**Key Domain Concepts:**
- MaintenanceTask (Aggregate Root)
- EquipmentStatus (Value Object): Operational, Degraded, Offline, UnderMaintenance
- Incident (Entity): Equipment failure, safety issue, user complaint
- MaintenanceSchedule (Entity)
- WorkOrder (Entity)
- Technician (Entity)
- EquipmentType (Value Object): Gate, Sensor, ChargingStation, Camera

**Business Rules:**
- Preventive maintenance scheduling
- Incident logging and tracking
- Equipment health monitoring (2025: Predictive maintenance via AI)
- Automated alerts for equipment failures
- Work order assignment and completion tracking
- Safety compliance checks

**Integration Points:**
- → Parking Space Management (space availability affected by maintenance)
- → EV Charging Management (charging station maintenance)
- → Analytics & Reporting (operational metrics)

---

### BC8: Analytics & Reporting
**Responsibility:** Provides business intelligence, operational metrics, revenue reports, and predictive analytics for decision-making.

**Key Domain Concepts:**
- Report (Aggregate Root)
- OccupancyMetrics (Value Object)
- RevenueMetrics (Value Object)
- ChargingMetrics (Value Object) - 2025: Energy consumption analytics
- PeakHoursAnalysis (Value Object)
- FacilityPerformance (Entity)
- Forecast (Entity) - 2025: AI-powered demand prediction
- Dashboard (Entity)

**Business Rules:**
- Real-time occupancy dashboard
- Revenue tracking per facility
- Charging station utilization metrics
- Peak hours identification
- Predictive analytics for demand forecasting (2025: ML models)
- Custom report generation
- KPI tracking for business goals

**Integration Points:**
- ← All contexts (data aggregation)
- → Facility operators and business stakeholders (reporting)

---

## 4. Bounded Context Relationships (Context Map)

### Partnership Patterns (Mutual Dependency)
- **Parking Space Management ↔ Vehicle Entry/Exit Management**: Close collaboration for real-time space allocation
- **Vehicle Entry/Exit Management ↔ EV Charging Management**: Coordinated EV session tracking

### Customer-Supplier Patterns
- **Parking Space Management → Reservation Management**: Supplies space availability
- **Vehicle Entry/Exit Management → Billing & Pricing**: Supplies session duration
- **EV Charging Management → Billing & Pricing**: Supplies energy consumption
- **User Management → All Contexts**: Supplies authentication/authorization

### Conformist Pattern
- **Billing & Pricing → Payment Processing**: Conforms to external payment gateway APIs
- **EV Charging Management → Smart Grid**: Conforms to OCPP protocol (2025 standard)

### Anti-Corruption Layer (ACL)
- **Analytics & Reporting**: ACL for aggregating data from all contexts with different models
- **Facility Operations**: ACL for integrating with legacy maintenance systems

### Shared Kernel (Minimal)
- Common domain primitives: Money, DateTime, Location
- Shared types should be minimal to maintain context autonomy

---

## 5. Context Prioritization for Implementation

### Phase 1 (MVP - Multi-Facility)
1. Parking Space Management
2. Vehicle Entry/Exit Management
3. User & Access Management
4. Billing & Pricing Management

### Phase 2 (EV Charging Addition)
5. EV Charging Station Management
6. Reservation Management

### Phase 3 (Operations Excellence)
7. Facility Operations & Maintenance
8. Analytics & Reporting

---

## 6. Key Insights & Decisions

### 2025 Technology Influences
1. **IoT Sensor Integration**: Real-time occupancy tracking is now standard
2. **OCPP Protocol**: Industry standard for EV charging communication
3. **Dynamic Pricing**: AI-driven demand-based pricing algorithms
4. **Predictive Maintenance**: ML models for equipment health monitoring
5. **Enhanced Security**: GDPR compliance, multi-factor auth, encrypted transactions
6. **Event-Driven Architecture**: Real-time data streaming (Kafka/Confluent) for scalability

### Why These Bounded Contexts?
1. **Business Alignment**: Each context maps to distinct business capabilities
2. **Team Autonomy**: Each context can be developed by independent teams
3. **Scalability**: Microservices can be scaled independently based on load
4. **Evolution**: New contexts (e.g., Autonomous Vehicle Support) can be added without disrupting existing ones
5. **Clear Boundaries**: Each context has well-defined responsibilities and minimal overlap

### What's Different from Single-Facility Prototype?
- **Multi-tenancy**: Support for multiple facilities with different operators
- **Reservation capability**: Not in prototype, critical for user experience
- **EV Charging as separate context**: Recognizes it as a distinct business domain
- **Operations context**: Maintenance and monitoring at scale
- **Analytics context**: Business intelligence for decision-making

---

## 7. Next Steps

1. ✅ Define ubiquitous language for each bounded context
2. ✅ Create domain models (entities, value objects, aggregates)
3. ✅ Draw bounded context diagram
4. ✅ Identify integration patterns and APIs
5. ✅ Document aggregate boundaries and consistency rules

---

**Status:** Bounded contexts identified and documented  
**Ready for:** Ubiquitous language definition and domain modeling

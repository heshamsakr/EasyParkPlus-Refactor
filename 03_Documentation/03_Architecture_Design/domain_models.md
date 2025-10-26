# EasyParkPlus: Domain Models (Refined with Michael's Input)

**Domain-Driven Design Lead:** Mihai  
**Date:** October 23, 2025 (Refined from Technical Manager input)  
**Project:** EasyParkPlus Multi-Facility Parking & EV Charging Management System  
**MVP Launch:** March 2026 (2 facilities: Boston Downtown, Philadelphia Center City)

---

## Purpose

This document defines the **domain models** for EasyParkPlus bounded contexts, including:
- **Entities**: Objects with unique identity that persist over time
- **Value Objects**: Immutable objects defined by their attributes
- **Aggregates**: Clusters of entities/value objects with consistency boundaries
- **Domain Services**: Operations that don't naturally belong to entities
- **Domain Events**: Significant occurrences in the domain

### Michael's Key Decisions Incorporated
✅ **Single-tenant architecture** (no TenantId)  
✅ **2 facilities at launch** (Boston Downtown, Philadelphia Center City)  
✅ **OCPP 2.0.1 mandatory**  
✅ **Cloud-native from day one**  
✅ **Cross-facility subscriptions**  
✅ **Pay-per-kWh + session fee + parking fee + idle fee** (EV charging)  
✅ **Hourly + daily cap + monthly passes** (parking)  
✅ **Static pricing in MVP** (dynamic pricing Phase 2 after 3-6 months)  
✅ **Smart grid features**: load balancing, peak shaving, demand response, energy metering

---

## BC1: Parking Space Management

### Aggregate: ParkingFacility

**Aggregate Root:** `ParkingFacility`

**Entities:**
- `ParkingFacility` (Root)
  - `facilityId: FacilityId` (Identity)
  - `name: String`
  - `city: City` (Boston, Philadelphia - MVP only)
  - `location: Location`
  - `floors: List<FloorLevel>`
  - `zones: List<Zone>`
  - `totalCapacity: Integer`
  - `operationalStatus: OperationalStatus`
  - `peakLoadCapacity: PowerCapacity` (350-400 kW for EV charging)
  
- `FloorLevel`
  - `floorId: FloorId`
  - `level: String` (e.g., "Ground", "Level 1", "Basement 1")
  - `spaces: List<ParkingSpace>`
  - `capacity: Integer`

- `Zone`
  - `zoneId: ZoneId`
  - `name: String` (e.g., "East Wing", "VIP Section")
  - `floorId: FloorId`
  - `spaces: List<ParkingSpace>`
  
- `ParkingSpace`
  - `spaceId: SpaceId` (Identity)
  - `spaceNumber: String` (e.g., "A-101")
  - `spaceType: SpaceType`
  - `occupancyStatus: OccupancyStatus`
  - `zoneId: ZoneId`
  - `floorId: FloorId`
  - `sensor: IoTSensor` (optional)
  - `lastUpdated: DateTime`

- `IoTSensor`
  - `sensorId: SensorId`
  - `spaceId: SpaceId`
  - `sensorType: String` (e.g., "Ultrasonic", "Camera-based")
  - `lastHeartbeat: DateTime`
  - `isOnline: Boolean`

**Value Objects:**
- `FacilityId`: UUID
- `SpaceId`: UUID
- `FloorId`: UUID
- `ZoneId`: UUID
- `SensorId`: UUID
- `City`: Enum { BOSTON_DOWNTOWN, PHILADELPHIA_CENTER_CITY } (MVP only)
- `Location`: { latitude: Decimal, longitude: Decimal, address: String }
- `SpaceType`: Enum { REGULAR, MOTORCYCLE, DISABLED, EV_READY, EV_CHARGING }
- `OccupancyStatus`: Enum { VACANT, OCCUPIED, RESERVED, MAINTENANCE }
- `OperationalStatus`: Enum { OPERATIONAL, PARTIAL, CLOSED, MAINTENANCE }
- `PowerCapacity`: Decimal (kW) - facility-level electrical capacity

**Domain Methods:**
- `ParkingFacility.allocateSpace(vehicleType: VehicleType, requiresCharging: Boolean): ParkingSpace`
- `ParkingFacility.releaseSpace(spaceId: SpaceId): void`
- `ParkingFacility.getAvailableSpaces(spaceType: SpaceType): List<ParkingSpace>`
- `ParkingFacility.reserveSpace(spaceId: SpaceId, reservationId: ReservationId): void`
- `ParkingFacility.markSpaceForMaintenance(spaceId: SpaceId): void`
- `ParkingSpace.occupy(): void`
- `ParkingSpace.vacate(): void`
- `ParkingSpace.canAccommodate(vehicleType: VehicleType): Boolean`

**Business Rules (Invariants):**
- A space can only be occupied by one vehicle at a time
- Reserved spaces cannot be allocated until reservation is released
- Maintenance spaces are excluded from availability
- Sensor-detected occupancy overrides manual status
- Total occupied spaces ≤ total capacity
- **Michael's Rule**: MVP operates 2 facilities only (Boston Downtown + Philadelphia Center City)
- **Michael's Rule**: Success metric = 70% average parking occupancy across both sites

**Domain Events:**
- `SpaceAllocated`: { spaceId, vehicleId, timestamp }
- `SpaceReleased`: { spaceId, timestamp }
- `SpaceOccupied`: { spaceId, timestamp }
- `SpaceVacated`: { spaceId, timestamp }
- `SpaceReserved`: { spaceId, reservationId, timestamp }
- `SensorStatusChanged`: { sensorId, isOnline, timestamp }

---

### Domain Service: SpaceAllocationService

**Responsibility:** Complex allocation logic based on proximity, vehicle type, and availability

**Operations:**
- `findOptimalSpace(facility: ParkingFacility, vehicleType: VehicleType, preferences: SpacePreference): ParkingSpace`
  - Algorithm: Prioritize spaces by type match, proximity to entrance/elevator, user preferences

---

## BC2: Vehicle Entry/Exit Management

### Aggregate: ParkingSession

**Aggregate Root:** `ParkingSession`

**Entities:**
- `ParkingSession` (Root)
  - `sessionId: SessionId` (Identity)
  - `vehicle: Vehicle`
  - `facilityId: FacilityId`
  - `spaceId: SpaceId`
  - `entryTime: DateTime`
  - `exitTime: DateTime` (nullable)
  - `status: SessionStatus`
  - `entryGateId: GateId`
  - `exitGateId: GateId` (nullable)
  - `userId: UserId` (optional)

- `Vehicle`
  - `vehicleId: VehicleId` (Identity)
  - `registrationNumber: RegistrationNumber`
  - `vehicleType: VehicleType`
  - `userId: UserId` (optional - for registered users)

- `EntryGate`
  - `gateId: GateId`
  - `facilityId: FacilityId`
  - `gateName: String`
  - `gateType: GateType`
  - `isOperational: Boolean`

**Value Objects:**
- `SessionId`: UUID
- `VehicleId`: UUID
- `GateId`: UUID
- `UserId`: UUID
- `RegistrationNumber`: String (validated format)
- `VehicleType`: Enum { CAR, MOTORCYCLE, ELECTRIC_CAR, ELECTRIC_MOTORCYCLE }
- `SessionStatus`: Enum { ACTIVE, COMPLETED, ABANDONED, DISPUTED }
- `GateType`: Enum { ENTRY, EXIT, BIDIRECTIONAL }
- `SessionDuration`: { hours: Integer, minutes: Integer }

**Domain Methods:**
- `ParkingSession.checkIn(vehicle: Vehicle, entryGate: EntryGate, space: ParkingSpace): ParkingSession`
- `ParkingSession.checkOut(exitGate: ExitGate): void`
- `ParkingSession.calculateDuration(): SessionDuration`
- `ParkingSession.markAbandoned(): void`
- `Vehicle.requiresEVSpace(): Boolean`

**Business Rules (Invariants):**
- Session must have entry time before exit time
- Vehicle cannot have multiple active sessions
- Electric vehicles must be assigned EV-ready or EV-charging spaces
- Session duration calculated from entry to exit
- Sessions without exit after 48 hours marked abandoned

**Domain Events:**
- `VehicleCheckedIn`: { sessionId, vehicleId, facilityId, spaceId, timestamp }
- `VehicleCheckedOut`: { sessionId, vehicleId, exitTime, duration }
- `SessionAbandoned`: { sessionId, vehicleId, abandonedAt }

---

## BC3: Reservation Management

### Aggregate: Reservation

**Aggregate Root:** `Reservation`

**Entities:**
- `Reservation` (Root)
  - `reservationId: ReservationId` (Identity)
  - `userId: UserId`
  - `facilityId: FacilityId`
  - `spaceId: SpaceId` (optional - assigned at confirmation)
  - `vehicle: Vehicle`
  - `timeSlot: TimeSlot`
  - `status: ReservationStatus`
  - `preferences: SpacePreference`
  - `createdAt: DateTime`
  - `confirmedAt: DateTime` (nullable)
  - `claimedAt: DateTime` (nullable)

**Value Objects:**
- `ReservationId`: UUID
- `TimeSlot`: { startTime: DateTime, endTime: DateTime, duration: Duration }
- `ReservationStatus`: Enum { PENDING, CONFIRMED, ACTIVE, COMPLETED, CANCELLED, EXPIRED }
- `SpacePreference`: { nearEntrance: Boolean, evCharging: Boolean, covered: Boolean, preferredZone: String }
- `GracePeriod`: Duration (default: 15 minutes)
- `CancellationPolicy`: { fullRefundBefore: Duration, partialRefundBefore: Duration }

**Domain Methods:**
- `Reservation.confirm(space: ParkingSpace): void`
- `Reservation.claim(session: ParkingSession): void`
- `Reservation.cancel(): void`
- `Reservation.markExpired(): void`
- `Reservation.isWithinGracePeriod(currentTime: DateTime): Boolean`
- `Reservation.calculateRefundAmount(cancellationTime: DateTime, originalFee: Money): Money`

**Business Rules (Invariants):**
- Reservation start time must be in the future at creation
- Cannot have overlapping reservations for same user
- Grace period starts at reservation start time
- Expired reservations release assigned space
- Cancellation refund based on time before start: >2hrs=100%, <2hrs=50%, <30min=0%

**Domain Events:**
- `ReservationCreated`: { reservationId, userId, facilityId, timeSlot }
- `ReservationConfirmed`: { reservationId, spaceId, timestamp }
- `ReservationClaimed`: { reservationId, sessionId, timestamp }
- `ReservationCancelled`: { reservationId, cancelledAt, refundAmount }
- `ReservationExpired`: { reservationId, expiredAt }
- `ReservationNoShow`: { reservationId, timestamp }

---

### Domain Service: ReservationScheduler

**Responsibility:** Prevent overbooking and manage reservation capacity

**Operations:**
- `checkAvailability(facility: ParkingFacility, timeSlot: TimeSlot, spaceType: SpaceType): Boolean`
- `findAvailableSlots(facility: ParkingFacility, date: Date, duration: Duration): List<TimeSlot>`

---

## BC4: EV Charging Station Management ⚡

### Aggregate: ChargingStation

**Aggregate Root:** `ChargingStation`

**Entities:**
- `ChargingStation` (Root)
  - `stationId: StationId` (Identity)
  - `facilityId: FacilityId`
  - `stationName: String`
  - `location: Location`
  - `chargingPoints: List<ChargingPoint>`
  - `maxPowerCapacity: PowerCapacity` (kW)
  - `currentPowerDraw: PowerCapacity` (real-time, for load balancing)
  - `operationalStatus: OperationalStatus`
  - `ocppProtocolVersion: String` (fixed at "2.0.1" per Michael)
  - `firmwareVersion: String`
  - `lastHeartbeat: DateTime`
  - `vendorId: String` (maintenance contractor reference)
  - `warrantyExpiration: Date`
  
- `ChargingPoint`
  - `pointId: PointId` (Identity)
  - `stationId: StationId`
  - `connectorType: ConnectorType`
  - `powerLevel: PowerLevel`
  - `maxPower: PowerCapacity` (15-20 kW per Michael)
  - `currentPower: PowerCapacity` (real-time metering)
  - `maxPowerAllocation: PowerCapacity` (dynamic, adjusted by load balancer)
  - `status: ChargeStatus`
  - `lastStatusUpdate: DateTime`

**Value Objects:**
- `StationId`: UUID
- `PointId`: UUID
- `ConnectorType`: Enum { TYPE1_J1772, TYPE2_MENNEKES, CCS_COMBO, CHADEMO, TESLA_PROPRIETARY }
- `PowerLevel`: Enum { LEVEL1_1_4KW, LEVEL2_7_22KW, DC_FAST_50_350KW }
- `PowerCapacity`: Decimal (kW)
- `ChargeStatus`: Enum { AVAILABLE, CHARGING, COMPLETED, FAULTED, OFFLINE, RESERVED }
- `OperationalStatus`: Enum { OPERATIONAL, DEGRADED, OFFLINE, MAINTENANCE }

**Domain Methods:**
- `ChargingStation.getAvailablePoints(): List<ChargingPoint>`
- `ChargingStation.reservePoint(pointId: PointId): void`
- `ChargingStation.getTotalPowerUsage(): PowerCapacity`
- `ChargingStation.updateFirmware(version: String): void`
- `ChargingStation.recordHeartbeat(timestamp: DateTime): void`
- `ChargingPoint.startCharging(): void`
- `ChargingPoint.stopCharging(): void`
- `ChargingPoint.reportFault(faultCode: String): void`
- `ChargingPoint.adjustPowerAllocation(newLimit: PowerCapacity): void` (for load balancing)

**Business Rules (Invariants):**
- Total power usage across all points ≤ station max capacity
- Each charging point can serve one vehicle at a time
- Faulted points automatically removed from available pool
- Points offline >5 minutes trigger maintenance alert
- **Michael's Rule**: OCPP 2.0.1 support is mandatory (vendor independence)
- **Michael's Rule**: Peak load = 350-400 kW per facility (20-25 chargers @ 15-20 kW each)
- **Michael's Rule**: EasyParkPlus owns infrastructure, vendor handles maintenance
- **Michael's Rule**: Load balancing prevents facility from exceeding 400 kW peak
- **Michael's Rule**: Success metric = 50% charger usage during operating hours

**Domain Events:**
- `ChargingPointAvailable`: { pointId, stationId, timestamp }
- `ChargingPointReserved`: { pointId, reservationId, timestamp }
- `ChargingPointFaulted`: { pointId, faultCode, timestamp }
- `StationPowerCapacityExceeded`: { stationId, currentPower, maxPower }
- `StationHeartbeatReceived`: { stationId, timestamp, firmwareVersion } (OCPP 2.0.1)
- `LoadBalancingAdjusted`: { stationId, pointsAffected, newAllocations } (smart grid)
- `PeakShavingActivated`: { facilityId, reducedLoadBy, timestamp } (smart grid)
- `DemandResponseReceived`: { facilityId, utilitySignal, timestamp } (smart grid)

---

### Aggregate: ChargingSession

**Aggregate Root:** `ChargingSession`

**Entities:**
- `ChargingSession` (Root)
  - `chargingSessionId: ChargingSessionId` (Identity)
  - `pointId: PointId`
  - `stationId: StationId`
  - `parkingSessionId: SessionId` (link to parking)
  - `vehicleId: VehicleId`
  - `userId: UserId`
  - `startTime: DateTime`
  - `endTime: DateTime` (nullable)
  - `chargingCompletedAt: DateTime` (nullable - when battery full/target reached)
  - `sessionEndedAt: DateTime` (nullable - when driver disconnects)
  - `initialSoC: StateOfCharge` (optional)
  - `targetSoC: StateOfCharge` (optional)
  - `currentSoC: StateOfCharge` (optional)
  - `energyDelivered: EnergyAmount` (kWh - metered per Michael)
  - `sessionFee: Money` (flat fee per Michael)
  - `parkingFee: Money` (if parked while charging per Michael)
  - `idleTime: Duration` (sessionEndedAt - chargingCompletedAt)
  - `idleFee: Money` (penalty for overstay per Michael)
  - `status: ChargingSessionStatus`
  - `authenticationMethod: AuthMethod`

**Value Objects:**
- `ChargingSessionId`: UUID
- `StateOfCharge`: Integer (0-100 %)
- `EnergyAmount`: Decimal (kWh)
- `ChargingSessionStatus`: Enum { INITIATED, CHARGING, COMPLETED, STOPPED_BY_USER, STOPPED_BY_SYSTEM, FAULTED }
- `AuthMethod`: Enum { RFID, MOBILE_APP, PLUG_AND_CHARGE, CREDIT_CARD }
- `ChargingDuration`: { hours: Integer, minutes: Integer }

**Domain Methods:**
- `ChargingSession.start(): void`
- `ChargingSession.stop(): void`
- `ChargingSession.updateEnergyDelivered(amount: EnergyAmount): void`
- `ChargingSession.updateSoC(currentSoC: StateOfCharge): void`
- `ChargingSession.hasReachedTarget(): Boolean`
- `ChargingSession.calculateDuration(): ChargingDuration`
- `ChargingSession.calculateIdleTime(): Duration`
- `ChargingSession.calculateIdleFee(idleFeeRate: Money): Money`
- `ChargingSession.calculateTotalFee(kWhRate: Money, sessionFee: Money, parkingFee: Money, idleFeeRate: Money): Money`

**Business Rules (Invariants):**
- Session must start before it ends
- Energy delivered ≥ 0
- SoC values between 0-100%
- Session auto-stops when target SoC reached
- Idle fee applies 10 minutes after charging completed
- DC Fast sessions timeout after 1 hour, Level 2 after 4 hours
- **Michael's Rule**: Billing = kWh consumed + session fee + parking fee (if applicable) + idle fee (if overstayed)
- **Michael's Rule**: Idle fee applies if driver stays after charging complete (chargingCompletedAt < sessionEndedAt)
- **Michael's Rule**: Payment methods = App, card terminal at exit, or subscription (auto-pay)

**Domain Events:**
- `ChargingStarted`: { chargingSessionId, pointId, vehicleId, startTime }
- `ChargingInProgress`: { chargingSessionId, energyDelivered, currentSoC, timestamp }
- `ChargingCompleted`: { chargingSessionId, totalEnergy, duration, endTime }
- `ChargingStopped`: { chargingSessionId, reason, timestamp }
- `ChargingFaulted`: { chargingSessionId, faultReason, timestamp }
- `IdleFeeApplied`: { chargingSessionId, feeAmount, timestamp }

---

### Domain Service: LoadBalancingService

**Responsibility:** Distribute power across charging points to prevent grid overload (Michael's smart grid requirement)

**Operations:**
- `balancePower(facility: ParkingFacility): void`
  - Algorithm: When total power >80% capacity (320 kW of 400 kW), reduce power to active sessions proportionally
- `calculateOptimalPowerDistribution(activeSessions: List<ChargingSession>, maxFacilityLoad: PowerCapacity): Map<PointId, PowerCapacity>`
- `peakShaving(facility: ParkingFacility, gridPeakHours: TimeRange): void`
  - Limit demand during utility peak hours to reduce costs
- `handleDemandResponse(facility: ParkingFacility, utilitySignal: DemandResponseSignal): void`
  - Respond to utility requests to reduce load temporarily

---

### Domain Service: OCPPIntegrationService

**Responsibility:** Handle communication with charging stations via OCPP 2.0.1 protocol (Michael's requirement)

**Operations:**
- `sendStartTransaction(pointId: PointId, userId: UserId): TransactionId`
- `sendStopTransaction(transactionId: TransactionId): void`
- `receiveMeterValues(pointId: PointId, energy: EnergyAmount, soc: StateOfCharge): void`
- `receiveStatusNotification(pointId: PointId, status: ChargeStatus): void`
- `sendFirmwareUpdate(stationId: StationId, firmwareUrl: URL): void` (OCPP 2.0.1 feature)
- `receiveHeartbeat(stationId: StationId, timestamp: DateTime): void` (OCPP 2.0.1 feature)

---

## BC5: Billing & Pricing Management

### Aggregate: Invoice

**Aggregate Root:** `Invoice`

**Entities:**
- `Invoice` (Root)
  - `invoiceId: InvoiceId` (Identity)
  - `userId: UserId`
  - `facilityId: FacilityId`
  - `sessionId: SessionId` (parking session)
  - `chargingSessionId: ChargingSessionId` (optional)
  - `lineItems: List<LineItem>`
  - `subtotal: Money`
  - `taxAmount: Money`
  - `totalAmount: Money`
  - `status: InvoiceStatus`
  - `createdAt: DateTime`
  - `dueAt: DateTime`
  - `paidAt: DateTime` (nullable)

- `LineItem`
  - `lineItemId: LineItemId`
  - `description: String`
  - `itemType: LineItemType`
  - `quantity: Decimal`
  - `unitPrice: Money`
  - `totalPrice: Money`

- `PaymentTransaction`
  - `transactionId: TransactionId` (Identity)
  - `invoiceId: InvoiceId`
  - `amount: Money`
  - `paymentMethod: PaymentMethod`
  - `status: TransactionStatus`
  - `processedAt: DateTime`
  - `gatewayReference: String`

**Value Objects:**
- `InvoiceId`: UUID
- `LineItemId`: UUID
- `TransactionId`: UUID
- `Money`: { amount: Decimal, currency: String }
- `InvoiceStatus`: Enum { DRAFT, ISSUED, PAID, PARTIALLY_PAID, OVERDUE, CANCELLED, REFUNDED }
- `LineItemType`: Enum { PARKING_HOURLY, PARKING_DAILY_CAP, PARKING_MONTHLY_PASS, CHARGING_ENERGY, CHARGING_SESSION_FEE, CHARGING_IDLE_FEE, RESERVATION_FEE, DISCOUNT, TAX }
- `PaymentMethod`: Enum { CREDIT_CARD, DEBIT_CARD, MOBILE_WALLET, FLEET_ACCOUNT, SUBSCRIPTION_AUTO_PAY }
- `TransactionStatus`: Enum { PENDING, AUTHORIZED, COMPLETED, FAILED, REFUNDED }
- `TaxRate`: Decimal (percentage)

**Domain Methods:**
- `Invoice.addLineItem(item: LineItem): void`
- `Invoice.applyDiscount(discount: Discount): void`
- `Invoice.calculateTotal(): Money`
- `Invoice.markPaid(transaction: PaymentTransaction): void`
- `Invoice.refund(amount: Money, reason: String): void`

**Business Rules (Invariants):**
- Subtotal = sum of all line items (excluding tax)
- Total amount = subtotal + tax amount
- Tax calculated on subtotal after discounts
- Invoice must be issued before payment
- Refunds ≤ paid amount
- **Michael's Rule**: Parking invoice line items = hourly rate × hours (up to daily cap)
- **Michael's Rule**: Charging invoice line items = (kWh × rate) + session fee + parking fee (if applicable) + idle fee (if overstayed)
- **Michael's Rule**: Payment methods = App, card terminal, subscription auto-pay

**Domain Events:**
- `InvoiceCreated`: { invoiceId, userId, totalAmount, timestamp }
- `InvoiceIssued`: { invoiceId, dueAt, timestamp }
- `InvoicePaid`: { invoiceId, transactionId, paidAt }
- `PaymentFailed`: { invoiceId, transactionId, reason }
- `RefundIssued`: { invoiceId, refundAmount, reason }

---

### Aggregate: PricingPolicy

**Aggregate Root:** `PricingPolicy`

**Entities:**
- `PricingPolicy` (Root)
  - `policyId: PolicyId` (Identity)
  - `facilityId: FacilityId`
  - `policyName: String`
  - `effectiveFrom: DateTime`
  - `effectiveTo: DateTime` (nullable)
  - `parkingRates: List<ParkingRate>`
  - `chargingRates: List<ChargingRate>`
  - `dynamicPricingEnabled: Boolean` (FALSE for MVP per Michael)
  - `dynamicPricingActivationDate: Date` (nullable - 3-6 months after launch per Michael)

- `ParkingRate`
  - `rateId: RateId`
  - `spaceType: SpaceType`
  - `rateType: RateType` (hourly, daily, monthly per Michael)
  - `hourlyRate: Money` (base rate per hour per Michael)
  - `dailyCap: Money` (maximum daily rate per Michael)
  - `hoursUntilDailyCap: Integer` (e.g., 8 hours)
  - `monthlyPassRate: Money` (discounted flat rate for regulars per Michael)
  - `specialRates: List<SpecialRate>` (nights, weekends, events per Michael)
  - `timeOfDayMultipliers: Map<TimeRange, Decimal>` (for future dynamic pricing)

- `ChargingRate`
  - `rateId: RateId`
  - `powerLevel: PowerLevel`
  - `baseRate: Money` (per kWh per Michael)
  - `sessionFee: Money` (flat fee per session per Michael)
  - `idleFeeRate: Money` (per minute after charging complete per Michael)
  - `timeOfDayMultipliers: Map<TimeRange, Decimal>` (for future dynamic pricing)
  
- `SpecialRate`
  - `specialRateId: RateId`
  - `name: String` (e.g., "Weekend Rate", "Night Parking")
  - `applicableHours: TimeRange`
  - `applicableDays: List<DayOfWeek>`
  - `rateMultiplier: Decimal` (e.g., 0.5 = 50% discount)

**Value Objects:**
- `PolicyId`: UUID
- `RateId`: UUID
- `RateType`: Enum { HOURLY, DAILY_CAP, MONTHLY_PASS, SPECIAL }
- `TimeRange`: { startHour: Integer, endHour: Integer }
- `SurgeMultiplier`: Decimal (1.0 = no surge, 1.5 = 50% increase - Phase 2 only)
- `DayOfWeek`: Enum { MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY }

**Domain Methods:**
- `PricingPolicy.calculateParkingFee(session: ParkingSession): Money`
  - Apply hourly rate up to daily cap
- `PricingPolicy.calculateChargingFee(chargingSession: ChargingSession): Money`
  - Calculate (kWh × rate) + session fee + idle fee
- `PricingPolicy.applySpecialRate(timestamp: DateTime, baseRate: Money): Money`
- `PricingPolicy.applyDynamicPricing(occupancyRate: Decimal): Decimal` (Phase 2 only)
- `PricingPolicy.activateDynamicPricing(activationDate: Date): void` (Phase 2 only)

**Business Rules (Invariants):**
- Only one active policy per facility at any time
- Base rates must be > 0
- Dynamic pricing triggers when occupancy >85% (Phase 2 only)
- Maximum daily parking fee capped at configured limit
- **Michael's Rule (MVP)**: Baseline parking = hourly with daily cap + monthly passes
- **Michael's Rule (MVP)**: Baseline charging = pay-per-kWh + session fee + idle fee
- **Michael's Rule (MVP)**: Dynamic pricing DISABLED at launch
- **Michael's Rule (Phase 2)**: Activate dynamic pricing after 3-6 months of usage data collection
- **Michael's Rule**: Special rates apply for nights, weekends, events (city-specific)
- **Michael's Rule**: Idle fee applies if driver overstays after charging complete

**Domain Events:**
- `PricingPolicyActivated`: { policyId, facilityId, effectiveFrom }
- `PricingPolicyDeactivated`: { policyId, effectiveTo }
- `DynamicPricingActivated`: { facilityId, activationDate } (Phase 2)
- `DynamicPricingTriggered`: { facilityId, surgeMultiplier, occupancyRate } (Phase 2)
- `SpecialRateApplied`: { facilityId, specialRateName, timestamp }

---

### Domain Service: FeeCalculationService

**Responsibility:** Complex fee calculations considering duration, time-of-day, discounts, daily caps

**Operations:**
- `calculateParkingFee(session: ParkingSession, policy: PricingPolicy): Money`
  - Apply hourly rate × hours, cap at daily maximum per Michael
- `calculateChargingFee(chargingSession: ChargingSession, policy: PricingPolicy): Money`
  - Calculate (kWh × kWhRate) + sessionFee + parkingFee + idleFee per Michael
- `applyDiscounts(amount: Money, discounts: List<Discount>): Money`
- `applySubscriptionBenefits(amount: Money, subscription: Subscription): Money`
  - Apply discounted rates for subscribers per Michael

---

## BC6: User & Access Management

### Aggregate: User

**Aggregate Root:** `User`

**Entities:**
- `User` (Root)
  - `userId: UserId` (Identity)
  - `profile: UserProfile`
  - `credentials: Credentials`
  - `role: UserRole`
  - `subscription: Subscription` (optional)
  - `preferences: UserPreferences`
  - `vehicles: List<Vehicle>`
  - `paymentMethods: List<PaymentMethod>`
  - `createdAt: DateTime`
  - `lastLoginAt: DateTime`
  - `accountStatus: AccountStatus`

- `UserProfile`
  - `firstName: String`
  - `lastName: String`
  - `email: EmailAddress`
  - `phone: PhoneNumber`
  - `address: Address` (optional)

- `Subscription`
  - `subscriptionId: SubscriptionId`
  - `tier: SubscriptionTier`
  - `startDate: DateTime`
  - `renewalDate: DateTime`
  - `autoRenew: Boolean`
  - `benefits: List<Benefit>`
  - `crossFacilityEnabled: Boolean` (TRUE per Michael - works across all facilities)
  - `facilitySpecificBenefits: Map<FacilityId, FacilityBenefit>` (varying discounts per Michael)
  - `discountedKwhRate: Money` (for monthly EV charging subscribers per Michael)
  - `reservedChargingSlots: Integer` (for peak hours per Michael)

**Value Objects:**
- `UserId`: UUID
- `SubscriptionId`: UUID
- `Credentials`: { username: String, passwordHash: String, salt: String, mfaEnabled: Boolean }
- `UserRole`: Enum { DRIVER, OPERATOR, FACILITY_MANAGER, SYSTEM_ADMIN }
- `SubscriptionTier`: Enum { BASIC, PREMIUM_PARKING, PREMIUM_EV_CHARGING, FLEET }
- `AccountStatus`: Enum { ACTIVE, SUSPENDED, LOCKED, CLOSED }
- `EmailAddress`: String (validated RFC 5322)
- `PhoneNumber`: String (E.164 format)
- `Address`: { street: String, city: String, state: String, zipCode: String, country: String }
- `UserPreferences`: { preferredFacility: FacilityId, notificationsEnabled: Boolean, evChargingDefault: Boolean }
- `Benefit`: { benefitType: String, description: String, value: String }
- `FacilityBenefit`: { facilityId: FacilityId, discountPercentage: Decimal, priorityAccess: Boolean } (per Michael - varying benefits)

**Domain Methods:**
- `User.authenticate(password: String): Boolean`
- `User.updateProfile(profile: UserProfile): void`
- `User.addVehicle(vehicle: Vehicle): void`
- `User.removeVehicle(vehicleId: VehicleId): void`
- `User.subscribe(tier: SubscriptionTier): Subscription`
- `User.cancelSubscription(): void`
- `User.hasPermission(permission: Permission): Boolean`

**Business Rules (Invariants):**
- Email must be unique across system
- Active users must have verified email
- Premium/Fleet subscriptions require payment method
- Failed login >5 times in 15 minutes = account locked
- Subscription benefits apply based on tier
- **Michael's Rule**: Subscriptions work across all EasyParkPlus facilities (cross-facility benefits)
- **Michael's Rule**: Facility-specific benefits may vary (e.g., 10% in Boston, 15% in Philly)
- **Michael's Rule**: EV charging subscriptions provide discounted kWh rates + reserved slots during peak hours
- **Michael's Rule**: Monthly subscriptions require payment method on file

**Domain Events:**
- `UserRegistered`: { userId, email, timestamp }
- `UserAuthenticated`: { userId, timestamp, ipAddress }
- `SubscriptionActivated`: { userId, subscriptionId, tier }
- `SubscriptionCancelled`: { userId, subscriptionId, timestamp }
- `AccountLocked`: { userId, reason, timestamp }
- `VehicleAdded`: { userId, vehicleId, registrationNumber }

---

### Domain Service: AuthenticationService

**Responsibility:** Handle authentication logic including MFA

**Operations:**
- `authenticate(username: String, password: String): AuthResult`
- `validateMFA(userId: UserId, mfaCode: String): Boolean`
- `generateMFACode(userId: UserId): String`
- `checkAccountLockout(userId: UserId): Boolean`

---

### Domain Service: AuthorizationService

**Responsibility:** Role-based access control

**Operations:**
- `hasPermission(userId: UserId, permission: Permission): Boolean`
- `getFacilityAccess(userId: UserId): List<FacilityId>`
- `canAccessContext(userId: UserId, context: BoundedContext): Boolean`

---

## BC7: Facility Operations & Maintenance

### Aggregate: MaintenanceTask

**Aggregate Root:** `MaintenanceTask`

**Entities:**
- `MaintenanceTask` (Root)
  - `taskId: TaskId` (Identity)
  - `facilityId: FacilityId`
  - `equipmentId: EquipmentId`
  - `taskType: MaintenanceType`
  - `priority: Priority`
  - `status: TaskStatus`
  - `description: String`
  - `scheduledFor: DateTime`
  - `completedAt: DateTime` (nullable)
  - `assignedTechnician: TechnicianId` (nullable)
  - `workOrder: WorkOrder` (nullable)

- `WorkOrder`
  - `workOrderId: WorkOrderId` (Identity)
  - `taskId: TaskId`
  - `createdAt: DateTime`
  - `estimatedDuration: Duration`
  - `actualDuration: Duration` (nullable)
  - `partsUsed: List<Part>`
  - `notes: String`

**Value Objects:**
- `TaskId`: UUID
- `WorkOrderId`: UUID
- `EquipmentId`: UUID
- `TechnicianId`: UUID
- `MaintenanceType`: Enum { PREVENTIVE, CORRECTIVE, INSPECTION, EMERGENCY }
- `Priority`: Enum { LOW, MEDIUM, HIGH, CRITICAL }
- `TaskStatus`: Enum { SCHEDULED, IN_PROGRESS, COMPLETED, CANCELLED, DEFERRED }
- `Part`: { partNumber: String, description: String, quantity: Integer }

**Domain Methods:**
- `MaintenanceTask.assign(technician: TechnicianId): void`
- `MaintenanceTask.start(): void`
- `MaintenanceTask.complete(workOrder: WorkOrder): void`
- `MaintenanceTask.escalate(): void`
- `MaintenanceTask.isOverdue(currentTime: DateTime): Boolean`

**Business Rules (Invariants):**
- Critical tasks must be assigned within 1 hour
- Emergency tasks require immediate escalation
- Completed tasks must have work order
- Preventive maintenance scheduled per manufacturer specs

**Domain Events:**
- `MaintenanceScheduled`: { taskId, equipmentId, scheduledFor }
- `MaintenanceStarted`: { taskId, technicianId, startedAt }
- `MaintenanceCompleted`: { taskId, completedAt, duration }
- `MaintenanceEscalated`: { taskId, priority, reason }

---

### Aggregate: Incident

**Aggregate Root:** `Incident`

**Entities:**
- `Incident` (Root)
  - `incidentId: IncidentId` (Identity)
  - `facilityId: FacilityId`
  - `equipmentId: EquipmentId` (optional)
  - `incidentType: IncidentType`
  - `severity: Severity`
  - `status: IncidentStatus`
  - `description: String`
  - `reportedBy: UserId`
  - `reportedAt: DateTime`
  - `resolvedAt: DateTime` (nullable)
  - `resolution: String` (nullable)

**Value Objects:**
- `IncidentId`: UUID
- `IncidentType`: Enum { EQUIPMENT_FAILURE, SAFETY_ISSUE, SECURITY_BREACH, USER_COMPLAINT }
- `Severity`: Enum { LOW, MEDIUM, HIGH, CRITICAL }
- `IncidentStatus`: Enum { REPORTED, ACKNOWLEDGED, IN_PROGRESS, RESOLVED, CLOSED }

**Domain Methods:**
- `Incident.acknowledge(): void`
- `Incident.resolve(resolution: String): void`
- `Incident.close(): void`
- `Incident.escalate(): void`

**Business Rules (Invariants):**
- Critical incidents must be acknowledged within 15 minutes
- Safety incidents trigger automatic facility notification
- Incidents create maintenance tasks automatically for equipment failures

**Domain Events:**
- `IncidentReported`: { incidentId, facilityId, severity, timestamp }
- `IncidentAcknowledged`: { incidentId, acknowledgedBy, timestamp }
- `IncidentResolved`: { incidentId, resolution, resolvedAt }
- `IncidentEscalated`: { incidentId, severity, reason }

---

### Aggregate: Equipment

**Aggregate Root:** `Equipment`

**Entities:**
- `Equipment` (Root)
  - `equipmentId: EquipmentId` (Identity)
  - `facilityId: FacilityId`
  - `equipmentType: EquipmentType`
  - `manufacturer: String`
  - `model: String`
  - `serialNumber: String`
  - `installDate: DateTime`
  - `status: EquipmentStatus`
  - `lastMaintenanceDate: DateTime`
  - `nextMaintenanceDate: DateTime`
  - `healthScore: HealthScore` (0-100)
  - `vendorId: String` (maintenance contractor - per Michael, vendor handles maintenance)
  - `warrantyExpiration: Date`

**Value Objects:**
- `EquipmentType`: Enum { ENTRY_GATE, EXIT_GATE, IOT_SENSOR, CHARGING_STATION, CAMERA, PAYMENT_KIOSK }
- `EquipmentStatus`: Enum { OPERATIONAL, DEGRADED, OFFLINE, UNDER_MAINTENANCE }
- `HealthScore`: Integer (0-100, calculated via predictive maintenance AI)

**Domain Methods:**
- `Equipment.updateStatus(status: EquipmentStatus): void`
- `Equipment.recordMaintenance(date: DateTime): void`
- `Equipment.calculateNextMaintenance(): DateTime`
- `Equipment.predictFailure(): FailurePrediction`

**Business Rules (Invariants):**
- Equipment offline >5 minutes triggers incident
- Health score <30 triggers preventive maintenance
- Predictive maintenance alerts 7 days before predicted failure
- **Michael's Rule**: EasyParkPlus owns charging infrastructure, vendor handles maintenance under SLA
- **Michael's Rule**: Vendor responsible for installation, upkeep, warranty claims

**Domain Events:**
- `EquipmentStatusChanged`: { equipmentId, oldStatus, newStatus, timestamp }
- `EquipmentOffline`: { equipmentId, offlineSince }
- `MaintenanceDue`: { equipmentId, dueDate }
- `FailurePredicted`: { equipmentId, predictedDate, confidence }

---

## BC8: Analytics & Reporting

### Aggregate: Report

**Aggregate Root:** `Report`

**Entities:**
- `Report` (Root)
  - `reportId: ReportId` (Identity)
  - `reportName: String`
  - `reportType: ReportType`
  - `facilityId: FacilityId` (nullable - null = system-wide)
  - `dateRange: DateRange`
  - `parameters: ReportParameters`
  - `generatedBy: UserId`
  - `generatedAt: DateTime`
  - `dataSnapshot: ReportData`
  - `format: ReportFormat`

**Value Objects:**
- `ReportId`: UUID
- `ReportType`: Enum { OCCUPANCY, REVENUE, CHARGING_UTILIZATION, FACILITY_PERFORMANCE, CUSTOM }
- `DateRange`: { startDate: Date, endDate: Date }
- `ReportParameters`: Map<String, String> (flexible key-value)
- `ReportFormat`: Enum { PDF, CSV, JSON, EXCEL }
- `ReportData`: { metrics: Map<String, Any>, charts: List<ChartData> }

**Domain Methods:**
- `Report.generate(): ReportData`
- `Report.export(format: ReportFormat): Bytes`

**Domain Events:**
- `ReportGenerated`: { reportId, reportType, generatedAt }

---

### Value Objects (Analytics Metrics)

**OccupancyMetrics:**
- `averageOccupancy: Decimal` (percentage)
- `peakOccupancy: Decimal`
- `peakTime: DateTime`
- `occupancyBySpaceType: Map<SpaceType, Decimal>`
- `targetOccupancyRate: Decimal` (70% per Michael - success metric)

**RevenueMetrics:**
- `totalRevenue: Money`
- `parkingRevenue: Money`
- `chargingRevenue: Money`
- `averageRevenuePerSession: Money`
- `revenueByFacility: Map<FacilityId, Money>`

**ChargingMetrics:**
- `totalEnergyDelivered: EnergyAmount` (kWh)
- `totalChargingSessions: Integer`
- `averageSessionDuration: Duration`
- `utilizationRate: Decimal` (percentage)
- `revenuePerKWh: Money`
- `targetUtilizationRate: Decimal` (50% per Michael - success metric during operating hours)

**FacilityPerformance:**
- `facilityId: FacilityId`
- `occupancyRate: Decimal`
- `revenue: Money`
- `averageSessionDuration: Duration`
- `equipmentUptime: Decimal` (percentage)

**Forecast:**
- `forecastType: String` (e.g., "occupancy", "revenue")
- `predictedValue: Decimal`
- `confidenceInterval: Range`
- `forecastDate: Date`
- `modelAccuracy: Decimal`

---

### Domain Service: MetricsAggregationService

**Responsibility:** Collect and aggregate data from all contexts for reporting

**Operations:**
- `aggregateOccupancyData(facilityId: FacilityId, dateRange: DateRange): OccupancyMetrics`
- `aggregateRevenueData(facilityId: FacilityId, dateRange: DateRange): RevenueMetrics`
- `aggregateChargingData(facilityId: FacilityId, dateRange: DateRange): ChargingMetrics`

---

### Domain Service: ForecastingService

**Responsibility:** Predictive analytics using ML models (data collection starts at MVP for Phase 2)

**Operations:**
- `forecastOccupancy(facilityId: FacilityId, forecastDate: Date): Forecast`
- `forecastRevenue(facilityId: FacilityId, period: Period): Forecast`
- `identifyPeakHours(facilityId: FacilityId, historicalData: TimeSeriesData): List<TimeRange>`
- `collectDataForDynamicPricing(facilityId: FacilityId): void` (for 3-6 months per Michael before activating dynamic pricing)

---

## Summary

### Michael's Architectural Decisions Impact

**MVP Simplifications**:
- ❌ Removed `TenantId` from all aggregates (single-tenant architecture)
- ✅ Added `City` enum (Boston Downtown, Philadelphia Center City only)
- ✅ Added `PowerCapacity` tracking at facility level (350-400 kW)
- ✅ Disabled dynamic pricing in MVP (Phase 2 activation after 3-6 months)

**EV Charging Enhancements**:
- ✅ OCPP 2.0.1 mandatory (firmwareVersion, lastHeartbeat tracking)
- ✅ Smart grid features (load balancing, peak shaving, demand response)
- ✅ Per-charger power metering (15-20 kW average)
- ✅ Idle fee tracking (overstay penalty)
- ✅ Multi-component billing (kWh + session fee + parking fee + idle fee)

**Pricing Model Clarity**:
- ✅ Parking: hourly + daily cap + monthly passes + special rates
- ✅ Charging: pay-per-kWh + session fee + idle fee
- ✅ Subscriptions: cross-facility benefits + discounted kWh + reserved slots

**Operational Requirements**:
- ✅ Cloud-native architecture from day one
- ✅ Real-time monitoring and remote management
- ✅ 70% parking occupancy target (success metric)
- ✅ 50% charger utilization target (success metric)
- ✅ Vendor-managed maintenance (SLA-based)

### Entity vs Value Object Guidelines
- **Entity**: Has identity, lifecycle, can change over time (e.g., ParkingSession, Vehicle)
- **Value Object**: Immutable, defined by attributes, interchangeable (e.g., Money, SpaceType)

### Aggregate Design Principles
1. **Consistency Boundary**: Aggregates enforce business invariants
2. **Transactional Boundary**: Changes to aggregate = single transaction
3. **Small Aggregates**: Prefer smaller aggregates for scalability
4. **Reference by ID**: Aggregates reference other aggregates by ID, not object reference

### Domain Services Usage
- Operations that don't naturally fit on an entity
- Stateless operations across multiple aggregates
- Complex calculations or algorithms

### Domain Events Benefits
- **Decoupling**: Bounded contexts communicate via events
- **Audit Trail**: Event log provides history
- **Event Sourcing**: Optional - rebuild state from events
- **Integration**: Events trigger workflows in other contexts

---

**Status:** Domain models refined based on Michael's Round 1 answers  
**MVP Launch:** March 2026 (5 months)  
**Next Step:** Update bounded context diagram with MVP phasing

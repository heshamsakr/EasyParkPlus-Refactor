# EasyParkPlus-Refactor

## Project Overview

This repository showcases a comprehensive **Software Design & Architecture (SDA) Project** for **EasyParkPlus**, transforming a basic parking lot prototype into a scalable, enterprise-grade system. By applying advanced software engineering principles, we demonstrate how to evolve legacy code into a robust, maintainable architecture that supports multi-facility operations and innovative EV charging features.

### Key Achievements
- **Code Refactoring Excellence**: Implemented Factory and Observer patterns to eliminate anti-patterns, improving code reusability, maintainability, and adherence to SOLID principles.
- **Domain-Driven Design (DDD) Mastery**: Modeled complex business domains with 8 bounded contexts and 12 aggregates, ensuring alignment with real-world requirements through strategic design and ubiquitous language.
- **Scalable Architecture**: Proposed a microservices-based solution with event-driven communication, supporting seamless expansion to multiple facilities while integrating cutting-edge features like OCPP 2.0.1-compliant EV charging and smart grid capabilities.
- **Business Impact**: Designed for MVP launch in March 2026, targeting 70% parking occupancy and 50% charger utilization, with a focus on user experience, real-time operations, and data-driven insights.

This project exemplifies best practices in software evolution, from anti-pattern removal to strategic architecture design, providing a blueprint for scaling parking management systems in a competitive market.

-----

## Project Deliverables

### Refactoring & Design Patterns

Requirement 1-2: Design patterns properly implemented and documented
- Factory Pattern in Vehicle.py for object creation
- Observer Pattern in ParkingLot.py for state change notifications
- Written assessment in REFACTORING_ASSESSMENT.md with detailed justification

### Code Quality & Anti-Patterns

Requirement 5-6: Bad coding practices identified and fixed
- 7 major anti-patterns identified (global variables, magic numbers, poor naming, improper inheritance, lack of abstraction, no validation, dead code)
- All improvements made with proper encapsulation and SOLID principles applied

### UML Documentation

Requirement 3-4: Original and Redesigned UML Diagrams
- 2 structural + 2 behavioral diagrams for original design (8 additional detail diagrams)
- 2 structural + 2 behavioral diagrams for refactored design with Factory + Observer patterns
- All diagrams in 03_Documentation/02_UML_Diagrams/

### Domain-Driven Design

Requirement 7-9: DDD implementation
- Bounded Context Diagram: 8 distinct contexts mapped to business domains
- Domain Models: 12 aggregates with 40+ domain events, value objects, and repositories
- Ubiquitous Language: Comprehensive business terminology across all contexts
- Microservices Architecture: Detailed service design with AWS infrastructure, Kafka/MSK communication, and OCPP 2.0.1 EV charging integration

### Source Code & Evidence

Requirement 10-12: Code, evidence, and supplementary materials
- Updated source code in 02_Refactored_App/ (926 lines, professionally structured)
- Application screenshots in 04_Evidence/Screenshots.docx (13.7 MB)
- Comprehensive final report in 05_Final_Report/ (PDF + DOCX, 2.2 MB)

-----

## Implementation Details by Rubric Requirement

This section maps our implementation to the official project rubric requirements:

### Rubric Requirement 1-2: Design Pattern Implementation & Documentation

**Requirement**: "Design and code improvements appropriately use two relevant design patterns" + "Written report is detailed and documents changes made"

**Implemented Pattern 1: Factory Pattern**
- **Location**: `02_Refactored_App/parking_manager/Vehicle.py` (lines 102-130)
- **Purpose**: Centralizes and abstracts vehicle object creation logic
- **Benefits**: Eliminates code duplication, supports extension without modification (Open/Closed Principle)
- **Implementation**: `VehicleFactory.createVehicle()` method handles ElectricVehicle and RegularVehicle instantiation
- **Compliance**: Adheres to SOLID principles, specifically Open/Closed and Dependency Inversion

**Implemented Pattern 2: Observer Pattern**
- **Location**: `02_Refactored_App/parking_manager/ParkingLot.py` (lines 3-50)
- **Purpose**: Enables real-time notifications when parking lot state changes
- **Benefits**: Decouples state management from notification logic, supports multiple observers (email, SMS, dashboard)
- **Implementation**: `ParkingObserver` interface with update() method, multiple concrete observers can subscribe
- **Compliance**: Adheres to SOLID Single Responsibility and Dependency Inversion principles

**Written Justification**:
- **Document**: `01_Baseline_Code/Aessesment/REFACTORING_ASSESSMENT.md` (319 lines)
- **Content**: Before/After code comparisons, detailed pattern justification, OO principles analysis (SOLID), design decisions

---

### Rubric Requirement 3-4: UML Diagrams (Original & Redesigned)

**Original Design Documentation**:
- **Location**: `03_Documentation/02_UML_Diagrams/Initial_Design/`
- **Structural Diagram**: Shows classes, attributes, methods, and relationships in baseline code
- **Behavioral Diagram**: Illustrates sequence of operations and interactions between objects
- **Detail Diagrams**: 7 additional diagrams breaking down complex behaviors for clarity

**Redesigned (Refactored) Documentation**:
- **Location**: `03_Documentation/02_UML_Diagrams/Redesign/`
- **Structural Diagram**: Demonstrates Factory and Observer pattern integration
- **Behavioral Diagram**: Shows improved interaction patterns and decoupling
- **Detail Diagrams**: 7 additional diagrams illustrating pattern behaviors and call sequences
- **Improvements Visible**: Reduced coupling, increased modularity, better separation of concerns

---

### Rubric Requirement 5-6: Anti-Pattern Identification & Fixes

**Anti-Patterns Identified** (7 major issues documented in `REFACTORING_ASSESSMENT.md`):

| # | Anti-Pattern | Severity | Location | Fix Applied |
|---|---|---|---|---|
| 1 | Global variables | HIGH | Original code variables | → Instance variables with proper encapsulation |
| 2 | Magic numbers | MEDIUM | Hard-coded values | → Named constants and configuration management |
| 3 | Poor variable naming | MEDIUM | Unclear method/variable names | → Descriptive, intention-revealing names |
| 4 | Improper inheritance | HIGH | Incorrect OO design | → Composition over inheritance where appropriate |
| 5 | Lack of abstraction | HIGH | Tight coupling | → Factory and Observer patterns introduced |
| 6 | No input validation | HIGH | Unvalidated parameters | → Validation added at method entry points |
| 7 | Dead code | LOW | Unused methods/variables | → Removed from refactored version |

**All improvements** made in `02_Refactored_App/` with SOLID principles applied throughout.

---

### Rubric Requirement 7: Bounded Context Diagram

**Delivered**: `03_Documentation/03_Architecture_Design/bounded_context_diagram.md` + PNG visualization

**8 Bounded Contexts Identified**:
1. **Parking Management** - Core parking operations, reservations, occupancy
2. **EV Charging Management** - Charging sessions, OCPP 2.0.1 integration, charger control
3. **Billing & Payments** - Invoice generation, payment processing, transaction records
4. **User & Access Management** - Authentication, authorization, user profiles
5. **Fleet Management** - Vehicle registration, tracking, maintenance scheduling
6. **Subscription Management** - Membership plans, recurring payments, plan management
7. **Smart Grid Management** - Load balancing, peak shaving, energy optimization
8. **Reporting & Analytics** - Data aggregation, reporting, business intelligence

**Context Relationships**: Partnership, Customer-Supplier, Anti-Corruption Layer patterns documented

**Artifacts**: Bounded context diagram PNG, detailed markdown documentation with relationships

---

### Rubric Requirement 8: Domain Models (DDD)

**Delivered**: `03_Documentation/03_Architecture_Design/domain_models.md` (38 KB comprehensive documentation)

**DDD Components Provided**:
- **12 Aggregates** with full specifications and business rules
  - Examples: ParkingSession, EVChargingSession, Invoice, Subscription, etc.
  - Each aggregate includes entity/value object definitions and repository interfaces
  
- **40+ Domain Events** documenting all state changes
  - Examples: ParkingSessionStarted, ChargeCompleted, InvoiceGenerated, etc.
  - Events enable event sourcing and audit trail capabilities
  
- **Value Objects**: Immutable objects representing measurement/concept (e.g., Money, Duration, Location)
  
- **Entities**: Objects with identity and lifecycle (e.g., Vehicle, User, ChargingStation)
  
- **Domain Services**: Cross-aggregate business logic
  - PricingCalculationService, LoadBalancingService, BillingService
  
- **Business Rules**: Constraints enforced at domain layer
  - 400 kW facility capacity limit, peak shaving rules, multi-component billing logic

**Supporting Documentation**:
- `ubiquitous_language.md` - Shared vocabulary across team and stakeholders
- `bounded_contexts_analysis.md` - Context dependency mapping
- `MICHAEL_QA_SESSIONS.md` - Business requirements clarification

---

### Rubric Requirement 9: Microservices Architecture

**Provided**: Microservices architecture design with multiple artifacts

**Architecture Documentation**:
- **File**: `03_Documentation/03_Architecture_Design/microservices_architecture.md`
- **Visual**: `03_Documentation/03_Architecture_Design/microservices.jpg` (high-resolution diagram)
- **Flowchart**: `03_Documentation/03_Architecture_Design/microservice.mmd` (Mermaid format)

**Microservices Design**:
- **Service Mapping**: 8 bounded contexts → 8+ microservices
- **Each Service**: Clear responsibilities, dedicated data store, independent deployment
- **API Layer**: REST endpoints for external consumers, internal service-to-service communication
- **Infrastructure**: AWS-based design with API Gateway, Event Bus (Kafka/MSK), RDS databases, ElastiCache

**Key Features**:
- OCPP 2.0.1 EV charger protocol integration for industry standard compliance
- Smart grid capabilities: Load balancing, peak shaving, demand response
- Multi-facility support with centralized billing and reporting
- Event-driven communication between services for scalability

---

### Rubric Requirement 10: Updated Source Code

**Delivered**: `02_Refactored_App/` (926 lines of production-quality Python)

**Code Structure**:
- **Module Organization**: `parking_manager/` package with clear separation of concerns
  - `ParkingLot.py` - Observer pattern implementation
  - `Vehicle.py` - Factory pattern implementation  
  - `ParkingManager.py` - Refactored core logic
  - `main.py` - Application entry point
  
- **Code Quality**: 
  - Follows SOLID principles throughout
  - Type hints and documentation
  - Proper error handling and input validation
  - No global state or magic numbers

---

### Rubric Requirement 11: Application Screenshots

**Delivered**: `04_Evidence/Screenshots.docx` (13.7 MB)

**Evidence Provided**:
- Screenshots of application running in Python environment
- Console output showing system operations
- Evidence of pattern implementation in action
- Proof of anti-pattern removal

---

### Rubric Requirement 12: Submission Format

**Format**: All artifacts organized in required structure

**Submission Package Includes**:

1. **Source Code**
   - Original: `01_Baseline_Code/` (ElectricVehicle.py, ParkingManager.py, Vehicle.py)
   - Refactored: `02_Refactored_App/` (926 lines with patterns implemented)

2. **Written Documentation**
   - Pattern justification: `REFACTORING_ASSESSMENT.md` (319 lines)
   - DDD models: `03_Documentation/03_Architecture_Design/domain_models.md` (38 KB)
   - Ubiquitous language: `03_Documentation/03_Architecture_Design/ubiquitous_language.md`
   - Architecture documentation: `microservices_architecture.md`

3. **UML Diagrams** (8 total + 14 detail diagrams)
   - Original design: 2 primary (structural + behavioral) + 7 detail diagrams
   - Redesigned: 2 primary (structural + behavioral) + 7 detail diagrams

4. **Architecture Artifacts**
   - Bounded context diagram: PNG + markdown
   - Microservices architecture: JPG + Mermaid flowchart + markdown
   - Domain models: Comprehensive specifications

5. **Evidence & Reports**
   - Screenshots: `04_Evidence/Screenshots.docx` (13.7 MB)
   - Final report: `05_Final_Report/` (PDF + DOCX, 2.2 MB)

---

## Project Summary

The project demonstrates practical application of software engineering principles through design pattern implementation, comprehensive Domain-Driven Design analysis, and enterprise-grade microservices architecture design. The refactored codebase exhibits improved maintainability and adherence to SOLID principles, while the architectural design supports scalability and multi-facility operations.

---

## AI Tools Usage Disclosure

In accordance with Quantic School's academic integrity policy, we disclose the following AI tool usage in this project:

### Overview of AI Tools Employed

The EasyParkPlus-Refactor project leveraged AI tools as enhancement assistants during the development and documentation phases. These tools were used to support team collaboration, synthesize complex information, and clarify business requirements—not to replace original engineering analysis and decision-making.

### Tools Used

| AI Tool | Function | Project Phase |
|---------|----------|----------------|
| Claude (Model: Sonnet 4.5) | Code Generation | Structural & behavioral diagrams and refactoring code |
| ChatGPT 4 | Technical Manager Consultant | Simulating Michael (Technical Manager) conversations to gather domain requirements, clarify technical details, and validate DDD concepts for bounded contexts and domain models (25 business requirement clarifications) - [View conversation](https://chatgpt.com/share/68fa4b3c-c230-8006-acbe-396a4c3a3bcb) |
| OpenCode Terminal (Models: Sonnet 4.5 and Haiku 4.5) | Development Assistant | Organize DDD documentation structure, format domain models and bounded contexts for consistency, and manage the synthesis of business requirements into coherent bounded contexts with aggregates and domain events |

### Scope of AI Tool Usage

**Purpose and Rationale**:
- Synthesizing Industry Standards: Quickly integrating complex, external requirements like the OCPP 2.0.1 protocol and smart grid features into the domain model definitions
- Validating DDD Concepts: Ensuring the Ubiquitous Language and Aggregate boundaries were robust and aligned with 2025 DDD best practices
- Refining Technical Q&A: Serving as an intermediary to process technical requirements into clear architectural constraints

**Applied to**:
- Synthesizing 25 business requirement clarifications into domain model definitions
- Refining Domain-Driven Design concepts and Ubiquitous Language
- Drafting microservices API specifications and responsibilities
- Organizing and formatting DDD documentation across multiple files
- Code refactoring proposals using Factory and Observer patterns

**NOT Applied to** (All Original Work):
- Strategic decisions on bounded context boundaries
- Identification of 12 aggregates and their relationships
- Definition of 40+ domain events and business rules
- Integration patterns between bounded contexts
- MVP phasing strategy and roadmap
- Design pattern selection and implementation decisions
- Anti-pattern identification and severity assessment
- UML diagram design and architectural decisions
- Final microservices architecture design

### Quality Assurance

All AI-generated content has been:
1. Reviewed by team members against project requirements
2. Adapted and modified to fit the specific context of EasyParkPlus
3. Integrated with team's original analysis and engineering decisions
4. Assessed for accuracy and appropriateness for academic submission

The team takes full responsibility for all deliverables and the accuracy of all technical content. AI tools enhanced productivity but did not replace rigorous software engineering analysis and design thinking. For comprehensive AI usage disclosure, refer to `05_Final_Report/Hesham_Mihai_HaVu_Software Design_EasyParkPlus_Report_V1.0.pdf`.

-----

## Project Goals

The successful completion of this project will enable the team to:

  * Pinpoint bad design, problematic source code, and bad coding practices
  * Identify and implement at least two distinct software design patterns
  * Utilize Object-Oriented design principles
  * Utilize UML (structural and behavioral) diagrams to represent the software designs
  * Utilize DDD principles to model the system and develop a high-level microservices architecture

-----

## Getting Started

### Prerequisites

To run the application and work on the codebase, **Python 3 (latest version)** is required.

  * Check your version: `python3 --version`
  * If any libraries are missing, use the `pip` command to install them.

### Installation & Execution

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/YourGitHubUsername/EasyParkPlus-Refactor-ScaleUp.git
    cd EasyParkPlus-Refactor-ScaleUp
    ```
2.  **Run the application:**
      * The original prototype code is located in `01_Baseline_Code/`.
      * The improved, refactored application's entry point is in `02_Refactored_App/main.py`.

-----

## Team

| Name | Primary Role | Initial Task Focus |
| :--- | :--- | :--- |
| **Ha Vu** | Code Implementation Lead | Code Analysis, Anti-Pattern Removal, Design Pattern Implementation |
| **Mihai** | DDD Modeling Lead | Bounded Contexts, Domain Modeling, Ubiquitous Language |
| **Hesham** | Architectural Lead | Microservices Architecture, API/DB Design, Written Justification Compilation |

-----

## Project Structure

The repository is structured to separate the original code, the refactored solution, and all required documentation artifacts.

```
EasyParkPlus-Refactor/
├── 01_Baseline_Code/                          # Original parking lot prototype
│   ├── Aessesment/
│   │   └── REFACTORING_ASSESSMENT.md          # Anti-pattern analysis + design patterns
│   ├── ElectricVehicle.py
│   ├── ParkingManager.py
│   └── Vehicle.py
│
├── 02_Refactored_App/                         # Refactored with Factory + Observer patterns
│   ├── parking_manager/
│   │   ├── __init__.py
│   │   ├── ParkingLot.py                      # Observer pattern implementation
│   │   ├── ParkingManager.py                  # Refactored manager
│   │   └── Vehicle.py                         # Factory pattern implementation
│   └── main.py                                # Application entry point
│
├── 03_Documentation/
│   ├── 01_Requirements_and_Scope/
│   │   ├── EMBA_MBA_Group_Project_Agreement.pdf
│   │   ├── Group Project Assignment Chart Template.xlsx
│   │   └── Software_Design_and_Architecture_Project.pdf
│   │
│   ├── 02_UML_Diagrams/
│   │   ├── Initial_Design/                    # Original design diagrams (8 total)
│   │   │   ├── Initial_Behavioral UML Diagram.png
│   │   │   ├── Initial_Behavioral UML Diagram_1-7.png
│   │   │   └── Initial_Structural UML Diagram.png
│   │   │
│   │   ├── Redesign/                          # Refactored design diagrams (8 total)
│   │   │   ├── Redesigned_Behavioral UML Diagram.png
│   │   │   ├── Redesigned_Behavioral UML Diagram_1-7.png
│   │   │   └── Redesigned_Structural UML Diagram.png
│   │   │
│   │   └── Architecture_Diagrams/
│   │       ├── bounded-context.png
│   │       └── microservices.png
│   │
│   └── 03_Architecture_Design/                # DDD & Architecture Documentation
│       ├── MICHAEL_QA_SESSIONS.md             # 25 technical business clarifications
│       ├── bounded_context_diagram.md         # 8 bounded contexts with relationships
│       ├── bounded_contexts_analysis.md       # Context dependency analysis
│       ├── bounded_context.png                # Visual representation
│       ├── domain_models.md                   # 12 aggregates, 40+ domain events
│       ├── microservice.mmd                   # Mermaid flowchart diagram
│       ├── microservices.jpg                  # High-resolution architecture diagram
│       ├── microservices_architecture.md      # Detailed service descriptions
│       ├── questions_for_technical_manager.md # Requirements gathering template
│       └── ubiquitous_language.md             # Business terminology glossary
│
├── 04_Evidence/
│   ├── Screenshots.docx                       # Application screenshots (13.7 MB)
│   └── Screenshots.pdf                        # Application screenshots (PDF format)
│
├── 05_Final_Report/
│   ├── Hesham_Mihai_HaVu_Software Design_EasyParkPlus_Report_V1.0.docx
│   └── Hesham_Mihai_HaVu_Software Design_EasyParkPlus_Report_V1.0.pdf
│
├── .gitignore
├── opencode.json
├── README.md                                   # Comprehensive project documentation
└── REFACTORING_ASSESSMENT.md                  # Anti-pattern analysis + patterns (in root for easy access)
```

### Directory Descriptions

| Directory | Contents |
|-----------|----------|
| 01_Baseline_Code | Original prototype code and anti-pattern assessment |
| 02_Refactored_App | Refactored code with Factory + Observer patterns |
| 03_Documentation | All DDD, UML, and architecture documentation |
| 04_Evidence | Screenshots demonstrating application functionality |
| 05_Final_Report | Comprehensive final project report (PDF + DOCX) |

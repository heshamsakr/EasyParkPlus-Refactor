# `EasyParkPlus-Refactor`

## 🅿️ Project Overview

This repository showcases a comprehensive **Software Design & Architecture (SDA) Project** for **EasyParkPlus**, transforming a basic parking lot prototype into a scalable, enterprise-grade system. By applying advanced software engineering principles, we demonstrate how to evolve legacy code into a robust, maintainable architecture that supports multi-facility operations and innovative EV charging features.

### Key Achievements
- **Code Refactoring Excellence**: Implemented Factory and Observer patterns to eliminate anti-patterns, improving code reusability, maintainability, and adherence to SOLID principles.
- **Domain-Driven Design (DDD) Mastery**: Modeled complex business domains with 8 bounded contexts and 12 aggregates, ensuring alignment with real-world requirements through strategic design and ubiquitous language.
- **Scalable Architecture**: Proposed a microservices-based solution with event-driven communication, supporting seamless expansion to multiple facilities while integrating cutting-edge features like OCPP 2.0.1-compliant EV charging and smart grid capabilities.
- **Business Impact**: Designed for MVP launch in March 2026, targeting 70% parking occupancy and 50% charger utilization, with a focus on user experience, real-time operations, and data-driven insights.

This project exemplifies best practices in software evolution, from anti-pattern removal to strategic architecture design, providing a blueprint for scaling parking management systems in a competitive market.

-----

## 📊 Current Status

**Project Completion**: 11/12 requirements complete (92%)  
**Last Updated**: October 24, 2025  
**Next Milestone**: UML Redesign Diagrams + Final Submission

### ✅ Completed Work

- **Code Refactoring**: Factory and Observer patterns implemented
- **Anti-Pattern Analysis**: 7 major issues identified and fixed in REFACTORING_ASSESSMENT.md
- **DDD Documentation**: 8 bounded contexts, 12 aggregates, ubiquitous language
- **Domain Models**: Comprehensive models with OCPP 2.0.1 integration and smart grid features
- **Technical Manager Q&A**: 25 critical business requirements clarified
- **Bounded Context Diagram**: PNG generated for clear viewing
- **Microservices Architecture Diagram**: PNG generated for clear viewing
- **Source Code**: Professional refactored application in `02_Refactored_App/`
- **Screenshots**: Evidence in `04_Evidence/Screenshots.docx`

### ⚠️ In Progress

- **Original UML Diagrams**: 2 PNG files exist, need verification

### 🚧 Remaining Tasks

1. **Redesign UML Diagrams** (Ha Vu) - 2 diagrams showing Factory + Observer patterns
2. **Final Submission Package** (Hesham) - Compile all deliverables

**Estimated Completion**: October 26-27, 2025

For detailed status updates, refer to commit history and documentation files.

-----

## 📋 What Has Been Implemented

This section maps our completed work to the project rubric requirements:

### 1. Design Patterns Implementation ✅
**Requirement**: "Design and code improvements appropriately use two relevant design patterns"

**Implemented**:
- **Factory Pattern** (`02_Refactored_App/parking_manager/Vehicle.py:102-130`)
  - `VehicleFactory.createVehicle()` centralizes vehicle object creation
  - Eliminates duplicate instantiation logic
  - Supports extension for new vehicle types (Open/Closed Principle)
  
- **Observer Pattern** (`02_Refactored_App/parking_manager/ParkingLot.py:3-50`)
  - `ParkingObserver` interface for real-time notifications
  - Decouples parking lot state changes from notification logic
  - Enables multiple observers (email, SMS, dashboard updates)

**Evidence**: Commits `d4c0846` (Factory), `4753560` (Code update)

---

### 2. Written Report on Design Patterns ✅
**Requirement**: "Written report is detailed and documents changes made and reasons the patterns were utilized"

**Delivered**: `REFACTORING_ASSESSMENT.md` (319 lines)
- Before/After code comparisons
- Justification for each pattern choice
- OO principles analysis (SOLID)
- Industry comparison showing improvements

---

### 3. UML Diagrams - Original Design ✅
**Requirement**: "Original design is represented correctly using two appropriate UML diagrams"

**Delivered**: `03_Documentation/02_UML_Diagrams/Initial_Design/`
- Structural diagram: `Initial_ULM Diagram-Page-1.drawio.png`
- Behavioral diagram: `Initial_ULM Diagram-Page-2.drawio.png`

---

### 4. UML Diagrams - Redesign 🚧
**Requirement**: "Redesign is represented correctly using two appropriate UML diagrams"

**Status**: In progress (Ha Vu)
- Structural diagram: Class diagram showing Factory + Observer patterns
- Behavioral diagram: Sequence diagram showing pattern interactions

**Expected**: `03_Documentation/02_UML_Diagrams/Redesign/` folder with 2 PNGs

---

### 5. Bad Coding Practices Identification ✅
**Requirement**: "All bad coding practices present in the code base are identified"

**Delivered**: `REFACTORING_ASSESSMENT.md` Section 2 identifies **7 major anti-patterns**:
1. Global variables (HIGH severity)
2. Magic numbers (MEDIUM severity)
3. Poor variable naming (MEDIUM severity)
4. Improper inheritance (HIGH severity)
5. Lack of abstraction (HIGH severity)
6. No input validation (HIGH severity)
7. Dead code (LOW severity)

Each anti-pattern includes:
- Code location
- Severity rating
- Impact analysis
- Recommended fix

---

### 6. Improvements to Bad Code ✅
**Requirement**: "Appropriate improvements are made to each of these bad coding examples"

**Delivered**: All 7 anti-patterns fixed in `02_Refactored_App/`
- Global variables → Instance variables with proper encapsulation
- Magic numbers → Named constants and enums
- Poor naming → Descriptive, intention-revealing names
- Improper inheritance → Composition over inheritance where appropriate
- Lack of abstraction → Factory and Observer patterns introduced
- No validation → Input validation added
- Dead code → Removed

**Evidence**: Git diff between commits `a2806af` (baseline) and `4753560` (refactored)

---

### 7. Bounded Context Diagram ✅
**Requirement**: "Appropriate bounded context diagram is provided"

**Delivered**: `03_Documentation/03_Architecture_Design/bounded_context_diagram.md`
- **8 bounded contexts** identified:
  1. Parking Management
  2. EV Charging Management
  3. Billing & Payments
  4. User & Access Management
  5. Fleet Management
  6. Subscription Management
  7. Smart Grid Management
  8. Reporting & Analytics
- Context relationships (Partnership, Customer-Supplier, ACL)
- MVP vs Phase 2 phasing strategy
- Mermaid diagram + detailed descriptions

**Note**: Converted to PNG image for final submission

---

### 8. Domain Models (DDD) ✅
**Requirement**: "Detailed DDD-based domain models are provided"

**Delivered**: `03_Documentation/03_Architecture_Design/domain_models.md` (38KB)
- **12 aggregates** with full specifications
- **40+ domain events** (SessionStarted, ChargingCompleted, InvoiceGenerated, etc.)
- Value objects and entities per aggregate
- Business rules per aggregate
- Repository interfaces
- Domain services (LoadBalancing, PricingCalculation, etc.)

**Technical highlights**:
- OCPP 2.0.1 integration for EV chargers
- Smart grid features: 400 kW capacity cap, peak shaving, load balancing
- Multi-component billing: kWh + session + parking + idle fees
- Cross-facility subscription management

**Supporting documentation**:
- `ubiquitous_language.md` - Business terminology across all contexts
- `MICHAEL_QA_SESSIONS.md` - Consolidated Q&A with ChatGPT link
- `bounded_contexts_analysis.md` - Context interaction patterns

---

### 9. Microservices Architecture Diagram 🚧
**Requirement**: "High-quality microservices architecture diagram is provided"

**Status**: In progress (Hesham)
- Will map 8 bounded contexts → microservices
- Define service responsibilities
- Design APIs (external + service-to-service)
- Specify database per service

**Delivered**: `03_Documentation/03_Architecture_Design/microservices.png`

---

### 10. Updated Source Code ✅
**Requirement**: "Your submission includes the updated source code"

**Delivered**: `02_Refactored_App/`
- Modular structure with `parking_manager/` package
- Factory Pattern implementation in `Vehicle.py`
- Observer Pattern implementation in `ParkingLot.py`
- Clean, maintainable code following SOLID principles

---

### 11. Screenshots/Video ✅
**Requirement**: "Screenshots of the application running on your computer"

**Delivered**: `04_Evidence/Screenshots.docx`

**Commit**: `e232a7c`

---

### 12. Submission Format 🚧
**Requirement**: "Submission has been correctly submitted in the format requested"

**Status**: Ready for final packaging (Hesham)

**Includes**:
- Written justifications (REFACTORING_ASSESSMENT.md)
- 4 UML diagrams (2 original + 2 redesign)
- Updated source code (`02_Refactored_App/`)
- Screenshots (`04_Evidence/Screenshots.docx`)
- DDD documentation (bounded context diagram, domain models)
- Microservices architecture diagram
- All packaged in .zip file

---

## 🔧 AI Tools Usage Disclosure

In accordance with Quantic School's academic integrity policy, we disclose the following AI tool usage in this project:

### Mihai Chindriș (DDD Lead)
**Tools used**:
- **ChatGPT (OpenAI)**: Used to simulate conversations with "Michael, Technical Manager" (as specified in project requirements) to gather business requirements and clarify technical details for the Domain-Driven Design phase
- **OpenCode Terminal (opencode.ai)**: Used as a development assistant to organize DDD documentation, structure bounded contexts, and format domain models based on the gathered requirements

**Scope**:
- ChatGPT was used to ask 15 technical and business questions (Round 1) and draft 10 architecture questions (Round 2) to understand system requirements
- OpenCode was used to structure the DDD analysis, organize documentation files, and ensure consistency across bounded contexts and domain models
- **All domain modeling decisions, bounded context identification, and architectural analysis represent original thought** based on project context and Michael's answers
- AI tools served as **enhancement tools for organization and formatting**, not as replacement for original analysis

**What was NOT AI-generated**:
- Strategic decisions on bounded context boundaries
- Identification of aggregates and their relationships
- Business rules and domain events
- Integration patterns between contexts
- MVP phasing strategy

### Ha Vu (Code Implementation Lead)
**Tools used**: [To be documented by Ha Vu]

### Hesham Sakr (Architectural Lead)
**Tools used**: [To be documented by Hesham]

**Note**: All AI-generated content has been reviewed, validated, and adapted to fit the specific requirements of the EasyParkPlus system. The team takes full responsibility for the accuracy and appropriateness of all submissions.

-----

## 🎯 Project Goals

The successful completion of this project will enable the team to:

  * Pinpoint bad design, problematic source code, and bad coding practices
  * Identify and implement at least two distinct software design patterns
  * Utilize Object-Oriented design principles
  * Utilize UML (structural and behavioral) diagrams to represent the software designs
  * Utilize DDD principles to model the system and develop a high-level microservices architecture

-----

## 🚀 Getting Started

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

## 👥 Team

| Name | Primary Role | Initial Task Focus |
| :--- | :--- | :--- |
| **Ha Vu** | Code Implementation Lead | Code Analysis, Anti-Pattern Removal, Design Pattern Implementation |
| **Mihai** | DDD Modeling Lead | Bounded Contexts, Domain Modeling, Ubiquitous Language |
| **Hesham** | Architectural Lead | Microservices Architecture, API/DB Design, Written Justification Compilation |

-----

## 📂 Project Structure

The repository is structured to separate the original code, the refactored solution, and all required documentation artifacts.

```
EasyParkPlus-Refactor/
├── 01_Baseline_Code/              # Original parking lot prototype
│   ├── ElectricVehicle.py
│   ├── ParkingManager.py
│   └── Vehicle.py
├── 02_Refactored_App/             # ✅ Refactored with Factory + Observer patterns
│   ├── parking_manager/
│   │   ├── ParkingLot.py         # Observer pattern implementation
│   │   ├── ParkingManager.py     # Refactored manager
│   │   └── Vehicle.py            # Factory pattern implementation
│   └── main.py
├── 03_Documentation/
│   ├── 01_Requirements_and_Scope/
│   │   ├── Software_Design_and_Architecture_Project.pdf
│   │   └── EMBA_MBA_Group_Project_Agreement.pdf
│   ├── 02_UML_Diagrams/
│   │   ├── Initial_Design/       # ⚠️ 2 PNG files (need verification)
│   │   └── Redesign/             # 🚧 TODO: 2 UML diagrams needed
│   └── 03_Architecture_Design/
│       ├── bounded_context_diagram.md      # ✅ 8 bounded contexts
│       ├── domain_models.md                # ✅ 12 aggregates with DDD
│       ├── ubiquitous_language.md          # ✅ Business terminology
│       ├── michael_answers_round1.md       # ✅ 15 Q&A with tech manager
│       ├── bounded_contexts_analysis.md
│       ├── questions_for_technical_manager.md
│       └── microservices_architecture_diagram.md  # 🚧 TODO: Hesham
├── 04_Evidence/
│   └── Screenshots.docx           # ✅ Application screenshots
├── REFACTORING_ASSESSMENT.md      # ✅ Anti-pattern analysis + patterns
└── README.md
```

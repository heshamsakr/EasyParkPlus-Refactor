# `EasyParkPlus-Refactor`

## 🅿️ Project Overview

This repository documents the work for a **Software Design & Architecture (SDA) Project** focused on improving and scaling an existing preliminary prototype for **EasyParkPlus**, a parking lot management company.

The project involves refactoring the initial prototype code base by implementing OO design patterns and removing anti-patterns. It also includes designing a scalable solution to handle multiple facilities and a new **Electric Vehicle (EV) Charging Station Management** feature using **Domain-Driven Design (DDD)** and a proposed **Microservices Architecture**.

-----

## 📊 Current Status

**Project Completion**: 9/12 requirements complete (75%)  
**Last Updated**: October 23, 2025  
**Next Milestone**: UML Redesign Diagrams + Microservices Architecture

### ✅ Completed Work

- **Code Refactoring**: Factory and Observer patterns implemented
- **Anti-Pattern Analysis**: 7 major issues identified and fixed in REFACTORING_ASSESSMENT.md
- **DDD Documentation**: 8 bounded contexts, 12 aggregates, ubiquitous language
- **Domain Models**: Comprehensive models with OCPP 2.0.1 integration and smart grid features
- **Technical Manager Q&A**: 15 critical business requirements clarified
- **Source Code**: Professional refactored application in `02_Refactored_App/`
- **Screenshots**: Evidence in `04_Evidence/Screenshots.docx`

### ⚠️ In Progress

- **Original UML Diagrams**: 2 PNG files exist, need verification

### 🚧 Remaining Tasks

1. **Redesign UML Diagrams** (Ha Vu) - 2 diagrams showing Factory + Observer patterns
2. **Microservices Architecture Diagram** (Hesham) - Service design with APIs and databases
3. **Final Submission Package** (Hesham) - Compile all deliverables

**Estimated Completion**: October 26-27, 2025

See [PROJECT_STATUS_RUBRIC_CHECK.md](PROJECT_STATUS_RUBRIC_CHECK.md) for detailed status.

-----

## 🎯 Project Goals

The successful completion of this project will enable the team to:

  * [cite\_start]Pinpoint bad design, problematic source code, and bad coding practices[cite: 4].
  * [cite\_start]Identify and implement at least two distinct software design patterns[cite: 18, 4].
  * [cite\_start]Utilize Object-Oriented design principles[cite: 4].
  * [cite\_start]Utilize UML (structural and behavioral) diagrams to represent the software designs[cite: 4].
  * [cite\_start]Utilize DDD principles to model the system and develop a high-level microservices architecture[cite: 4].

-----

## 🚀 Getting Started

### Prerequisites

[cite\_start]To run the application and work on the codebase, **Python 3 (latest version)** is required[cite: 28].

  * [cite\_start]Check your version: `python3 --version` [cite: 30]
  * [cite\_start]If any libraries are missing, use the `pip` command to install them[cite: 31].

### Installation & Execution

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/YourGitHubUsername/EasyParkPlus-Refactor-ScaleUp.git
    cd EasyParkPlus-Refactor-ScaleUp
    ```
2.  **Run the application:**
      * [cite\_start]The original prototype code is located in `01_Baseline_Code/`[cite: 15].
      * The improved, refactored application's entry point is in `02_Refactored_App/`.

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
├── PROJECT_STATUS_RUBRIC_CHECK.md # ✅ Detailed status (9/12 complete)
└── README.md
```

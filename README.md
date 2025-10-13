# `EasyParkPlus-Refactor`

## 🅿️ Project Overview

[cite\_start]This repository documents the work for a **Software Design & Architecture (SDA) Project** focused on improving and scaling an existing preliminary prototype for **EasyParkPlus**, a parking lot management company[cite: 14].

[cite\_start]The project involves refactoring the initial prototype code base by implementing OO design patterns and removing anti-patterns[cite: 1, 19]. [cite\_start]It also includes designing a scalable solution to handle multiple facilities and a new **Electric Vehicle (EV) Charging Station Management** feature using **Domain-Driven Design (DDD)** and a proposed **Microservices Architecture**[cite: 22, 23, 25].

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
EasyParkPlus-Refactor-ScaleUp/
├── 01_Baseline_Code/
[cite_start]│   └── (Original parking lot prototype files) [cite: 14, 15]
├── 02_Refactored_App/
│   ├── parking_manager/     # Contains refactored, pattern-based core logic
│   └── main.py              # Entry point for the improved application
├── 03_Documentation/
│   ├── 01_Requirements_and_Scope/
│   │   └── Project_Prompt.md      # Full project instructions and requirements
│   ├── 02_UML_Diagrams/
[cite_start]│   │   ├── Initial_Design/      # Initial structural and behavioral diagrams [cite: 33]
[cite_start]│   │   └── Redesign/            # Redesigned structural and behavioral diagrams [cite: 33]
│   ├── 03_Architecture_Design/
[cite_start]│   │   ├── bounded_context_diagram.png # High-level bounded context diagram [cite: 34]
[cite_start]│   │   ├── domain_models.md / .png     # Basic domain models [cite: 34]
[cite_start]│   │   └── microservices_architecture_diagram.png # Proposed architecture diagram [cite: 34]
[cite_start]│   └── Written_Report.docx / .pdf / .md # Justification, DDD application, and arch proposal [cite: 21, 25]
├── 04_Evidence/
[cite_start]│   ├── screenshots/              # Screenshots of the application running [cite: 34]
│   └── video/                    # Brief video (optional)
├── .gitignore
└── README.md
```

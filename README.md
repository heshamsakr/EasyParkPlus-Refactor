# `EasyParkPlus-Refactor`

## 🅿️ Project Overview

[cite\_start]This repository contains the source code and design documentation for a Software Design & Architecture (SDA) project focused on improving and scaling an existing preliminary prototype for **EasyParkPlus**, a parking lot management company[cite: 14].

[cite\_start]The original application is a single parking lot manager[cite: 14]. [cite\_start]The primary goals of this project are to refactor the prototype code base to improve its quality, implement modern design patterns, and propose a scalable **Microservices-based architecture** to handle operations across multiple facilities and incorporate a new **Electric Vehicle (EV) Charging Station Management** feature[cite: 22, 23].

## 🎯 Project Goals

The project is divided into two main phases:

### Phase 1: Code Refactoring & Design Patterns

  * [cite\_start]Pinpoint and remove anti-patterns and problematic source code in the existing prototype[cite: 1, 19].
  * [cite\_start]Identify and implement **at least two distinct Object-Oriented (OO) design patterns** to introduce significant structural and architectural improvements[cite: 19, 20].
  * [cite\_start]Utilize Object-Oriented design principles throughout the refactoring process[cite: 4].

### Phase 2: Architectural Design & Scaling

  * [cite\_start]Apply **Domain-Driven Design (DDD)** principles to model the entire system, including the new EV charging capability[cite: 25, 26].
  * [cite\_start]Identify the core domain, subdomains, and **Bounded Contexts**[cite: 26].
  * [cite\_start]Propose and document a high-level, scalable **Microservices architecture** that aligns with the Bounded Contexts[cite: 25, 27].

## 🚀 Getting Started (Original Prototype)

### Prerequisites

To run the initial prototype and work on the refactored code:

  * [cite\_start]**Python 3 (Latest Version):** You are responsible for ensuring your code works with Python[cite: 28, 29].
      * *Check your version:* `python3 --version`
  * [cite\_start]**Missing Libraries:** Use the `pip` command to install any missing libraries[cite: 31].

### Installation & Execution

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/YourGitHubUsername/EasyParkPlus-Refactor-ScaleUp.git
    cd EasyParkPlus-Refactor-ScaleUp
    ```
2.  [cite\_start]**Download Baseline Code:** The initial prototype code base must be downloaded and placed within this repository's structure (link provided in project instructions)[cite: 15].
3.  **Run the application:**
    ```bash
    # Command will vary based on the original application's entry point (e.g., app.py)
    python3 parking_lot_manager.py 
    ```

## 👥 Team

| Name | Primary Role | Initial Task Focus |
| :--- | :--- | :--- |
| **Ha Vu** | Code Implementation Lead | [cite\_start]Code Analysis, Anti-Pattern Removal, Design Pattern Implementation [cite: 19] |
| **Mihai** | DDD Modeling Lead | [cite\_start]Bounded Contexts, Domain Modeling, Ubiquitous Language [cite: 26] |
| **Hesham** | Architectural Lead | [cite\_start]Microservices Architecture, API/DB Design, Written Justification Compilation [cite: 27] |

## 📦 Final Submission Deliverables

[cite\_start]The final submission will be a packaged archive including the following elements[cite: 33, 34]:

  * **Source Code:** The updated, refactored source code.
  * **UML Diagrams (4):** Two for the original design (structural, behavioral) and two for the re-designed code (structural, behavioral).
  * **Screenshots/Video:** Proof of the application running.
  * **Written Document:**
      * Justification for code fixes and chosen design patterns.
      * **DDD Modeling:** Bounded context diagram and basic domain models.
      * **Microservices Architecture:** Diagram including services, APIs/endpoints, and per-service DBs.

# Utility-Based Surveillance AI

A Python simulation demonstrating **utility-based decision making** in a resource-constrained surveillance environment. The AI autonomously prioritizes monitoring and mitigation actions by evaluating multiple dynamic threats under partial observability rather than relying on scripted behavior.

## Features

* Monitors **3 independently evolving threats**, each with unique progression rates and continuously changing risk levels.
* Uses a **utility-based decision system** to evaluate scanning, threat mitigation, and idle actions every simulation tick.
* Implements **partial observability**, requiring the AI to balance information gathering with direct intervention as threat information becomes stale over time.
* Models **resource-constrained planning** through a finite power system, forcing long-term tradeoffs between acquiring information and preventing failures.
* Employs a nonlinear risk model combining threat proximity, observation latency, and opportunity cost to produce adaptive, explainable decision making.

## Technical Highlights

* **Language:** Python
* **Architecture:** Object-Oriented Programming (OOP)
* **AI Technique:** Utility-Based Decision Making
* **Simulation:** 3 concurrent threats, 50-tick survival episodes
* **Concepts:** Risk Assessment, Partial Observability, Resource Optimization, Opportunity Cost Modeling, Autonomous Decision Making

## Learning Outcomes

This project demonstrates the design and implementation of a utility-driven AI capable of prioritizing competing objectives in a dynamic environment. It served as a foundation for exploring autonomous decision systems, simulation design, and AI architectures that can be extended with finite state machines, predictive models, or more complex environments.

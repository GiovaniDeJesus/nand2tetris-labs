# Nand2Tetris Labs

This repository contains my solutions and implementations for the **Nand2Tetris** project. The course provides a hands-on approach to building a computer from the ground up, starting with basic logic gates and progressing to a high-level programming language and operating system.

## Table of Contents

- [About Nand2Tetris](#about-nand2tetris)
- [Project Structure](#project-structure)
- [Setup](#setup)
- [Usage](#usage)
- [Progress](#progress)
- [Resources](#resources)

---

## About Nand2Tetris

The Nand2Tetris project guides learners through constructing a modern computer system step by step. It starts with designing elementary logic gates, progresses through constructing a CPU and memory, and culminates in creating a basic operating system and a compiler.

Visit the [official website](https://www.nand2tetris.org/) for more details.

---

## Project Structure

The repository is organized into folders corresponding to each project in the course:

```plaintext
├── 01-Boolean-Logic
│   ├── And.hdl
│   ├── Or.hdl
│   └── README.md
├── 02-Boolean-Arithmetic
│   ├── Adder.hdl
│   ├── ALU.hdl
│   └── README.md
├── 03-Sequential-Logic
│   ├── FlipFlop.hdl
│   └── README.md
...

Each folder contains:

    HDL files: Implementations of the hardware modules.
    README.md: Specific instructions or notes about the project.
    Test scripts: Files to verify the correctness of the designs.

Setup
Prerequisites

    Download the Nand2Tetris software suite.
    Java Runtime Environment (JRE) for running the Hardware Simulator and other tools.

Installation

    Clone the repository:

    git clone https://github.com/<your-username>/nand2tetris-labs.git
    cd nand2tetris-labs

    Ensure the Nand2Tetris tools are accessible (e.g., HardwareSimulator.sh).

Usage

    Open the Hardware Simulator:

    java -jar /path/to/HardwareSimulator.jar

    Load the .hdl file for the desired project.
    Run the provided test scripts to validate your implementation.

Progress
Project	Status
01. Boolean Logic	✅ Completed
02. Boolean Arithmetic	🚧 In Progress
03. Sequential Logic	❌ Not Started
04. Machine Language	❌ Not Started
...	...
Resources

    Nand2Tetris Official Website
    Course on Coursera
    HDL Syntax Reference

Contributing

Feel free to fork this repository and submit pull requests for improvements or additional content!
License

This project is licensed under the MIT License.


### Notes:
- Replace `<your-username>` with your GitHub username in the clone command.
- Update the `Progress` section as you complete the projects.
- Include the `LICENSE` file in your repository if you decide to use the MIT License or another license.


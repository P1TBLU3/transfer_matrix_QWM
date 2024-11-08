# Quantum Mechanics: Transfer Matrix Method for Multi-Step Potential

This project calculates the reflection and transmission of a quantum particle encountering a multi-step potential. Using the transfer matrix method, it models both the propagation and interaction of the wavefunction through each region in the potential profile. The code allows you to set initial conditions, calculate propagation coefficients, and obtain reflectance and transmittance values for a given energy level.

## Table of Contents
1. [Introduction](#introduction)
2. [Requirements](#requirements)
3. [Project Structure](#project-structure)
4. [How It Works](#how-it-works)
5. [Example Usage](#example-usage)
6. [Output](#output)
7. [Notes](#notes)

---

## Introduction

The transfer matrix method is a powerful numerical technique to solve the 1D Schrödinger equation for scattering solutions across piecewise-constant potentials. By decomposing the wavefunction into components in each potential step, it provides a framework for calculating the total reflectance and transmittance across any given potential profile.

### Quantum Background
In quantum mechanics, a particle encountering a potential can be either reflected or transmitted depending on its energy relative to the potential energy of each region. This code calculates:

- **Reflection Coefficient** (R): Probability of the wave being reflected.
- **Transmission Coefficient** (T): Probability of the wave being transmitted.

## Requirements

- Python 3.x
- Numpy (`pip install numpy`)

## Project Structure

```plaintext
├── quantum_transfer_matrix.py  # Main script with all functions and constants
├── README.md                   # This file
└── requirements.txt            # Python dependencies


## How It Works

### Constants
The script defines physical constants for the electron mass `m` and reduced Planck's constant `hbar`. You can modify these if working with particles other than electrons.

### Functions

- **get_k(E, V):** Computes the wave number \( k \) in each region based on the particle's energy \( E \) and potential \( V \).
  - Returns a real \( k \) if \( E \geq V \), else an imaginary \( k \).

- **propagation_matrix(k, L):** Calculates the transfer matrix for a region of constant potential \( V \) and length \( L \).

- **step_matrix(k_left, k_right):** Calculates the transfer matrix for the interface between two regions with different wave numbers.

- **calculate_total_matrix(E, V0, VF):** Calculates the total transfer matrix for the complete potential profile, including the final step to \( V_F \).

- **get_coefficients(M):** Extracts the reflection and transmission coefficients from the final transfer matrix.

### Variables

- **V0** and **VF**: Initial and final potential energies.
- **potential_profile**: List of tuples defining each region in the potential profile (potential energy \( V \) and length \( L \)).
- **E**: Energy of the incoming wave.
- **A0**: Amplitude of the incoming wave.


## Output

The script will print:

- **Amplitude of the reflected wave**
- **Amplitude of the transmitted wave**
- **Reflected energy** (in Joules)
- **Transmitted energy** (in Joules)

## Notes

- **Normalization**: The initial wave amplitude \( A_0 \) should ideally be chosen to normalize the wavefunction. This can be adjusted based on the intended interpretation.
- **Reflection and Transmission**: Values are automatically calculated based on the transfer matrix for a multi-step potential.
- **Extension**: This model can be extend





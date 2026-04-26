# QR Code Generator and Analysis

## Overview
This project explores the **design, implementation, and analysis of QR code systems**. It includes a Python-based QR code generator and a series of experiments evaluating how different error correction levels impact robustness and scannability.

The goal of this project is to understand how QR codes function in practice and how their parameters affect performance in real-world conditions.

---

## Features
- Generate QR codes using Python
- Configure different **error correction levels** (L, M, Q, H)
- Compare QR code density and structure
- Analyse robustness under **partial damage**
- Evaluate trade-offs between **data capacity and reliability**

---

## Technologies Used
- Python
- `qrcode` library

---

## Implementation
The QR codes are generated programmatically using configurable parameters such as:
- Error correction level
- QR version
- Module size and border

Multiple QR codes are generated to support experimental comparison.

---

## Experiments
The project includes experiments to analyse:

### 1. Error Correction vs Damage
Higher error correction levels (e.g. H) were shown to remain scannable even when partially damaged, while lower levels failed under minimal damage.

### 2. Data Size vs QR Density
Increasing the amount of encoded data resulted in denser QR codes, which reduced scanning reliability.

### 3. Environmental Conditions
Factors such as lighting, distance, and angle impacted scanning performance, particularly for dense QR codes.

---

## Key Insights
- Higher error correction improves robustness but increases density
- Larger data sizes reduce scanning reliability
- Optimal QR configuration depends on the use case

---

## Example Output
The project generates QR codes with different error correction levels:

- L (Low)
- M (Medium)
- Q (Quartile)
- H (High)

---

## Blog
For a detailed explanation of the design, experiments, and findings, read the full blog here:

👉 [[Blog Post](https://medium.com/p/377e22c6b8a8?postPublishedType=initial)]

---

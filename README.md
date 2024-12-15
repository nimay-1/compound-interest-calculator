# Compound Interest Calculator in Python

## Overview
This project is a simple Python-based **Compound Interest Calculator**. It allows users to calculate the future value of an investment based on their input values, including initial capital, annual interest rate, compounding frequency, and investment duration.

This project is perfect for beginners learning Python or finance concepts, as it demonstrates input validation, user interaction, and financial calculations.

---

## Features
- User-friendly prompts to input required values.
- Input validation to ensure all inputs are positive numbers.
- Calculation of compound interest using the formula:

  **A = P × (1 + r/n)^(n × t)**

  Where:
  - **A** = Final amount
  - **P** = Initial capital (principal)
  - **r** = Annual interest rate (as a decimal)
  - **n** = Compounding frequency (number of times per year)
  - **t** = Time (in years)


---

## Getting Started

### Prerequisites
- Python 3.x installed on your system.

### Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/compound-interest-calculator.git
   ```
2. Navigate to the project folder:
   ```bash
   cd compound-interest-calculator
   ```
3. Run the script:
   ```bash
   python compound_interest.py
   ```

---

## Usage
1. Run the program.
2. Enter the following values when prompted:
   - Initial capital
   - Annual interest rate (as a percentage, e.g., 5 for 5%)
   - Compounding frequency (in months per year, e.g., 12 for monthly)
   - Investment duration (in years)
3. The program will calculate and display the final investment amount after the specified duration.

---

## Example Output
```
Enter your initial capital: 1000
Enter your annual interest rate in % (e.g., 4 for 4%): 5
Enter your compounding frequency in number of months per year: 12
Enter your investment duration (in years): 10

You plan to grow 1000€ over 10 year(s) with an interest rate of 5%.
At the end of 10 year(s), your capital will amount to 1647.01€.
```

---

## File Structure
```
compound-interest-calculator/
|-- compound_interest.py   # Main Python script
|-- README.md              # Project documentation
```

---

## Future Improvements
- Add support for different currencies.
- Allow users to calculate with continuous compounding.
- Create a GUI or web interface for a more interactive experience.
- Add unit tests for validating calculations.

---

## Acknowledgments
- Formula reference: [Wikipedia - Compound Interest](https://en.wikipedia.org/wiki/Compound_interest)
- Developed as a learning project for Python and financial calculations.


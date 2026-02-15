# GWA-calculator

## Overview 
-The goal of our code is to make a calculator that computes a student’s General Weighted Average(GWA) based on subject grades and corresponding units.

-You enter grades + units for each subject, and the program does the calculations for you. 

## Features
-Computes a student’s GWA based on grades and units.

-Accepts both percentage and GWA inputs.

-Automatically converts percentage grades to GWA equivalents.

-Supports Python 3.8 and newer versions.

-Allows multiple subjects with corresponding grades and units.

-Automatically calculates weighted average and rounds final GWA to 2 decimal places.

-Validates user input to ensure correct numerical entries.

-Allows repeated calculations without restarting the program.
## Requirements
- Python 3.8+

## Core Feature Implementation
-percent_to_grade(p): converts percentage grades to standard GWA scale.

-get_input(mode): handles user input and ensures valid grades and units.

-calc_gwa(data): calculates weighted average

Program outputs classification based on calculated GWA:

    ≤ 1.50 → Director’s Lister
    
    ≤ 3.00 → Passed
    
    3.00 → Failed

## Technologies Used & Justification
  Python 3: Easy to use, supports loops and conditionals efficiently.
  
  CLI interface: Lightweight and works on all platforms.
  
  GitHub: Version control and project organization.

## Key Design Decisions / Trade-offs
  -CLI interface chosen for simplicity.
  
  -Input validation ensures correct calculations but requires additional       prompts.
  
  -Hardcoded percentage-to-GWA mapping ensures accuracy.

## Ethical Considerations
  -User data is not stored externally to ensure privacy.
  
  -Code is written originally; no uncredited external code used.
  
  -CLI interface is accessible and inclusive.
  
  -All references properly cited according to APA style.

## How to Run
1. Download or clone this repository
2. Open terminal or command prompt
3. Navigate to the project folder
4. Run:

## Sample Run
## GWA subject grade value
=== GWA Calculator ===

Choose what grade input type(1 or 2):

1 - Percentage
2 - GWA (1.0–5.0)

> 1

Enter subject grade (or 'done' to finish): 1.5
Enter subject units: 3

> 2

Enter subject grade (or 'done' to finish): 2.0
Enter subject units: 4

> 3

Enter subject grade (or 'done' to finish): 1.75
Enter subject units: 3

> 4

Enter subject grade (or 'done' to finish): done

Your General Weighted Average (GWA) is: 1.78
Classification: Dean's Lister

Another calculation? (y/n): n
Thanks for using the program!

## Percetage subject grade value
=== GWA Calculator ===

Choose what grade input type(1 or 2):
1 - Percentage
2 - GWA (1.0–5.0)

> 1

Enter subject grade (or 'done' to finish): 85
Converted to GWA grade: 1.5
Enter subject units: 3

Enter subject grade (or 'done' to finish): 75 
Converted to GWA grade: 2.0
Enter subject units: 4

Enter subject grade (or 'done' to finish): 80
Converted to GWA grade: 1.75
Enter subject units: 3

Enter subject grade (or 'done' to finish): done

Your General Weighted Average (GWA) is: 1.77
Classification: You passed

Another calculation? (y/n): n
Thanks for using the program!


## Contributors
- Josh Nathaniel P. Pestañas
- Kingston Miguell Ilagan
- Sasha Kaye M. Directo

## References
  W3Schools. (2023). Python tutorial. https://www.w3schools.com/python/

  Association for Computing Machinery. (2018). ACM code of ethics and professional conduct. https://www.acm.org/code-of-ethics

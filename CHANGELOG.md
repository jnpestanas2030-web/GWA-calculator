#  Changelog

## v1.0.0 - 15/08/25
- Created the repository for our code: G.W.A-Calculator
- User can:
   - Calculate their G.W.A
   - Displays student’s GWA based on the user’s data for grades and corresponding units

## v2.0.0 - 28/11/25
- Can pick to input percentage subject grade values or GWA subject grade values
- Converts percentage subject grade values to GWA subject grade values
- User can:
   - Enter percentage or GWA subject grade values
   - Calculate their G.W.A
   - Displays student’s GWA based on the user’s data for grades and corresponding units

 ## v2.0.1 - 05/12/25
 - Fixed a bug wherein it wont show the final GWA
 - Corrected Grammar and changed out wording
- User can:
   - Enter percentage or GWA subject grade values
   - Calculate their G.W.A
   - Displays student’s GWA based on the user’s data for grades and corresponding units
 
## v2.1.0 – 05/02/26
- Refactored code to use functions for better readability and modularity:

      main() function for program flow.

      classify_gwa() function to determine user classification.

- Added detailed inline comments and docstrings for maintainability.

- Improved error handling for numeric inputs and units.

Features:

- Clearer prompts and input instructions.

- Console-based G.W.A. calculator remains fully functional for both percentage and G.W.A. inputs.

## v3.0.0 – 07/03/26

- Full GUI Implementation:
Replaced the console-based input/output with a Tkinter GUI.
Users can now enter grades and units via input boxes instead of typing in the console.

- Mode and Type Selection:
Users can select Percentile or GWA mode.
Users can choose Subject-level or Overall-level calculation.

- Dynamic Input Generation:
Generates input fields automatically based on the number of subjects or quarters.
Supports different layouts for GWA vs Percentile and Subject vs Overall.

- Scrollable Input Area:
Added a scrollable frame for handling large numbers of subjects or quarters.

- Real-Time Label Updates:
The label for “Number of subjects/quarters” updates automatically when the mode/type changes.

- Integrated Calculation:
The program now automatically computes results based on the inputs in the GUI:
   Percentile mode → calculates average percentile.
   GWA mode → calculates General Weighted Average (GWA) using grades and units.
Shows the result directly in the result box without using the console.

## v3.1.0 – 21/03/26


Added user assistance and saving functionality to improve usability:

New Features:

-Help Button
A new “Help” button was added. When pressed, it displays essential information on how to use the program, including explanations of each button and a simple tutorial for users.
-Save Button
A Save button was implemented. When clicked, it allows users to save their computed result (e.g., GWA or percentile), confirming that the output has been successfully stored.

User can now:

Access guidance on how to use the program through the Help feature
Save their computed results for future reference
Enter percentage or GWA subject grade values
Calculate their G.W.A
View results directly in the GUI interface

(Contributors; Pestañas, Directo, Ilagan)

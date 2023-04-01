# CS-515-A-FOC Project Adventure

## Name and Steven login
  RAMANISH REDDY EEDA   reeda@stevens.edu

## Github Repo URL
  - https://github.com/Eeda-RR/CS-515-A-FOC

## Estimate of how many hours you spent on the project
  - Around 30 hours spread across 4 days

## Description of how you tested your code
  - Firstly implemented the programming logic for individual parts of assignment 
  - Tested it using the examples presented in the problem statement document using loop.map and ambig.map files
  - After completion of entire coding, tested it on multiple mix and match of extensions and verbs implemented on the custom map file adventure_map.map file
  - Also tested using the files present in the problem statement with custom test examples
 
## Any bugs or issues you could not resolve
  - No
 
## Example of a difficult issue or bug and how you resolved
  - **Prefixed based matching**
    - To implement prefix based matching, I made use of str.startswith() but then realised while testing, 
      if a room has exits:  north northwest
      and the player command go north was actually printing a message if user would like to go north or northwest
      while ideally it should go north
    - To fix this I first made a list of all possible directions and searched if the direction given as user input is present in it
    - And then filter the list of current room exits that startswith the direction given as user input using str.startswith()
    - Adding the check to first see if the direction given as user input is present in the list of all possible directions helped to execute
      the prefix based logic 
      
  - **Printing ... after verbs that expect a target of some kind**
    - I was initially storing the valid verbs in a list
    - And was providing it as input to the execute_help method that I defined to print the list of valid verbs
    - To print ... after verbs that expect a target of some kind i was using a if condition on  the current item of list if it is present within a list of 
      verbs that expect a target of some kind that I defined within the execute_help method and it was working fine
    - But at the end of help verb extension it was mentioned, that any new command added should also be printed by help without modifications to it
    - Then figured to maintain valid verbs within project as a map with key being the verb and value representing 1 if it expects a target of some kind else 0
      
## List of Extensions you've chosen to implement
  I have chosen from the list of extensions provided within the problem statement itself.
  - Abbreviations for verbs, directions, and items
  - A help verb
  - A drop verb
  - Directions become verbs 
  
  

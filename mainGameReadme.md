10/03/2024 Initial notes.

Game: Medieval Life Simulation (pending)
Creator: RausellStudios
Credits: Angel (Programmer, Art Director, Concept Artist, Animation, Technical Artist, UI Designer, Technical Director, Audio Engineer, Creative Director).

[[ FILE STRUCTURE ]]

mainGame.py - The motherboard of our program. This is where the main workflow will occur for our current game. 
inventory.py - Deals with the storage amount and management of items existing in its vicinity.
item.py - Deals with the creation of items, space they take, and their attributes.


10/7/24
1.0
Updates: Added our graphical display into the program. That way when the game runs the image appears until exit out by the user. The image is currently a placeholder for where the text should appear as the text currently appears in our terminal not the created graphical screen.

Currently this document serves as a log for our current working progress on the game as well as keep track of what purpose each file serves. On top of the page we have a breakdown of the files currently being used. We also incorporated a brief explanation for each of the files to better understand the goals each page targets.

10/14/24
1.1

This update is centered on file mainGame.py. The changes implemented have been primarily made to the text function via the use of pygame modules.

This change includes the use of text variable tts to determine the way text will fluctuate throughout the program (specially as we begin to incorporate fluidity on information the user might need in regards to their farm).

Additionally updating the screen to center the given text in the middle will allow us to further explore the other methods of text formatting to screen approaches we can take as we develop the UI for this farming simulation system.

Next updates will focus on the fluidity of text for user information based on the user input. As well as revamping the item/inventory files to become more consistent with a farming simulation item system that changes via user input.

The code at the moment should update these changes made only to mainGame.py. More information on the actions each module does on the program can be spotted in mainGame.py (to transfer later into a more technical README.md file).
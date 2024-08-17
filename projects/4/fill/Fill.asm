// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/4/Fill.asm

// Runs an infinite loop that listens to the keyboard input. 
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel. When no key is pressed, 
// the screen should be cleared.

//Pseudocode:

//Define top limit of display:

//n = @24576 - 16384 (no. registers between start and finish)

//Checkloop:
//	Check if keyboard value greater than zero:
//		Greater: Jump to blackloop
//		Else:    Jump to Whiteloop

//Whiteloop:
//	for i = 16384, i < 24576, i++{
//		@i = 0
//	}
//	Goto Checkloop

//Blackloop:
//	for i = 16384, i < 24576, i++{
//		@i = -1
//	}
//	Goto Checkloop

//Check Loop and Variable Initialization

(CHECK)
@8192
D=A
@N
M=D
@i
M=0
@KBD //Check Keyboard
D=M
@BLACK //If < 0, go to black loop
D;JGT
@WHITE //Else go to white loop
D;JEQ
@CHECK // If < 0, stay in check
D;JLT

//Blackloop
(BLACK) 
@SCREEN //Get Screen Address
D=A 
@i 
D=D+M //Get point in iteraiton, starting at 0 going to last register of screen
A=D
M=-1  //Set pixels
@i    //Add one to iterator
M=M+1
D=M
@N
D=M-D //Compare point in iteration to final register address
@CHECK //Jump to appropriate block
D;JEQ
@BLACK
D;JGT

//The code below works the same as above.
//Whiteloop
(WHITE)
@SCREEN
D=A
@i
D=D+M
A=D
M=0
@i
M=M+1
D=M
@N
D=M-D
@CHECK
D;JEQ
@WHITE
D;JGT





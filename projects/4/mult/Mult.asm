// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/4/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)
// The algorithm is based on repetitive addition.



//Establish variables and values.
@i
M = 0
@R1
D = M
@n
M = D
@pro
M = 0
// Below we have a while loop with an initial increment increase.

(LOOP)

@i
M=M+1
D=M
@n
D = D - M
@STOP
D;JGT

// Add value of R0 to @pro (product)
@R0
D=M
@pro
M=M+D
@LOOP
0;JMP

//Loop Condition is met, put @pro into R2
(STOP)
@pro
D=M
@R2
M=D
@END
0;JMP

//End Of Program
(END)
@END
0;JMP

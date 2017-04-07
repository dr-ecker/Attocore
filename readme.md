# The Attocore Tiny CPU

The Attocore is definitely not the smallest computer possible, as has been proven by Alan Turing.  However, it is very, very small compared to any modern computer and actually a fair bit smaller than many of the classic CPUs such as the Z80.  The Attocore doesn't have "a cache" or "literally any concept of a protected mode" or even "multiply operations".  The Attocore is minimalist enough that it fits on a few pages of Verilog code, thus making it a great candidate for learning the basics of very low-level programming.

I started the Attocore project because the soft processors available on certain FPGA systems seemed to have an awful lot of strings attached for something that theoretically is an easy drop-in of some chunk of verilog code, which then talks to some 0's and 1's.  In short, the Attocore is what I wish my students had as their first soft processor.  (Or rather, the best, cleaned-up, deeply-tested, works-every-time version of it is.)


## Features:

- 8-bit instructions and data words
- 16-bit address space
- 16 registers (8 of which are special-purpose)
- 1 laughably-underpowered ALU
- No Cache
- No Stack
- No Protected Mode
- No MMU
- No Floating Point
- No Multiply Operation
- No Branch Pointer
- No Interrupts
- Basically No Advanced Features Of Any Kind Honestly


## Special-Purpose Registers:
- ADDR: r0 and r1 are a combined register that stores 16-bit addresses. r0 is LSB, r1 MSB.
- PC: r2 and r3 make up the program counter, which also is 16 bits.
- IR: r4 stores the current active instructions
- ALU A: ALU left operand
- ALU B: ALU right operand
- ALU Y: ALU output


## Instruction Set:

The Attocore has 6 instructions:

**No Op:** Do nothing.  
**Binary:** 00000000

**Jump:** Program Jump.  Note that the address for the jump comes from ADDR.  
**Binary:** 0010000x, x = conditional jump, only if ALU lsb is zero

**Arithmatic:** Calculation on ALU.  Just clocks sets ALU operation select and clocks ALU Y.  
**Binary:** 010[op], op = 5-bit operation select

**Value Set:** Store a specified value in a register.  Note that this operation takes two words.  
**Binary:** 0110[reg], reg = 4-bit register select, including special purpose registers.  
**Binary:** [word], word = the 8-bit word to be stored.

**Read:** Read a value from memory to a specified register.  Note that the address for read comes from ADDR.  
**Binary:** 1000[reg], reg = 4-bit register select, including special purpose registers.

**Write:** Write a value to memory from a specified register.  Note that the address for write comes from ADDR.  
**Binary:** 1010[reg], reg = 4-bit register select, including special purpose registers.

**Copy:** Overwrite one register with another register's contents.  
**Binary:** (src reg)(dest reg), two 4-bit register selects, including special purpose registers.

## Add-Ons:

The attocore proper is contained entirely in cpu.v, but for usability it comes with a ROM, a RAM, an address selector, a test bench, and a sample program.  Other features planned will not be mentioned for fear of not getting them done.

__The Attocore Will Return, But You Have To Push All Zeroes Into ADDR First.__

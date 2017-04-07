module rom(address, data, cs);
 input [9:0]address;
 output [7:0]data;
 input cs;

 reg [7:0] mem [0:1023];

 assign data=(cs)?mem[address]:8'bz;

 initial begin
     $readmemb("rom.txt", mem);
 end
endmodule

module sel64(sel,out);

 input [5:0] sel  ;
 output [63:0] out; 

 assign out = 1 << sel;

endmodule

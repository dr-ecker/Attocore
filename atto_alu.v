module atto_alu(control, a, b, y);
 input [3:0]control;
 input [7:0]a;
 input [7:0]b;
 output reg [7:0]y;

 
 always@(*)
 begin
     case(control)
         0:y=a+b;
         1:y=a-b;
         2:y=a>b;
         3:y=a<b;
         4:y=a==b;
         5:y=a<<b;
         6:y=a>>b;
     endcase
 end
endmodule

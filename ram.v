module ram(address, data, cs,rw,clock);
 input [9:0]address;
 output [7:0]data;
 input cs;
 input rw;
 input clock;

 reg [7:0] mem [0:1023];
 reg [7:0] dataout;

 wire [7:0]addr0;
 wire [7:0]addr1;
 assign addr0=mem[0];
 assign addr1=mem[1];

 always@(posedge clock)
 begin
     if(cs)
     begin
         if(rw)
         begin
             mem[address]=data;
         end
         else
         begin
             dataout=mem[address];
         end
     end
 end

 assign data=(cs&&~rw)?dataout:8'bz;

 initial begin
     dataout=8'bz;
 end
endmodule

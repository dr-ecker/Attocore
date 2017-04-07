module bench;
 reg clock,reset;
 wire data_dir;
 reg [7:0]data_in;
 wire [15:0]address_bus;
 wire [7:0]data_bus;
 wire [63:0]memselect;

 attocore a1(clock, reset, data_dir, data_bus, address_bus);
 sel64 s1(address_bus[15:10],memselect);
 rom r1(address_bus[9:0],data_bus,memselect[0]);
 ram m1(address_bus[9:0],data_bus,memselect[1],~data_dir,clock);

 initial begin
     $dumpvars(0,bench);
     reset=0;
     clock=0;
     data_in=0;
     #5;
     reset=1;
     #7000;
     $finish;
 end

 always begin
     #10 clock=~clock;
 end
endmodule

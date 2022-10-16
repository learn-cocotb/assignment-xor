module xor_test(
	input wire a,
	input wire b,
	output wire y
);
xor_gate xor_gate(
	.a(a),
	.b(b),
	.y(y)
);

initial begin
	$dumpfile("or.vcd");
	$dumpvars;
end
endmodule
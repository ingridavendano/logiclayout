--http://vhdlguru.blogspot.com/p/example-codes.html

--libraries to be used are specified here
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;


--entity declaration with port definitions
entity rc_adder is
port(	num1:	in std_logic_vector(3 downto 0);  --4 bit input 1
		num2:	in std_logic_vector(3 downto 0);  -- 4 bit input 2
		sum:	out std_logic_vector(3 downto 0);   -- 4 bit sum
		carry:	out std_logic   -- carry out.
);
end rc_adder;


--architecture of entity
architecture Behavioral of rc_adder is

--temporary signal declarations(for intermediate carry's).
signal c0,c1,c2,c3 : std_logic := '0';
begin
	--first full adder
	sum(0) <= num1(0) xor num2(0);	--sum calculation
	c0 <= num1(0) and num2(0);		--carry calculation
	
	--second full adder
	sum(1) <= num1(1) xor num2(1) xor c0;
	c1 <= (num1(1) and num2(1)) or (num1(1) and c0) or (num2(1) and c0);
	
	--third full adder
	sum(2) <= num1(2) xor num2(2) xor c1;
	c2 <= (num1(2) and num2(2)) or (num1(2) and c1) or (num2(2) and c1);
	
	--fourth(final) full adder
	sum(3) <= num1(3) xor num2(3) xor c2;
	c3 <= (num1(3) and num2(3)) or (num1(3) and c2) or (num2(3) and c2);
	
	--final carry assignment
	carry <= c3;

end Behavioral;

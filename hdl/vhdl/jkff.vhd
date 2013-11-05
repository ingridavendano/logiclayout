----------------------------------------------
-- JK Flip-Flop with reset 
-- (ESD book Chapter 2.3.1)
-- by Weijun Zhang, 04/2001
--
-- the description of JK Flip-Flop is based 
-- on functional truth table
-- concurrent statement and signal assignment
-- are using in this example 
----------------------------------------------

library ieee;
use ieee.std_logic_1164.all;

----------------------------------------------

entity JK_FF is
port (	clock:		in std_logic;
		J, K:		in std_logic;
		reset:		in std_logic;
		Q, Qbar:	out std_logic
);
end JK_FF;

-----------------------------------------------

architecture behv of JK_FF is

	-- define the useful signals here

	signal state: std_logic;
	signal input: std_logic_vector(1 downto 0);

begin

	-- combine inputs into vector
	input <= J & K;		

	p: process(clock, reset) is
	begin
	
	if (reset='1') then
		state <= '0';
	elsif (rising_edge(clock)) then

			-- compare to the truth table
		case (input) is
		when "11" =>
			state <= not state;
		when "10" =>
			state <= '1';
		when "01" =>
			state <= '0';
		when others =>
			null;
		end case;
	end if;

	end process;
	
	-- concurrent statements
	Q <= state;
	Qbar <= not state;

end behv;

-------------------------------------------------

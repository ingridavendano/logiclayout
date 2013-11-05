---------------------------------------------
-- D Flip-Flop (ESD book Chapter 2.3.1)
-- by Weijun Zhang, 04/2001
--
-- Flip-flop is the basic component in 
-- sequential logic design
-- we assign input signal to the output 
-- at the clock rising edge 
---------------------------------------------

library ieee ;
use ieee.std_logic_1164.all;
use work.all;

---------------------------------------------

entity dff is
port(	data_in:	in std_logic;
		clock:		in std_logic;
		data_out:	out std_logic
);
end dff;

----------------------------------------------

architecture behv of dff is
begin

	process(data_in, clock)
	begin

		-- clock rising edge

	if (clock='1' and clock'event) then
		data_out <= data_in;
	end if;

	end process;	

end behv;

----------------------------------------------

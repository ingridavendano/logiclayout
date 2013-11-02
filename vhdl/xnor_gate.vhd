--------------------------------------
-- XOR gate (ESD figure 2.3)
--
-- two descriptions provided
--------------------------------------

library ieee;
use ieee.std_logic_1164.all;

--------------------------------------

entity XNOR_ent is
port(	x: in std_logic;
		y: in std_logic;
		F: out std_logic
);
end XNOR_ent;

---------------------------------------

architecture behv1 of XNOR_ent is
begin

	process(x, y)
	begin
		-- compare to truth table
		if (x/=y) then
		F <= '0';
	else
		F <= '1';
	end if;
	end process;

end behv1;

architecture behv2 of XNOR_ent is 
begin 

	F <= x xnor y; 

end behv2;

---------------------------------------

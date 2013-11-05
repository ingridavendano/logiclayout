--------------------------------------
-- OR gate (ESD book figure 2.3)
--
-- two descriptions provided
--------------------------------------

library ieee;
use ieee.std_logic_1164.all;

--------------------------------------

entity OR_ent is
port(	x: in std_logic;
	y: in std_logic;
	F: out std_logic
);
end OR_ent;

---------------------------------------

architecture OR_arch of OR_ent is
begin

	process(x, y)
	begin
		-- compare to truth table
		if ((x='0') and (y='0')) then
		F <= '0';
	else
		F <= '1';
	end if;
	end process;

end OR_arch;

architecture OR_beh of OR_ent is 
begin

	F <= x or y; 

end OR_beh;

---------------------------------------

-----------------------------------------
-- NAND gate (ESD figure 2.3)
-- 
-- two descriptions provided
-----------------------------------------

library ieee;
use ieee.std_logic_1164.all;

------------------------------------------

entity NAND_ent is
port(	x: in std_logic;
	y: in std_logic;
	F: out std_logic
);
end NAND_ent;

------------------------------------------

architecture behv1 of NAND_ent is
begin

	process(x, y)
	begin
		-- compare to truth table
		if (x='1' and y='1') then
		F <= '0';
	else
		F <= '1';
	end if;
	end process;

end behv1;

-----------------------------------------

architecture behv2 of NAND_ent is 
begin 

	F <= x nand y; 

end behv2;

-----------------------------------------

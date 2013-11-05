--------------------------------------------------
-- AND gate (ESD book figure 2.3)		
-- two descriptions provided
--------------------------------------------------

library ieee;
use ieee.std_logic_1164.all;

--------------------------------------------------

entity AND is
port(	x: in std_logic;
	y: in std_logic;
	F: out std_logic
);
end AND;  

--------------------------------------------------

-- architecture behav of AND is
-- begin

-- 	process(x, y)
-- 	begin
-- 		-- compare to truth table
-- 		if ((x='1') and (y='1')) then
-- 			F <= '1';
-- 		else
-- 			F <= '0';
-- 		end if;
-- 	end process;

-- end behav;

architecture behav of AND is
begin

	F <= x and y;

end behav;

--------------------------------------------------

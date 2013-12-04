/* -------------------------------------------------------------------------
 * display.js
 * Created by Ingrid Avendano on 12/3/13. 
 * -------------------------------------------------------------------------
 * Contains functions to display a circuit schematic.
 * ------------------------------------------------------------------------- */

// text box submits because enter key is hit
$("logic-expression").bind("keypress", {}, keypressInBox);

function keypressInBox(event) {
	var code = (event.keyCode ? event.keyCode : event.which);

	// enter button keycode is 13
	if (code == 13) {
		alert('works!');
		event.preventDefault();

		$("logic-expression").submit();
	}
};

// zooms the project window view of the circuit schematic
var zoom = $('.slider').slider().on('slide', zoomCanvas).data('slider');

function zoomCanvas(event) {
	paper.project.view.zoom = zoom.getValue();
}

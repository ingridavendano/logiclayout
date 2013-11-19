/* ----------------------------------------------------------------------------
 * logicgates.js
 * Created by Ingrid Avendano on 11/18/13. 
 *	
 * Contains the JS Canvas functions to draw logic gates. 
 * ------------------------------------------------------------------------- */



function gate(ctx, x, y, scale) {

}




function drawNotGate(ctx, x, y, scale, color) {
	ctx.fillStyle = color;

	// // setting up stroke for gate
	ctx.lineWidth = 5*scale;

	// triangle portion of the not gate
	var offset = -5;
	ctx.beginPath();
	ctx.moveTo(x, y);
	ctx.lineTo(x-74*scale-offset, y+48*scale);
	ctx.lineTo(x-74*scale-offset, y-48*scale);
	ctx.closePath()
	ctx.fill();
	ctx.stroke();

	// circle at the front of the not gate
	ctx.beginPath();
	ctx.arc(x+10*scale, y, 12*scale, 0, 2*Math.PI, false);
	ctx.closePath();
	ctx.fill();
	// ctx.stroke();
}

function drawAndGate(ctx, x, y, scale, color) {
	ctx.fillStyle = color;

	// setting up stroke for gate
	ctx.lineWidth = 5*scale;
	ctx.strokeStyle = "rgb(0,0,0)";

	// circle portion of the not gate
	var offset = -5;
	ctx.beginPath();
	ctx.arc(x, y, 50*scale, 0.5*Math.PI, 1.5*Math.PI, true);
	ctx.lineTo(x-75*scale-offset, y-50*scale);
	ctx.lineTo(x-75*scale-offset, y+50*scale);
	ctx.lineTo(x, y+50*scale);
	ctx.closePath()
	ctx.fill();
	ctx.stroke();
}


function drawNandGate(ctx, x, y, scale, color) {
	drawAndGate(ctx, x, y, scale, color);
	ctx.fillStyle = color;

	// setting up stroke for gate
	ctx.lineWidth = 5*scale;
	ctx.strokeStyle = "rgb(0,0,0)";

	// circle at the front of the not gate
	ctx.beginPath();
	ctx.arc(x+10*scale+52, y, 12*scale, 0, 2*Math.PI, false);
	ctx.closePath();
	ctx.fill();
	ctx.stroke();
}

function drawOrGate(ctx, x, y, scale, color) {
	ctx.fillStyle = color;

	// setting up stroke for gate
	ctx.lineWidth = 5*scale;
	ctx.strokeStyle = "rgb(0,0,0)";

	var offset = -5;
	ctx.beginPath();
	ctx.moveTo(x-75*scale-offset, y+50*scale);
	ctx.quadraticCurveTo(x, y+50*scale, x+50*scale, y);
	ctx.quadraticCurveTo(x, y-50*scale, x-75*scale-offset, y-50*scale);
	ctx.moveTo(x-75*scale-offset, y-50*scale);
	ctx.bezierCurveTo(x-35*scale, y-25*scale, x-35*scale, y+25*scale, x-75*scale-offset, y+50*scale);

	ctx.fill();
	ctx.stroke();
}

function drawNorGate(ctx, x, y, scale, color) {
	drawOrGate(ctx, x, y, scale, color);
	ctx.fillStyle = color;

	// setting up stroke for gate
	ctx.lineWidth = 5*scale;
	ctx.strokeStyle = "rgb(0,0,0)";

	// circle at the front of the not gate
	ctx.beginPath();
	ctx.arc(x+10*scale+52, y, 12*scale, 0, 2*Math.PI, false);
	ctx.closePath();
	ctx.fill();
	ctx.stroke();
}

function drawXorGate(ctx, x, y, scale, color) {
	drawOrGate(ctx, x, y, scale, color);
	ctx.fillStyle = color;

	// setting up stroke for gate
	ctx.lineWidth = 5*scale;
	ctx.strokeStyle = "rgb(0,0,0)";

	var xOffset = 15;
	var yOffset = 0;
	ctx.moveTo(x-75*scale-xOffset, y-50*scale+yOffset);
	ctx.bezierCurveTo(x-35*scale-xOffset, y-25*scale, x-35*scale-xOffset, y+25*scale, x-75*scale-xOffset, y+50*scale-yOffset);
	ctx.stroke();
}

function drawNxorGate(ctx, x, y, scale, color) {
	drawXorGate(ctx, x, y, scale, color);
	ctx.fillStyle = color;

	// setting up stroke for gate
	ctx.lineWidth = 5*scale;
	ctx.strokeStyle = "rgb(0,0,0)";

	// circle at the front of the not gate
	ctx.beginPath();
	ctx.arc(x+10*scale+52, y, 12*scale, 0, 2*Math.PI, false);
	ctx.closePath();
	ctx.fill();
	ctx.stroke();
}



function draw(x, y, scale) {

	var canvas = document.getElementById('schematic')

	if (canvas.getContext) {
		var ctx = canvas.getContext('2d');

		// setting up stroke for gate
		
		ctx.strokeStyle = "rgb(0,0,0)";

		drawNotGate(ctx, x+600, y+100, scale, "#E5CCFF");
		ctx.stroke();

		drawAndGate(ctx, x, y, scale, "#FFFFCC");
		drawNandGate(ctx, x, y+200, scale, "#CCFFFF");

		drawOrGate(ctx, x+200, y, scale, "#FFCCE5");
		drawNorGate(ctx, x+200, y+200, scale, "#CCCCFF");

		drawXorGate(ctx, x+400, y, scale, "#FFE5CC");
		drawNxorGate(ctx, x+400, y+200, scale, "#CCFFCC");

		
	}
}
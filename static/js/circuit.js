/* ----------------------------------------------------------------------------
 * circuit.js
 * Created by Ingrid Avendano on 11/20/13. 
 * ----------------------------------------------------------------------------
 * Contains the JS Canvas functions to draw logic gates. 
 * ------------------------------------------------------------------------- */


function andGate(x, y, h, l) {

	var topLeft = new Point(x - l/2, y - h/2);
	var bottomLeft = new Point(x - l/2, y + h/2);
	var leftLine = new Path.Line(bottomLeft, topLeft);
	leftLine.strokeColor = 'black';

}

function drawCircuit() {
	andGate(100, 100, 50, 50);
}



// // main body of and gate
// function andGate(ctx, x, y, height, length) {
// 	ctx.save();
// 	ctx.beginPath();
// 	ctx.arc(x, y, height/2, 1.5*Math.PI, 0.5*Math.PI, false);
// 	ctx.lineTo(x - length*0.75, y + height/2);
// 	ctx.lineTo(x - length*0.75, y - height/2);
// 	ctx.closePath()
// 	ctx.fill();
// 	ctx.stroke();
// 	ctx.restore();
// }

// // create a nand gate out of and gate and not symbol
// function drawAndGate(ctx, x, y, scale, color, inputs) {
// 	ctx.fillStyle = color;
// 	ctx.lineWidth = 3*scale;

// 	var increment = 30*scale;
// 	var height = increment*inputs;
// 	var length = height;
// 	var radius = height*0.2;
// 	var mid_increment = increment/2;

// 	var outputPoints = [];

// 	for (var i=0; i < inputs; i++){
// 		var tick_y = (y - height/2) + mid_increment + increment*i;
// 		var tick_x = x - length*0.75;
// 		drawYTicks(ctx, tick_x, tick_y);
// 	} 

	

// 	andGate(ctx, x, y, height, length);
// 	centerPoint(ctx, x, y, scale);

// 	// drawYTicks(ctx, x, y)
// }


// function draw(x, y, scale) {

// 	var canvas = document.getElementById('schematic')

// 	if (canvas.getContext) {
// 		var ctx = canvas.getContext('2d');
// 		ctx.strokeStyle = "#404040";
	
// 		drawInput(ctx, x+20, y, scale, "#ff6c48");
// 		drawInput(ctx, x+20, y+40, scale, "#ff6c48");
// 		// drawAndGate(ctx, x+200, y+20, scale, "#ff4980");
// 		drawAndGate(ctx, x+200, y+20, scale, "#ff4980", 3);
// 		// drawNodes(ctx, 400, 400, 20);
// 		// drawNandGate(ctx, x, y+200, scale, "#F0FFF0");
	
// 		// drawOrGate(ctx, x+150, y, scale, "#F0FFF0");
// 		// drawNorGate(ctx, x+150, y+200, scale, "#F0FFF0");

// 		// drawXorGate(ctx, x+320, y, scale, "#F0FFF0");
// 		// drawNxorGate(ctx, x+320, y+200, scale, "#F0FFF0");

// 		// drawNotGate(ctx, x+450, y+100, scale, "#F0FFF0");

// 		// drawInput(ctx, x+300, y+300, scale, "#F0FFF0");
// 		// drawOutput(ctx, x+300, y+100, scale, "#F0FFF0");
// 	}
// }

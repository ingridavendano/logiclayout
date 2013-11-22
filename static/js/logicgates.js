/* ----------------------------------------------------------------------------
 * logicgates.js
 * Created by Ingrid Avendano on 11/18/13. 
 * ----------------------------------------------------------------------------
 * Contains the JS Canvas functions to draw logic gates. 
 * ------------------------------------------------------------------------- */

// visual reference point to where the center of a gate is
function centerPoint(ctx, x, y, scale) {
	ctx.save();
	ctx.fillStyle = "black";
	ctx.fillRect(x-2, y-2, 4, 4);
	ctx.restore();
}

// the circle in front of gate the designates it as "not"
function notCircleSymbol(ctx, x, y, radius) {
	ctx.save();
	ctx.beginPath();
	ctx.arc(x + radius, y, radius, 0, 2*Math.PI, false);
	ctx.closePath()

	// coloring for the not symbol
	ctx.fill();
	ctx.stroke();
	ctx.restore();
}

/* ------------------------------------------------------------------------- */

// main body of not gate - the triangle
function notGate(ctx, x, y, height, length) {
	ctx.save();
	ctx.beginPath();
	ctx.moveTo(x + length/2, y);
	ctx.lineTo(x - length/2, y + height);
	ctx.lineTo(x - length/2, y - height);
	ctx.closePath()
	ctx.fill();
	ctx.stroke();
	ctx.restore();
}

// draw a not gate and establishes color
function drawNotGate(ctx, x, y, scale, color) {
	ctx.fillStyle = color;
	ctx.lineWidth = 3*scale;

	var height = 40*scale;
	var length = height*1.5;
	var radius = height*0.2; 

	// not gate drawn to the scale where x, y are in the center
	notGate(ctx, x, y, height, length);
	notCircleSymbol(ctx, x + length/2, y, radius);
	// centerPoint(ctx, x, y, scale);
}

/* ------------------------------------------------------------------------- */



// main body of and gate
function andGate(ctx, x, y, height, length) {
	ctx.save();
	ctx.beginPath();
	ctx.arc(x, y, height, 1.5*Math.PI, 0.5*Math.PI, false);
	ctx.lineTo(x - length*0.75, y + height);
	ctx.lineTo(x - length*0.75, y - height);
	ctx.closePath()
	ctx.fill();
	ctx.stroke();
	ctx.restore();
}

// draw an and gate and give it color
function drawAndGate(ctx, x, y, scale, color) {
	ctx.fillStyle = color;
	ctx.lineWidth = 3*scale;

	var height = 40*scale;
	var length = 60*scale;

	andGate(ctx, x, y, height, length);
	// centerPoint(ctx, x, y, scale);
}

// create a nand gate out of and gate and not symbol
function drawNandGate(ctx, x, y, scale, color) {
	ctx.fillStyle = color;
	ctx.lineWidth = 3*scale;

	var height = 40*scale;
	var length = 60*scale;
	var radius = 8*scale; 

	andGate(ctx, x, y, height, length);
	notCircleSymbol(ctx, x + height, y, radius);
	centerPoint(ctx, x, y, scale);
}

/* ------------------------------------------------------------------------- */

function orGate(ctx, x, y, height, length) {
	ctx.save();
	ctx.beginPath();
	ctx.moveTo(x - length*0.75, y + height);
	ctx.quadraticCurveTo(x + length/4, y + height, x + length*0.75, y);
	ctx.quadraticCurveTo(x + length/4, y - height, x - length*0.75, y - height);
	ctx.moveTo(x - length*0.75, y - height);
	ctx.bezierCurveTo(x - length/4, y - height/2, x - length/4, y + height/2, x - length*0.75, y + height);
	ctx.fill();
	ctx.stroke();
	ctx.restore();
}

function drawOrGate(ctx, x, y, scale, color) {
	ctx.fillStyle = color;
	ctx.lineWidth = 3*scale;

	var height = 40*scale;
	var length = 60*scale;

	orGate(ctx, x, y, height, length);
	// centerPoint(ctx, x, y, scale);
}

function drawNorGate(ctx, x, y, scale, color) {
	ctx.fillStyle = color;
	ctx.lineWidth = 3*scale;

	var height = 40*scale;
	var length = 60*scale;
	var radius = 8*scale; 

	orGate(ctx, x, y, height, length);
	notCircleSymbol(ctx, x + length*0.75, y, radius);
	centerPoint(ctx, x, y, scale);
}

/* ------------------------------------------------------------------------- */

function xorGate(ctx, x, y, height, length) {
	var offset = height/10;

	orGate(ctx, x, y, height, length);

	ctx.save();
	ctx.beginPath();
	ctx.moveTo(x - length-offset, y - height);
	ctx.bezierCurveTo(x - length/2, y - height/2, x - length/2, y + height/2, x - length -offset, y + height);
	ctx.stroke();
	ctx.restore();

}

function drawXorGate(ctx, x, y, scale, color) {
	ctx.fillStyle = color;
	ctx.lineWidth = 3*scale;

	var height = 40*scale;
	var length = 60*scale;

	xorGate(ctx, x, y, height, length);
	// centerPoint(ctx, x, y, scale);
}

function drawNxorGate(ctx, x, y, scale, color) {
	ctx.fillStyle = color;
	ctx.lineWidth = 3*scale;

	var height = 40*scale;
	var length = 60*scale;
	var radius = 8*scale;

	xorGate(ctx, x, y, height, length);
	notCircleSymbol(ctx, x + length*0.75, y, radius);
	// centerPoint(ctx, x, y, scale);
}

/* ------------------------------------------------------------------------- */

function inputPin(ctx, x, y, height, length) {
	ctx.save();
	ctx.beginPath();
	ctx.moveTo(x + length/2, y - height/2);
	ctx.lineTo(x - length/2, y - height/2);
	ctx.lineTo(x - length/2, y + height/2);
	ctx.lineTo(x + length/2, y + height/2);
	ctx.lineTo(x + length, y);
	ctx.closePath()
	ctx.fill();
	ctx.stroke();
	ctx.restore();
}

function outputPin(ctx, x, y, height, length) {
	ctx.save();
	ctx.beginPath();
	ctx.moveTo(x - length/2, y - height/2);
	ctx.lineTo(x + length/2, y - height/2);
	ctx.lineTo(x + length/2, y + height/2);
	ctx.lineTo(x - length/2, y + height/2);
	ctx.lineTo(x - length, y);
	ctx.closePath()
	ctx.fill();
	ctx.stroke();
	ctx.restore();
}


function drawInput(ctx, x, y, scale, color) {
	ctx.fillStyle = color;
	ctx.lineWidth = 3*scale;

	var height = 20*scale;
	var length = 40*scale;

	inputPin(ctx, x, y, height, length);
	// centerPoint(ctx, x, y, scale);
}

function drawOutput(ctx, x, y, scale, color) {
	ctx.fillStyle = color;
	ctx.lineWidth = 3*scale;

	var height = 20*scale;
	var length = 40*scale;

	outputPin(ctx, x, y, height, length);
	// centerPoint(ctx, x, y, scale);
}

/* ------------------------------------------------------------------------- */

function drawXTicks(ctx, x, y) {
	ctx.strokeStyle = "#CCFFFF";
	ctx.lineWidth = 1/2;
	ctx.save();
	ctx.moveTo(x,y-4);
	ctx.lineTo(x,y+4);
	ctx.fill();
	ctx.stroke();
	ctx.restore();
}

function drawYTicks(ctx, x, y) {
	ctx.strokeStyle = "#CCCCFF";
	ctx.lineWidth = 1/2;
	ctx.save();
	ctx.moveTo(x-4,y);
	ctx.lineTo(x+4,y);
	ctx.fill();
	ctx.stroke();
	ctx.restore();
}

function outlineWindow(ctx, xWin, yWin, xTicks, yTicks) {
	ctx.strokeStyle = "#000000";
	ctx.lineWidth = 2;
	ctx.save();
	ctx.strokeRect(0,0,xWin,yWin);
	ctx.closePath();
	ctx.restore();


	var xIncrement = xWin/xTicks;
	var yIncrement = yWin/yTicks;
	for (var i=1; i < xTicks; i++) {
		for (var j=1; j < yTicks; j++) {
			drawXTicks(ctx, xIncrement*i, yIncrement*j);
		}
	}

	
	for (var i=1; i < yTicks; i++) {
		for (var j=1; j < xTicks; j++) {
			drawYTicks(ctx, xIncrement*j, yIncrement*i);
		}
	}

	// ctx.moveTo(0,0);
	// ctx.lineTo(0,yWin);
	ctx.closePath();
	ctx.fill();
	ctx.stroke();
	ctx.restore();
}

/* ------------------------------------------------------------------------- */

function drawNodes(ctx, x, y, size, kind) {
	ctx.fillStyle = "#CC99FF";
	// ctx.lineWidth = 2;
	// ctx.save();
	// ctx.moveTo(x-size/2,y-size/2);
	// ctx.lineTo(x-size/2,y+size/2);
	// ctx.lineTo(x+size/2,y+size/2);
	// ctx.lineTo(x+size/2,y-size/2);
	// ctx.closePath();
	// ctx.fill();
	// ctx.stroke();
	// ctx.restore();

	if (kind == 'and') {
		drawAndGate(ctx, x, y, size, "#F0FFF0");
	} else if (kind == 'or') {
		drawOrGate(ctx, x, y, size, "#F0FFF0");
	} else if (kind == 'xor') {
		drawXorGate(ctx, x, y, size, "#F0FFF0");
	} else if (kind == 'pin') {
		drawInput(ctx, x, y, size, "#bde5b9");
	} else if (kind == 'output') {
		drawOutput(ctx, x, y, size, "#bde5b9");
	} else if (kind == 'not') {
		drawNotGate(ctx, x, y, size, "#F0FFF0");
	}
}  


function draw(x, y, scale) {

	var canvas = document.getElementById('schematic')

	if (canvas.getContext) {
		var ctx = canvas.getContext('2d');
		ctx.strokeStyle = "#404040";
	
		drawAndGate(ctx, x, y, scale, "#F0FFF0");
		drawNodes(ctx, 400, 400, 20);
		// drawNandGate(ctx, x, y+200, scale, "#F0FFF0");
	
		// drawOrGate(ctx, x+150, y, scale, "#F0FFF0");
		// drawNorGate(ctx, x+150, y+200, scale, "#F0FFF0");

		// drawXorGate(ctx, x+320, y, scale, "#F0FFF0");
		// drawNxorGate(ctx, x+320, y+200, scale, "#F0FFF0");

		// drawNotGate(ctx, x+450, y+100, scale, "#F0FFF0");

		// drawInput(ctx, x+300, y+300, scale, "#F0FFF0");
		// drawOutput(ctx, x+300, y+100, scale, "#F0FFF0");
	}
}

/* ------------------------------------------------------------------------- */

function drawSchematic(xWin, yWin, circuit) {
	// var x = 100;
	// var y = 100;
	var scale = 1;

	// determining the x-axis
	var xTicks = circuit.depth; 
	var yTicks = circuit.weight;


	var xIncrement = (xWin/xTicks);
	var yIncrement = (yWin/yTicks);
	var xStartingPoint = xWin - xIncrement/2;
	

	var xNodeIncr = xIncrement/2;
	var	yNodeIncr = yIncrement/2;

	var canvas = document.getElementById('schematic');

	if (canvas.getContext) {
		var ctx = canvas.getContext('2d');
		ctx.strokeStyle = "#404040";

		outlineWindow(ctx, xWin, yWin, xTicks, yTicks);

		// run through each level
		for (var i=0; i<circuit.depth; i++) {

			var x = xStartingPoint - i*xIncrement;
			var yStartingPoint = 0;
		

			// run through each cluster
			for (var j=0; j<circuit.levels[i].length; j++) {

				// var yTempIncr = 
				// run through nodes in cluser
				for (var k=0; k<circuit.levels[i][j].length; k++) {
					console.log(circuit.levels[i][j][k].name);
					console.log(circuit.levels[i][j][k].weight);

					var y = yStartingPoint + (circuit.levels[i][j][k].weight * yIncrement)/2;

					var kind = circuit.levels[i][j][k].type;
					if (circuit.levels[i][j][k].level == 0) {
						kind = 'output';
					}

					drawNodes(ctx, x, y, 0.5, kind);

					yStartingPoint += circuit.levels[i][j][k].weight*yIncrement;

				}

				
			}
		}

		

		// if (firstGate == 'OR') {
		// 	drawOrGate(ctx, x+150, y+150, scale, "#F0FFF0");
		// }
	}
	return false;
}


// function drawSchematic(xWin, yWin, circuit) {

// 	var x = 100;
// 	var y = 100;
// 	var scale = 1;

// 	// determining the x-axis
// 	var levels = circuit.levels;
// 	var xTicks = levels; 
// 	var yTicks = circuit.weight;


// 	var xIncrement = (xWin/xTicks)/2;
// 	var yIncrement = (yWin/yTicks)/2;
// 	var xStartingPoint = xWin - xIncrement;
// 	var yStartingPoint = yWin;

// 	var firstGate = circuit.input.type;
// 	console.log(firstGate);

// 	var canvas = document.getElementById('schematic');

// 	if (canvas.getContext) {
// 		var ctx = canvas.getContext('2d');
// 		ctx.strokeStyle = "#404040";

// 		outlineWindow(ctx, xWin, yWin, xTicks, yTicks);


// 		// output
// 		var outputName = circuit.output.name;
// 		var outputLevel = circuit.output.level;
// 		drawInput(ctx, xStartingPoint - xIncrement*outputLevel, yStartingPoint/2, scale, "#F0FFF0");

// 		drawNodes(ctx, x, y, circuit.inputs);



// 		// if (firstGate == 'OR') {
// 		// 	drawOrGate(ctx, x+150, y+150, scale, "#F0FFF0");
// 		// }
// 	}
// 	return false;
// }







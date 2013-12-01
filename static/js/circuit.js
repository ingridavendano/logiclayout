/* ----------------------------------------------------------------------------
 * circuit.js
 * Created by Ingrid Avendano on 11/20/13. 
 * ----------------------------------------------------------------------------
 * Contains the JS Canvas functions to draw logic gates. 
 * ------------------------------------------------------------------------- */

function drawLine(a, b) {
	var net = new Path.Line(a, b);
	net.strokeColor = 'black';
	net.strokeWidth = 2;
}

function drawAndGate(x, y, size, inputs, netPoint) {

	// determine height and length based on inputs
	var h = size*inputs;
	var l = h;
	var midPoint = size/2; 

	var gate = new Path({
		strokeColor: 'black', 
		strokeWidth: 2,
	});

	// creating the body of an AND gate
	gate.moveTo(new Point(x - l/2, y - h/2));
	gate.lineTo(new Point(x - l/2, y + h/2));
	gate.lineTo(new Point(x, y + h/2));
	gate.arcTo(new Point(x + l/2, y), new Point(x, y - h/2));
	gate.closePath();

	var andInputPoints = [];

	// input pins
	for (var i=0; i<inputs; i++) {
		var from = new Point(x - l, y - h/2 + midPoint + i*size);
		var to = new Point(x - l/2, y - h/2 + midPoint + i*size);

		drawLine(from, to);
		andInputPoints[i] = from;
	}

	// output pin
	var from = new Point(x + l/2, y);
	var to = new Point(x + l, y);
	drawLine(from, to);
	drawLine(to, netPoint);

	return andInputPoints;
}

function drawOrGate(x, y, size, inputs, netPoint) {

	// determine height and length based on inputs
	var h = size*inputs;
	var l = h;
	var midPoint = size/2; 

	var orInputPoints = [];

	// input pins
	for (var i=0; i<inputs; i++) {
		var from = new Point(x - l, y - h/2 + midPoint + i*size);
		var to = new Point(x - l/4, y - h/2 + midPoint + i*size);
		drawLine(from, to);
		orInputPoints[i] = from;
	}

	// creating the body of an AND gate
	var gate = new Path({
		strokeColor: 'black', 
		strokeWidth: 2,
		fillColor: 'white'
	});
	gate.moveTo(new Point(x - l/2, y - h/2));
	gate.curveTo(new Point(x - l/4,y), new Point(x - l/2, y + h/2));
	gate.quadraticCurveTo(new Point(x + l/4, y + h/2), new Point(x + l/2, y));
	gate.quadraticCurveTo(new Point(x + l/4, y - h/2), new Point(x - l/2, y - h/2));

	gate.closePath();

	// output pin
	var from = new Point(x + l/2, y);
	var to = new Point(x + l, y);
	drawLine(from, to);

	// points for net of output wires
	var xMidpoint = to.x + (netPoint.x - to.x)/2;
	var pointNearOrOuput = new Point(xMidpoint, to.y);
	var pointNearOrNewInput = new Point(xMidpoint, netPoint.y);

	// left horizontal line
	drawLine(to, pointNearOrOuput);

	// vertical line
	drawLine(pointNearOrOuput, pointNearOrNewInput);

	// right horizontal line
	drawLine(pointNearOrNewInput, netPoint);

	return orInputPoints;
}

function drawXorGate(x, y, size, inputs, netPoint) {

	// determine height and length based on inputs
	var h = size*inputs;
	var l = h;
	var offset = h/5;
	var midPoint = size/2; 

	var xorInputPoints = [];

	// input pins
	for (var i=0; i<inputs; i++) {
		var from = new Point(x - l, y - h/2 + midPoint + i*size);
		var to = new Point(x - l/4, y - h/2 + midPoint + i*size);
		drawLine(from, to);
		xorInputPoints[i] = from;
	}

	// creating the body of an AND gate
	var gate = new Path({
		strokeColor: 'black', 
		strokeWidth: 2,
		fillColor: 'white'
	});
	gate.moveTo(new Point(x - l/2, y - h/2));
	gate.curveTo(new Point(x - l/4,y), new Point(x - l/2, y + h/2));
	gate.quadraticCurveTo(new Point(x + l/4, y + h/2), new Point(x + l/2, y));
	gate.quadraticCurveTo(new Point(x + l/4, y - h/2), new Point(x - l/2, y - h/2));

	gate.closePath();

	// xor line
	var xorLine = new Path({
		strokeColor: 'black', 
		strokeWidth: 2
	});
	xorLine.moveTo(new Point(x - l/2 - offset, y - h/2));
	xorLine.curveTo(new Point(x - l/4 - offset,y), new Point(x - l/2 - offset, y + h/2));


	// output pin
	var from = new Point(x + l/2, y);
	var to = new Point(x + l*1.25, y);
	drawLine(from, to);
	drawLine(to, netPoint);

	return xorInputPoints;
}

function drawNotGate(x, y, size, netPoint) {

	// determine height and length based on inputs
	var h = size;
	var l = h;
	var midPoint = size/2; 

	var notInputPoints = [];

	var from = new Point(x - l*1.5, y);
	var to = new Point(x - l/2, y);
	drawLine(from, to);
	notInputPoints[0] = from;

	// creating the body of an AND gate
	var gate = new Path({
		strokeColor: 'black', 
		strokeWidth: 2,
		fillColor: 'white'
	});
	gate.moveTo(new Point(x - l/2, y - h/2));
	gate.lineTo(new Point(x - l/2, y + h/2));
	gate.lineTo(new Point(x + l/2, y));
	gate.closePath();

	// output pin
	var outFrom = new Point(x + l/2, y);
	var outTo = new Point(x + l*1.5, y);
	drawLine(outFrom, outTo);
	drawLine(outTo, netPoint);

	// not circile of gate
	var notCircle = new Path.Circle(new Point(x + l/2 + (size/6)/2,y), size/6);
	notCircle.fillColor = 'white';	
	notCircle.strokeColor = 'black';
	notCircle.strokeWidth = 2;

	return notInputPoints;
}


function drawInput(x, y, size, name, outputPoint) {

	// determine height and length based on inputs
	var h = size/2;
	var l = size;

	var pin = new Path({
		strokeColor: 'black', 
		strokeWidth: 2,
	});

	// creating the body of input
	pin.moveTo(new Point(x - l/2, y + h/2));
	pin.lineTo(new Point(x + l*0.75, y + h/2));
	pin.lineTo(new Point(x + l, y));
	pin.lineTo(new Point(x + l*0.75, y - h/2));
	pin.lineTo(new Point(x - l/2, y - h/2));
	pin.closePath();

	// name of input
	var text = new PointText(new Point(x - l*1.5, y + 4));
	text.fillColor = 'black';
	text.content = name;

	// output pin
	var rightOfPin = new Point(x + l, y);
	var outputOfPin = new Point(x + l*1.5, y);
	drawLine(rightOfPin, outputOfPin);

	// points for net of output wires
	var xMidpoint = outputOfPin.x + (outputPoint.x - outputOfPin.x)/2;
	var pointNearOrOuput = new Point(xMidpoint, outputOfPin.y);
	var pointNearOrNewInput = new Point(xMidpoint, outputPoint.y);

	// left horizontal line
	drawLine(outputOfPin, pointNearOrOuput);

	// vertical line
	drawLine(pointNearOrOuput, pointNearOrNewInput);

	// right horizontal line
	drawLine(pointNearOrNewInput, outputPoint);

	return [];
}

function drawOutput(x, y, size, name) {

	// determine height and length based on inputs
	var h = size/2;
	var l = size;

	var pin = new Path({
		strokeColor: 'black', 
		strokeWidth: 2,
	});

	// creating the body of input
	pin.moveTo(new Point(x + l/2, y + h/2));
	pin.lineTo(new Point(x - l*0.75, y + h/2));
	pin.lineTo(new Point(x - l, y));
	pin.lineTo(new Point(x - l*0.75, y - h/2));
	pin.lineTo(new Point(x + l/2, y - h/2));
	pin.closePath();

	// name of input
	var text = new PointText(new Point(x + l, y + 4));
	text.fillColor = 'black';
	text.content = name;

	var inputPoints = [];

	// output pin
	var from = new Point(x - l*1.5, y);
	var to = new Point(x - l, y);
	
	drawLine(from, to);
	inputPoints[0] = to;

	console.log(inputPoints[0]);

	return inputPoints;
}

function drawNodes(node, xIncr, yWin, netPoints) {
	console.log(node.name);


	var x = xIncr/2 + (node.x * xIncr);
	var y = node.y * yWin;

	var inputs = node.inputs;
	console.log(inputs);
	var kind = node.kind;
	var size = 20;

	var newNetPoints = [];

	if (kind == 'and') {
		newNetPoints = drawAndGate(x, y, size, inputs, netPoints);
	} else if (kind == 'or') {
		newNetPoints = drawOrGate(x, y, size, inputs, netPoints);
	} else if (kind == 'xor') {
		newNetPoints = drawXorGate(x, y, size, inputs, netPoints);
	} else if (kind == 'not') {
		newNetPoints = drawNotGate(x, y, size, netPoints);
	} else if (kind == 'input') {
		newNetPoints = drawInput(x, y, size, node.name, netPoints);
	} else if (kind == 'output') {
		newNetPoints = drawOutput(x, y, size, node.name);
	} 

	console.log("netPoints");
	console.log(newNetPoints);
	
	for (var i=0; i<node.nodes.length; i++) {
		console.log(newNetPoints[i]);
		drawNodes(node.nodes[i], xIncr, yWin, newNetPoints[i]);
	}

	return 0;
}  


function drawCircuit(circuit, xWin, yWin) {
	var xTicks = circuit.depth; 
	var yTicks = circuit.weight;
	var xIncr = (xWin/xTicks);
	var yIncr = (yWin/yTicks);


	for (var i=0; i<circuit.nodes.length; i++) {
		var newPoints = [];

		drawNodes(circuit.nodes[i], xIncr, yWin, newPoints);
	}

}

function onResize(event) {
	var xWin = view.bounds.width;
	var yWin = view.bounds.height;

	if(project.activeLayer.hasChildren()){
        project.activeLayer.removeChildren();
    }
	drawCircuit(results, xWin, yWin);
}

/* function dealing with window resizing and zoming in and out */



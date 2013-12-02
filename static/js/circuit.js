
/* ----------------------------------------------------------------------------
 * circuit.js
 * Created by Ingrid Avendano on 11/20/13. 
 * ----------------------------------------------------------------------------
 * Contains the JS Canvas functions to draw logic gates. 
 * ------------------------------------------------------------------------- */

function schematicAttributes(object, gate) {
	if (gate) object.fillColor = 'white';

	object.strokeColor = 'black';
	object.strokeWidth = 2;
	return object;
}

function shapeAttributes(fillColor) {
	var gate = new Path();
	return schematicAttributes(gate, fillColor);
}

function drawLine(a, b) {
	var net = new Path.Line(a, b);
	schematicAttributes(net, false);
}

function drawNet(a, b) {
	var x = a.x + (b.x - a.x)/2;
	var _a = new Point(x, a.y);
	var _b = new Point(x, b.y);

	drawLine(a, _a);
	drawLine(_a, _b);
	drawLine(_b, b);
}

/* ------------------------------------------------------------------------- */

function inputPins(x, y, numberOfPins, size) {
	var offset = numberOfPins*size;
	var pinPoints = [];

	for (var i = 0; i < numberOfPins; i++) {
		var a = new Point(x - offset,   y - offset/2 + (i+0.5)*size);
		var b = new Point(x, y - offset/2 + (i+0.5)*size);
		drawLine(a, b);

		pinPoints[i] = a;
	}

	return pinPoints;
}

function outputPin(x, y, offset, netPoint) {
	var a = new Point(x + offset/2, y);
	var b = new Point(x + offset, y);
	drawLine(a, b);
	drawNet(b, netPoint);
}

function outPin(p, o, net) {
	drawLine(new Point(p.x+(o*0.5), p.y), new Point(p.x+o, p.y));
	drawNet(new Point(p.x+o, p.y), net);
}

/* ----------------------------------------------------------------------------
 * all gate functions take in 'p' for center point of gate and 'o' for offset
 * ------------------------------------------------------------------------- */

function notCircle(p, o) {
	var point = new Point(p.x+(o*1.2), p.y);
	var circle = new Path.Circle(point, o*0.3);
	circle.fillColor = 'white';	
	circle.strokeColor = 'black';
	circle.strokeWidth = 2;
}

function notGate(p, o) {
	var g = shapeAttributes(true);
	g.moveTo(new Point(p.x-o, p.y-o));
	g.lineTo(new Point(p.x-o, p.y+o));
	g.lineTo(new Point(p.x+o, p.y));
	g.closePath();
	notCircle(p, o);
} 

function andGate(p, o) {
	var g = shapeAttributes(true);
	g.moveTo(new Point(p.x-o, p.y-o));
	g.lineTo(new Point(p.x-o, p.y+o));
	g.lineTo(new Point(p.x, p.y+o));
	g.arcTo(new Point(p.x+o, p.y), new Point(p.x, p.y-o));
	g.closePath();
}

function orGate(p, o) {
	var g = shapeAttributes(true);
	g.moveTo(new Point(p.x-o, p.y-o));
	g.curveTo(new Point(p.x-(o*0.5), p.y), new Point(p.x-o, p.y+o));
	g.quadraticCurveTo(new Point(p.x+(o*0.5), p.y+o), new Point(p.x+o, p.y));
	g.quadraticCurveTo(new Point(p.x+(o*0.5), p.y-o), new Point(p.x-o, p.y-o));
	g.closePath();
}

function xorGate(p, o) {
	orGate(p, o);
	// create the xor line
	var l = shapeAttributes(false);
	l.moveTo(new Point(p.x-(o*1.4), p.y-o));
	l.curveTo(new Point(p.x-(o*0.9), p.y), new Point(p.x-(o*1.4), p.y+o));
}

function port(p, size, name, direction) {
	var o = size/4.0;
	var _o = ((direction == 'input') ? o : -o)*2.0;

	var i = shapeAttributes(true);
	i.moveTo(new Point(p.x-_o, p.y+o));
	i.lineTo(new Point(p.x+(_o*1.5), p.y+o));
	i.lineTo(new Point(p.x+(_o*2.0), p.y));
	i.lineTo(new Point(p.x+(_o*1.5), p.y-o));
	i.lineTo(new Point(p.x-_o, p.y-o));
	i.closePath();

	_o = ((direction == 'input') ? size : -size)*1.2 + name.length*4.0;
	var text = new PointText(new Point(p.x-_o, p.y+4.0));
	text.fillColor = 'black';
	text.content = name;
}

/* ------------------------------------------------------------------------- */

function drawXorGate(x, y, size, inputs, netPoint) {
	var h = size*inputs;
	var point = new Point(x,y);
	xorGate(point, h/2);
}


function drawNodes(node, xIncr, yWin, netPoints) {
	console.log(node.name);


	var x = xIncr/2 + (node.x * xIncr);
	var y = node.y * yWin;
	var point = new Point(xIncr/2 + (node.x * xIncr), node.y * yWin);
	// var size = new Size(20,20);

	var inputs = node.inputs;
	var size = 20;

	var newNetPoints = inputPins(x,y,inputs,size);
	if (node.kind != 'output') outPin(point,size,netPoints);

	switch (node.kind) {
		case 'not':
			notGate(point, size/2);
			break;
		case 'and':
			andGate(point, (size*inputs)/2);
			break;
		case 'or':
			orGate(point, (size*inputs)/2);
			break;
		case 'xor':
			drawXorGate(x, y, size, inputs, netPoints);
			break;
		default: 
			port(point, size, node.name, node.kind);
	}


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
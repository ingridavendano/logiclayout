/* -------------------------------------------------------------------------
 * circuit.js
 * Created by Ingrid Avendano on 11/20/13. 
 * -------------------------------------------------------------------------
 * Contains the JS Canvas functions to draw logic gates. 
 * ------------------------------------------------------------------------- */

function schematicAttributes(object, gate) {
	if (gate) object.fillColor = 'white';
	object.strokeColor = 'black';
	object.strokeWidth = 2;
	return object;
}

function drawShape(fillColor) {
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

function inPins(p, n, o) {
	// lines drawn are dependent if there are even or odd number of inputs
	var pinPoints = [];
	var even = (n%2 == 0) ? 1 : 0; 

	// draws one or two lines at a time making center lines longer
	for (var i=0; i<n/2; i++) {
		var y = p.y + (i + 0.5*even)*o;
		var _y = p.y - (i + 0.5*even)*o;

		var a = new Point(p.x+(o*((2.0*i)-n)), y);
		var _a = new Point(p.x+(o*((2.0*i)-n)), _y);

		drawLine(a, new Point(p.x, y));
		if (y != _y) drawLine(_a, new Point(p.x, _y));

		pinPoints[Math.floor(n/2) + i] = a;
		pinPoints[Math.floor(n/2) - i - even] = _a;
	}
	return pinPoints;
}

function outPin(p, o, net) {
	// checks to make sure that a net does exist
	if (net) {
		drawLine(new Point(p.x+(o*0.5), p.y), new Point(p.x+o, p.y));
		drawNet(new Point(p.x+o, p.y), net);
	}
}

/* -------------------------------------------------------------------------
 * all gate functions take 'p' for center point of gate and 'o' for offset
 * ------------------------------------------------------------------------- */

function notCircle(p, o, gate) {
	var radius = ((gate) ? 0.25 : 0.4)*o;
	var point = new Point(p.x+o+radius, p.y);
	schematicAttributes(new Path.Circle(point, radius), true);
}

function notGate(s, p, o) {
	s.moveTo(new Point(p.x-o, p.y-o));
	s.lineTo(new Point(p.x-o, p.y+o));
	s.lineTo(new Point(p.x+o, p.y));
	s.closePath();
	notCircle(p, o, false);
} 

function andGate(s, p, o) {
	s.moveTo(new Point(p.x-o, p.y-o));
	s.lineTo(new Point(p.x-o, p.y+o));
	s.lineTo(new Point(p.x, p.y+o));
	s.arcTo(new Point(p.x+o, p.y), new Point(p.x, p.y-o));
	s.closePath();
}

function nandGate(s, p, o) {
	andGate(s, p, o);
	notCircle(p, o, true);
}

function orGate(s, p, o) {
	s.moveTo(new Point(p.x-o, p.y-o));
	s.curveTo(new Point(p.x-(o*0.5), p.y), new Point(p.x-o, p.y+o));
	s.quadraticCurveTo(new Point(p.x+(o*0.5), p.y+o), new Point(p.x+o, p.y));
	s.quadraticCurveTo(new Point(p.x+(o*0.5), p.y-o), new Point(p.x-o, p.y-o));
	s.closePath();
}

function norGate(s, p, o) {
	orGate(s, p, o);
	notCircle(p, o, true);
}

function xorGate(s, p, o) {
	orGate(s, p, o);
	// create the xor line
	var l = drawShape(false);
	l.moveTo(new Point(p.x-(o*1.4), p.y-o));
	l.curveTo(new Point(p.x-(o*0.9), p.y), new Point(p.x-(o*1.4), p.y+o));
}

function nxorGate(s, p, o) {
	xorGate(s, p, o);
	notCircle(p, o, true);
}

function port(s, p, size, name, direction) {
	var o = size/4.0;
	var _o = ((direction == 'input') ? o : -o)*2.0;

	s.moveTo(new Point(p.x-_o, p.y+o));
	s.lineTo(new Point(p.x+(_o*1.5), p.y+o));
	s.lineTo(new Point(p.x+(_o*2.0), p.y));
	s.lineTo(new Point(p.x+(_o*1.5), p.y-o));
	s.lineTo(new Point(p.x-_o, p.y-o));
	s.closePath();

	_o = ((direction == 'input') ? size : -size)*1.2 + name.length*4.0;
	var text = new PointText(new Point(p.x-_o, p.y+4.0));
	text.fillColor = 'black';
	text.content = name;
}

/* ------------------------------------------------------------------------- */

function drawNodes(node, xIncr, yWin, netPoints) {
	var x = xIncr/2 + (node.x * xIncr);
	var y = node.y * yWin;
	var point = new Point(xIncr/2 + (node.x * xIncr), node.y * yWin);

	var inputs = node.inputs;
	var size = 20;

	var newNetPoints = inPins(point, inputs, size);
	outPin(point,size,netPoints);

	// recursively go through and draw every child node
	for (var i=0; i<node.nodes.length; i++) {
		drawNodes(node.nodes[i], xIncr, yWin, newNetPoints[i]);
	}
	
	var shape = drawShape(true);
	switch (node.kind) {
		case 'not':
			notGate(shape, point, size/2);
			break;
		case 'and':
			andGate(shape, point, (size*inputs)/2);
			break;
		case 'nand':
			nandGate(shape, point, (size*inputs)/2);
			break;
		case 'or':
			orGate(shape, point, (size*inputs)/2);
			break;
		case 'nor':
			norGate(shape, point, (size*inputs)/2);
			break;
		case 'xor':
			xorGate(shape, point, (size*inputs)/2);
			break;
		case 'nxor':
			nxorGate(shape, point, (size*inputs)/2);
			break;
		default: 
			port(shape, point, size, node.name, node.kind);
	}

	return 0;
}  

function drawCircuit(circuit, xWin, yWin) {
	var xIncr = (xWin/circuit.depth);
	var yIncr = (yWin/circuit.weight);

	for (var i=0; i<circuit.nodes.length; i++) {
		drawNodes(circuit.nodes[i], xIncr, yWin, false);
	}

}

function onResize(event) {
	var xWin = view.bounds.width;
	var yWin = view.bounds.height;

	// clears previous image drawn when resizing the window view 
	if (project.activeLayer.hasChildren()){
        project.activeLayer.removeChildren();
    }

    if (run) drawCircuit(results, xWin, yWin);
    
	
}

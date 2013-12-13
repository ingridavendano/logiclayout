/* -------------------------------------------------------------------------
 * examples.js
 * Created by Ingrid Avendano on 12/12/13. 
 * -------------------------------------------------------------------------
 * Contains digital logic schematic functions as examples.
 * ------------------------------------------------------------------------- */

var circuit;
var color = { 
	on: '#F2CB05',
	off: '#0d59c3',
	fill: '#FFFFFF',
	wire: '#0d59c3'
};

/* ------------------------------------------------------------------------- */

function schematicAttributes(object, gate) {
	if (gate) object.fillColor = color.fill;
	object.strokeColor = color.wire;
	object.strokeWidth = 2;
	object.state = null;
	object.pin = false;
	object.change = true;

	// adds every item created to a group to make it easier to move around
	circuit.addChild(object);
	
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


function port(s, p, size, name, direction) {
	var o = size/4.0;
	var _o = ((direction == 'input') ? o : -o)*2.0;

	s.moveTo(new Point(p.x-_o, p.y+o));
	s.lineTo(new Point(p.x+(_o*1.5), p.y+o));
	s.lineTo(new Point(p.x+(_o*2.0), p.y));
	s.lineTo(new Point(p.x+(_o*1.5), p.y-o));
	s.lineTo(new Point(p.x-_o, p.y-o));
	s.closePath();

	// ports are assigned spectial abilities because they alter simulations
	if (direction == 'input') {
		s.pin = true;
		s.change = true;
		s.state = null;

		// checks if a port is actually assigned as on or off
		if (typeof name == 'number') {
			s.change = false;
			s.state = (name) ? true : false;
			s.fillColor = (s.state) ? color.on : color.off;
		}
	}

	_o = ((direction == 'input') ? size : -size)*1.2 + String(name).length*4.0;
	var text = new PointText(new Point(p.x-_o, p.y+4.0));
	text.fillColor = color.wire;
	text.content = String(name);
	circuit.addChild(text);
	return s; 
}


/* ------------------------------------------------------------------------- */

function inPins(p, n, o) {
	// lines drawn are dependent if there are even or odd number of in pins
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
	return schematicAttributes(new Path.Circle(point, radius), true);
}

function notGate(s, p, o) {
	s.moveTo(new Point(p.x-o, p.y-o));
	s.lineTo(new Point(p.x-o, p.y+o));
	s.lineTo(new Point(p.x+o, p.y));
	s.closePath();
	
	var compound = new CompoundPath(s, notCircle(p, o, false));
	compound = schematicAttributes(compound, true);
	return compound;
} 

/* ------------------------------------------------------------------------- */

circuit = new Group()

var size = 20;


function newObj() {
	var obj = new Path();
	obj.fillColor = color.fill;
	obj.strokeColor = color.wire;
	obj.strokeWidth = 2;
	obj.state = null;

	// adds object to circuit to allow it to move and change states
	circuit.addChild(obj);
	return obj
}

function notCircle(p, o, gate) {
	var radius = ((gate) ? 0.25 : 0.4)*o;
	var point = new Point(p.x+o+radius, p.y);
	return schematicAttributes(new Path.Circle(point, radius), true);
}

function notGate(x, y) {
	var o = 10;
	
	var gate = newObj();
	gate.moveTo(new Point(x-o, y-o));
	gate.lineTo(new Point(x-o, y+o));
	gate.lineTo(new Point(x+o, y));
	gate.closePath();



}

var gate = newObj();







// var gatePoint = new Point(100,50);
// var gate = drawShape(true);
// gate = notGate(gate, gatePoint, size/2);

var inputPoint = new Point(50,50);
var input = drawShape(true);
input = port(input, inputPoint, size, 'x', 'input')

var outputPoint = new Point(150,50);
var output = drawShape(true);
output = port(output, outputPoint, size, 'f', 'output');



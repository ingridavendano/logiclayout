/* -------------------------------------------------------------------------
 * circuit.js
 * Created by Ingrid Avendano on 11/20/13. 
 * -------------------------------------------------------------------------
 * Contains the JS Canvas functions to draw logic gates. 
 * ------------------------------------------------------------------------- */

// global variables 
var circuit;
var output;
var inputs = [];
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

function andGate(s, p, o) {
	s.moveTo(new Point(p.x-o, p.y-o));
	s.lineTo(new Point(p.x-o, p.y+o));
	s.lineTo(new Point(p.x, p.y+o));
	s.arcTo(new Point(p.x+o, p.y), new Point(p.x, p.y-o));
	s.closePath();
	return s; 
}

function nandGate(s, p, o) {
	var compound = new CompoundPath(andGate(s, p, o), notCircle(p, o, true));
	compound = schematicAttributes(compound, true);
	return compound;
}

function orGate(s, p, o) {
	s.moveTo(new Point(p.x-o, p.y-o));
	s.curveTo(new Point(p.x-(o*0.5), p.y), new Point(p.x-o, p.y+o));
	s.quadraticCurveTo(new Point(p.x+(o*0.5), p.y+o), new Point(p.x+o, p.y));
	s.quadraticCurveTo(new Point(p.x+(o*0.5), p.y-o), new Point(p.x-o, p.y-o));
	s.closePath();
	return s; 
}

function norGate(s, p, o) {
	var compound = new CompoundPath(orGate(s, p, o), notCircle(p, o, true));
	compound = schematicAttributes(compound, true);
	return compound;
}

function xorGate(s, p, o) {
	s = orGate(s, p, o);
	// create the xor line
	var l = drawShape(false);
	l.moveTo(new Point(p.x-(o*1.4), p.y-o));
	l.curveTo(new Point(p.x-(o*0.9), p.y), new Point(p.x-(o*1.4), p.y+o));
	return s;
}

function nxorGate(s, p, o) {
	var compound = new CompoundPath(xorGate(s, p, o), notCircle(p, o, true));
	compound = schematicAttributes(compound, true);
	return compound;
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

function drawNodes(node, xWin, xIncr, yWin, netPoints) {
	// console.log(node.name);
	var x = xIncr/2 + (node.x * xIncr);
	// x = xWin + x;
	var y = node.y * yWin;
	var point = new Point(x, y);

	var size = 20;
	var gateSize = (size*node.inputs)/2;

	var newNetPoints = inPins(point, node.inputs, size);
	outPin(point,size,netPoints);

	var shape = drawShape(true);
	var shapeNode = new Group();
	shapeNode.nameText = String(node.name);
	shapeNode.kind = node.kind;
	shapeNode.state = null;

	// shape.children = [];

	// recursively go through and draw every child node
	for (var i=0; i<node.nodes.length; i++) {
		var child = drawNodes(node.nodes[i], xWin, xIncr, yWin, newNetPoints[i]);
		shapeNode.addChild(child);
	}

	switch (node.kind) {
		case 'not':
			shape = notGate(shape, point, size/2);
			break;
		case 'and':
			shape = andGate(shape, point, gateSize);
			break;
		case 'nand':
			shape = nandGate(shape, point, gateSize);
			break;
		case 'or':
			shape = orGate(shape, point, gateSize);
			break;
		case 'nor':
			shape = norGate(shape, point, gateSize);
			break;
		case 'xor':
			shape = xorGate(shape, point, gateSize);
			break;
		case 'nxor':
			shape = nxorGate(shape, point, gateSize);
			break;
		default: 
			shape = port(shape, point, size, node.name, node.kind);
			if (node.kind == 'input') {
				inputs.push(shapeNode);

				// sets input state if node is alreay preset
				shapeNode.state = shape.state;
			} else {
				output = shapeNode;
			}
	}
	shapeNode.image = shape;
	return shapeNode;
}  

/* ------------------------------------------------------------------------- */

function drawCircuit(tree, xWin, yWin) {
	var xIncr = (xWin/tree.depth);
	var yIncr = (yWin/tree.weight);

	// xIncr = 100;
	// yWin = tree.weight*40;
	// xWin = xWin/2;

	// creating a group of nodes to be easy to move around
	circuit = new Group()
	var outputPin;

	for (var i=0; i<tree.nodes.length; i++) {
		outputPin = drawNodes(tree.nodes[i], xWin, xIncr, yWin, false);
	}
	// console.log(outputPin.nameText);

	// console.log(output.hasChildren());
	return 0;
}

/* ------------------------------------------------------------------------- */

function drawSimulator(nodeShape) {
	var childrenValues = [];
	
	for (var i=0; i<nodeShape.children.length; i++) {
		childrenValues.push(drawSimulator(nodeShape.children[i]));
	}

	switch (nodeShape.kind) {
		case 'output':
			nodeShape.state = childrenValues[0];
			break;
		case 'input':
			nodeShape.state = nodeShape.image.state;
			break;
		case 'not':
			nodeShape.state = !(childrenValues[0]);
			break;
		case 'and':
			var result = nodeShape.children[0].state & nodeShape.children[1].state;
			for (var i=2; i<nodeShape.children.length; i++) {
				result = nodeShape.children[i].state & result;
			}
			nodeShape.state = result;
			nodeShape.image.state = (result) ? true : false;
			break;
		case 'nand':
			var result = nodeShape.children[0].state & nodeShape.children[1].state;
			for (var i=2; i<nodeShape.children.length; i++) {
				result = nodeShape.children[i].state & result;
			}
			nodeShape.state = !result;
			nodeShape.image.state = (result) ? true : false;
			break;
		case 'or':
			var result = nodeShape.children[0].state | nodeShape.children[1].state;
			for (var i=2; i<nodeShape.children.length; i++) {
				result = nodeShape.children[i].state | result;
			}
			nodeShape.state = result;
			nodeShape.image.state = (result) ? true : false;
			break;
		case 'nor':
			var result = nodeShape.children[0].state | nodeShape.children[1].state;
			for (var i=2; i<nodeShape.children.length; i++) {
				result = nodeShape.children[i].state | result;
			}
			nodeShape.state = !result;
			nodeShape.image.state = (result) ? true : false;
			break;
		case 'xor':
			var result = nodeShape.children[0].state ^ nodeShape.children[1].state;
			for (var i=2; i<nodeShape.children.length; i++) {
				result = nodeShape.children[i].state ^ result;
			}
			nodeShape.state = result;
			nodeShape.image.state = (result) ? true : false;
			break;
		case 'nxor':
			var result = nodeShape.children[0].state ^ nodeShape.children[1].state;
			for (var i=2; i<nodeShape.children.length; i++) {
				result = nodeShape.children[i].state ^ result;
			}
			nodeShape.state = !result;
			nodeShape.image.state = (result) ? true : false;
			break;

	}

	if (nodeShape.state != true && nodeShape.state != false) {
		nodeShape.state = false;
		if (nodeShape.kind == 'input') nodeShape.image.state = false;
	}

	if (nodeShape.image.change) {
		// change the color of a shape
		if (nodeShape.state == false) {
			nodeShape.image.fillColor = color.off;
			nodeShape.image.state = false;
			if (nodeShape.kind == 'input') {
				nodeShape.image.state = false;
			}
		} else {
			nodeShape.image.fillColor = color.on;
			nodeShape.image.state = true;
			if (nodeShape.kind == 'input') nodeShape.image.state = true;
		}
	}
	
	return nodeShape.state;
}

// window.globals.simulate = function() {
// 	// drawSimulator(output);
// }

/* ------------------------------------------------------------------------- */

function onResize(event) {
	var xWin = view.bounds.width;
	var yWin = view.bounds.height/2;

	// have the scroll bar be the same height as viewing window
	$('.slider').css('height',$(".schematic").height());

	var x = $(".schematic").width();
	var y = yWin*2*0.8;


	// clears previous image drawn when resizing the window view 
	if (project.activeLayer.hasChildren()){
        project.activeLayer.removeChildren();
    }
    
    if (run) {
    	drawCircuit(results, x, y);
    	// drawSimulator(output);
    }
}

function onMouseDrag(event) {
	circuit.position += event.delta;
}

var hitOptions = {
	segments: true,
	stroke: true,
	fill: true,
	tolerance: 10
};


var segment, path;
var movePath = false;

function onMouseDown(event) {
	segment = path = null;
	var hitResult = project.hitTest(event.point, hitOptions);

	if (!hitResult)
		return;

	if (event.modifiers.shift) {
		if (hitResult.type == 'segment') {
			hitResult.segment.remove();
		};
		return;
	}

	if (hitResult) {
		path = hitResult.item;

		if (path.pin == true && path.change == true) {
			if (path.state) {
				path.fillColor = color.off;
				path.state = false;
			} else {
				path.fillColor = color.on;
				path.state = true;
			}
		}
	}
	drawSimulator(output);
	movePath = hitResult.type == 'fill';
	if (movePath)
		project.activeLayer.addChild(hitResult.itxzem);
}


/* -------------------------------------------------------------------------
 * circuit.js
 * Created by Ingrid Avendano on 11/20/13. 
 * -------------------------------------------------------------------------
 * Contains the JS Canvas functions to draw logic gates. 
 * ------------------------------------------------------------------------- */

var circuit;
var output;
var inputs = [];
// var color = {
// 	on: '#FF876C', 
// 	off: '#008A83',
// 	fill: '#CEFFBC',
// 	wire: '#66635D'
// };

var color = {
	on: '#E54140', 
	off: '#6CC5C1',
	fill: '#F7EBD5',
	wire: '#66635D'
};

// var color = {
// 	on: '#000000', 
// 	off: '#FFFFFF',
// 	fill: '#FFFFFF',
// 	wire: '#000000'
// };

/* ------------------------------------------------------------------------- */

function schematicAttributes(object, gate) {
	if (gate) object.fillColor = color.fill;
	object.strokeColor = color.wire;
	object.strokeWidth = 2;
	object.pin = false;
	object.change = false;

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
	schematicAttributes(new Path.Circle(point, radius), true);
}

function notGate(s, p, o) {
	s.moveTo(new Point(p.x-o, p.y-o));
	s.lineTo(new Point(p.x-o, p.y+o));
	s.lineTo(new Point(p.x+o, p.y));
	s.closePath();
	notCircle(p, o, false);
	return s;
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
	s = andGate(s, p, o);
	notCircle(p, o, true);
	return s;
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
	s = orGate(s, p, o);
	notCircle(p, o, true);
	return s;
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
	s = xorGate(s, p, o);
	notCircle(p, o, true);
	return s;
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
		s.status = null;
		
		// checks if a port is actually assigned as on or off
		if (typeof name == 'number') {
			s.change = false;
			s.status = (name) ? true : false;
			s.fillColor = (s.status) ? color.on : color.off;
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

function drawNodes(node, xIncr, yWin, netPoints) {
	// console.log(node.name);
	var x = xIncr/2 + (node.x * xIncr);
	var y = node.y * yWin;
	var point = new Point(xIncr/2 + (node.x * xIncr), node.y * yWin);

	var size = 20;
	var gateSize = (size*node.inputs)/2;

	var newNetPoints = inPins(point, node.inputs, size);
	outPin(point,size,netPoints);

	var shape = drawShape(true);
	var shapeNode = new Group();
	shapeNode.image = shape;
	shapeNode.name = node.name;
	shapeNode.kind = node.kind;
	shapeNode.status = null;
	// shape.children = [];

	// recursively go through and draw every child node
	for (var i=0; i<node.nodes.length; i++) {
		var child = drawNodes(node.nodes[i], xIncr, yWin, newNetPoints[i]);
		console.log(" "+child.name);
		shapeNode.addChild(child);
	}

	console.log(shapeNode.hasChildren());

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

				// sets input status if node is alreay preset
				shapeNode.status = shape.status;
			} else {
				output = shapeNode;
			}
	}

	return shapeNode;
}  

/* ------------------------------------------------------------------------- */

function drawCircuit(tree, xWin, yWin) {
	var xIncr = (xWin/tree.depth);
	var yIncr = (yWin/tree.weight);

	// xIncr = 100;
	// yWin = circuit.weight*40;

	// creating a group of nodes to be easy to move around
	circuit = new Group()
	var outputPin;

	for (var i=0; i<tree.nodes.length; i++) {
		outputPin = drawNodes(tree.nodes[i], xIncr, yWin, false);
	}
	console.log(outputPin.name);

	console.log(output.hasChildren());
	return 0;
}

/* ------------------------------------------------------------------------- */

function drawSimulator(nodeShape) {
	var childrenValues = [];
	console.log(nodeShape.name);
	console.log(nodeShape.status);


	for (var i=0; i<nodeShape.children.length; i++) {
		// console.log(nodeShape.children[i].name);

		// compiles all of the status of the nodes 
		childrenValues.push(drawSimulator(nodeShape.children[i]));
	}

	console.log(childrenValues);


	// switch (nodeShape.kind) {
	// 	case 'not':
	// 		shape = notGate(shape, point, size/2);
	// 		break;
	// 	case 'and':
	// 		shape = andGate(shape, point, gateSize);
	// 		break;
	// 	case 'nand':
	// 		shape = nandGate(shape, point, gateSize);
	// 		break;
	// 	case 'or':
	// 		shape = orGate(shape, point, gateSize);
	// 		break;
	// 	case 'nor':
	// 		shape = norGate(shape, point, gateSize);
	// 		break;
	// 	case 'xor':
	// 		shape = xorGate(shape, point, gateSize);
	// 		break;
	// 	case 'nxor':
	// 		shape = nxorGate(shape, point, gateSize);
	// 		break;
	// 	default: 
	// 		shape = port(shape, point, size, node.name, node.kind);
	// 		if (node.kind == 'input') {
	// 			inputs.push(shapeNode);
	// 		} else {
	// 			output = shapeNode;
	// 		}
	// }

	return nodeShape.status;
}

/* ------------------------------------------------------------------------- */

function onResize(event) {
	var xWin = view.bounds.width;
	var yWin = view.bounds.height/2;

	// have the scroll bar be the same height as viewing window
	$('.slider').css('height',$(".schematic").height());

	console.log(xWin);
	console.log(yWin);


	var x = $(".schematic").width();
	var Y = $(".schematic").height();
	console.log(Y);
	// var y = $(".schematic").height()/2;
	var y = yWin*2*0.8;
	console.log(x);
	console.log(y);


	// clears previous image drawn when resizing the window view 
	if (project.activeLayer.hasChildren()){
        project.activeLayer.removeChildren();
    }
    
    if (run) {
    	drawCircuit(results, x, y);
    	drawSimulator(output);
    	// var pins = drawCircuit(results);
    	// drawSimulator(xWin, yWin, pins);
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
			if (path.status) {
				path.fillColor = color.off;
				path.status = false;
			} else {
				path.fillColor = color.on;
				path.status = true;
			}
		}
		
		// if (hitResult.type == 'segment') {
		// 	segment = hitResult.segment;
		// } else if (hitResult.type == 'stroke') {
		// 	var location = hitResult.location;
		// 	segment = path.insert(location.index + 1, event.point);
		// 	path.smooth();
		// }
	}

	movePath = hitResult.type == 'fill';
	if (movePath)
		project.activeLayer.addChild(hitResult.itxzem);
}














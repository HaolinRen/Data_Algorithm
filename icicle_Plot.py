from tulip import *
import random
from time import *
def incerement(d, n, a):
	if n in a.keys():
		d[n] += 1
	else:
		d[n] = 1	
def roundNeighbour(node):
	k = random.randint(1,graph.deg(node))
	j = 0
	for neigh in graph.getInOutNodes(node):
		j += 1
		if j == k:
			return neigh
def clusting(nbPas):
	d = {}
	node = graph.getOneNode()
	for i in range(nbPas):
		incerement(d,node, d)
		node = roundNeighbour(node)
	return d
def getRoot(nbPas):
	dic = clusting(nbPas)
	s = dic.keys()
	if len(s) != 0:
		res = s[0]
	
		for i in range(len(s)):
			if dic[s[i]] > dic[res]:
				res = s[i]
		return res
Tree = {}
def combienFils(node, s):
	for item in Tree[node]:
		s.append(1)
		combienFils(item,s)
	return len(s)
def getTree(node):
	if node not in Tree:
		Tree[node] = []
		for voisin in graph.getInOutNodes(node):
			if voisin not in Tree:
				Tree[node].append(voisin)
				getTree(voisin)
def Coloring(viewLabel, viewColor):
	for node in graph.getNodes():
		blue = tlp.Color(0,0,255)
		green = tlp.Color(0,255,0)
		lightblue = tlp.Color(119,255,234)
		viewLabel[node] = str(node.id)
		if graph.deg(node) == 1:
			viewColor[node] = green
		if graph.deg(node) == 3:
			viewColor[node] = lightblue
		if graph.deg(node) > 3:
			viewColor[node] = blue
def main(graph): 
	viewBorderColor =  graph.getColorProperty("viewBorderColor")
	viewBorderWidth =  graph.getDoubleProperty("viewBorderWidth")
	viewColor =  graph.getColorProperty("viewColor")
	viewFont =  graph.getStringProperty("viewFont")
	viewFontSize =  graph.getIntegerProperty("viewFontSize")
	viewLabel =  graph.getStringProperty("viewLabel")
	viewLabelBorderColor =  graph.getColorProperty("viewLabelBorderColor")
	viewLabelBorderWidth =  graph.getDoubleProperty("viewLabelBorderWidth")
	viewLabelColor =  graph.getColorProperty("viewLabelColor")
	viewLabelPosition =  graph.getIntegerProperty("viewLabelPosition")
	viewLayout =  graph.getLayoutProperty("viewLayout")
	viewMetaGraph =  graph.getGraphProperty("viewMetaGraph")
	viewMetric =  graph.getDoubleProperty("viewMetric")
	viewRotation =  graph.getDoubleProperty("viewRotation")
	viewSelection =  graph.getBooleanProperty("viewSelection")
	viewShape =  graph.getIntegerProperty("viewShape")
	viewSize =  graph.getSizeProperty("viewSize")
	viewSrcAnchorShape =  graph.getIntegerProperty("viewSrcAnchorShape")
	viewSrcAnchorSize =  graph.getSizeProperty("viewSrcAnchorSize")
	viewTexture =  graph.getStringProperty("viewTexture")
	viewTgtAnchorShape =  graph.getIntegerProperty("viewTgtAnchorShape")
	viewTgtAnchorSize =  graph.getSizeProperty("viewTgtAnchorSize")
	numNodes = graph.numberOfNodes()
	baseWidth = 4
	baseHeight = 2 * baseWidth
	def iciclePlot(node, x, y, nodeSize):
		viewShape[node] = tlp.NodeShape.CubeOutlined
		viewSize[node] = tlp.Size(nodeSize, baseHeight, 1)
		sleep(0.1)
		updateVisualization()
		viewLayout[node] = tlp.Coord(x,y)
		n = len(Tree[node])
		if n != 0:
			y -= baseHeight			
			x -= (nodeSize - baseWidth) / 2
			for item in Tree[node]:
				SonNum = combienFils(item,[1]) 
				x += (SonNum * baseWidth) / 2
				updateVisualization(True)
				iciclePlot(item, x, y, SonNum * baseWidth)
				x += (SonNum * baseWidth) / 2
	nbPas = 100	
	root = getRoot(nbPas*numNodes)
	getTree(root)
	Coloring(viewLabel,viewColor)
	iciclePlot(root, 0, 0, numNodes * baseWidth)
	
		

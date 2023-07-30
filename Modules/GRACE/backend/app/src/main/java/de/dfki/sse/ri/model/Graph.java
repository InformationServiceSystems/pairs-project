package de.dfki.sse.ri.model;

import java.util.ArrayList;

public class Graph {

	private ArrayList<Node> nodes;

	public Graph() {
		nodes = new ArrayList<Node>();
	}

	public ArrayList<Node> getNodes() {
		return nodes;
	}

	public void setNodes(ArrayList<Node> nodes) {
		this.nodes = nodes;
	}
	
}

package de.dfki.sse.ri.model;

import java.util.ArrayList;
import java.util.List;

public class Node {

  private List<Node> adjacentNodes = new ArrayList<Node>();

  public Node() {
    this.adjacentNodes = new ArrayList<>();
  }

  public List<Node> getAdjacentNodes() { return adjacentNodes; }

  public void connecNode(Node adjacentNode) {
    this.adjacentNodes.add(adjacentNode);
  }

  public int getNumberOfAdjacents() { return this.adjacentNodes.size(); }
}

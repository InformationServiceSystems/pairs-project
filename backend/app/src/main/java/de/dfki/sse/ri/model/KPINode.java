package de.dfki.sse.ri.model;

public class KPINode extends Node {

  private int id;
  private float value;
  private float weight;
  private String name;

  public KPINode(String kpiName, int kpiId, float kpiWeight) {
    this.name = kpiName;
    this.id = kpiId;
    this.weight = kpiWeight;
  }

  public void setValue(float value) {
    this.value = value;
  }

  public float getValue() { return value; }

  public float getWeight() { return weight; }

  public String getName() { return name; }

  public int getId() { return id; }
}

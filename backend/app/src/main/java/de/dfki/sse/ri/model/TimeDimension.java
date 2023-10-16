package de.dfki.sse.ri.model;

public class TimeDimension {

  private int id;
  private String description;
  private float weight;

  public TimeDimension(String description, int id, float weight) {
    this.description = description;
    this.id = id;
    this.weight = weight;
  }

  public int getId() { return id; }
  public String getDescription() { return description; }
  public float getWeight() { return weight; }
}

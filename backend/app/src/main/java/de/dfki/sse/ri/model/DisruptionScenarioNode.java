package de.dfki.sse.ri.model;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class DisruptionScenarioNode extends Node {

  private int id;
  private String name;
  private Map<Integer, TimeDimension> timeDimensions;
  private float probability;
  private TimeDimension selectedDimension;

  public DisruptionScenarioNode(String name, int id, float probability,
                                List<TimeDimension> timeDimensions) {

    this.id = id;
    this.name = name;
    this.probability = probability;
    this.timeDimensions = new HashMap<>();
    for (TimeDimension dimension: timeDimensions) {
      this.timeDimensions.put(dimension.getId(), dimension);
    }
  }

  public float getProbability() { return probability; }

  public int getId() { return this.id; }

  public String getName() { return this.name; }

  public void setTimeDimension(int dimensionId) {
    this.selectedDimension = timeDimensions.get(dimensionId);
  }

  public TimeDimension getTimeDimension() {
    return selectedDimension;
  }
}

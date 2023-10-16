package de.dfki.sse.ri.core;

import de.dfki.sse.ri.model.Model;

public interface RIStrategy {

  public float calculateRI(Model model);
  public void transform(Model model);

}

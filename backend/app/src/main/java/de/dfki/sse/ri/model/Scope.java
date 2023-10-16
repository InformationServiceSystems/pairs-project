package de.dfki.sse.ri.model;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class Scope {

  private int id;
  private String name;
  private List<Integer> kpiIds;

  public Scope(String scopeName, int scopeId) {
    this.name = scopeName;
    this.id = scopeId;
    this.kpiIds = new ArrayList<>();
  }

  public String getName() { return name; }

  public int getId() { return id; }

  public void addKPIIds(List<Integer> kpiIds) { this.kpiIds.addAll(kpiIds); }

  public Set<Integer> getKpiIds() {
    return new HashSet<>(kpiIds);
  }
}

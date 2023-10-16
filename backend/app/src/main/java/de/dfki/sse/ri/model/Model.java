package de.dfki.sse.ri.model;

import java.util.Collection;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Model {

  private Map<Integer, Scope> scopes;
  private Map<Integer, KPINode> kpis;
  private Map<Integer, DisruptionScenarioNode> disruptions;
  private DisruptionScenarioNode disruption;

  public Model() {
    this.scopes = new HashMap<>();
    this.kpis = new HashMap<>();
    this.disruptions = new HashMap<>();
  }

  public void initializeScopes(List<Scope> scopes) {
    for (Scope scope : scopes) {
      int scopeId = scope.getId();
      this.scopes.put(scopeId, scope);
    }
  }

  public void initializeKPIs(List<KPINode> kpis) {
    for (KPINode kpi : kpis) {
      int kpiId = kpi.getId();
      this.kpis.put(kpiId, kpi);
    }
  }

  public void initializeDisruptions(List<DisruptionScenarioNode> disruptions) {
    for (DisruptionScenarioNode disruption : disruptions) {
      int disruptionId = disruption.getId();
      this.disruptions.put(disruptionId, disruption);
    }
  }

  public void matchDisruptionWithKPIs(int disruptionId, List<Integer> kpiIds) {
    DisruptionScenarioNode discruption = disruptions.get(disruptionId);
    for (int kpiId : kpiIds) {
      KPINode kpi = kpis.get(kpiId);
      discruption.connecNode(kpi);
    }
  }

  public void matchScopeWithKPIs(int scopeId, List<Integer> kpiIds) {
    Scope scope = scopes.get(scopeId);
    scope.addKPIIds(kpiIds);
  }

  public void connetKPIs(int sourceKPIId, List<Integer> kpiIds) {
    KPINode sourceKPI = kpis.get(sourceKPIId);
    for (int kpiId : kpiIds) {
      KPINode kpi = kpis.get(kpiId);
      sourceKPI.connecNode(kpi);
    }
  }

  public KPINode getKPI(int kpiId) { return kpis.get(kpiId); }

  public void setDisruption(int disruptionId, int timeDimensionId) {
    DisruptionScenarioNode disruption = disruptions.get(disruptionId);
    disruption.setTimeDimension(timeDimensionId);
    this.disruption = disruption;
  }

  public DisruptionScenarioNode getSelectedDisruption() {
    return this.disruption;
  }

  public Collection<Scope> getScopes() {
    return scopes.values();
  }

  public int getTotalNumberOfKPIs() {
    return kpis.size();
  }

  public Collection<KPINode> getKPIs() {
    return kpis.values();
  }
}

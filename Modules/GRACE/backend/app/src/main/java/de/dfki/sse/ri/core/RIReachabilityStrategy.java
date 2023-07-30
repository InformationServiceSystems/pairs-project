package de.dfki.sse.ri.core;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.Set;

import de.dfki.sse.ri.model.DisruptionScenarioNode;
import de.dfki.sse.ri.model.KPINode;
import de.dfki.sse.ri.model.Model;
import de.dfki.sse.ri.model.Node;
import de.dfki.sse.ri.model.Scope;
import de.dfki.sse.ri.model.TimeDimension;

public class RIReachabilityStrategy implements RIStrategy {

  @Override
  public float calculateRI(Model model) {
    float resilienceIndex = 0;
    ArrayList<Scope> scopes = new ArrayList<>(model.getScopes());
    for (Scope scope: scopes) {
      float scopeIndex = 0;
      Set<Integer> kpiIds = scope.getKpiIds();
      for (int kpiId : kpiIds) {
        KPINode kpi = model.getKPI(kpiId);
        scopeIndex += kpi.getValue();
        System.out.println("KPI id " + kpiId + ": " + kpi.getValue());
      }
      scopeIndex = scopeIndex / kpiIds.size();
      System.out.println("Scope index: " + scopeIndex);
      resilienceIndex += scopeIndex;
    }
    resilienceIndex = resilienceIndex / scopes.size();
    return resilienceIndex;
  }

  @Override
  public void transform(Model model) {
    DisruptionScenarioNode disruption = model.getSelectedDisruption();
    TimeDimension dimension = disruption.getTimeDimension();
    float sumOfPathWeights =  0;
    for (Node currentNode: disruption.getAdjacentNodes()) {
      Set<Node> reachableNodes = new HashSet<>();
      collectReachableNodes(currentNode, reachableNodes);
      float sumOfWeights = 0;
      for (Node node : reachableNodes) {
        KPINode kpiNode = (KPINode) node;  
        sumOfWeights += kpiNode.getWeight();
      }
      float pathWeight = sumOfWeights / reachableNodes.size();
      sumOfPathWeights += pathWeight;
    }
    float backgroundRisk = dimension.getWeight() * sumOfPathWeights;
    float impact = disruption.getProbability() * backgroundRisk;
    for (KPINode kpi : model.getKPIs()) {
      kpi.setValue(kpi.getValue() - impact);
    }
  }

  private void collectReachableNodes(Node currentNode, Set<Node> reachableNodes) {
    reachableNodes.add(currentNode);
    for (Node adjacentNode : currentNode.getAdjacentNodes()) {
      if (!reachableNodes.contains(adjacentNode)) {
        collectReachableNodes(adjacentNode, reachableNodes);
      }
    }
  }


}

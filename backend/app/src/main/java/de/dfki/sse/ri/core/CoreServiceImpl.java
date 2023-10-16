package de.dfki.sse.ri.core;

public class CoreServiceImpl implements CoreService {

// 	private Graph graph;
// 	private ArrayList<Scope> scopes;
// 	private ResilienceIndex resilienceIndex;

// 	public CoreServiceImpl() {
// 	}

// 	public void readGraph(Graph importedGraph) {
// 		graph = importedGraph;
// 	}

// 	public void readScopes(ArrayList<Scope> importedScopes) {
// 		scopes = importedScopes;
// 	}

// 	@Override
// 	public ArrayList<KPINode> getKPIs() {
// 		ArrayList<KPINode> kpiNodes = new ArrayList<>();

// 			// All kpi nodes directly contained in graph
// 			List<Node> nodes = graph.getNodes();
// 			for (Node node : nodes) {
// 				if (node instanceof KPINode) {
// 					kpiNodes.add((KPINode) node);
// 				}
// 			}
// 			return kpiNodes;
// 		}

// 	@Override
// 	public ArrayList<DisruptionScenarioNode> getDisruptionScenarios() {
// 		ArrayList<DisruptionScenarioNode> dsNodes = new ArrayList<>();
// 		List<Node> nodes = graph.getNodes();
// 		for (Node node : nodes) {
// 			if (node instanceof DisruptionScenarioNode) {
// 				dsNodes.add((DisruptionScenarioNode) node);
// 			}
// 		}
// 		return dsNodes;
// 	}

// 	@Override
// 	public ArrayList<ActionCategory> getActionCategories() {
// 		ArrayList<ActionCategory> categories = new ArrayList<>();
// 		List<DisruptionScenarioNode> dsNodes = getDisruptionScenarios();
// 		for (DisruptionScenarioNode dsNode : dsNodes) {
// 			categories.addAll(dsNode.getPotentialActions());
// 		}
// 		return categories;
// 	}

// 	@Override
// 	public Graph getGraph() {return this.graph;}

// 	@Override
// 	public Index getActualResilienceIndex() {
// 		ResilienceIndex resilienceIndex = new ResilienceIndex();
// 		resilienceIndex.setScopes(this.scopes);
// 		List<KPINode> kpiNodes = getKPIs();
// 		for (KPINode node : kpiNodes) {
// 			Scope scope = node.getKpiScope();
// 			resilienceIndex.addScope(scope);
// 		}
// 		float derivedResilienceIndex = resilienceIndex.deriveResilienceIndex();
// 		System.out.println("Derived resilience index: " + derivedResilienceIndex);
// 		return resilienceIndex;
// 	}

// 	@Override
// 	public HistoryItem getResilienceIndexHistory() {
// 		ArrayList<HistoryItem> history = resilienceIndex.getIndexHistory();
// 		int size = history.size();
// 		// Check if there is a history item contained in the resilience history
// 		if (size > 0) {
// 			return history.get(history.size()-1);
// 		}
// 		return null;
// 	}

// 	@Override
// 	public Index getActualScopeIndex(Scope scope) {
// 		return scope.getScopeIndex();
// 	}

// 	@Override
// 	public HistoryItem getScopeIndexHistory(Scope scope) {
// 		ArrayList<HistoryItem> history = scope.getScopeIndex().getIndexHistory();
// 		int size = history.size();
// 		// Check if there is a history item contained in the resilience history
// 		if (size > 0) {
// 			return history.get(history.size()-1);
// 		}
// 		return null;
// 	}

// 	@Override
// 	public DisruptionScenarioNode getScenarioClassOfDisruption(DisruptionItem disruption) {
// 		return disruption.getScenarioClass();
// 	}

// 	@Override
// 	public ActionCategory getPossibleActions(DisruptionItem disruption) {
// 		return null;
// 	}

// 	@Override
// 	public ActualImpact getImpact(DisruptionItem disruption) {
// 		return disruption.getImpact();
// 	}

// 	@Override
// 	public ArrayList<KPINode> getInfluencedKPIs(ActionCategory action) {
// 		return action.getKPIsLoadingOn();
// 	}


}

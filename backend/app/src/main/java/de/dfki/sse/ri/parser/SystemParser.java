package de.dfki.sse.ri.parser;

import de.dfki.sse.ri.model.DisruptionScenarioNode;
import de.dfki.sse.ri.model.KPINode;
import de.dfki.sse.ri.model.Model;
import de.dfki.sse.ri.model.Scope;
import de.dfki.sse.ri.model.TimeDimension;
import java.util.ArrayList;
import java.util.List;
import org.json.JSONArray;
import org.json.JSONObject;

public class SystemParser {

  public static void parse(String config, Model model) {
    JSONObject json = new JSONObject(config);

    JSONArray jsonScopes = json.getJSONArray("scopes");
    List<Scope> scopes = parseScopes(jsonScopes);
    model.initializeScopes(scopes);

    JSONArray jsonKPIs = json.getJSONArray("kpis");
    List<KPINode> kpis = parseKPKpis(jsonKPIs);
    model.initializeKPIs(kpis);

    JSONArray jsonDisruptions = json.getJSONArray("disruptions");
    List<DisruptionScenarioNode> disruptions =
        parseDisruptions(jsonDisruptions);
    model.initializeDisruptions(disruptions);

    JSONArray jsonScopeKPIMatching = json.getJSONArray("scope_kpi_matching");
    matchScopeWithKPIs(jsonScopeKPIMatching, model);

    JSONArray jsonDisruptionKPIMatching =
        json.getJSONArray("disruption_kpi_matching");
    matchDisruptionWithKPIs(jsonDisruptionKPIMatching, model);

    JSONArray jsonGraph = json.getJSONArray("graph");
    initializeGraph(jsonGraph, model);
  }

  private static List<Scope> parseScopes(JSONArray jsonScopes) {
    List<Scope> scopes = new ArrayList<>();
    for (int i = 0; i < jsonScopes.length(); i++) {
      JSONObject jsonScope = jsonScopes.getJSONObject(i);
      int id = jsonScope.getInt("id");
      String name = jsonScope.getString("name");
      Scope scope = new Scope(name, id);
      scopes.add(scope);
    }
    return scopes;
  }

  private static List<KPINode> parseKPKpis(JSONArray jsonKPIs) {
    List<KPINode> kpis = new ArrayList<>();
    for (int i = 0; i < jsonKPIs.length(); i++) {
      JSONObject jsonKPI = jsonKPIs.getJSONObject(i);
      int id = jsonKPI.getInt("id");
      String name = jsonKPI.getString("name");
      float weight = jsonKPI.getFloat("weight");
      KPINode kpi = new KPINode(name, id, weight);
      kpis.add(kpi);
    }
    return kpis;
  }

  private static List<DisruptionScenarioNode>
  parseDisruptions(JSONArray jsonDisruptions) {
    List<DisruptionScenarioNode> disruptions = new ArrayList<>();
    for (int i = 0; i < jsonDisruptions.length(); i++) {
      JSONObject jsonDisruption = jsonDisruptions.getJSONObject(i);
      int id = jsonDisruption.getInt("id");
      String name = jsonDisruption.getString("name");
      float probability = jsonDisruption.getFloat("probability");
      JSONArray jsonTimeDimensions =
          jsonDisruption.getJSONArray("time_dimensions");
      List<TimeDimension> timeDimensions =
          parseTimeDimensions(jsonTimeDimensions);
      DisruptionScenarioNode discruption =
          new DisruptionScenarioNode(name, id, probability, timeDimensions);
      disruptions.add(discruption);
    }
    return disruptions;
  }

  private static List<TimeDimension>
  parseTimeDimensions(JSONArray jsonTimeDimensions) {
    List<TimeDimension> timeDimensions = new ArrayList<>();
    for (int i = 0; i < jsonTimeDimensions.length(); i++) {
      JSONObject jsonTimeDimension = jsonTimeDimensions.getJSONObject(i);
      int id = jsonTimeDimension.getInt("id");
      String description = jsonTimeDimension.getString("description");
      float weight = jsonTimeDimension.getFloat("weight");
      TimeDimension timeDimension = new TimeDimension(description, id, weight);
      timeDimensions.add(timeDimension);
    }
    return timeDimensions;
  }

  private static void
  matchDisruptionWithKPIs(JSONArray jsonDisruptionKPIMatching, Model model) {
    for (int i = 0; i < jsonDisruptionKPIMatching.length(); i++) {
      JSONObject jsonMatching = jsonDisruptionKPIMatching.getJSONObject(i);
      int disruptionId = jsonMatching.getInt("disruption");
      JSONArray jsonKPIs = jsonMatching.getJSONArray("kpis");
      List<Integer> kpiIds = parseKPIIds(jsonKPIs);
      model.matchDisruptionWithKPIs(disruptionId, kpiIds);
    }
  }

  private static void matchScopeWithKPIs(JSONArray jsonScopeKPIMatching,
                                         Model model) {
    for (int i = 0; i < jsonScopeKPIMatching.length(); i++) {
      JSONObject jsonMatching = jsonScopeKPIMatching.getJSONObject(i);
      int scopeId = jsonMatching.getInt("scope");
      JSONArray jsonKPIs = jsonMatching.getJSONArray("kpis");
      List<Integer> kpiIds = parseKPIIds(jsonKPIs);
      model.matchScopeWithKPIs(scopeId, kpiIds);
    }
  }

  private static void initializeGraph(JSONArray jsonGraph, Model model) {
    for (int i = 0; i < jsonGraph.length(); i++) {
      JSONObject jsonConnection = jsonGraph.getJSONObject(i);
      int sourceKPIId = jsonConnection.getInt("source");
      JSONArray jsonKPIs = jsonConnection.getJSONArray("destinations");
      List<Integer> kpiIds = parseKPIIds(jsonKPIs);
      model.connetKPIs(sourceKPIId, kpiIds);
    }
  }

  private static List<Integer> parseKPIIds(JSONArray jsonKPIs) {
    List<Integer> kpiIds = new ArrayList<>();
    for (int j = 0; j < jsonKPIs.length(); j++) {
      int kpiId = jsonKPIs.getInt(j);
      kpiIds.add(kpiId);
    }
    return kpiIds;
  }
}

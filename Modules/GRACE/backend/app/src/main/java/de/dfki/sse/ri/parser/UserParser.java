package de.dfki.sse.ri.parser;

import de.dfki.sse.ri.model.KPINode;
import de.dfki.sse.ri.model.Model;
import org.json.JSONArray;
import org.json.JSONObject;

public class UserParser {

  public static void parse(String config, Model model) {
    JSONObject json = new JSONObject(config);

    JSONArray jsonKPIs = json.getJSONArray("kpis");
    parseKPKpis(jsonKPIs, model);

    JSONObject jsonDisruption = json.getJSONObject("disruption");
    parseDisruption(jsonDisruption, model);
  }

  private static void parseKPKpis(JSONArray jsonKPIs, Model model) {
    for (int i = 0; i < jsonKPIs.length(); i++) {
      JSONObject jsonKPI = jsonKPIs.getJSONObject(i);
      int id = jsonKPI.getInt("id");
      float value = jsonKPI.getFloat("value");
      KPINode kpi = model.getKPI(id);
      kpi.setValue(value);
    }
  }

  private static void parseDisruption(JSONObject jsonDisruption, Model model) {
    int disruptionId = jsonDisruption.getInt("disruption_id");
    int timeDimensionId = jsonDisruption.getInt("time_dimension_id");
    model.setDisruption(disruptionId, timeDimensionId);
  }
}

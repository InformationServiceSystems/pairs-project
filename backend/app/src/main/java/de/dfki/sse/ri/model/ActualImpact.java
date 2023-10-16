package de.dfki.sse.ri.model;

public class ActualImpact {

	private DisruptionScenarioNode disruption;
	private float impact; 
	
	public ActualImpact() {
	}

	public DisruptionScenarioNode getDisruption() {
		return disruption;
	}

	public void setDisruption(DisruptionScenarioNode disruption) {
		this.disruption = disruption;
	}

	public float getImpact() {
		return impact;
	}

	public void setImpact(float impact) {
		this.impact = impact;
	} 
	
	// public void deriveActualImpact(){
	// 	this.impact=this.disruption.getProbabilityOfDisruption() * this.disruption.getScenarioClass().getBackgroundRisk().getRisk();
	// }
	
}

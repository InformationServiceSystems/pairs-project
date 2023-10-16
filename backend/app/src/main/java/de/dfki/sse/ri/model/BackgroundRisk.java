package de.dfki.sse.ri.model;

public class BackgroundRisk {

	private float backgroundRisk;
	private TimeDimension timeDimension;

	public float getRisk() {
		return backgroundRisk;
	}

	public void setRisk(float backgroundRisk) {
		this.backgroundRisk = backgroundRisk;
	}

	public TimeDimension getTimeDimensionImpact() {
		return timeDimension;
	}

	public void setTimeDimensionImpact(TimeDimension timeDimension) {
		this.timeDimension = timeDimension;
	}
	
}

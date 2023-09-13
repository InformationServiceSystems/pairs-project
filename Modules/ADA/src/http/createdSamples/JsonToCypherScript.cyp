CALL apoc.load.json('XXXXX') 
YIELD value
MERGE (dp:DPDO {id: value["dpdo:ProductDescriptionFacet"]["@id"]})

MERGE (p:ProductDescriptionFacet {id: value["dpdo:ProductDescriptionFacet"]["@id"]})
SET p.title = value["dpdo:ProductDescriptionFacet"]["gax-DataServiceOffering:hasServiceTitle"],
	p.theme = value["dpdo:ProductDescriptionFacet"]["dcat:theme"],
    p.subcategory = value["dpdo:ProductDescriptionFacet"]["dpdo:subcategory"],
    p.type = value["dpdo:ProductDescriptionFacet"]["gax-DataServiceOffering:hasType"],
    p.description = value["dpdo:ProductDescriptionFacet"]["gax-DataServiceOffering:hasServiceDescription"],
    p.accrualPeriodicity = value["dpdo:ProductDescriptionFacet"]["dct:accrualPeriodicity"],
    p.fileType = value["dpdo:ProductDescriptionFacet"]["gax-DataServiceOffering:hasContentType"],
    p.fileSize = value["dpdo:ProductDescriptionFacet"]["gax-DataServiceOffering:hasContentLength"],
    p.csvcol = value["dpdo:ProductDescriptionFacet"]["ov:csvcol"],
    p.dataType = value["dpdo:ProductDescriptionFacet"]["schema:DataType"]
MERGE (dp)-[:hasProductDescriptionFacet]->(p)

MERGE (q:QualityDescriptionFacet {id: value["dpdo:QualityDescriptionFacet"]["@id"]})
SET q.standard = value["dpdo:QualityDescriptionFacet"]["gax-DataServiceOffering:conformsToStandard"],
    q.standardReference = value["dpdo:QualityDescriptionFacet"]["gax-DataServiceOffering:StandardReference"]
MERGE (dp)-[:hasQualityDescriptionFacet]->(q)

MERGE (qs:QualityScore {id: value["dpdo:QualityDescriptionFacet"]["dqm:DataQualityScore"]["@id"]})
SET qs.plainScore = value["dpdo:QualityDescriptionFacet"]["dqm:DataQualityScore"]["dqm:plainScore"],
    qs.unit = value["dpdo:QualityDescriptionFacet"]["dqm:DataQualityScore"]["dqm:unitOfMeasurement"]
MERGE (q)-[:hasQualityScore]->(qs)

MERGE (a:Accuracy {id: value["dpdo:QualityDescriptionFacet"]["dqm:Accuracy"]["@id"]})
SET a.plainScore = value["dpdo:QualityDescriptionFacet"]["dqm:Accuracy"]["dqm:plainScore"],
    a.unit = value["dpdo:QualityDescriptionFacet"]["dqm:Accuracy"]["dqm:unitOfMeasurement"]
MERGE (q)-[:hasAccuracy]->(a)


MERGE (u:UsageDescriptionFacet {id: value["dpdo:UsageDescriptionFacet"]["@id"]})
SET u.localURL = value["dpdo:UsageDescriptionFacet"]["gax-DataServiceOffering:hasLocalURL"],
    u.modified = value["dpdo:UsageDescriptionFacet"]["dct:modified"]
MERGE (dp)-[:hasUsageDescriptionFacet]->(u)

MERGE (dist:Distribution {id: value["dpdo:UsageDescriptionFacet"]["dcat:Distribution"]["@id"]})
SET dist.startDate = value["dpdo:UsageDescriptionFacet"]["dcat:Distribution"]["dct:PeriodOfTime"]["dcat:startDate"],
    dist.endDate = value["dpdo:UsageDescriptionFacet"]["dcat:Distribution"]["dct:PeriodOfTime"]["dcat:endDate"]
MERGE (u)-[:hasDistribution]->(dist)

MERGE (tc:technicalContact {id: value["dpdo:UsageDescriptionFacet"]["gax-participant:IndividualContactTechnical"]["vcard:hasEmail"]})
SET tc.name = value["dpdo:UsageDescriptionFacet"]["gax-participant:IndividualContactTechnical"]["vcard:givenName"]
MERGE (u)-[:hasTechnicalContact]->(tc)


MERGE (v:Version {id: value["dpdo:UsageDescriptionFacet"]["dct:hasVersion"]["dct:isVersionOf"]["gax-DataServiceOffering:wasCreatedOn"]})
SET v.type = value["dpdo:UsageDescriptionFacet"]["dct:hasVersion"]["dct:isVersionOf"]["dpdo:type"],
	v.description = value["dpdo:UsageDescriptionFacet"]["dct:hasVersion"]["dct:isVersionOf"]["schema:description"],
    v.References = value["dpdo:UsageDescriptionFacet"]["dct:hasVersion"]["dct:isVersionOf"]["dct:References"]
MERGE (u)-[:hasVersion]->(v)


MERGE (b:BusinessDescriptionFacet {id: value["dpdo:BusinessDescriptionFacet"]["@id"]})
SET b.license = value["dpdo:BusinessDescriptionFacet"]["gax-DataServiceOffering:hasLicense"],
    b.PriceSpecification = value["dpdo:BusinessDescriptionFacet"]["schema:PriceSpecification"]
MERGE (dp)-[:hasBusinessDescriptionFacet]->(b)


MERGE (c:ContractDescription {id: value["dpdo:BusinessDescriptionFacet"]["proton:Contract"]["@id"]})
SET c.endDate = value["dpdo:BusinessDescriptionFacet"]["proton:Contract"]["dcat:endDate"],
    c.startDate = value["dpdo:BusinessDescriptionFacet"]["proton:Contract"]["dcat:startDate"],
	c.description = value["dpdo:BusinessDescriptionFacet"]["proton:Contract"]["schema:description"],
    c.permissions = value["dpdo:BusinessDescriptionFacet"]["proton:Contract"]["dpdo:Permissions"],
    c.sanctions = value["dpdo:BusinessDescriptionFacet"]["proton:Contract"]["dpdo:Sanctions"]
MERGE (b)-[:hasContractDescription]->(c)


MERGE (n:NegotiationProtocol {description: value["dpdo:BusinessDescriptionFacet"]["dpdo:NegotiationProtocol"]["schema:description"]})
MERGE (b)-[:hasNegotiationProtocol]->(n)


MERGE (t:TrustDescriptionFacet {id: value["dpdo:TrustDescriptionFacet"]["@id"]})
SET t.owner = value["dpdo:TrustDescriptionFacet"]["gax-asset:owned_by"]
MERGE (dp)-[:hasTrustDescriptionFacet]->(t)

MERGE (s:Source {id: value["dpdo:TrustDescriptionFacet"]["dct:Provenance"]["gax-participant:Provider"]["gax-participant:hasLegallyBindingName"]})
SET s.webAddress = value["dpdo:TrustDescriptionFacet"]["dct:Provenance"]["gax-participant:Provider"]["gax-provider:hasWebAddress"],
    s.jurisdiction = value["dpdo:TrustDescriptionFacet"]["dct:Provenance"]["gax-participant:Provider"]["gax-provider:hasJurisdiction"],
    s.salesTaxID = value["dpdo:TrustDescriptionFacet"]["dct:Provenance"]["gax-participant:Provider"]["gax-provider:hasSalesTaxID"],
    s.legalRegistrationNumber = value["dpdo:TrustDescriptionFacet"]["dct:Provenance"]["gax-participant:Provider"]["gax-provider:hasLegalRegistrationNumber"]
MERGE (t)-[:hasSource]->(s)

MERGE (pa:ProviderAddress {id: value["dpdo:TrustDescriptionFacet"]["dct:Provenance"]["gax-participant:Provider"]["gax-participant:hasLegallyBindingAddress"]["@id"]})
SET pa.street = value["dpdo:TrustDescriptionFacet"]["dct:Provenance"]["gax-participant:Provider"]["gax-participant:hasLegallyBindingAddress"]["vcard:street-address"],
    pa.locality = value["dpdo:TrustDescriptionFacet"]["dct:Provenance"]["gax-participant:Provider"]["gax-participant:hasLegallyBindingAddress"]["vcard:locality"],
    pa.country = value["dpdo:TrustDescriptionFacet"]["dct:Provenance"]["gax-participant:Provider"]["gax-participant:hasLegallyBindingAddress"]["vcard:country-name"]
MERGE (s)-[:hasProviderAddress]->(pa)

MERGE (lc:legalContact {id: value["dpdo:TrustDescriptionFacet"]["dct:Provenance"]["gax-participant:Provider"]["gax-participant:hasIndividualContactLegal"]["vcard:hasEmail"]})
SET lc.name = value["dpdo:TrustDescriptionFacet"]["dct:Provenance"]["gax-participant:Provider"]["gax-participant:hasIndividualContactLegal"]["vcard:givenName"]
MERGE (s)-[:hasLegalContact]->(lc)










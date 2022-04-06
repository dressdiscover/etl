from paradicms_etl.extractors.airtable_extractor import AirtableExtractor


class CostumeCoreOntologyAirtableExtractor(AirtableExtractor):
    def __init__(self, *, api_key: str, **kwds):
        AirtableExtractor.__init__(
            self,
            api_key=api_key,
            base_id="appfEYYWWn3CqSAxW",
            tables=(
                "feature_values",
                "features",
                "feature_sets",
                "images",
                "rights_licenses",
            ),
            **kwds,
        )

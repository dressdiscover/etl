import dataclasses

from paradicms_etl.models.creative_commons_licenses import CreativeCommonsLicenses
from paradicms_etl.models.rights import Rights
from paradicms_etl.transformers.luna_transformer import LunaTransformer


class UcDaapVacTransformer(LunaTransformer):
    def transform(self, **kwds):
        yield CreativeCommonsLicenses.BY_NC_ND
        yield from LunaTransformer.transform(**kwds)

    def _transform_institution(self, **kwds):
        institution = LunaTransformer._transform_institution(self, **kwds)
        assert institution.rights is None
        return dataclasses.replace(
            institution,
            rights=Rights(
                license=CreativeCommonsLicenses.BY_NC_ND.uri,
                statement="Copyright University of Cincinnati Libraries",
            ),
        )

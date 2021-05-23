from paradicms_etl._loader import _Loader
from paradicms_etl.models.dublin_core_property_definitions import (
    DublinCorePropertyDefinitions,
)
from paradicms_etl.models.object import Object
from rdflib import Literal


class AntConcTxtLoader(_Loader):
    def load(self, *, models):
        with open(
            self._loaded_data_dir_path / "AntConc.txt", "w+", newline="\n"
        ) as txt_file:
            for model in models:
                if not isinstance(model, Object):
                    continue
                object_ = model
                descriptions = set()
                if object_.abstract is not None:
                    descriptions.add(object.abstract)
                for property_ in object_.properties:
                    if not isinstance(property_.value, Literal):
                        continue
                    if property_.uri in (DublinCorePropertyDefinitions.DESCRIPTION,):
                        descriptions.add(str(property_.value.toPython()))
                if not descriptions:
                    continue

                txt_file.writelines([object_.uri] + list(descriptions) + [""])

from paradicms_etl.loader import Loader
from paradicms_etl.models.work import Work
from rdflib import Literal, DCTERMS


class AntConcTxtLoader(Loader):
    def load(self, *, models):
        with open(
            self._loaded_data_dir_path / "AntConc.txt",
            "w+",
            encoding="utf-8",
            newline="\n",
        ) as txt_file:
            for model in models:
                if not isinstance(model, Work):
                    continue
                work = model
                descriptions = set()
                if work.abstract is not None:
                    descriptions.add(work.abstract)
                for property_ in work.properties:
                    if not isinstance(property_.value, Literal):
                        continue
                    if property_.uri in [DCTERMS.description]:
                        descriptions.add(str(property_.value.toPython()))
                if not descriptions:
                    self._logger.warn("work %s has no description", work.uri)
                    continue

                lines = [str(work.uri), work.title]
                lines.extend(descriptions)
                lines.append("")
                lines.append("")
                txt_file.write("\n".join(lines))

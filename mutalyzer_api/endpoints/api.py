import logging

from flask import Blueprint, url_for
from flask_restx import Api, apidoc, Namespace, Resource

from mutalyzer.util import log_dir
# from .genes import ns as ns_annotated_genes
# from .transcripts import ns as ns_annotated_transcripts
from .coordinate_to_genomic import ns as ns_coordinate_to_g
from .coordinate_to_genomic_coding import ns as ns_coordinate_to_c_with_selector
from .serialization import ns as ns_serialization
from .coordinate_to_transcript_coding import ns as ns_coordinate_to_c_without_selector
from .coordinate_to_genomic_noncoding import ns as ns_coordinate_to_n_selector
from .coordinate_to_transcript_noncoding import ns as ns_coordinate_to_n_no_selector
from .coordinate_to_protein import ns as ns_coordinate_to_protein
from .coordinate_to_transcript_protein import ns as ns_coordinate_to_transcript_protein
from .coordinate_to_genomic_protein import ns as ns_coordinate_to_genomic_protein
from .genomic_to_coordinate import ns as ns_genomic_to_coordinate
from .genomic_coding_to_transcript import ns as ns_genomic_coding_to_transcript
from .trancript_coding_to_coordinate import ns as ns_trancript_coding_to_coordinate
from .genomic_noncoding_to_trancript import ns as ns_genomic_noncoding_to_trancript
from .transcript_noncoding_to_coordinate import ns as ns_transcript_noncoding_to_coordinate
from .protein_to_coordinate import ns as ns_protein_to_coordinate
from .genomic_protein_to_coordinate import ns as ns_genomic_protein_to_coordinate
from .transcript_protein_to_coordinate import ns as ns_transcript_protein_to_coordinate

from pkg_resources import get_distribution


logging.basicConfig(
    level=logging.INFO,
    filename=log_dir(),
    format='%(asctime)s %(levelname)-8s %(message)s'
)


API_VERSION = "3.0.0"


# Trick to make the swagger files available under "/api".
class PatchedApi(Api):
    def _register_apidoc(self, app):
        patched_api = apidoc.Apidoc(
            "restx_doc",
            "flask_restx.apidoc",
            template_folder="templates",
            static_folder="static",
            static_url_path="/api",
        )

        @patched_api.add_app_template_global
        def swagger_static(filename):
            return url_for("restx_doc.static", filename=filename)

        app.register_blueprint(patched_api)


blueprint = Blueprint("api", __name__)

api = PatchedApi(blueprint, version=API_VERSION, title="Mutalyzer3 API, Hello")

ns_version = Namespace("/")


@ns_version.route("/version")
class Version(Resource):
    def get(self):
        """Get versions."""
        return {"mutalyzer": get_distribution("mutalyzer").version, "api": API_VERSION}

api.add_namespace(ns_version)
# api.add_namespace(ns_annotated_genes)
# api.add_namespace(ns_annotated_transcripts)
api.add_namespace(ns_coordinate_to_g)
api.add_namespace(ns_coordinate_to_c_with_selector)
api.add_namespace(ns_serialization)
api.add_namespace(ns_coordinate_to_c_without_selector)
api.add_namespace(ns_coordinate_to_n_no_selector)
api.add_namespace(ns_coordinate_to_n_selector)
api.add_namespace(ns_coordinate_to_protein)
api.add_namespace(ns_coordinate_to_transcript_protein)
api.add_namespace(ns_coordinate_to_genomic_protein)

api.add_namespace(ns_genomic_to_coordinate)
api.add_namespace(ns_genomic_coding_to_transcript)
api.add_namespace(ns_trancript_coding_to_coordinate)
api.add_namespace(ns_genomic_noncoding_to_trancript)
api.add_namespace(ns_transcript_noncoding_to_coordinate)
api.add_namespace(ns_protein_to_coordinate)
api.add_namespace(ns_genomic_protein_to_coordinate)
api.add_namespace(ns_transcript_protein_to_coordinate)

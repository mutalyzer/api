from flask_restx import Namespace, Resource, inputs, reqparse

from mutalyzer.rna import dna_to_rna

from .common import errors

ns = Namespace("/")


@ns.route("/dna_to_rna/<string:description>")
class DnaToRna(Resource):
    @errors
    def get(self, description):
        """Predict the RNA description from a DNA description."""
        return dna_to_rna(description)

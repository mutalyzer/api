from flask_restx import Namespace, Resource, reqparse, inputs
from mutalyzer.equivalent import convert_to_genomic_description
from .common import errors

ns = Namespace("equivalent_hgvs")

@ns.route("/to-genomic/<string:description>")
class EquivalentHGVS(Resource):
    @errors
    def get(self, description):
        """Output genomic equivalent description."""
        return convert_to_genomic_description(description)
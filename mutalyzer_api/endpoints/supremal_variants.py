from flask_restx import Namespace, Resource, reqparse, inputs
from mutalyzer.equivalent import get_canonical_variants_string
from .common import errors

ns = Namespace("equivalent_hgvs")

@ns.route("/superemal_variants/<string:description>")
class Superemals(Resource):
    @errors
    def get(self, description):
        """Obtain supermal from input description."""
        return get_canonical_variants_string(description)
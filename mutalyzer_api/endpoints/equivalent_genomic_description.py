from flask_restx import Namespace, Resource, reqparse, inputs
from mutalyzer.equivalent import convert_to_genomic_description
from .common import errors
import argparse

ns = Namespace("equivalent_hgvs")

_args = reqparse.RequestParser()


_args.add_argument(
    "description",
    type=str,
    help="Variant description.",
    required=True,
)

@ns.route("/to_genomic/")
class EquivalentHGVStoGenomic(Resource):
    @ns.expect(_args)
    @errors
    def get(self):
        """Output genomic equivalent description."""
        args = _args.parse_args()
        return convert_to_genomic_description(**args)
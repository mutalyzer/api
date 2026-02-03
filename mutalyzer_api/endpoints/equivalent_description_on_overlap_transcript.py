from flask_restx import Namespace, Resource, reqparse, inputs
from mutalyzer.equivalent import convert_to_selector_description
from .common import errors

ns = Namespace("equivalent_hgvs")

_args = reqparse.RequestParser()

_args.add_argument(
    "description",
    type=str,
    help="Variant description.",
    required=True,
)

_args.add_argument(
    "selector_id",
    type=str,
    help="Selector ID.",
    required=True,
)

@ns.route("/to_selector/")
class EquivalentHGVStoSelector(Resource):
    @ns.expect(_args)
    @errors
    def get(self):
        """Output equivalent description on a selector."""
        args = _args.parse_args()
        return convert_to_selector_description(**args)
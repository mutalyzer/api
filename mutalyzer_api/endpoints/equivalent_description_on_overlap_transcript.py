from flask_restx import Namespace, Resource, reqparse, inputs
from mutalyzer.equivalent import convert_to_selector_description
from .common import errors

ns = Namespace("equivalent_hgvs")

_args = reqparse.RequestParser()

_args.add_argument(
    "selector_id",
    type=str,
    help="Selector ID.",
    required=True,
)

@ns.route("/to-selector/<string:description>")
class EquivalentHGVS(Resource):
    @ns.expect(_args)
    @errors
    def get(self, description):
        """Output equivalent description on a selector."""
        return convert_to_selector_description(description, **_args.parse_args())
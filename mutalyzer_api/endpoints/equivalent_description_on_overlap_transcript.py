from flask_restx import Namespace, Resource, reqparse, inputs
from mutalyzer.equivalent import convert_description
from .common import errors

ns = Namespace("equivalent_hgvs")

_args = reqparse.RequestParser()

_args.add_argument(
    "selectors",
    type=str,
    action="append",
    help="Selector IDs.",
    required=True,
)

@ns.route("/on_selectors/<string:description>")
class EquivalentHGVS(Resource):
    @ns.expect(_args)
    @errors
    def get(self, description):
        """Output equivalent desctiptions on a list of selectors/transcripts."""
        return convert_description(description, **_args.parse_args())
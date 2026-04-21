from flask_restx import Namespace, Resource, reqparse, inputs
from mutalyzer.positions import coordinate_to_protein
from .common import errors

ns = Namespace("position_converter", path="/")

_args = reqparse.RequestParser()

_args.add_argument(
    "coordinate",
    type=int,
    help="Zero based coordinate on reference sequence.",
    required=True
)

@ns.route("/coordinate_to_protein/")
@ns.param('coordinate', 'Zero-based coordinate on reference sequence.', example=100)
class CoordinateToProtein(Resource):
    @ns.expect(_args)
    @errors
    def get(self):
        """Convert from coordinate to protein position."""
        args = _args.parse_args()
        coordinate = args.get("coordinate")
        try:
            converted_model = coordinate_to_protein(coordinate)
            return converted_model
        except Exception as e:
            return {"errors": [str(e)]}
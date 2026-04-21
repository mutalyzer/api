from flask_restx import Namespace, Resource, reqparse, inputs
from mutalyzer.positions import coordinate_to_genomic
from .common import errors

ns = Namespace("position_converter", path="/")

_args = reqparse.RequestParser()

_args.add_argument(
    "coordinate",
    type=int,
    help="Zero based coordinate on reference sequence.",
    required=True
)

@ns.route("/coordinate_to_genomic/")
@ns.param('coordinate', 'Zero-based coordinate on reference sequence.', example=1000000)
class CoordinateToGenomic(Resource):
    @ns.expect(_args)
    @errors
    def get(self):
        """Convert from coordinate to genomic position."""
        args = _args.parse_args()
        coordinate = args.get("coordinate")

        try:
            converted_model = coordinate_to_genomic(coordinate)
            return converted_model
        except ValueError as e:
            return {"error": str(e)}
from flask_restx import Namespace, Resource, reqparse, inputs
from mutalyzer.positions import protein_to_coordinate
from .common import errors

ns = Namespace("position_converter", path="/")

_args = reqparse.RequestParser()


_args.add_argument(
    "position",
    type=int,
    help="Zero based position on reference sequence.",
    required=True
)


@ns.route("/protein_to_coordinate/")
class ProteinToCoordinate(Resource):
    @ns.expect(_args)
    @errors
    def get(self):
        """Convert from protein position to coordinate."""
        args = _args.parse_args()
        position = args.get("position")

        position_m = {'position': position,'position_in_codon': 1, 'offset': 0, 'region': ""}
        try:
            coordinate = protein_to_coordinate(position_m)
            return coordinate
        except Exception as e:
            return {"errors": [str(e)]}

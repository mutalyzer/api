from flask_restx import Namespace, Resource, reqparse, inputs
from mutalyzer.positions import genomic_to_coordinate
from .common import errors

ns = Namespace("position_converter", path="/")

_args = reqparse.RequestParser()

_args.add_argument(
    "position",
    type=int,
    help="Position in HGVS genomic model.",
    required=True
)


@ns.route("/genomic_to_coordinate/")
class GenomicToCoordinate(Resource):
    @ns.expect(_args)
    @errors
    def get(self):
        """Convert from genomic position to coordinate."""
        args = _args.parse_args()
        position = args.get("position")

        position_model = {'position': position}

        try:
            coordinate = genomic_to_coordinate(position_model)
            return coordinate
        except Exception as e:
            return {"errors": [str(e)]}
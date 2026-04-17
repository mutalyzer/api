from flask_restx import Namespace, Resource, reqparse, inputs
from mutalyzer.positions import coordinate_to_coding
from .common import errors
from dataclasses import asdict


ns = Namespace("position_converter", path="/")

_args = reqparse.RequestParser()

_args.add_argument(
    "reference_id",
    type=str,
    help="Reference ID.",
    required=True,
)

_args.add_argument(
    "transcript_id",
    type=str,
    help="Transcript ID.",
    required=True,
)

_args.add_argument(
    "coordinate",
    type=int,
    help="Zero based coordinate on reference sequence.",
    required=True
)

@ns.route("/coordinate_to_genomic_coding")
class CoordinateToCodingSelector(Resource):
    @ns.expect(_args)
    @errors
    def get(self):
        """Convert from coordinate to coding position."""
        args = _args.parse_args()
        ref_id = args.get("reference_id")
        transcript_id = args.get("transcript_id")
        coordinate = args.get("coordinate")

        try:
            position_model = coordinate_to_coding(ref_id, coordinate, transcript_id)
            return position_model
        except ValueError as e:
            return {"error": str(e)}

from flask_restx import Namespace, Resource, reqparse, inputs
from mutalyzer.positions import coordinate_to_noncoding
from .common import errors

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

@ns.route("/coordinate_to_genomic_noncoding")
@ns.param('coordinate', 'Zero-based coordinate on reference sequence.', example=73852615)
@ns.param('transcript_id', 'Transcript ID.', example='NR_001564.3')
@ns.param('reference_id', 'Reference ID.', example='NC_000023.11')
class CoordinateToNoncodingSelector(Resource):
    @ns.expect(_args)
    @errors
    def get(self):
        """Convert from coordinate to non-coding position."""
        args = _args.parse_args()
        ref_id = args.get("reference_id")
        transcript_id = args.get("transcript_id")
        coordinate = args.get("coordinate")

        try:
            converted_model = coordinate_to_noncoding(ref_id, coordinate, transcript_id)
            return converted_model
        except ValueError as e:
            return {"error": str(e)}

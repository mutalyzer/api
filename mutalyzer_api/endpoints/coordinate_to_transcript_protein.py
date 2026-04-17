from flask_restx import Namespace, Resource, reqparse, inputs
from mutalyzer.positions import coordinate_to_reference_protein
from .common import errors

ns = Namespace("position_converter", path="/")

_args = reqparse.RequestParser()

_args.add_argument(
    "transcript_id",
    type=str,
    help="Transcript ID.",
    required=True
)

_args.add_argument(
    "protein_id",
    type=str,
    help="Protein ID.",
    required=True
)

_args.add_argument(
    "coordinate",
    type=int,
    help="Zero based coordinate on reference sequence.",
    required=True
)

@ns.route("/coordinate_to_transcript_protein/")
class CoordinateToTranscriptProtein(Resource):
    @ns.expect(_args)
    @errors
    def get(self):
        """Convert from coordinate to  protein position."""
        args = _args.parse_args()
        ref_id = args.get("transcript_id")
        protein_id = args.get("protein_id")
        coordinate = args.get("coordinate")
        try:
            converted_model = coordinate_to_reference_protein(ref_id, coordinate, protein_id)
            return converted_model
        except Exception as e:
            return {"errors": [str(e)]}
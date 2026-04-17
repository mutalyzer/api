from flask_restx import Namespace, Resource, reqparse, inputs
from mutalyzer.positions import transcript_protein_to_coordinate
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
    "position",
    type=int,
    help="Position in HGVS protein model.",
    required=True
)

_args.add_argument(
    "position_in_codon",
    type=int,
    help="Position in the codon, 1, 2, or 3.",
    required=True,
    choices=[1, 2, 3],
    default=1
)


@ns.route("/transcript_protein_to_coordinate/")
class TranscriptProteinToCoordinate(Resource):
    @ns.expect(_args)
    @errors
    def get(self):
        """Convert from protein position to coordinate."""
        args = _args.parse_args()
        transcript_id = args.get("transcript_id")
        protein_id = args.get("protein_id")
        position = args.get("position")
        position_in_codon = args.get("position_in_codon")

        position_model = {'position': position, 'position_in_codon': position_in_codon, 'offset': 0, 'region': ""}

        try:
            coordinate = transcript_protein_to_coordinate(transcript_id, protein_id, position_model)
            return coordinate
        except Exception as e:
            return {"errors": [str(e)]}
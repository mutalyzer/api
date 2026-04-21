from flask_restx import Namespace, Resource, reqparse, inputs
from mutalyzer.positions import transcript_noncoding_to_coordinate
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
    "position",
    type=int,
    help="Position in HGVS non-coding model.",
    required=True
)

_args.add_argument(
    "offset",
    type=int,
    help="Offset in HGVS non-coding model.",
    required=False,
    default=0
)




@ns.route("/transcript_noncoding_to_coordinate/")
@ns.param('offset', 'Offset in HGVS non-coding model.', example=0)
@ns.param('position', 'Position in HGVS non-coding model.', example=100)
@ns.param('transcript_id', 'Transcript ID.', example='NR_001564.3')

class TranscriptNoncodingToCoordinate(Resource):
    @ns.expect(_args)
    @errors
    def get(self):
        """Convert from non-coding position to coordinate."""
        args = _args.parse_args()
        transcript_id = args.get("transcript_id")
        position = args.get("position")
        offset = args.get("offset")

        position_model = {'position': position, 'position_in_codon': 1, 'offset': offset, 'region': ""}

        try:
            coordinate = transcript_noncoding_to_coordinate(transcript_id, position_model)
            return coordinate
        except Exception as e:
            return {"errors": [str(e)]}
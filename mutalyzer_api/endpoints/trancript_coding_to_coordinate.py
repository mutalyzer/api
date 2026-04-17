from flask_restx import Namespace, Resource, reqparse, inputs
from mutalyzer.positions import transcript_coding_to_coordinate
from mutalyzer.positions import genomic_to_coordinate
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
    help="Position in HGVS coding model.",
    required=True
)

_args.add_argument(
    "region",
    type=str,
    help=("Region type in HGVS coding model."),
    required=True,
    choices=["-: 5 prime", ": cds", "*: 3 prime",],
)

@ns.route("/trancript_coding_to_coordinate/")
class TrancriptCodingToCoordinate(Resource):
    @ns.expect(_args)
    @errors
    def get(self):
        """Convert from coding position to coordinate."""
        args = _args.parse_args()
        transcript_id = args.get("transcript_id")
        position = args.get("position")
        region = args.get("region").split(":")[0]

        position_model = {'position': position, 'offset': 0, 'region': region}

        try:
            coordinate = transcript_coding_to_coordinate(transcript_id, position_model)
            return coordinate
        except Exception as e:
            return {"errors": [str(e)]}
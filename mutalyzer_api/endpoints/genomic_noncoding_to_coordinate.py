from flask_restx import Namespace, Resource, reqparse, inputs
from mutalyzer.positions import genomic_noncoding_to_coordinate
from .common import errors

ns = Namespace("position_converter", path="/")

_args = reqparse.RequestParser()

_args.add_argument(
    "reference_id",
    type=str,
    help="Reference ID.",
    required=True
)

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

_args.add_argument(
    "region",
    type=str,
    help=("Region type in HGVS non-coding model."),
    required=False,
    default="transcribed region",
    choices=["u: upstream", ": transcribed region",  "d: downstream"],
)


@ns.route("/genomic_noncoding_to_coordinate/")
@ns.param('region', 'Region type in HGVS non-coding model.', example='transcribed region')
@ns.param("offset", "Offset in HGVS non-coding model.", example=0)
@ns.param('position', 'Position in HGVS non-coding model.', example=100)
@ns.param('transcript_id', 'Transcript ID.', example='NR_001564.3')
@ns.param('reference_id', 'Reference ID.', example='NC_000023.11')
class GenomicNoncodingToCoordinate(Resource):
    @ns.expect(_args)
    @errors
    def get(self):
        """Convert from non-coding position to coordinate."""
        args = _args.parse_args()
        ref_id = args.get("reference_id")
        transcript_id = args.get("transcript_id")
        position = args.get("position")
        offset = args.get("offset")
        region = args.get("region").split(":")[0]

        position_model = {'position': position, 'offset': offset, 'region': region}

        try:
            coordinate = genomic_noncoding_to_coordinate(ref_id, transcript_id, position_model)
            return coordinate
        except Exception as e:
            return {"errors": [str(e)]}
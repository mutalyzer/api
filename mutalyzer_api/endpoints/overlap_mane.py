from flask_restx import Namespace, Resource, reqparse
from mutalyzer.equivalent import overlap_mane_selectors
from .common import errors

ns = Namespace("equivalent_hgvs")

# define query parameters parser
_args = reqparse.RequestParser()
_args.add_argument(
    "start",
    type=int,
    required=True,
    help="Start position (integer)."
)
_args.add_argument(
    "end",
    type=int,
    required=True,
    help="End position (integer)."
)

@ns.route("/transcripts/overlap_mane/<string:reference_id>")
class OverlapMANE(Resource):
    @errors
    @ns.expect(_args)
    def get(self, reference_id):
        """Obtain overlapping MANE Select transcripts from input reference and location."""
        args = _args.parse_args()
        start = args["start"]
        end = args["end"]
        return overlap_mane_selectors(reference_id, start, end)

from flask_restx import Namespace, Resource, reqparse
from mutalyzer.equivalent import overlap_genes
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

@ns.route("/genes/overlap/<string:reference_id>")
class OverlapGenes(Resource):
    @errors
    @ns.expect(_args)
    def get(self, reference_id):
        """Obtain overlapping genes from input reference and location."""
        args = _args.parse_args()
        start = args["start"]
        end = args["end"]
        return overlap_genes(reference_id, start, end)

from flask_restx import Namespace, Resource, reqparse
from mutalyzer.equivalent import overlap_genes
from .common import errors

ns = Namespace("equivalent_hgvs")

# define query parameters parser
_args = reqparse.RequestParser()
_args.add_argument("start", required=True, type=int)
_args.add_argument("end", required=True, type=int)

@ns.route("/<string:reference_id>/genes/overlap")
class Genes(Resource):
    @errors
    @ns.expect(_args)
    def get(self, reference_id):
        """List genes under a reference and filtered by overlap."""
        args = _args.parse_args()
        start = args.get("start")
        end = args.get("end")

        if (start is None) != (end is None):
            return {"Infos": "Both 'start' and 'end' must be provided."}, 400

        if start is not None:
            if start > end:
                return {"Infos": "'start' must be no less than 'end'."}, 400
            return overlap_genes(reference_id, start, end)

        return overlap_genes(reference_id)

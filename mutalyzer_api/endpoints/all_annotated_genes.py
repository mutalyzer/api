from flask_restx import Namespace, Resource, reqparse
from mutalyzer.equivalent import annotated_genes
from .common import errors

ns = Namespace("equivalent_hgvs")

_args = reqparse.RequestParser()

_args.add_argument(
    "reference_id",
    type=str,
    help="Reference ID.",
    required=True,
)

@ns.route("/annotated_genes/")
class AnnotatedGenes(Resource):
    @ns.expect(_args)
    @errors
    def get(self):
        """List all annotated genes under a reference sequence ID."""
        reference_id = _args.parse_args().get("reference_id")
        return annotated_genes(reference_id)

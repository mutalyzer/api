from flask_restx import Namespace, Resource, reqparse, inputs
from mutalyzer.equivalent import annotated_transcripts
from .common import errors

ns = Namespace("equivalent_hgvs")

# define query parameters parser
_args = reqparse.RequestParser()
_args.add_argument(
    "gene_symbol",
    type=str,
    required=True,
    help="Gene symbol (string)."
)

@ns.route("/transcripts/annotated_under_gene/<string:reference_id>")
class AnnotatedTranscripts(Resource):
    @errors
    @ns.expect(_args)
    def get(self, reference_id):
        """Obtain all annotated transcripts from a reference sequence ID under a specific gene."""
        args = _args.parse_args()
        return annotated_transcripts(reference_id, args.gene_symbol)
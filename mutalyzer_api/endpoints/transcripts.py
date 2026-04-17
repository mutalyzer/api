from flask_restx import Namespace, Resource, reqparse, inputs
from mutalyzer.equivalent import annotated_transcripts, overlap_mane_selectors
from .common import errors

ns = Namespace("transcripts", path="/")

_args_all_transcripts = reqparse.RequestParser()

_args_all_transcripts.add_argument(
    "reference_id",
    type=str,
    help="Reference ID.",
    required=True,
)

_args_all_transcripts.add_argument(
    "gene_symbol",
    type=str,
    help="Gene symbol.",
    required=True,
)


@ns.route("/all_transcripts/")
class AnnotatedTranscripts(Resource):
    @ns.expect(_args_all_transcripts)
    @errors
    def get(self):
        """List all annotated transcripts for a gene under a reference sequence."""
        args = _args_all_transcripts.parse_args()
        reference_id = args.get("reference_id")
        gene_symbol = args.get("gene_symbol")
        return annotated_transcripts(reference_id, gene_symbol=gene_symbol)




_args_mane_transcript = reqparse.RequestParser()
_args_mane_transcript.add_argument(
    "gene_symbol",
    type=str,
    help="Gene symbol.",
    required=True,
)

@ns.route("/mane_transcripts/")
class AnnotatedMANETranscripts(Resource):
    @ns.expect(_args_mane_transcript)
    @errors
    def get(self):
        """Get a MANE Select transcript for a gene under a reference sequence."""
        args = _args_mane_transcript.parse_args()
        gene_symbol = args.get("gene_symbol")
        return overlap_mane_selectors(gene_symbol)

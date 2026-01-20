from flask_restx import Namespace, Resource, reqparse, inputs
from mutalyzer.equivalent import annotated_transcripts
from .common import errors

ns = Namespace("equivalent_hgvs")

@ns.route("/<string:reference_id>/transcripts/all/on-gene/<string:gene_symbol>")
class AnnotatedTranscripts(Resource):
    @errors
    def get(self, reference_id, gene_symbol):
        """List all annotated transcripts for a gene under a reference sequence."""
        return annotated_transcripts(reference_id, gene_symbol)
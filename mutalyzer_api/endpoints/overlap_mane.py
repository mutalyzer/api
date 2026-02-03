from flask_restx import Namespace, Resource, reqparse
from mutalyzer.equivalent import overlap_mane_selectors
from .common import errors

ns = Namespace("equivalent_hgvs")

@ns.route("/<string:reference_id>/transcripts/MANE/on-gene/<string:gene_symbol>")
class AnnotatedTranscripts(Resource):
    @errors
    def get(self, reference_id, gene_symbol):
        """Get a MANE Select transcript for a gene under a reference sequence."""
        return overlap_mane_selectors(reference_id, gene_symbol)

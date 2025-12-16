from flask_restx import Namespace, Resource, reqparse, inputs
from mutalyzer.equivalent import annotated_transcripts
from .common import errors

ns = Namespace("equivalent_hgvs")

@ns.route("/transcripts/all/<string:reference_id>")
class AnnotatedTranscripts(Resource):
    @errors
    def get(self, reference_id):
        """Obtain all annoated transcripts from input description."""
        return annotated_transcripts(reference_id)

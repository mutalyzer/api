from flask_restx import Namespace, Resource
from mutalyzer.equivalent import annotated_genes
from .common import errors

ns = Namespace("equivalent_hgvs")

@ns.route("/<string:reference_id>/genes/all")
class AnnotatedGenes(Resource):
    @errors
    def get(self, reference_id):
        """List all annotated genes under a reference sequence ID."""
        return annotated_genes(reference_id)

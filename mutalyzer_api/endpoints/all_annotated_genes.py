from flask_restx import Namespace, Resource, reqparse, inputs
from mutalyzer.equivalent import annotated_genes
from .common import errors

ns = Namespace("equivalent_hgvs")

@ns.route("/genes/all/<string:reference_id>")
class AnnotatedGenes(Resource):
    @errors
    def get(self, reference_id):
        """Obtain all annotated genes from a reference sequence ID."""
        return annotated_genes(reference_id)
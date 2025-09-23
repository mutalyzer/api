from flask import request
from flask_restx import Namespace, Resource, reqparse
from mutalyzer_retriever.related import get_related

from .common import errors

ns = Namespace("/")

parser = reqparse.RequestParser()
parser.add_argument(
    'locations',
    type=str,
    required=False,
    default="0",
    help='Semicolon-separated genomic location ranges (e.g., 100;300_400)'
)
@ns.route("/related/<string:accession>")
class RelatedReferences(Resource):
    @ns.expect(parser)
    @errors
    def get(self, accession):
        args = parser.parse_args()
        locations = args['locations']

        return get_related(accession, locations)


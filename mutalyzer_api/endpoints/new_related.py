from flask import request
from flask_restx import Namespace, Resource, reqparse
from mutalyzer_retriever.new_related import get_new_related

from .common import errors

ns = Namespace("/")

parser = reqparse.RequestParser()
parser.add_argument(
    'locations',
    type=str,
    action='append',
    required=False,
    default=["0-0"],
    help='Location ranges (e.g., 100-200). Repeat this parameter for multiple values.'
)
@ns.route("/new_related/<string:accession>")
class NewRelatedReferences(Resource):
    @ns.expect(parser)
    @errors
    def get(self, accession):
        args = parser.parse_args()
        locations = args['locations']  # e.g. ["112088970-112088970", "130000000-131000000"]

        # Convert each "start-end" string into ["start", "end"]
        parsed_locations = [loc.split("-", 1) for loc in locations]

        return get_new_related(accession, parsed_locations)


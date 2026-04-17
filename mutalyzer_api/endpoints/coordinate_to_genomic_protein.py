from flask_restx import Namespace, Resource, reqparse, inputs
from mutalyzer.positions import coordinate_to_reference_protein
from .common import errors

ns = Namespace("position_converter", path="/")

_args = reqparse.RequestParser()

_args.add_argument(
    "reference_id",
    type=str,
    help="Reference ID.",
    required=True
)

_args.add_argument(
    "protein_id",
    type=str,
    help="Protein ID.",
    required=True
)

_args.add_argument(
    "coordinate",
    type=int,
    help="Zero based coordinate on reference sequence.",
    required=True
)

@ns.route("/coordinate_to_genomic_protein/")
class CoordinateToGenomicProtein(Resource):
    @ns.expect(_args)
    @errors
    def get(self):
        """Convert from coordinate to protein position."""
        args = _args.parse_args()
        ref_id = args.get("reference_id")
        protein_id = args.get("protein_id")
        coordinate = args.get("coordinate")
        try:
            converted_model = coordinate_to_reference_protein(ref_id, coordinate, protein_id)
            return converted_model
        except Exception as e:
            return {"errors": [str(e)]}
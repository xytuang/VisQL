import json

class Diagram:
    def __init__(self):
        self.diagram = True

    def add_rect(self, source_table, x, y, width, height):
        pass

    def render(self):
        schema = {
            "$schema": "https://vega.github.io/schema/vega/v5.json",
            "width": 200,
            "height": 100,
            "padding": 5,

            "data": [
                {
                    "name": "table",
                    "values": [
                        {"category": "A", "amount": 28},
                        {"category": "B", "amount": 55},
                        {"category": "C", "amount": 43}
                    ]
                }
            ],

            "scales": [
                {
                    "name": "xscale",
                    "type": "band",
                    "domain": {"data": "table", "field": "category"},
                    "range": "width",
                    "padding": 0.05,
                    "round": True
                },
                {
                    "name": "yscale",
                    "domain": {"data": "table", "field": "amount"},
                    "nice": True,
                    "range": "height"
                }
            ],

            "axes": [
                {"orient": "bottom", "scale": "xscale"},
                {"orient": "left", "scale": "yscale"}
            ],

            "marks": [
                {
                    "type": "rect",
                    "from": {"data": "table"},
                    "encode": {
                        "enter": {
                            "x": {"scale": "xscale", "field": "category"},
                            "width": {"scale": "xscale", "band": 1},
                            "y": {"scale": "yscale", "field": "amount"},
                            "y2": {"scale": "yscale", "value": 0}
                        },
                        "update": {
                            "fill": {"value": "steelblue"}
                        },
                        "hover": {
                            "fill": {"value": "red"}
                        }
                    }
                }
            ]
        }
        print(json.dumps(schema))
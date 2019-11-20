from tempfile import NamedTemporaryFile

import pytest

from anytree.importer import JsonImporter
from anytree.exporter import DictExporter


def test_json_importer():
    """Json Importer."""
    refdata = {
        'id': 'root', 'children': [
            {'id': 'sub0', 'children': [
                {'id': 'sub0B'},
                {'id': 'sub0A'}
            ]},
            {'id': 'sub1', 'children': [
                {'id': 'sub1A'},
                {'id': 'sub1B'},
                {'id': 'sub1C', 'children': [
                    {'id': 'sub1Ca'}
                ]}
            ]}
        ]}
    lines = [
        '{',
        '  "children": [',
        '    {',
        '      "children": [',
        '        {',
        '          "id": "sub0B"',
        '        },',
        '        {',
        '          "id": "sub0A"',
        '        }',
        '      ],',
        '      "id": "sub0"',
        '    },',
        '    {',
        '      "children": [',
        '        {',
        '          "id": "sub1A"',
        '        },',
        '        {',
        '          "id": "sub1B"',
        '        },',
        '        {',
        '          "children": [',
        '            {',
        '              "id": "sub1Ca"',
        '            }',
        '          ],',
        '          "id": "sub1C"',
        '        }',
        '      ],',
        '      "id": "sub1"',
        '    }',
        '  ],',
        '  "id": "root"',
        '}'
    ]

    imported = DictExporter().export(JsonImporter().import_("\n".join(lines)))
    assert refdata == imported
    with NamedTemporaryFile(mode="w+") as ref:
        ref.write("\n".join(lines))
        ref.seek(0)
        imported = DictExporter().export(JsonImporter().read(ref))
    assert refdata == imported

# Simpress

Simpress, simple document server based on GitHub flavored Markdown.

## Installation

You can install it through PyPI (the Python Package Index).

```
pip install simpress
```

## Quickstart

```
press-init <your document dir>
```

press-init command creates the new document directory, so your document dir shouldn't exist in advance.

```
cd <your document dir>
./press.py preview
```

Start preview server on port 3776 in default.

Edit `index.md` or add new file(s).

## Publish static HTMLs

```
./press.py publish
```

Publish all pages as static file in `<your document dir>/_deploy/`.

## Customize

### Configuration file

`press.py` has a little config parameters.

### Your original theme

You can customize the document theme in `_templates/*`, `css/*`, `js/*` on your document directory.

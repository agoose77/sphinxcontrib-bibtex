import common
import pytest


@pytest.mark.sphinx('latex', testroot='latex_refs')
def test_latex_refs(app, warning):
    app.build()
    assert not warning.getvalue()
    output = (app.outdir / "test.tex").read_text()
    assert len(common.latex_citations().findall(output)) == 1
    assert len(common.latex_citation_refs().findall(output)) == 1
    match = common.latex_citations().search(output)
    match_ref = common.latex_citation_refs().search(output)
    assert match.group('label') == 'Huy57'
    assert match.group('docname') == 'index'
    assert "De ratiociniis in ludo aleæ." in match.group('text')
    assert match_ref.group('refid') == match.group('id_')
    assert match_ref.group('docname') == 'index'


@pytest.mark.sphinx('latex', testroot='latex_multidoc')
def test_latex_multidoc(app, warning):
    app.build()
    assert not warning.getvalue()
    output = (app.outdir / "test.tex").read_text()
    assert len(common.latex_citations().findall(output)) == 1
    assert len(common.latex_citation_refs().findall(output)) == 1
    match = common.latex_citations().search(output)
    match_ref = common.latex_citation_refs().search(output)
    assert match.group('docname') == match_ref.group('docname') == 'sources'
    assert match.group('id_') is not None
    assert match_ref.group('refid') == match.group('id_')


@pytest.mark.skip('potential upstream sphinx problem, see issue #226')
@pytest.mark.sphinx('html', testroot='latex_refs')
def test_latex_after_html(make_app, app_params):
    args, kwargs = app_params
    app = make_app('html', freshenv=True, **kwargs)
    app.build()
    assert not app._warning.getvalue()
    app = make_app('latex', freshenv=False, **kwargs)
    app.build()
    assert 'could not find bibtex key' not in app._warning.getvalue()

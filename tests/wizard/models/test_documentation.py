import pytest
from django.core.exceptions import ValidationError

from wizard import models
from .tools import make_challenge

pytestmark = pytest.mark.django_db


def make_page(name, content, doc=None):
    doc = doc or models.DocumentationModel.create()
    t = models.DocumentationPageModel.create(doc=doc,
                                             name=name,
                                             content=content)
    return t


class TestTemplatingSystem:
    def test_challenge_template_mapping(self):
        c = make_challenge()
        mapping = c.template_mapping

        assert mapping['challenge_title'] == c.title
        assert mapping['challenge_organization_name'] == c.organization_name
        assert mapping['challenge_description'] == c.description

    def test_challenge_template_doc(self):
        c = make_challenge(None)
        auto_doc = c.template_doc

        assert 'challenge_title' in auto_doc
        assert 'challenge_organization_name' in auto_doc
        assert 'challenge_description' in auto_doc


class TestDocumentationPageModel:
    def test_has_title_and_content(self):
        t = make_page('my_title', 'lorem ipsum')

        assert t.name == 'my_title'
        assert t.content == 'lorem ipsum'

    def test_rendered_is_none_by_default(self):
        t = make_page('my_title', 'lorem ipsum')

        assert t.rendered is None

    def test_can_be_compiled(self):
        t = make_page('my_title', 'this is a $variable')
        t.render({'variable': 'template'})

        assert t.rendered == 'this is a template'

    def test_displayed_shows_content_by_default(self):
        t = make_page('my_title', 'this is a $variable')
        assert t.displayed == t.content

    def test_displayed_shows_rendered_when_present(self):
        t = make_page('my_title', 'this is a $variable')
        t.render({'variable': 'template'})
        assert t.displayed == t.rendered

    def test_is_rendered_is_false_by_default(self):
        t = make_page('my_title', 'this is a $variable')
        assert not t.is_rendered

    def test_is_rendered_is_true_after_render(self):
        t = make_page('my_title', 'this is a $variable')
        t.render({'variable': 'template'})
        assert t.is_rendered

    def test_title_should_be_a_slug(self):
        try:
            make_page('something with spaces', 'content')
            assert False, 'spaces in title should not pass'
        except ValidationError:
            assert True


class TestDocumentationModel:
    def test_create_the_default_documentation_model(self):
        t = models.DocumentationModel.create()
        assert t is not None

    def test_default_documentation_contains_3_pages(self):
        t = models.DocumentationModel.create()

        assert len(t.pages) == 4

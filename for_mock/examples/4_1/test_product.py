# test_product.py

from unittest.mock import MagicMock
# from mock import MagicMock

from pytest import raises

from factory import Product, BadProductQualityError


def test_bed_product_quality_because_of_shape():
    mock_quality_checker = MagicMock()
    mock_quality_checker.checkpoint_1.return_value = 94

    p = Product(mock_quality_checker)
    p.create()
    with raises(BadProductQualityError) as e:
        p.check_quality()
    assert "Shape" in str(e)


def test_bed_product_quality_because_of_color():
    mock_quality_checker = MagicMock()
    mock_quality_checker.checkpoint_1.return_value = 95
    mock_quality_checker.checkpoint_2.return_value = 89

    p = Product(mock_quality_checker)
    p.create()
    with raises(BadProductQualityError) as e:
        p.check_quality()
    assert "Color" in str(e)


def test_bed_product_quality_because_of_smell():
    mock_quality_checker = MagicMock()
    mock_quality_checker.checkpoint_1.return_value = 95
    mock_quality_checker.checkpoint_2.return_value = 90
    mock_quality_checker.checkpoint_3.return_value = 97

    p = Product(mock_quality_checker)
    p.create()
    with raises(BadProductQualityError) as e:
        p.check_quality()
    assert "Smell" in str(e)


def test_good_product_quality():
    mock_quality_checker = MagicMock()
    mock_quality_checker.checkpoint_1.return_value = 95
    mock_quality_checker.checkpoint_2.return_value = 90
    mock_quality_checker.checkpoint_3.return_value = 98

    p = Product(mock_quality_checker)
    p.create()
    p.check_quality()
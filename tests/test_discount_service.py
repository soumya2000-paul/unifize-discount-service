import pytest # type: ignore
pytestmark = pytest.mark.asyncio
from decimal import Decimal

from src.service.discount_service import DiscountService
from src.data.fake_data import sample_cart, dummy_customer, payment_info

@pytest.mark.asyncio
async def test_calculate_cart_discounts_without_voucher():
    service = DiscountService()
    result = await service.calculate_cart_discounts(sample_cart, dummy_customer, payment_info)

    assert result.original_price == Decimal("1000.00")

    expected_brand_discount = Decimal("400.00")  # 40%
    expected_category_discount = Decimal("60.00")  # 10% of 600
    expected_bank_discount = Decimal("54.00")  # 10% of 540
    expected_final_price = Decimal("486.00")

    assert result.applied_discounts["Brand discount on PUMA"] == expected_brand_discount
    assert result.applied_discounts["Category discount on T-shirts"] == expected_category_discount
    assert result.applied_discounts["ICICI Bank Offer"] == expected_bank_discount
    assert result.final_price == expected_final_price

@pytest.mark.asyncio
async def test_validate_valid_voucher():
    service = DiscountService()
    is_valid = await service.validate_discount_code("SUPER69", sample_cart, dummy_customer)
    assert is_valid

@pytest.mark.asyncio
async def test_validate_invalid_voucher():
    service = DiscountService()
    is_valid = await service.validate_discount_code("INVALID123", sample_cart, dummy_customer)
    assert not is_valid

@pytest.mark.asyncio
async def test_discount_with_super69_voucher():
    service = DiscountService()
    result = await service.calculate_cart_discounts(
        sample_cart, dummy_customer, payment_info, voucher_code="SUPER69"
    )

    # Base discount steps
    assert result.original_price == Decimal("1000.00")
    assert result.applied_discounts["Brand discount on PUMA"] == Decimal("400.00")
    assert result.applied_discounts["Category discount on T-shirts"] == Decimal("60.00")
    assert result.applied_discounts["ICICI Bank Offer"] == Decimal("54.00")

    # Super69 on ₹486.00 → 69% of 486 = 335.34
    assert result.applied_discounts["Voucher SUPER69"] == Decimal("335.34")
    assert result.final_price == Decimal("150.66")  # 486 - 335.34

@pytest.mark.asyncio
async def test_discount_with_save20_voucher():
    service = DiscountService()
    result = await service.calculate_cart_discounts(
        sample_cart, dummy_customer, payment_info, voucher_code="SAVE20"
    )

    # 20% of ₹486 = 97.20
    assert result.applied_discounts["Voucher SAVE20"] == Decimal("97.20")
    assert result.final_price == Decimal("388.80")

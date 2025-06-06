from decimal import Decimal
from models.models import Product, CartItem, PaymentInfo, BrandTier, CustomerProfile

puma_tshirt = Product(
    id="puma-ts-001",
    brand="PUMA",
    brand_tier=BrandTier.REGULAR,
    category="T-shirts",
    base_price=Decimal("1000.00"),
    current_price=Decimal("1000.00")
)

cart_item = CartItem(
    product=puma_tshirt,
    quantity=1,
    size="M"
)

payment_info = PaymentInfo(
    method="CARD",
    bank_name="ICICI",
    card_type="CREDIT"
)

dummy_customer = CustomerProfile(
    id="cust-001",
    tier="silver"
)

sample_cart = [cart_item]

valid_voucher = ["SUPER69", "SAVE20"]

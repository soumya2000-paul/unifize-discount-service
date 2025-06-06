import asyncio
from data.fake_data import sample_cart, dummy_customer, payment_info
from service.discount_service import DiscountService

async def main():
    service = DiscountService()
    result = await service.calculate_cart_discounts(sample_cart, dummy_customer, payment_info)

    print("Original Price:", result.original_price)
    print("Final Price:", result.final_price)
    print("Applied Discounts:")
    for k, v in result.applied_discounts.items():
        print(f" - {k}: ₹{v}")
    print("Message:", result.message)

if __name__ == "__main__":
    asyncio.run(main())
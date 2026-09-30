import asyncio

async def process_claim(claim_id, delay):

    print(f"Started processing claim: {claim_id}")
    await asyncio.sleep(delay)
    print(f"Completed processing claim: {claim_id}")

async def main():

    await asyncio.gather(
        process_claim("CLM1001", 3),
        process_claim("CLM1002", 2),
        process_claim("CLM1003", 1)
    )


asyncio.run(main())
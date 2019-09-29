from molotov import scenario


@scenario(weight=50)
async def scenario_one(session):
    async with session.get('http://127.0.0.1:5000/') as resp:
        res = await resp.json()
        assert len(res) == 0


@scenario(weight=30)
async def scenario_two(session):
    res = await session.get('http://127.0.0.1:5000/')
    assert res.status == 200

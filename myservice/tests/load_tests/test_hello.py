from molotov import scenario


@scenario(weight=50)
async def scenario_one(session):
    async with session.get('http://127.0.0.1:5000/hello') as resp:
        res = await resp.json()
        assert res['Hello'] == 'World'


@scenario(weight=30)
async def scenario_two(session):
    res = await session.get('http://127.0.0.1:5000/hello')
    assert res.status == 200

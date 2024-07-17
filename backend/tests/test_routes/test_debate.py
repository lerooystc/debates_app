from tests.utils.debate import create_random_debate


def test_should_fetch_debate_created(client, db_session):
    debate = create_random_debate(db=db_session)
    response = client.get(f"debates/{debate.access_code}/")
    assert response.status_code == 200
    assert response.json()["name"] == debate.name

def populate(config):

    # Initialize the database
    db = config.db
    Fixtures = config.Fixtures

    # Create the database and the database table
    db.create_all()

    # Fixtures
    Fixtures.query.delete()
    db.session.add(Fixtures(time="14:00",day_month="Thursday Oct",date="05/10/23",team_1="England",team_2="New Zealand",venue="Narendra Modi Staduium",matchNumber="1"))
    db.session.add(Fixtures(time="14:00",day_month="Friday Oct",date="06/10/23",team_1="Pakistan",team_2="Netherlands",venue="Rajiv Gandhi International Stadium",matchNumber="2"))
    db.session.add(Fixtures(time="10:30",day_month="Saturday Oct",date="07/10/23",team_1="Afghanistan",team_2="Bangladesh",venue="Himachal Pradesh Cricket Association Stadium",matchNumber="3"))
    db.session.add(Fixtures(time="14:00",day_month="Saturday Oct",date="07/10/23",team_1="South Africa",team_2="Sri Lanka",venue="Arun Jaitley Stadium",matchNumber="4"))
    db.session.add(Fixtures(time="14:00",day_month="Sunday Oct",date="08/10/23",team_1="Australia",team_2="India",venue="MA Chidambaram Stadium",matchNumber="5"))

    # Commit the changes
    db.session.commit()
        

        


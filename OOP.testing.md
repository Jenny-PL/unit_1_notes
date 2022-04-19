# Testing in OOP

- test for each attribute
- test whether the methods do what they should
- Our test files need to import all of the classes they depend on!   
- Also import packages if needed. (tests are likely not in the same folders as our class modules)   


```
def test_some_example_test_case():
    # Arrange
    # Create an instance of the class
    # and set up any other necessary test variables

    # Act
    # Call the method that we are testing

    # Assert
    # Verify all relevant return values and state changes
```

Here's a test for initial state:
```
def test_new_valid_driver():
    name = "Batman"
    vin = "NAN4NAN4NA"
    trip_a = Trip()
    trip_b = Trip()
    trips = [trip_a, trip_b]

    batman = Driver(name=name, vin=vin, trips=trips)

    assert batman.name == name
    assert batman.vin == vin
    assert len(batman.trips) == 2
    assert trip_a in batman.trips
    assert trip_b in batman.trips
```
Testing a method calculate_avg_rating():
```
def test_driver_calculate_avg_rating():
    # arrange
    good_trip = Trip(rating=4)
    bad_trip = Trip(rating=2)
    batman = Driver(trips=[good_trip, bad_trip])

    # act
    avg_rating = batman.calculate_avg_rating()

    # assert
    assert avg_rating == 3

def test_driver_calculate_avg_rating_is_zero_with_no_trips():
    # arrange
    batman = Driver(trips=[])

    # act
    avg_rating = batman.calculate_avg_rating()

    # assert
    assert avg_rating == 0
```

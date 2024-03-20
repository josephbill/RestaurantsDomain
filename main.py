# test instances 
from database.database import conn
from models.customers import Customer
from models.restaurants import Restaurant
from models.reviews import Review

restaurant1 = Restaurant(1,"Kenya 1 Restaurant",500)
restaurant2 = Restaurant(2,"Kenya 2 Restaurant",300)
restaurant3 = Restaurant(3, "Swahili Dishes", 200)

customer1 = Customer(1,"Joseph", "Mbugua")
customer2 = Customer(2,"Mary","Mbugua")
customer3 = Customer(3,"Keith", "Lee")

review1 = Review(1,restaurant1,customer1,5)
review2 = Review(2,restaurant1,customer2,2)
review3 = Review(3,restaurant2,customer1,4)
review4 = Review(4,restaurant2,customer2,5)
review5 = Review(5,restaurant3,customer1,12)


# create customer 
Customer.create_customer(customer1)
Customer.create_customer(customer2)
Customer.create_customer(customer3)

# create restuarants 
Restaurant.create_restaurant(restaurant1)
Restaurant.create_restaurant(restaurant2)
Restaurant.create_restaurant(restaurant3)

# restaurant reviews 
Restaurant.add_review(restaurant1,review1)
Restaurant.add_review(restaurant1,review2)
Restaurant.add_review(restaurant2,review3)
Restaurant.add_review(restaurant2,review4)
Restaurant.add_review(restaurant3,review5)


# print customers 
customers = Customer.get_all_customers()
for customer in customers:
    print(f"{customer.id} {customer.last_name} {customer.first_name}")

# print restaurants 
restaurants = Restaurant.get_all_restaurants()
for restaurant in restaurants:
    print(f"{restaurant.id} {restaurant.price} {restaurant.name}")


# get restaurants reviews 
print(restaurant1.reviews())
# get customers who reviewed the restaurant 
print(restaurant1.customers())


# get customers reviews 
print(customer1.reviews())
print(customer1.restaurants())

#reviews block 
print(review1.customer())
print(review1.restaurant())

#customer fullname 
print("Full Name: ", customer1.full_name)

#customer favourite restaurant 
print("Favourite restaurant " , customer1.favourite_restaurant())

#customer add review 
print(customer2.add_review(restaurant3,10))

# delete reviews belonging to a restaurant 
print(customer1.delete_all_reviews(restaurant3))
print(customer2.delete_all_reviews(restaurant3))

# get customers favourite restaurants 
print(customer1.favourite_restaurant())

# get a reviews full review statement 
print(review1.full_review())
print(review3.full_review())


# get restaurants reviews  // all_reviews
print(restaurant1.reviews())

# get fanciest restaurants 
print(Restaurant.fanciest())





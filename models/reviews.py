from models.restaurants import Restaurant
from models.customers import Customer
from database.database import conn

class Review:
    cursor = conn.cursor()
    def __init__(self,id, restaurants, customers, star_rating) -> None:
        if not isinstance(restaurants, Restaurant):
            raise ValueError("restaurant id should be an instance of Restaurant.")
        if not isinstance(customers, Customer):
            raise ValueError("customer id should be an instance of Customer.")
        self.id = id
        self.restaurants = restaurants
        self.customers = customers
        self.star_rating = star_rating

    def full_review(self):
         # query the reviews table for self.id of the restaurant 
        Review.cursor.execute("SELECT * FROM reviews WHERE id = ? ", (self.id,))
        rows = Review.cursor.fetchall()
        review_details = []
        for row in rows:
            # destructuring the row 
            review_id, restaurantId , customerId, starRating = row
            print(review_id,restaurantId,customerId,starRating)
            # get restaurant name 
            r_name = Restaurant.get_restaurant_name(restaurantId)
            # get customer name 
            c_name = Restaurant.get_customer_name(customerId)
            # return the list of reviews 
            review_str = f"Review for {r_name[0]} by {c_name}: {starRating} stars."
            review_details.append(review_str)

        conn.commit()
        print(rows)
        return review_details[0]


    def customer(self):
        # query the reviews table for self.id of the restaurant 
        Review.cursor.execute("SELECT * FROM reviews WHERE id =?",(self.id,))
        rows = Review.cursor.fetchone()
        print(rows)
        review_id, restaurantId , customerId, starRating = rows
        print("destructured" ,review_id,restaurantId,customerId,starRating)      
        c_name = Restaurant.get_customer_name(customerId)
        # return the list of reviews 
        customer_str = f"{c_name}"

        conn.commit()
        print(rows)
        return customer_str

    def restaurant(self):
        # query the reviews table for self.id of the restaurant 
        Review.cursor.execute("SELECT * FROM reviews WHERE id =?",(self.id,))
        rows = Review.cursor.fetchone()
        print(rows)
        review_id, restaurantId , customerId, starRating = rows
        print("destructured" ,review_id,restaurantId,customerId,starRating)      
        r_name = Restaurant.get_restaurant_name(restaurantId)
        # return the list of reviews 
        r_str = f"{r_name}"

        conn.commit()
        print(rows)
        return r_str




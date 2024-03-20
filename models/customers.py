from database.database import conn
class Customer:
    # create the cursor object. 
    cursor = conn.cursor()
    review_details = []
    def __init__(self,id, first_name, last_name) -> None:
        self.id = id
        self.first_name = first_name
        self.last_name = last_name


    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def create_customer(customer):
        Customer.cursor.execute("SELECT id FROM customers WHERE first_name = ? AND last_name = ?",(customer.first_name, customer.last_name))
        existing_record = Customer.cursor.fetchone()
        if not existing_record:

            Customer.cursor.execute('''
              INSERT INTO customers(first_name,last_name) VALUES(?,?)''',(customer.first_name, customer.last_name))
            conn.commit()
        else: 
            print("record already exists")

    def get_all_customers():
        Customer.cursor.execute("SELECT * FROM customers")
        rows = Customer.cursor.fetchall()

        customers = []
        for row in rows:
            customer = Customer(row[0],row[1], row[2])
            customers.append(customer)

        conn.commit()
        print(customers)
        return customers

    # return all reviews for the restaurant by the customer 
    def reviews(self):
        # query the reviews table for self.id of the restaurant 
        Review.cursor.execute("SELECT * FROM reviews WHERE customer_id =?",(self.id,))
        rows = Review.cursor.fetchall()
        for row in rows:
            # destructuring the row 
            review_id, restaurantId , customerId, starRating = row
            print(review_id,restaurantId,customerId,starRating)
            # get restaurant name 
            r_name = Restaurant.get_restaurant_name(restaurantId)
            # get customer name 
            c_name = Restaurant.get_customer_name(customerId)
            # return the list of reviews 
            review_str = f"{review_id} Restaurant- {r_name} Customer- {c_name} gave the rating {starRating}"
            Customer.review_details.append(review_str)

        conn.commit()
        print(rows)
        return Customer.review_details
    
      # return the customers that reviewed the restaurant 
    def restaurants(self):
 # query the reviews table for self.id of the restaurant 
        Review.cursor.execute("SELECT * FROM reviews WHERE customer_id =?",(self.id,))
        rows = Review.cursor.fetchall()
        r_names = []
        for row in rows:
            # destructuring the row 
            review_id, restaurantId , customerId, starRating = row
            print(review_id,restaurantId,customerId,starRating)
            # get restaurant name 
            r_name = Restaurant.get_restaurant_name(restaurantId)
            # get customer name 
            c_name = Restaurant.get_customer_name(customerId)
            # return the list of reviews 
            rest_str = f"{r_name}"
            r_names.append(rest_str)

        conn.commit()
        print(rows)
        return r_names
    
    def favourite_restaurant(self):
        Review.cursor.execute("SELECT * FROM reviews WHERE customer_id =?",(self.id,))
        rows = Review.cursor.fetchall()
        print(rows)
        result = max(rows, key=lambda x: int(x[3]))
        print("restaurant id " ,result[1])
        restaurant_name = Restaurant.get_restaurant_name(result[1])
        print(restaurant_name)
        return restaurant_name[0]
    
    def add_review(self,restaurant,rating):
        if not isinstance(restaurant, Restaurant):
            raise ValueError("Restaurant should be an instance of the restaurant class.")
        Review.cursor.execute("SELECT id FROM reviews WHERE restaurant_id = ? AND customer_id = ?",(restaurant.id, self.id))
        existing_record = Review.cursor.fetchone()
        if not existing_record:
            Review.cursor.execute('''
              INSERT INTO reviews(restaurant_id,customer_id,star_rating) VALUES(?,?,?)''',(restaurant.id, self.id,rating))
            conn.commit()
            return f"Record created."
        else: 
            return f"restaurant record review already exists"
        
    def delete_all_reviews(self,restaurant):
        print(self.id, restaurant.id)
        if not isinstance(restaurant, Restaurant):
            raise ValueError("Restaurant should be an instance of the restaurant class.")
        deleteR = Review.cursor.execute("DELETE FROM reviews WHERE customer_id = ?  AND restaurant_id = ?" ,(self.id, restaurant.id))
        print(deleteR)
        conn.commit()
        if deleteR:
            return f"Restaurant review successfully deleted."
        else:
            return f"delete was not successful."


  

from models.restaurants import Restaurant
from models.reviews import Review


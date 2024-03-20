from database.database import conn
class Restaurant:
    cursor = conn.cursor()
    review_details = []
    all_restaurants = []
    def __init__(self,id, name, price) -> None:
        self.id  = id
        self.name = name
        self.price = price
        Restaurant.all_restaurants.append(self)

    
    def create_restaurant(restaurant):
        Restaurant.cursor.execute("SELECT id FROM restaurants WHERE name = ? AND price = ?",(restaurant.name, restaurant.price))
        existing_record = Restaurant.cursor.fetchone()
        if not existing_record:

            Restaurant.cursor.execute('''
              INSERT INTO restaurants(name,price) VALUES(?,?)''',(restaurant.name, restaurant.price))
            conn.commit()
        else: 
            print("restaurant record already exists")

    def get_all_restaurants():
        Restaurant.cursor.execute("SELECT * FROM restaurants")
        rows = Restaurant.cursor.fetchall()

        restaurants = []
        for row in rows:
            restaurant = Restaurant(row[0],row[1], row[2])
            restaurants.append(restaurant)

        conn.commit()
        print(restaurants)
        return restaurants
    

    def add_review(self,review):
        Review.cursor.execute("SELECT id FROM reviews WHERE restaurant_id = ? AND customer_id = ?",(review.restaurants.id, review.customers.id))
        existing_record = Review.cursor.fetchone()
        if not existing_record:
          Review.cursor.execute('''INSERT INTO reviews (restaurant_id, customer_id, star_rating)
                                  VALUES (?,?,?)
                 ''',(review.restaurants.id,review.customers.id,review.star_rating))
          conn.commit()
        else:
            print("These customers already gave reviews")
    
    # return all reviews for the restaurant 
    def reviews(self):
        # query the reviews table for self.id of the restaurant 
        Review.cursor.execute("SELECT * FROM reviews WHERE restaurant_id =?",(self.id,))
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
            review_str = f"Review for {r_name[0]} by {c_name}: {starRating} stars."
            Restaurant.review_details.append(review_str)

        conn.commit()
        print(rows)
        return Restaurant.review_details
    
    # return the customers that reviewed the restaurant 
    def customers(self):
 # query the reviews table for self.id of the restaurant 
        Review.cursor.execute("SELECT * FROM reviews WHERE restaurant_id =?",(self.id,))
        rows = Review.cursor.fetchall()
        customer_names = []
        for row in rows:
            # destructuring the row 
            review_id, restaurantId , customerId, starRating = row
            print(review_id,restaurantId,customerId,starRating)
            # get restaurant name 
            r_name = Restaurant.get_restaurant_name(restaurantId)
            # get customer name 
            c_name = Restaurant.get_customer_name(customerId)
            # return the list of reviews 
            customer_str = f"{c_name}"
            customer_names.append(customer_str)

        conn.commit()
        print(rows)
        return customer_names

        

    # static methods to get restuarant and customer details 
    @staticmethod
    def get_restaurant_name(restid):
        print(restid)
        Restaurant.cursor.execute("SELECT name FROM restaurants WHERE id = ?",(restid,))
        restaurant_name = Restaurant.cursor.fetchone()
        return restaurant_name
    
    @staticmethod
    def get_customer_name(custid):
        Restaurant.cursor.execute("SELECT first_name, last_name FROM customers WHERE id = ?",(custid,))
        first_name, last_name = Restaurant.cursor.fetchone()
        customer_name = f"{first_name} {last_name}"
        return customer_name
    

    @classmethod
    def fanciest(cls):
        # query to get rest with highest price 
        Restaurant.cursor.execute("SELECT * FROM restaurants WHERE price = (SELECT MAX(price) FROM restaurants)")  
        rows = Restaurant.cursor.fetchall()
        if len(rows) > 1:
            restaurant_fanciest = []
            for row in rows:
                print(row)
                id, name , price  = row 
                restuarant = {'id': id, 'name': name , 'price': price}
                print(restuarant)
                restaurant_fanciest.append(restuarant)
            return restaurant_fanciest

        elif len(rows) == 1:
            id , name , price = rows[0]
            restuarant = {'id': id, 'name': name , 'price': price}
            return restuarant
        else: 
            return "All restaurants fall in same class"      
        


from models.reviews import Review



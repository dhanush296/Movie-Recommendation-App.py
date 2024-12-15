import tkinter as tk
import random

movies_by_genre = {
    "Action": ["Gabbar Singh", "Aravinda Sametha Veera Raghava", "Sahoo", "Akhanda", "Devara", "Narappa","Bhemala Nayak","Chatrapathi","Pushpa: The Rule-2","Pokiri","Jawan","Major","Baashha","Vishwaroopam","Leo","Thani Oruvan","Thuppakki","Kaithi"],
    "Comedy": ["Nuvvu Naaku Nachchav", "Pelli Choopulu", "Jathi Ratnalu", "Ee Nagaraniki Emaindi", "Tillu Square", "Love Today", "Joker", "Nanban", "Remo", "Don", "Prince", "Mark Antony"],
    "Drama": ["Lucky Baskhar", "Rangasthalam", "Pratinidhi 2", "Oopiri", "C/o Kancharapalem","Mr.Perfect","Vada Chennai","Pushpa:The Rise-1","Animal","Yeh jawani hai deewani","Nayagan","Dhalapathy","Company","Rakta charitra","Satya","Sarkar","Mohabattein","Forrest gump","Good fellas","Godfather","The wolf of the street","Jailer","Varun Doctor","Good Night","Aramm","Soodhu Kavvum","Dada","Ayothi","Maaveeran","Chithha"],
    "Horror": ["Masooda", "Virupaksha", "Maa Oori Polimera", "Kanchana", "Taxiwala", "Bhaagamathie","Chandramukhi","Demonte Colony 2","Prema Katha Chitram","Raju Gari Gadhi","Dayam","Pizza","Maya","Thuneri"],
    "Sci-Fi": ["Aditya 369","Antariksham 9000KMPH","Kaliki 2898-AD", "Oke Oka Jeevitham", "Ismart Shankar", "Adbhutham", "Maanaadu","Tic-Tic-Tic","Robo","ra one","Interstellar","Tenet","Oppenheimer","Inception","The prestige","Memento","Insomnia"],
    "Family": ["Murari", "Srikaram", "Balagam", "F2", "Srimanthudu", "Seethamma Vakitlo Sirimalle Chettu", "Ala Vaikunthapurramuloo", "Samajavaragamana","S/o Sathyamuruty","Guntur Karam"],
    "Love": ["Orange", "Tholi Prema", "Kushi", "Sita Ramam", "Colour Photo", "Radhe Shyam", "Jaanu", "Shyam Singha Roy", "Arjun Reddy", "Joe","Uppena","Hi Nanna","Premam","Darling","Ok jaanu","Aei dil hai mushkil","Rockstar","Wake up sid","Tamasha","Dil se","Roja","Geethanjali","Mounaragam","Tuu jhooti mai makhar","Bombay","Ok kanmani","Rangeela","Dilwale dil le jayenge","Chennai express","Om shanti om","Mai hoon na","Devdas","Veer-zarra","Zero","Alaipayuthey","96","Sethu","Vinnaithaandi Varuvaayaa","Moondram Pirai","Thulladha Manamum Thullum","Minnale","Pariyerum Perumal","Kaadhal","Raja Rani","7G Rainbow Colony"],
    "Thriller": ["Drishyam", "Hit", "Mathu Vadhalara", "Agent Sai Srinivasa Athreya", "Kshanam", "Rakshahudu", "V","Oka Kshnam","Gudachari","Avaru","Vikram","Gargi","Mahaan","Diary","Veeramae Vaagai Soodum","Cadaver","Ayirathil Oruvan","Lingaa"],
    "Periodical": ["Bahubali-1&2", "Bimbisara", "Magadheera", "Gautamiputra Satakarni", "Rudhuramadevi", "Ghazi","RRR","poniyan selvan 1-2"],
    "Friendship": ["Happydays", "Vunnadi Okate Zindagi", "Yevade Subramanyam", "Maharshi", "Kerintha", "Devadas", "Kirrak party", "Aarya 1&2","Salaar","Ee Nagaraniki Emaindi","3 idiots","Thoza","Priyamaana Thozhi","Friends","Endrendrum Punnagai","Chennai 28","Goa","Priyamana Thozhi"]
}

def recommend_movie(genre, previous_recommendations):
    if genre in movies_by_genre:
        movies = movies_by_genre[genre][1:]
        movies = [movie for movie in movies if movie not in previous_recommendations]
        return random.choice(movies) if movies else "No more recommendations available."
    else:
        return "Sorry, we don't have any recommendations for that genre."

def show_recommendation():
    genre = genre_var.get()
    recommendation = recommend_movie(genre, previous_recommendations)
    result_label.config(text=recommendation)
    if recommendation != "No more recommendations available.":
        previous_recommendations.append(recommendation)
    satisfaction_frame.pack(pady=10)

def handle_satisfaction(satisfied):
    if satisfied:
        rate_frame.pack(pady=10)
    else:
        show_recommendation()

def handle_rating(rating):
    result_label.config(text="")
    rate_frame.pack_forget()
    for widget in root.winfo_children():
        widget.pack_forget()
    thank_you_label.config(text="Thanks for using the Movie Recommendation App!\nEnjoy the movie!")
    thank_you_label.pack(pady=10)
    tk.Button(root, text="Generate Another Genre", command=reset_app, font=('Arial', 14)).pack(pady=20)

def reset_app():
    previous_recommendations.clear()
    result_label.config(text="")
    thank_you_label.config(text="")
    satisfaction_frame.pack_forget()
    rate_frame.pack_forget()
    genre_var.set("")
    for widget in root.winfo_children():
        widget.pack()
    genre_label.pack(pady=10)
    genre_menu.pack(pady=10)
    recommend_button.pack(pady=20)

root = tk.Tk()
root.title("Movie Recommendation App")
root.geometry("400x400")

genre_var = tk.StringVar()
genre_label = tk.Label(root, text="Select a genre:", font=('Arial', 14))
genre_label.pack(pady=10)
genre_menu = tk.OptionMenu(root, genre_var, "Action", "Comedy", "Drama", "Horror", "Sci-Fi", "Family", "Love", "Thriller", "Periodical", "Friendship")
genre_menu.pack(pady=10)
recommend_button = tk.Button(root, text="Recommend a Movie", command=show_recommendation, font=('Arial', 14))
recommend_button.pack(pady=20)
result_label = tk.Label(root, text="", font=('Arial', 14))
result_label.pack(pady=10)

satisfaction_frame = tk.Frame(root)
tk.Label(satisfaction_frame, text="Are you satisfied with the recommendation?", font=('Arial', 12)).pack(side=tk.LEFT)
tk.Button(satisfaction_frame, text="Yes", command=lambda: handle_satisfaction(True), font=('Arial', 12)).pack(side=tk.LEFT, padx=5)
tk.Button(satisfaction_frame, text="No", command=lambda: handle_satisfaction(False), font=('Arial', 12)).pack(side=tk.LEFT, padx=5)

rate_frame = tk.Frame(root)
tk.Label(rate_frame, text="Please rate the app:", font=('Arial', 12)).pack(side=tk.LEFT)
tk.Button(rate_frame, text="Bad", command=lambda: handle_rating("Bad"), font=('Arial', 12)).pack(side=tk.LEFT, padx=5)
tk.Button(rate_frame, text="Average", command=lambda: handle_rating("Average"), font=('Arial', 12)).pack(side=tk.LEFT, padx=5)
tk.Button(rate_frame, text="Good", command=lambda: handle_rating("Good"), font=('Arial', 12)).pack(side=tk.LEFT, padx=5)

thank_you_label = tk.Label(root, text="", font=('Arial', 14))

previous_recommendations = []

root.mainloop()

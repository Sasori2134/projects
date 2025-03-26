import pandas as pd
import numpy as np


movies = pd.read_csv(".\\project_movie_recommendations\\TMDB_movie_dataset_v11.csv")
df = pd.DataFrame(movies)
df.sort_values("vote_average", ascending=False, inplace=True)
def get_recommendation(df,user,amount):
    cleaned = np.array([i.replace(" ","").capitalize() for i in user])
    recommendations = []
    for genre in cleaned:
        filtered = df[df["genres"].str.contains(genre, na = False)]
        recommendations.extend(filtered[["title", "vote_average", "genres"]].values.tolist())
    return recommendations[:amount]

def main():
    while True:
        print("------------------Movies------------------")
        try:
            user = input("What Genre Do You Like?(If You Want To Type Multiple Genres Use ',' To Seperate Them Type 'q' To Exit): ").split(",")
            if "q" in user or "Q" in user:
                break
            amount = int(input("How Many Movies Do You Want?: ").strip())
            if amount <= 0:
                print("Not Valid Amount,Type More Than 0")
            else:
                recommendations = get_recommendation(df,user,amount)
                if recommendations:
                    for idx,i in enumerate(recommendations,start=1):
                        print(f"{idx}.Title: {i[0]} |Rating: {i[1]:.1f}★ |Genre: {i[2]}")
                else:
                    print("This Kind Of Genre Doesn't Exist In Our Database")
        except ValueError:
            print("You Typed Amount Wrong Please Use Only Numbers")


if __name__ == "__main__":
    main()
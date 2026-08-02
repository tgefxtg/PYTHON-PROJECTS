import pandas as pd


# Student Data
data = {
    "Name": [
        "Rahul", "Anu", "Vishnu", "Akhil",
        "Sneha", "Arjun", "Meera", "Riya"
    ],

    "Math": [90, 78, 56, 88, 95, 67, 82, 74],
    "Science": [85, 80, 60, 90, 98, 70, 84, 72],
    "English": [88, 76, 58, 84, 94, 65, 86, 75]
}

df = pd.DataFrame(data)


df["Total"] = df["Math"] + df["Science"] + df["English"]

df["Average"] = (df["Total"] / 3).round(2)


def grade(avg):

    if avg >= 90:
        return "A+"

    elif avg >= 80:
        return "A"

    elif avg >= 70:
        return "B"

    elif avg >= 60:
        return "C"

    elif avg >= 50:
        return "D"

    else:
        return "F"

df["Grade"] = df["Average"].apply(grade)



df["Result"] = df["Average"].apply(
    lambda x: "Pass" if x >= 50 else "Fail"
)


print("\n========== STUDENT MARKS ==========\n")
print(df)


print("\n========== CLASS STATISTICS ==========\n")

print("Total Students :", len(df))
print("Highest Total  :", df["Total"].max())
print("Lowest Total   :", df["Total"].min())
print("Average Marks  :", round(df["Average"].mean(),2))


topper = df.loc[df["Total"].idxmax()]

print("\n========== CLASS TOPPER ==========\n")
print(topper)


print("\n========== ABOVE 80 AVERAGE ==========\n")
print(df[df["Average"] >= 80])


print("\n========== PASSED STUDENTS ==========\n")
print(df[df["Result"] == "Pass"])

print("\n========== FAILED STUDENTS ==========\n")
print(df[df["Result"] == "Fail"])


print("\n========== RANK LIST ==========\n")

rank = df.sort_values(by="Total", ascending=False)

print(rank)

df.to_csv("student_report.csv", index=False)

print("\nReport saved as student_report.csv")
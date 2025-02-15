import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("cleanbrogdonstats.csv")
df = df.dropna()
df["PTS"] = df["PTS"].astype(float)
df["Game"] = range(1, len(df) + 1)

print("Data Cleaning Complete! Launching UI...")

plt.figure(figsize=(10, 6))
plt.plot(df["Game"], df["PTS"], marker="o", linestyle="-", color="b")

plt.xlabel("Game Number")
plt.ylabel("Points Scored (PTS)")
plt.title("Points Per Game Over the Season")
plt.grid(True)

plt.show()

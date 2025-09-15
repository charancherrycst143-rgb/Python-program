import statistics as st
data = [12, 45, 83, 52]
mean = st.mean(data)
median = st.median(data)
mode = st.mode(data)
print("Output:", (mean + median + mode) / 3)

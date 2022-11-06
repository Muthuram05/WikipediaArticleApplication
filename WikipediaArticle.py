import wikipedia
query = "phone"
results = wikipedia.summary(query, sentences=2)
print(results)
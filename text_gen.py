from transformers import pipeline

model = pipeline('text-generation')

sentence = model("Hello Microwave", do_sample=True, top_k=50, temperature=0.9, max_length=100, num_return_sequences=2)

for _ in sentence:
    print(_)
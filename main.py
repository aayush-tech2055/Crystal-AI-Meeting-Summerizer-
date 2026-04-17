from transcribe import transcribe_audio
from embed import create_chunks, create_vector_store
from rag import retrieve_best_chunk
from summerize import answer_question

# Step 1: Transcribe
text = transcribe_audio("data/audio.mp3")

# Step 2: Chunk
chunks = create_chunks(text)

# Step 3: Vector DB
index, model = create_vector_store(chunks)

# Step 4: Ask Question
question = input("Ask your question: ")

best_chunk = retrieve_best_chunk(question, chunks, index, model)

# Step 5: Answer
answer = answer_question(question, best_chunk)

print("\nAnswer:\n", answer)